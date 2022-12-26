url = 'https://novelbin.com/b/supreme-magus-novel/chapter-'
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
}

pagin_url = 'https://novelbin.com/ajax/chapter-option?novelId=supreme-magus-novel&currentChapterId=chapter-4'

"""
Как можно сохранить прогресс

Можно словарь, ключи ссылки, значение скачен или нет.
Сохранить в json
    Если файла не существует то происходит первая загрузка

    # Первое сохранение, когда мы получаем ссылки, 
    #     и сохраняем его в виде словаря с ключами ссылками и занчениями False
    функция получающая страницу,
        Проверяет загружалась ли раньше страница
        при получении что-то вместо 200 ответа,
        и при вызове исключения возвращает пустой текст.
    
    Уже после выполнения, или прерывания функции(незнаю как сделать)
        Мы изменяем контрольный файл.
        Те станицы которые загрузились отмечаем True, нет - False
        И сохраняем измененный json
        
        

"""