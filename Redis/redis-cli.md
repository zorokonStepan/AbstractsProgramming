### start
```redis-cli```

### задать значения
```
    SET key value
    GET key
    
    GETSET key value  вернуть старое значение и задать новое
    
    SET key value EX 20 сохранить значение на 20 секунд 
    SET key value PX 20 сохранить значение на 20 милисекунд     
    
    HSET person1 name "Igor" задать хэш значение
    HSET person1 age 19      задать хэш значение
    HGET person1 name        получить значение по ключу хэша
    HGETALL person1          получить все key+value хэша
    HVALS person1            получить все value хэша
    HKEYS person1            получить все key хэша
    
    в Redis множества не упорядоченны, у них нет индексов
    SADD persons "Masha" добавить значение в множество persons
    SMEMBERS persons получить все значения множества
    SCARD persons количество элементов в множестве(кардинальное число множества)
    SUNION set1 set2 объединение двух множеств, т.е. все уникальные значения множеств
    SDIFF set1 set2   это set1 - set2
    SINTER set1 set2 пересечение множеств, т.е. общие элементы
    SPOP persons удаляет и возвращает случайный элемент множества

    списки - упорядоченные 
    LPUSH mylist "one"  добавить элемент в список с начала
    LRANGE mylist 0 1    вывести элементы с 0 по 1
    LRANGE mylist 0 -1  вывести  все элементы
    RPUSH mylist "two"  добавить элемент в список с конца
    LPOP mylist  слева одно значение удалить и вывести
    RPOP mylist справа одно значение удалить и вывести

    APPEND key value добовить к значению по ключу значение
```

### проверить существование ключа
```
    EXIST key
    вернет 1 если ключ существует или 0 если такого ключа нет
```

### работа с ключами
```
    KEYS * вывести все ключи. !НЕ ИСПОЛЬЗОВАТЬ В ПРОДАКШЕНЕ, т.к. она очень медленная (это совет разработчиков Redis)
```

### удалить значения
```
    FLUSHALL  удалить все ключи
```

### разные комманды
```    
    INCR key увеличить значение на 1
    DECR key уменьшение значения на 1 
```