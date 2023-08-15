### Основные команды
```
    SELECT - выбор данных
    
    DISTINCT - аргумент, дающий возможность исключить дублирующися значения из результатов выборки.
               Т.е. в результате будут только уникальные строки.
               
    ALL - противоположность DISTINCT. Если не заданы ни ALL ни DISTINCT, по умолчанию используется ALL.
    
    WHERE - определение выборки
```

### Примеры
```
SELECT
    
    SELECT * FROM table;
    
    SELECT column*, ..., column* FROM table;
    
DISTINCT    

    SELECT DISTINCT snum FROM Orders; 
    
WHERE    
    SELECT sname, city FROM Salespeople WHERE city = 'London';     
```