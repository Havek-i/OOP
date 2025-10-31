from abc import ABC, abstractmethod
import time

class BaseDecorate(ABC):
    '''Абстрактный клас для будющих декораторов'''

    @abstractmethod
    def __init__(self, func):
        self.func = func

    @abstractmethod
    def __call__(self, *args, **kwds):
        '''Абстрактный метод, который вызывается при вызове функции'''
        pass

class LoggerDecorate(BaseDecorate):
    '''Декоратор логирования функций'''

    def __init__(self, func):
        super().__init__(func)
    
    def __call__(self, *args, **kwds):
        with open('./PR23/log.txt', 'a+', encoding='utf-8') as f:
            f.write(f'Function {self.func} was started\n')
            result = self.func(*args, **kwds)
            f.write(f'Function {self.func} was finished\n')
            print('Отчёт представлен в log.txt')
            return result

class CountDecorate(BaseDecorate):
    '''Декоратор подсчёта количества вызова функции'''

    def __init__(self, func):
        super().__init__(func)
        self.count = 0

    def __call__(self, *args, **kwds):
        self.count += 1
        print(f'Функция {self.func} вызвана {self.count} {'раза' if str(self.count)[-1] in ('2', '3', '4') else 'раз'}')
        return self.func(*args, **kwds)
    
class TimeDecorate(BaseDecorate):
    '''Декоратор подсчёта времени работы функции'''

    def __init__(self, func):
        super().__init__(func)
    
    def __call__(self, *args, **kwds):
        start_time = time.time()
        result = self.func(*args, **kwds)
        end_time = time.time()
        print(f'Функция {self.func} отработала за {(end_time - start_time):.4f} сек.')
        return result