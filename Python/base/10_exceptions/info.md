https://pythonchik.ru/osnovy/python-try-except

# 20 типов встроенных исключений в Python

```
    Иерархия классов для встроенных исключений в Python выглядит так:

    BaseException
        SystemExit
        KeyboardInterrupt
        GeneratorExit
        Exception
            ArithmeticError
            AssertionError
            ...
            ...
            ...
            ValueError
            Warning
```

```
    Все исключения в Python наследуются от базового BaseException:

    SystemExit — системное исключение, вызываемое функцией sys.exit() во время выхода из приложения;
    KeyboardInterrupt — возникает при завершении программы пользователем (чаще всего при нажатии клавиш Ctrl+C);
    GeneratorExit — вызывается методом close объекта generator;
    Exception — исключения, которые можно и нужно обрабатывать (предыдущие были системными и их трогать не рекомендуется).
```

``` 
    От Exception  наследуются:
    
    1 StopIteration — вызывается функцией next в том случае если в итераторе закончились элементы;
    
    2 ArithmeticError — ошибки, возникающие при вычислении, бывают следующие типы:
        * FloatingPointError — ошибки при выполнении вычислений с плавающей точкой (встречаются редко);
        * OverflowError — результат вычислений большой для текущего представления 
                          (не появляется при операциях с целыми числами, но может появиться в некоторых других случаях);
        * ZeroDivisionError — возникает при попытке деления на ноль.
    
    3 AssertionError — выражение, используемое в функции assert неверно;
    
    4 AttributeError — у объекта отсутствует нужный атрибут;
    
    5 BufferError — операция, для выполнения которой требуется буфер, не выполнена;
    
    6 EOFError — ошибка чтения из файла;
    
    7 ImportError — ошибка импортирования модуля;
    
    8 LookupError — неверный индекс, делится на два типа:
        * IndexError — индекс выходит за пределы диапазона элементов;
        * KeyError — индекс отсутствует (для словарей, множеств и подобных объектов);
    
    9 MemoryError — память переполнена;
    
    10 NameError — отсутствует переменная с данным именем;
    
    11 OSError — исключения, генерируемые операционной системой:    
        * ChildProcessError — ошибки, связанные с выполнением дочернего процесса;
        * ConnectionError — исключения связанные с подключениями (BrokenPipeError, ConnectionResetError, ConnectionRefusedError, ConnectionAbortedError);
        * FileExistsError — возникает при попытке создания уже существующего файла или директории;
        * FileNotFoundError — генерируется при попытке обращения к несуществующему файлу;
        * InterruptedError — возникает в том случае если системный вызов был прерван внешним сигналом;
        * IsADirectoryError — программа обращается к файлу, а это директория;
        * NotADirectoryError — приложение обращается к директории, а это файл;
        * PermissionError — прав доступа недостаточно для выполнения операции;
        * ProcessLookupError — процесс, к которому обращается приложение не запущен или отсутствует;
        * TimeoutError — время ожидания истекло;
    
    12 ReferenceError — попытка доступа к объекту с помощью слабой ссылки, когда объект не существует;
    
    13 RuntimeError — генерируется в случае, когда исключение не может быть классифицировано или не подпадает под любую другую категорию;
    
    14 NotImplementedError — абстрактные методы класса нуждаются в переопределении;
    
    15 SyntaxError — ошибка синтаксиса;
    
    16 SystemError — сигнализирует о внутренне ошибке;
    
    17 TypeError — операция не может быть выполнена с переменной этого типа;
    
    18 ValueError — возникает когда в функцию передается объект правильного типа, но имеющий некорректное значение;
    
    19 UnicodeError — исключение связанное с кодирование текста в unicode, бывает трех видов:    
        * UnicodeEncodeError — ошибка кодирования;
        * UnicodeDecodeError — ошибка декодирования;
        * UnicodeTranslateError — ошибка перевода unicode.
    
    20 Warning — предупреждение, некритическая ошибка.
```

```    
    Посмотреть всю цепочку наследования конкретного типа исключения можно с помощью модуля inspect:
    
        import inspect
    
        print(inspect.getmro(TimeoutError))
    
        >>> (<class 'TimeoutError'>, <class 'OSError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
```

# Как создать свой тип Exception
```
    class MyError(Exception):
    def __init__(self, text):
        self.txt = text


    try:
        raise MyError('Моя ошибка')
    except MyError as er:
        print(er)
    
    >>> Моя ошибка
```