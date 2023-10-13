```admin.ру — модуль административных настроек и классов-редакторов;```

### Варианты регистрации моделей
```
    1. admin.site.register(ModelName, ModelNameAdmin) или admin.site.register(ModelName)
    2.     
```

### admin.site.register(ModelName)
```
    from django.contrib import admin
    from .models import ModelName
        
    admin.site.register(ModelName)
        
    вызвали метод register() у экземпляра класса Adminsite, представляющего сам административный сайт и хранящегося в 
    переменной site модуля django.contrib.admin. 
    
    Этому методу мы передали в качестве параметра ссылку на класс нашей модели ModelName.
```

