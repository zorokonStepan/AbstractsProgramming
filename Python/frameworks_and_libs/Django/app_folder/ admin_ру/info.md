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

###  Редактор модели
```
    Класс редактора объявляется как производный от класса ModelAdmin из модуля django.contrib.admin. 
    
    Он содержит набор атрибутов класса, которые и задают параметры представления модели. 
    
    list_display — последовательность имен полей, которые должны выводиться в списке записей;
    list_display_links — последовательность имен полей, которые должны быть преобразованы в гиперссылки, 
                         ведущие на страницу правки записи;
    search_fields — последовательность имен полей, по которым должна выполняться фильтрация.

    class BboardAdmin(admin.ModelAdmin):
        list_display = ('title', 'content', 'price', 'published')
        list_display_links = ('title', 'content')
        search_fields = ('title', 'content', )


    admin.site.register(Bboard, BboardAdmin)
```