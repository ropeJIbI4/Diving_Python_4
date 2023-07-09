# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def hesh(**heshs):
    result = {}
    for key, value in heshs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result

print(hesh(name = "Rocky", Age = "2", Pet = "Dog",
                     Smartphone = {'Iphone': '11pro', 'Samsung': 'A32'},
                     week = ['Monday', 'Sunday', 'Friday'],))
