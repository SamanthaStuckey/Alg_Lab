import sys


def solve():
    # Чтение данных из input.txt
    try:
        with open('input.txt', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return

    output_lines = []

    # Константы для хеширования
    P = 31
    MOD = 10 ** 9 + 9

    for line in lines:
        parts = line.split()
        if len(parts) < 3: continue

        k = int(parts[0])
        t = parts[1]
        p = parts[2]

        n, m = len(t), len(p)
        if m > n:
            output_lines.append("0")
            continue

        # Предвычисление хешей и степеней для t
        h_t = [0] * (n + 1)
        pow_p = [1] * (max(n, m) + 1)
        for i in range(n):
            h_t[i + 1] = (h_t[i] * P + (ord(t[i]) - ord('a') + 1)) % MOD
            pow_p[i + 1] = (pow_p[i] * P) % MOD

        # Предвычисление хешей для p
        h_p = [0] * (m + 1)
        for i in range(m):
            h_p[i + 1] = (h_p[i] * P + (ord(p[i]) - ord('a') + 1)) % MOD

        def get_hash(h, l, r):  # хеш подстроки [l, r)
            return (h[r] - h[l] * pow_p[r - l]) % MOD

        results = []

        # Проверяем каждую возможную позицию начала i в тексте t
        for i in range(n - m + 1):
            mismatches = 0
            curr_pos = 0  # текущая позиция внутри паттерна p

            while curr_pos < m:
                # Бинарный поиск самого длинного совпадающего префикса
                low = 1
                high = m - curr_pos
                match_len = 0

                while low <= high:
                    mid = (low + high) // 2
                    if get_hash(h_t, i + curr_pos, i + curr_pos + mid) == get_hash(h_p, curr_pos, curr_pos + mid):
                        match_len = mid
                        low = mid + 1
                    else:
                        high = mid - 1

                curr_pos += match_len
                if curr_pos < m:
                    mismatches += 1
                    if mismatches > k:
                        break
                    curr_pos += 1  # Пропускаем несовпадающий символ

            if mismatches <= k:
                results.append(i)

        # Формируем строку ответа: количество и сами индексы
        output_lines.append(f"{len(results)} " + " ".join(map(str, results)))

    # Запись в output.txt
    with open('output.txt', 'w') as f:
        f.write("\n".join(output_lines) + "\n")


if __name__ == "__main__":
    solve()
