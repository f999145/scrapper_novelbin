import requests
import asyncio, aiohttp
from config import url, headers, pagin_url
from operations_with_paths import ChangeDir
import time
from pars import _pars_text, _pars_urls
from typing import NamedTuple

class PageTuple(NamedTuple):
    i: int
    url: str
    comment: str
    text: str

def get_urls() -> dict[str,str]:
    count = 0
    while True:
        urls_page = requests.get(url=pagin_url,headers=headers)
        if int(urls_page.status_code) == 200:
            break
        print('Что-то пошло не так!')
        print('\t\tНе загрузилась страница с адресами')
        print(f'Попытка {count+1}')
        if count < 5:
            count += 1
        else:
            exit()
        time.sleep(3)
    return dict(_pars_urls(urls_page.text))

async def _worker(queue: asyncio.Queue) -> PageTuple:
    """Асинхронный воркер который получает информацию с помощью очереди"""
    index, (url, done) = await queue.get()
    if not done == 'done':
        async with aiohttp.ClientSession() as session:
            try:
                response = await session.get(url=url, headers=headers)
            except:
                response_text = ""
                comment = 'ex'
            else:
                if response.status == 200:
                    text = await response.text()
                    response_text, comment = _pars_text(text)
                else:
                    response_text = ""
                    comment = 'not 200'
    else:
        response_text = ""
        comment = 'done'
    print(f'{index:04d} is {comment}')
    queue.task_done()
    return PageTuple(index, url, comment, response_text)

# Создаем очередь, которую будем использовать
# для хранения рабочей нагрузки.    
def _queue(urls_list: dict[str, str]) -> asyncio.Queue[tuple[int, tuple[str, str]]]:
    queue: asyncio.Queue[tuple[int, tuple[str, str]]]  = asyncio.Queue()
    for op in list(enumerate(urls_list.items()))[:7]:
        # добавляем информацию в очередь
        queue.put_nowait(op)
    return queue
    

async def get_pages_tasks(urls_list: dict[str, str]) -> list[PageTuple]:
    tasks = []
    queue = _queue(urls_list)
    # Создаем семь рабочих задач для одновременной обработки очереди.
    for _ in range(7):
        task = asyncio.create_task(_worker(queue))
        tasks.append(task)
    
    # Запускаем обработку очереди и ожидаем, 
    # пока элементы не закончатся
    await queue.join()
    # После того как очередь израсходована
    # останавливаем задачи
    for task in tasks:
        task.cancel()
    # Ждем, остановку задач.
    pages = await asyncio.gather(*tasks, return_exceptions=True)
    return pages

def run_async(urls_list: dict[str, str]) -> list[PageTuple]:
    return asyncio.run(get_pages_tasks(urls_list))
    