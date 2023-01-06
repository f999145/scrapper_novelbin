from json import loads as json_loads, dumps as json_dumps
from os import makedirs as os_makedirs, getcwd as os_getcwd
from os.path import join as os_path_join, isfile as os_path_isfile
from zipfile import ZipFile, ZIP_DEFLATED
from typing import Iterable
from my_class import PageTuple

# import sys
# sys.path.append(os_getcwd())
# from config import folder_result, name_eng_zipfile

from config_dub import folder_result, name_eng_zipfile

def control_save(control: dict[str, bool]) -> None:
    os_makedirs(folder_result, exist_ok=True)
    with open(os_path_join(folder_result,'control.json'), mode='w', encoding='utf-8') as file:
        file.write(json_dumps(control, indent=4, ensure_ascii=False))

def control_load() -> dict[str, bool]:
    if (os_path_isfile(os_path_join(folder_result,'control.json'))):
        with open(os_path_join(folder_result,'control.json'), mode='r', encoding='utf-8') as file:
            return json_loads(file.read())
    return {}

def _save_texts(datas: dict[str, str], name_zip: str = os_path_join(folder_result,name_eng_zipfile)) -> None:
    os_makedirs(folder_result, exist_ok=True)
    with ZipFile(
        file=name_zip,
        mode='w',
        compression=ZIP_DEFLATED,
        compresslevel=1
    ) as zfile:
        for key, value in datas.items():
            if value:
                zfile.writestr(key, value.encode())

def _load_texts(name_zip: str = os_path_join(folder_result,name_eng_zipfile)) -> dict[str, str]:
    if os_path_isfile(os_path_join(folder_result,name_eng_zipfile)):
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