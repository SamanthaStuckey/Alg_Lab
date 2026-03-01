def bubble_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        for j in range(n - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a


def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'

    try:
        with open(input_filename, 'r') as f:
            lines = f.readlines()

        if not lines:
            print("Ошибка: Файл пуст.")
            return

        try:
            n = int(lines[0].strip())
        except ValueError:
            print(f"Ошибка: Первая строка файла '{input_filename}' должна быть целым числом (n).")
            return

        if len(lines) < 2:
            if n > 0:
                print("Ошибка: В файле отсутствует строка с массивом.")
                return
            else:
                a = []
        else:
            try:
                a = list(map(int, lines[1].split()))
            except ValueError:
                print(f"Ошибка: Элементы массива в строке 2 должны быть целыми числами.")
                return

        if len(a) != n:
            print(f"Предупреждение: Ожидалось {n} элементов, но найдено {len(a)}. Сортирую всё, что имеется.")

        sorted_a = bubble_sort(a)

        # Запись результата
        with open(output_filename, 'w') as f:
            f.write(" ".join(map(str, sorted_a)))

        print(f"Успех! Результат записан в {output_filename}")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_filename}' не найден в текущей папке.")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
