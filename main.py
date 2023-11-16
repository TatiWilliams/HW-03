def binary_search(arr, target): # эта функция принимает отсортированый список и определяет интервал, в котором будет проходить поиск. Устанавливает номер позиции элемента.

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        if guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return low


def main():
    sequence = input("Введите последовательность чисел через пробел: ")
    target = int(input("Введите число: "))

    numbers = list(map(int, sequence.split())) # преобразует введенную последовательность в список 
    numbers.sort() # сортирует список

    index = binary_search(numbers, target)

    if index == len(numbers):
        print("Число больше всех элементов последовательности")
    else:
        print(f"Число {target} должно находиться на позиции {index}")


if __name__ == "__main__": # проверяем запускается ли скрипт напрямую или импортируется в другой модуль. 


    main()
