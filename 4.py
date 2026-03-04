def solve():
    try:
        with open('input2.txt', 'r') as f_in:  # читаем строку из файла
            s = f_in.read().rstrip('\r\n')
    except FileNotFoundError:
        return
    stack = []
    opening_brackets = {'(': ')', '[': ']', '{': '}'}
    error_pos = None
    for i, char in enumerate(s, start=1):  #  цикл перебирает строку, i — это номер текущего символа начиная с 1
        if char in opening_brackets: # если открывающая — запоминаем её и позицию
            stack.append((char, i))
        elif char in opening_brackets.values(): # если закрывающая — проверяем стек
            if not stack: # ошибка 1: закрывающая без открывающей
                error_pos = i
                break

            top_char, top_pos = stack.pop()
            if opening_brackets[top_char] != char: # ошибка 2: закрывающая не соответствует открывающей ((]
                error_pos = i
                break
    with open('output2.txt', 'w') as f_out: # результат
        if error_pos is not None: # выводим позицию первой несовпадающей закрывающей скобки
            f_out.write(str(error_pos))
        elif stack: # выводим позицию первой открывающей скобки без пары (берем самый первый элемент стека)
            f_out.write(str(stack[0][1]))
        else:
            f_out.write("Success") # ошибок нет
if __name__ == "__main__":
    solve()
