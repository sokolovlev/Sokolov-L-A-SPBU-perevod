
# Соколов Л.А перевод на 2-ой курс
# программа сортировки вставками


def sortfunction(array:list):                       #функция сортировки вставками

    n = len(array)

    for i in range(1, n):                       #цикл для прохода массива
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array

# основная программа
line = input("Input your number list: ")
array = list(map(int, line.split()))

result = sortfunction(array)
print(result)