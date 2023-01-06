from yandexfreetranslate import YandexFreeTranslate
from data.save_and_load import _load_texts
import multiprocessing as mp
from typing import Iterable

def _get_row(text_list: list[str]) -> Iterable[tuple[int, str]]:
    count = 0
    for lst in text_list:
        rows = lst.split('\n')
        for row in rows:
            yield (count, row)
            count += 1

def _worker(queue: tuple[int, str]) -> str:
    key, value = queue
    if not value:
        return ''
    yt = YandexFreeTranslate()
    text = yt.translate("en", "ru", value)
    return texts


def run_translate()-> list[str]:
    tmp = _load_texts()
    queue = _get_row(list(tmp.values()))
    with mp.Pool(mp.cpu_count()) as process:
        workreturn = process.map(_worker, queue)
    
    return workreturn


def main():
    pass

if __name__ == '__main__':
    main()