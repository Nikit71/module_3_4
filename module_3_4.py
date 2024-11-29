#       Самостоятельная работа по уроку "Произвольное число параметров"
#       Задача "Однокоренные"

def single_root_words(root_word, *other_words):
    same_words = []                     # создание пустого списка
    k = root_word.lower()               # перевод в нижний регистр строки стравниения
    for i in other_words:
        m = i.lower()                   # перевод в нижний регистр элемента входных элементов
        if m.count(k) or k.count(m):    # реврсивная проверка включения строк
            same_words.append(i)        # увеличение списка при выполнении условия
    return same_words                   # возврат значения функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)



