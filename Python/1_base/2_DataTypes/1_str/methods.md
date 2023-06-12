```
    text.split(seporator)               --> list[str, ..., str]
    seporator.join(list[str, ..., str]) --> new_text
    
    text.replace(old, new, count) --> new_text  # if not count then replace all
    
    text.strip(symbols)  --> new_text удалить справа и слева символы, если без аргументов - пробелы
    text.lstrip(symbols) --> new_text
    text.rstrip(symbols) --> new_text
    
    # РЕГИСТР
    text.capitalize()    --> new_text с большой буквы первое слово
    text.title()         --> new_text все слова с большой буквы
    text.upper()         --> new_text все слова большими буквами
    text.lower()         --> new_text все слова маленькими буквами
    text.swapcase()      --> new_text сменить регистры букв на противоположный
       
    # ПОИСК И ВЫБОР   
    text.find(symbols)  --> index or -1
    text.index(symbols) --> index or exception
    
    text.rfind(symbols)  --> index or -1
    text.rindex(symbols) --> index or exception
    
    text.count(word)  --> количество вхождений word в text 
    
    # ВЫРАВНИВАНИЕ
    text.center(number: int)
    text.ljust(number: int)
    text.rjust(number: int)
    
    # ПРОВЕРКИ СТРОКИ    
    text.startswith(symbols) --> boolean
    text.endswith(symbols)   --> boolean
    text.isalnum()           --> boolean все символы в text буквы или цифры  
```