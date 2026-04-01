def solve():
    try:
        with open('input.txt', 'r') as f_in: # читаем файл
            data = f_in.read().split() 

        if not data:
            return

        n = int(data[0])
        a = [int(x) for x in data[1:]]

        all_good = True # для того, чтобы понять гладко ли все идет и является ли это пирамидой

        for i in range(n):
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2

            if left_idx < n: # проверяем левый индекс
                if a[i] > a[left_idx]:
                    all_good = False
                    break

            if right_idx < n: # проверяем правый индекс
                if a[i] > a[right_idx]:
                    all_good = False
                    break

        with open('output.txt', 'w') as f_out: # записываем результат в выходной файл
            if all_good:
                f_out.write("YES")
            else:
                f_out.write("NO")

    except FileNotFoundError:
        print("Файл не найден")


if __name__ == "__main__":
    solve()
