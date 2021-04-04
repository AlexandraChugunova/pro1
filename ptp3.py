def get_absolute_url(url, *args, **kwargs):
    """Формируем полный URL из домена и параметров
    :param url: домен
    :param args: произвольное количество позиционных параметров
    :param kwargs: произвольное количество именованных параметров"""


# добавляем к домену "/позиционный аргумент" и '?' после всех позиционных аргументов
    for i in args:
        url +='/'+i
    url += '?'
# добавляем к url именованные аргументы
    for k, v in kwargs.items():
        url += k + '=' + v + '&'
# убираем лишний '&' в конце строки
    url = url [0: -1]

    return url

print (get_absolute_url('www.yandex.ru', 'posts','news',id='24',author='admin'))
print (get_absolute_url('www.google.com','images',id='24',category='auto',color='red',size='small'))