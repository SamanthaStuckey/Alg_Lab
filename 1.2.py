def solve():
    # Читаем количество строк
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
    except EOFError:
        return
    except ValueError:
        return

    my_set = set()

    for _ in range(n):
        try:
            # Читаем команду (например, "A 2")
            row = input().split()
            if not row:
                break

            command = row[0]  # 'A', 'D' или '?'
            value = int(row[1])  # само число

            if command == 'A':
                my_set.add(value)
            elif command == 'D':
                my_set.discard(value)
            elif command == '?':
                if value in my_set:
                    print("Y")
                else:
                    print("N")
        except (EOFError, IndexError):
            break


if __name__ == "__main__":
    solve()
