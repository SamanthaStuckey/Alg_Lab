def is_balanced(s):
    stack = []# список, куда записываем открывающиеся скобки
    brackets = {")": "(", "]": "["}

    for char in s:
        if char in "([":
            stack.append(char) # как раз таки пишем в список
        elif char in ")]":
            if not stack or stack.pop() != brackets[char]:  # если стек пуст или скобки не совпали — это ошибка
                return False
    return len(stack) == 0 # проверяем не осталось ли в стеке лишних открытых скобок. Если стек пуст — всё гуд - тру

def main():
    try:
        with open('input.txt', 'r') as f_in, open('output.txt', 'w') as f_out:
            line = f_in.readline()
            if not line: return

            n = int(line.strip())
            for _ in range(n):
                s = f_in.readline().strip() # убираем лишние пробелы и переносы, если они есть
                if is_balanced(s): #
                    f_out.write("YES\n")
                else:
                    f_out.write("NO\n")
    except (FileNotFoundError, ValueError):
        pass

if __name__ == "__main__":
    main()
