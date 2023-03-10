from requests import get as requests_get
import asyncio, aiohttp
from time import sleep as time_sleep
from pars import _pars_text, _pars_urls
from my_class import PageTuple
from config_dub import pagin_url, get_headers




def get_urls() -> dict[str,str]:
    count = 0
    while True:
        urls_page = requests_get(url=pagin_url, headers=get_headers())
        if int(urls_page.status_code) == 200:
            break
        print('Что-то пошло не так!')
        print('\t\tНе загрузилась страница с адресами')
        print(f'Попытка {count+1}')
        if count < 5:
            count += 1
        else:
            exit()
        time_sleep(3)
    return dict(_pars_urls(urls_page.text))

async def _worker(queue: asyncio.Queue)  -> list[PageTuple]:
    """Асинхронный воркер который получает информацию с помощью очереди"""
    reponse_assync: list[PageTuple] = []
    while True:
        index, (url, done) = await queue.get()
        if not done == 'done':
            async with aiohttp.ClientSession(headers=get_headers()) as session:
                try:
                    response = await session.get(url=url)
                except:
                    response_text = ""
                    comment = 'ex'
                else:
                    if response.status == 200:
                        text = await response.text()
                        response_text, comment = _pars_text(text)
                    else:
                        response_text = ""
                        comment = f'not; is {response.status}'
            print(f'{index:04d} is {comment}')
        else:
            response_text = ""
            comment = 'done'
        queue.task_done()
        reponse_assync.append(PageTuple(index, url, comment, response_text))
        if queue.empty():
            break
    return reponse_assync

# Создаем очередь, которую будем использовать
# для хранения рабочей нагрузки.    
def _queue(urls_list: dict[str, str]) -> asyncio.Queue[tuple[int, tuple[str, str]]]:
    queue: asyncio.Queue[tuple[int, tuple[str, str]]]  = asyncio.Queue()
    for op in list(enumerate(urls_list.items()))[:14]:
        # добавляем информацию в очередь
        queue.put_nowait(op)
    return queue
    

async def get_pages_tasks(urls_list: dict[str, str]) -> list[list[PageTuple]]:
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
    return await asyncio.gather(*tasks, return_exceptions=True)


def run_async(urls_list: dict[str, str]) -> list[PageTuple]:
    list_pages = asyncio.run(get_pages_tasks(urls_list))
    return sum(list_pages, [])
    