https://habr.com/ru/companies/ruvds/articles/426413/

# Вот как расшифровывается акроним SOLID:
```
    S: Single Responsibility Principle (Принцип единственной ответственности).
    O: Open-Closed Principle (Принцип открытости-закрытости).
    L: Liskov Substitution Principle (Принцип подстановки Барбары Лисков).
    I: Interface Segregation Principle (Принцип разделения интерфейса).
    D: Dependency Inversion Principle (Принцип инверсии зависимостей).
```

## S: Single Responsibility Principle (Принцип единственной ответственности).
```
    Класс должен быть ответственен лишь за что-то одно. Если класс отвечает за решение нескольких задач, его подсистемы, 
    реализующие решение этих задач, оказываются связанными друг с другом. Изменения в одной такой подсистеме ведут к 
    изменениям в другой.     
   
    этот принцип применим не только к классам, но и к компонентам программного обеспечения в более широком смысле.
   
    Вот что по этому поводу говорит Стив Фентон: «Проектируя классы, мы должны стремиться к тому, чтобы объединять 
    родственные компоненты, то есть такие, изменения в которых происходят по одним и тем же причинам. 
    Нам следует стараться разделять компоненты, изменения в которых вызывают различные причины».

    Правильное применение принципа единственной ответственности приводит к высокой степени связности элементов внутри 
    модуля, то есть к тому, что задачи, решаемые внутри него, хорошо соответствуют его главной цели.
```

## O: Open-Closed Principle (Принцип открытости-закрытости).
```
    Программные сущности (классы, модули, функции) должны быть открыты для расширения, но не для модификации.    
```

## L: Liskov Substitution Principle (Принцип подстановки Барбары Лисков).
```
    Необходимо, чтобы подклассы могли бы служить заменой для своих суперклассов.
    
    Цель этого принципа заключаются в том, чтобы классы-наследники могли бы использоваться вместо родительских классов, 
    от которых они образованы, не нарушая работу программы. Если оказывается, что в коде проверяется тип класса, значит 
    принцип подстановки нарушается.    
```

## I: Interface Segregation Principle (Принцип разделения интерфейса).
```
    Создавайте узкоспециализированные интерфейсы, предназначенные для конкретного клиента. 
    Клиенты не должны зависеть от интерфейсов, которые они не используют.
    
    Клиенты не должны реализовывать методы, которые им не нужно использовать. 
    Кроме того, этот принцип указывает на то, что интерфейс должен решать лишь какую-то одну задачу 
    (в этом он похож на принцип единственной ответственности), поэтому всё, что выходит за рамки этой задачи, 
    должно быть вынесено в другой интерфейс или интерфейсы.
```

## D: Dependency Inversion Principle (Принцип инверсии зависимостей).
```
    Объектом зависимости должна быть абстракция, а не что-то конкретное.
    
    1. Модули верхних уровней не должны зависеть от модулей нижних уровней. 
       Оба типа модулей должны зависеть от абстракций.
    2. Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.
```