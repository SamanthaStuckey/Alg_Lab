import time
def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a


try:
    numbers = [int(x) for x in input("Введите числа через пробел: ").split()]

    print(f"\nИсходный список: {numbers}")

    # Замеряем время
    start = time.perf_counter()
    selection_sort(numbers)
    end = time.perf_counter()

    # Вывод результата
    print(f"Отсортированный список: {numbers}")
    print(f"Затраченное время: {end - start:.6f} секунд")

except ValueError:
    print("Ошибка: нужно вводить только числа.")
