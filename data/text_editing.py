from data.save_and_load import _load_texts, _save_texts
# from os.path import join as os_path_join
from typing import Iterable




# test = _load_texts()
# text = test[list(test.keys())[163]]
# # print()
# # print(yt.translate("en", "ru", text))
clear_list=[
    'Read Latest Chapters at​ ｎ0ｖｅｌｂｉｎ',
    'Best novel online free at ⓝ0ⓥⓔⓛⓑⓘⓝ',
    'please visit n0ve1b(in).ne)t',
    'Thank you readers',
    '6054d257f56b520818c0fb96'
]

def _search_clear_list(row: str) -> str:
    for cl in clear_list:
        if cl in row:
            row = row.replace(cl, '')
    return row

def _first_text_gen(text: list[str]) -> Iterable[str]:
    count = 0
    for row in text:
        row = _search_clear_list(row)
        row_new = row.strip()
        if row_new == '':
            if not count:
                count = 1
            else:
                count += 1
            if count > 1:
                continue
        else:
            count = 0
        yield row_new


def novel_editing(text: str) -> str:
    text_list = text.split('\n')
    text_fin = '\n'.join(_first_text_gen(text_list)).strip()
    return text_fin

# def _through_files(texts: dict[str, str]) -> Iterable[tuple[str, str]]:
#     for key, value in texts.items():
#         text = novel_editing(value)
#         yield (key, text)


# def main():
#     texts = _load_texts()
#     new_texts = dict(_through_files(texts))
#     _save_texts(new_texts)
    

# if __name__ == '__main__':
#     main()


# with open(os_path_join('data','text.txt'), mode='w', encoding='utf-8') as file:
#     file.write(text)