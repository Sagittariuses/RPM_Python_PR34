print("Выберите номер программы ")
print("Готовые программы: 4, 5, 6, 7, 9, 10, 11, 13, 15, 17, 19 ")

task = int(input("Выбранная программа: "))
if task == 4:
    a = int(input('A = '))
    b = int(input('B = '))
    c = a*b
    while a!=0 and b!=0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print (c/(a+b))

elif task == 5:
    a=int(input("Введите число a: "))
    b=int(input("Введите число b: "))
    numbers = [x for x in range(a, b+1) if x%3 == 0]
    print("Числа, кратные 3: ", numbers)
    print("Их среднее арифметическое: ", sum(numbers)/float((len(numbers))))

elif task == 6:
    print("Введите строку: ")
    genome = input().lower()
    cnt = 0
    for nucl in genome:
        if (nucl == 'c') or (nucl == 'g'):
            cnt += 1
    print("Результат: ", (cnt/len(genome))*100) 

elif task == 7:
    str_ = input("Введите строку: ")
    from itertools import groupby
    l = [k + str(len(list(g))) if k.isalpha() else ''.join(list(g)) for k, g in groupby(str_)]
    print("Результат: ", ''.join(l).replace('1', ''))

elif task ==9:
    inp = list(map(int, input("Введите строку чисел: ").split()))
    out = []
    
    for i in range(len(inp) - 1):
        out.append(inp[i - 1] + inp[i + 1])
    else:
        out.append(inp[i] + inp[0])
    print("Новая строка: ", out)

elif task == 10:
    a =[int(i) for i in input("Введите список чисел: ").split()]
    a.sort()
    b = []
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            if a[i] not in b:
                b.append(a[i])
    print("Результат: " )
    for i in range(0, len(b)):
        print(b[i], end =' ')

elif task == 11:
    summ = [0, 0]
    print("Введите список чисел: ")
    while True:
        i = int(input("Число: "))
        summ[0] += i
        summ[1] += i*i
        if not summ[0]:
            break
    print("Результат: ", summ[1])

elif task == 13:
    lst = map(int, input("Введите список чисел: ").split())
    x = int(input("Введите число: "))
    lst_x = [i for i, v in enumerate(lst) if v == x]
    print("Результат: ", *lst_x) if lst_x else print("Отсутствует")

elif task == 15:
    def zm(n):
        dx, dy = 1, 0
        x, y = 0, 0
        arr = [[None] * n for _ in range(n)]
        for i in range(1, n**2+1):
            arr[x][y] = i
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
                x, y = nx, ny
            else:
                dx, dy = -dy, dx
                x, y = x+dx, y+dy
        for x in list(zip(*arr)):
            print(*x)
    zm(int(input("Введите размер матрицы: ")))
elif task == 17:
    x = int(input("Введите число: "))
    if -15 < x <= 12 or 14 < x < 17 or x >= 19:
        print("Результат: ", True)
    else:
        print("Результат: ",False)
elif task == 19:
    a = int(input("Первое число: "))
    b = int(input("Второе число: "))
    c = int(input("Третье число: "))
    s = a + b + c
    print("Максимум: ", max(a,b,c))
    print("Минимум: ", min(a,b,c))
    print("Оставшееся число: ", s - max(a,b,c) - min(a,b,c))