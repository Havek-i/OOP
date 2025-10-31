import time

def summ(a: int, start=0):
    sum = 0
    for i in range(start, a + 1):
        sum += i
    return sum
    
def minus_sum(a: int, start=0):
    sum = 0
    for i in range(start, a + 1):
        sum -= i
    return sum

def say(text: str):
    print(text.upper())


# Главная функция
def main():
    itter_count = {}

    for i in range(5):
        with open('./PR25/log.txt', 'a+') as f:
            f.write(f'Function {summ.__name__} was started\n')
            if itter_count.get(f'{summ.__name__}'):
                itter_count[f'{summ.__name__}'] += 1
                print(f"Функция {summ.__name__} была запущена {itter_count[summ.__name__]} раз(-а)")
            else:
                itter_count[f'{summ.__name__}'] = 1
                print(f"Функция {summ.__name__} была запущена 1 раз")
            res = summ(4, 2)
            f.write(f'Function {summ.__name__} was finished\n')
            print(f'Функция {summ.__name__} выполнилась со значением {res}')

    start = time.time()
    res = minus_sum(7, 4)
    end = time.time()
    print(f'Функция {minus_sum.__name__} выполнилась за {(end - start):.8f} сек. со значением {res}')

    start = time.time()
    res = say('Hi!!')
    end = time.time()
    print(f'Функция {minus_sum.__name__} выполнилась за {(end - start):.8f} сек. со значением {res}')
    

# Запуск программы
if __name__ == '__main__':
    main()