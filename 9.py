def add_binary_numbers(a, b):
    n = len(a)
    c = [0] * (n + 1)
    carry = 0

    for i in range(n - 1, -1, -1):
        total = a[i] + b[i] + carry
        c[i + 1] = total % 2
        carry = total // 2

    c[0] = carry
    return c


def main():
    try:
        with open('input2.txt', 'r') as f:
            content = f.read().split()
            if len(content) < 2: return

            a = [int(bit) for bit in content[0]]
            b = [int(bit) for bit in content[1]]

        result = add_binary_numbers(a, b)

        with open('output2.txt', 'w') as f:
            f.write("".join(map(str, result)))

    except FileNotFoundError:
        print("Файл input2.txt не найден")


if __name__ == "__main__":
    main()
