from scrapper import get_urls, run_async, PageTuple
from typing import Iterable
from decor import spent_time
from save_and_load import control_load, control_save, save_texts_to_zip


def _get_dict_control(pages: list[PageTuple]) -> Iterable[tuple[str, str]]:
    for page in pages:
        yield (page.url, page.comment)
    

@spent_time
def scrapping():
    urls_list = control_load()
    urls_list_new = get_urls()
    if not (urls_list.keys() == urls_list_new.keys()):
        urls_list.update(urls_list_new)
        control_save(urls_list)
    
    pages = run_async(urls_list)
    urls_list_new = dict(_get_dict_control(pages))
    if not (urls_list.values() == urls_list_new.values()):
        urls_list.update(urls_list_new)
        control_save(urls_list)
    save_texts_to_zip(pages)

# @spent_time
def main():
    scrapping()

if __name__ == '__main__':
    main()