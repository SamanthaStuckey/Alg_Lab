def solve():
    try:
        with open('input.txt', 'r') as f_in:
            lines = f_in.readlines()
    except FileNotFoundError:
        return

    if not lines:
        return

    n = int(lines[0].strip())
    dims = []
    for i in range(1, n + 1):
        a, b = map(int, lines[i].split())
        if i == 1:
            dims.append(a)
        dims.append(b)

    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    # Формирование строки результата
    def format_res(i, j):
        if i == j:
            return "A"
        k = split[i][j]
        return "(" + format_res(i, k) + format_res(k+1, j) + ")"

    # Запись результата в файл
    with open('output.txt', 'w') as f_out:
        f_out.write(format_res(0, n - 1) + '\n')

if __name__ == "__main__":
    solve()
