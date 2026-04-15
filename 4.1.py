def solve():
    try:
        with open('input.txt', 'r') as f:
            numbers = [int(x) for x in f.read().split()]
    except:
        print("Файл не найден или в нем ошибка")
        return

    if not numbers:
        return

    target = numbers[0]  # Нужная сумма
    count_types = numbers[1]  # Сколько видов монет
    coins = numbers[2:]  # Список самих номиналов

    limit = target + 1
    min_coins = [limit] * (target + 1)
    min_coins[0] = 0

    # Считаем минимальное количество монет для каждой суммы по очереди
    for current_sum in range(1, target + 1):
        for coin in coins:
            if current_sum >= coin:
                variants = min_coins[current_sum - coin] + 1
                if variants < min_coins[current_sum]:
                    min_coins[current_sum] = variants

    # Проверяем результат и записываем в файл
    result = min_coins[target]

    # Если число осталось слишком большим — значит, разменять нельзя
    if result > target:
        result = 0

    with open('output.txt', 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    solve()


