from data.scrapper import get_urls, run_async
from typing import Iterable
from data.decor import spent_time
from data.save_and_load import control_load, control_save, save_texts_to_zip, _save_texts, _load_texts
from data.translate import run_translate
from data.my_class import PageTuple



def _get_dict_control(pages: list[PageTuple]) -> Iterable[tuple[str, str]]:
    for page in pages:
        yield (page.url, page.comment)
    

@spent_time
def scrapping():
    urls_list = control_load()
    urls_list_new = get_urls()
    print('_'*20)
    print(list(urls_list_new)[:5])
    if not (urls_list.keys() == urls_list_new.keys()):
        urls_list.update(urls_list_new)
        control_save(urls_list)
    
    pages = run_async(urls_list)
    urls_list_new = dict(_get_dict_control(pages))
    if not (urls_list.values() == urls_list_new.values()):
        urls_list.update(urls_list_new)
        control_save(urls_list)
    save_texts_to_zip(pages)
    
@spent_time
def translate():
    texts = run_translate()
    
    text = '\n'.join(texts)
    
    with open('data/text_rus.txt', mode='w', encoding='utf-8') as file:
        file.write(text)

def _sorted_texts():
    texts = _load_texts()
    texts = dict(sorted(texts.items()))
    _save_texts(texts)

# @spent_time
def main():
    # scrapping()
    translate()
    # _sorted_texts()
    # _join_text()
    pass

if __name__ == '__main__':
    main()