from decorators import TimeDecorate, CountDecorate, LoggerDecorate

@LoggerDecorate
@CountDecorate
def summ(a: int, start=0):
    sum = 0
    for i in range(start, a + 1):
        sum += i
    return sum

@TimeDecorate
def minus_sum(a: int, start=0):
    sum = 0
    for i in range(start, a + 1):
        sum -= i
    return sum

@LoggerDecorate
def say(text: str):
    print(text.upper())


# Главная функция
def main():
    for i in range(5):
        print(summ(4, 2))

    print(minus_sum(7, 4))
    say('Hi!!')


# Запуск программы
if __name__ == '__main__':
    main()

