```
    async def - создать сопрограмму
    await - вызов сопрограммы. Вызов сопрограммы вне цикла событий с помощью await останавливает
    программу в ожидании результата. Если последовательно await корутины, то получится синхронный код    
```

### Создание задачи
```
    import asyncio
    from util import delay
    
    async def main():
    
        sleep_for_three = asyncio.create_task(delay(3))        
        print(type(sleep_for_three))
        result = await sleep_for_three
        print(result)
    
    asyncio.run(main())
```

###  Конкурентное выполнение нескольких задач
```
    import asyncio
    from util import delay
    
    async def main():
    
        sleep_for_three = asyncio.create_task(delay(3))
        sleep_again = asyncio.create_task(delay(3))
        sleep_once_more = asyncio.create_task(delay(3))
        
        await sleep_for_three
        await sleep_again
        await sleep_once_more
        
    asyncio.run(main())
```

### Ожидание будущего объекта
```
    from asyncio import Future
    import asyncio
    
    
    def make_request() -> Future:
        future = Future()
        asyncio.create_task(set_future_value(future))
        return future
        
        
    async def set_future_value(future) -> None:
        await asyncio.sleep(1)
        future.set_result(42)
        
        
    async def main():
        future = make_request()
        print(f'Будущий объект готов? {future.done()}')
        value = await future
        print(f'Будущий объект готов? {future.done()}')
        print(value)
        
        
    asyncio.run(main())
```

### Связь между будущими объектами, задачами и сопрограммами
```
    class Awaitable --> class Coroutine
    class Awaitable --> class Future --> class Task
```

### Конкурентное выполнение запросов с помощью gather
```
    Для конкурентного выполнения допускающих ожидание объектов широко используется функция asyncio.gather. 
    Она принимает последовательность допускающих ожидание объектов и запускает их конкурентно всего в одной
    строке кода. Если среди объектов есть сопрограмма, то gather автоматически обертывает ее задачей, чтобы 
    гарантировать конкурентное выполнение. Это значит, что не нужно отдельно обертывать все сопрограммы по 
    отдельности с помощью функции asyncio.create_task
    
    asyncio.gather возвращает объект, допускающий ожидание. Если использовать его в выражении await, то 
    выполнение будет приостановлено, пока не завершатся все переданные объекты. А когда это произойдет, 
    asyncio.gather вернет список результатов работы.
    
    
    import asyncio
    from aiohttp import ClientSession
    
    from Python.book_abstracts.Asycio_MatthewFowler.code.util.async_timer import async_timed
    from Python.book_abstracts.Asycio_MatthewFowler.code.util.fetch_status import fetch_status
    
    
    @async_timed()
    async def main():
        async with ClientSession() as session:
            urls = ['https://example.com' for _ in range(1000)]
            requests = [fetch_status(session, url) for url in urls]
            status_codes = await asyncio.gather(*requests)
            print(status_codes)
    
    
    asyncio.run(main())
    
    -----------------------------------------------------------------------------------------------------
    Функция gather гарантирует детерминированный порядок результатов, несмотря на недетерминированность 
    их получения. На внутреннем уровне gather использует для этой цели специальную реализацию future.
    
    import asyncio
    from util import delay
    
    
    async def main():
        results = await asyncio.gather(delay(3), delay(1))
        print(results)
        
        
    asyncio.run(main())
    
    Здесь мы передали gather две сопрограммы. Первой для завершения требуется 3 с, второй  – одна. 
    Можно ожидать, что результатом будет список [1, 3], потому что односекундная сопрограмма завершается 
    раньше трехсекундной. Но на самом деле возвращается [3, 1] – в том порядке, в каком сопрограммы передавались.
```