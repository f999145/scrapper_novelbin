import os, json
from zipfile import ZipFile, ZIP_DEFLATED
from scrapper import PageTuple
from typing import Iterable

def control_save(control: dict[str, bool]) -> None:
    os.makedirs('data', exist_ok=True)
    with open(os.path.join('data','control.json'), mode='w', encoding='utf-8') as file:
        file.write(json.dumps(control, indent=4, ensure_ascii=False))

def control_load() -> dict[str, bool]:
    if (os.path.isfile(os.path.join('data','control.json'))):
        with open(os.path.join('data','control.json'), mode='r', encoding='utf-8') as file:
            return json.loads(file.read())
    return {}

def _save_texts(datas: dict[str, str], name_zip: str = os.path.join('data','texts.zip')) -> None:
    os.makedirs('data', exist_ok=True)
    with ZipFile(
        file=name_zip,
        mode='w',
        compression=ZIP_DEFLATED,
        compresslevel=1
    ) as zfile:
        for key, value in datas.items():
            if value:
                zfile.writestr(key, value.encode())

def _load_texts(name_zip: str = os.path.join('data','texts.zip')) -> dict[str, str]:
    if os.path.isfile(os.path.join('data','texts.zip')):
        return_dict = {}
        with ZipFile(name_zip) as zfile:
            for item in zfile.filelist:
                with zfile.open(item.filename) as file:
                    data = file.read().decode('utf-8')
                    return_dict[item.filename] = data
            return return_dict
    else:
        return {}

def _convert_PageTuple(pages: list[PageTuple]) -> Iterable[tuple[str, str]]:
    for page in pages:
        yield (f'{page.i:04d}.txt', page.text)

def save_texts_to_zip(pages: list[PageTuple]) -> None:
    texts_dict = _load_texts()
    texts_dict_new = dict(_convert_PageTuple(pages))
    texts_dict.update(texts_dict_new)
    _save_texts(texts_dict)