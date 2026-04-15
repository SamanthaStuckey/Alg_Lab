def solve():
    try:
        with open('input.txt', 'r') as f_in:
            data = f_in.read().split()

        if not data: return

        # Считываем данные
        target = int(data[0])  # Какую сумму хотим собрать
        k = int(data[1])  # Сколько разных видов монет

        nominals = list(map(int, data[2:2 + k]))  # Номиналы
        counts = list(map(int, data[2 + k: 2 + 2 * k]))  # Сколько штук каждой монеты есть

        dp = [float('inf')] * (target + 1)
        dp[0] = 0

        # Основной цикл
        for i in range(k):  # Берем по очереди каждый вид монет
            coin_val = nominals[i]  # Номинал текущей монеты
            how_many = counts[i]  # Сколько таких монет у нас в кармане

            # Идем по суммам от цели назад к нулю
            for s in range(target, 0, -1):
                for n in range(1, how_many + 1):
                    if s >= n * coin_val:
                        old_sum = s - n * coin_val
                        dp[s] = min(dp[s], dp[old_sum] + n)
                    else:
                        break  # Если сумма 's' меньше, чем монеты, дальше пробовать нет смысла

        # Пишем результат
        if dp[target] == float('inf'):
            result = 0
        else:
            result = dp[target]

        # Записываем результат в файл
        with open('output.txt', 'w') as f_out:
            f_out.write(f"{result}\n")


    except Exception as e:
        print(f"Ошибка: {e}")


solve()
