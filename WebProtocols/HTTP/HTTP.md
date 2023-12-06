### Сервис RESTful использует глаголы HTTP определенными способами:
- HEAD   - получает информацию о ресурсе, но не его данные;
- GET    - получает данные ресурса с сервера. 
           Это стандартный метод, используемый вашим браузером. 
           GET не должен применяться для создания, изменения или удаления данных;
- POST   - создает новый ресурс;
- PUT    - заменяет существующий ресурс, создавая его, если его нет;
- PATCH  - частично обновляет ресурс;
- DELETE - удаляет ресурс. 

#### https://ru.stackoverflow.com/questions/1070324/Разница-отличия-между-put-и-patch-в-rest
```
    Представьте, что у вас на сайте публикуются статьи. 
    У статей есть заголовок и содержание, которые вы можете редактировать.

        PUT /articles/12
        
        {
          title: 'Новый заголовок',
          content: 'Новое содержание'
        }
        PATCH /articles/12
        
        {
          title: 'Новый заголовок',
          content: 'Новое содержание'
        }
    
    Они работают идентично. Отличия возникают, если вы изменяете например только заголовок.

        PUT /articles/12
        
        {
          title: 'Новый заголовок'
        }
        
        PATCH /articles/12
        
        {
          title: 'Новый заголовок'
        }
    
    Первый запрос изменит заголовок title и очистит поле content, потому что вы его не передали. 
    PUT меняет объект целиком.
    
    Второй запрос изменит только поле заголовок, не трогая поля content, потому что вы его не передали. 
    PATCH изменяет отдельные поля ресурса.
```