from bs4 import BeautifulSoup as BS
from text_editing import novel_editing
from typing import Iterator

def _pars_urls(urls_page: str) -> Iterator[tuple[str, str]]:
    soup = BS(urls_page, 'html.parser')
    option = soup.find_all('option')
    for op in option:
        yield (op.get('value'), 'url')

def _pars_text(html: str):
    soup = BS(html, 'html.parser')
    try:
        text = soup.find('div', {'id':'chr-content'}).get_text()
        text = novel_editing(text)
        comment = 'done'
    except:
        text = ''
        comment = 'pars not find'
    return (text, comment)