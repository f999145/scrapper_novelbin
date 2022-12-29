from yandexfreetranslate import YandexFreeTranslate
from save_and_load import _load_texts
import multiprocessing as mp



def _worker(queue: tuple[str, str]) -> tuple[str, str]:
    key, value = queue
    yt = YandexFreeTranslate()
    print(f'{key}')
    text = yt.translate("en", "ru", value)
    return (key, text)


def run_translate()-> list[tuple[str, str]]:
    queue = _load_texts().items()
    with mp.Pool(mp.cpu_count()) as process:
        workreturn = process.map(_worker, queue)
    return workreturn


def main():
    pass

if __name__ == '__main__':
    main()