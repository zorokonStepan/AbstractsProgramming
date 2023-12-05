```
    Result имеет множество методов для получения и преобразования строк, один из них - Result.all(). 
    
    В дополнении к этому сам объект Result также реализует интерфейс итератора Python, так что мы можем проходить по 
    всем элементам с помощью циклов. Строка (или Row) - это объект, который ведет себя как именованный кортеж в
    Python, у нас есть несколько способов получать данные из него:
    
        1. Получение в виде кортежа:        
            result = conn.execute(text("select x, y from some_table"))
                for x, y in result:
                    # ...
    
        2. Получение данных по индексу:        
            result = conn.execute(text("select x, y from some_table"))
                for row in result:
                    x = row[0]
                    
        3. Получение данных по имени - мы можем использовать функционал именованных кортежей:
            result = conn.execute(text("select x, y from some_table"))
                for row in result:
                    y = row.y
                    print(f"Row: {row.x} {y}")
                    
        4. Получение в виде ассоциативных массивов (карт) - для получения строк в качестве ассоциативных массивов 
           Python, которые по сути являются неизменяемой версией словарей, объект Result имеет такой метод как 
           Result.mappings(), преобразующий все строчки в подобные словарю RowMapping объекты.
            result = conn.execute(text("select x, y from some_table"))
            for dict_row in result.mappings():
                x = dict_row["x"]
                y = dict_row["y"]
```