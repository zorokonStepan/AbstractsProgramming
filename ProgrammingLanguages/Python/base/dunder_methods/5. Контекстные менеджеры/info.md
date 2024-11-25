```
    Любой объект может быть представлен как контекстный менеджер, который вызывается с помощью with или async with. 
    Данная конструкция позволяет выполнить какие-либо действия по настройке объекта и при выходе из контекстного 
    менеджера, произвести какие-либо действия по очистке, не смотря на то, было ли вызвано исключение в блоке 
    контекстного менеджера.

    __enter__(self) — определяет начало блока контекстного менеджера, вызванного с помощью with
    
    __exit__(self, exc_type, exc_value, traceback) — определяет конец блока контекстного менеджера. 
    Может использоваться для контролирования исключений, очистки, или любых действий, которые должны быть выполнены 
    после блока внутри with. Если блок выполнился успешно, то все три аргумента 
    (exc_type, exc_value и traceback) будут установлены в значение None.
    
    Например:
    >>> class ContextManager:
    >>>     def __enter__(self):
    >>>         log("entering context")
    >>>
    >>>     def __exit__(self, exc_type, exc_value, traceback):
    >>>         log("exiting context")
    >>>
    >>> with ContextManager():
    ...     print("in context manager")
    ...
    ... 'entering context'
    ... 'in context manager'
    ... 'exiting context'
    
    < ---------------------------------------------------------------------------------------------------------------- >
    
    __aenter__(self) — аналогично __enter__, только функция возвращает корутину (результат которой можно получить с 
                       помощью await)

    __aexit__(self, exc_type, exc_value, traceback) — аналогично __exit__, только функция возвращает корутину 
                                                      (результат которой можно получить с помощью await)
                                                      
    >>> class AsyncContextManager:
    >>>     async def __aenter__(self):
    >>>         await log("entering context")
    >>>
    >>>     async def __aexit__(self, exc_type, exc_value, traceback):
    >>>         await log("exiting context")
    >>>
    >>> async with AsyncContextManager():
    ...     print("in context manager")
    ...
    ... 'entering context'
    ... 'in context manager'
    ... 'exiting context'
```