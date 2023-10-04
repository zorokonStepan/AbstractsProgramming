https://django.fun/ru/docs/django/4.2/ref/urls/#django.urls.path

### path(route, view, kwargs=None, name=None)
```
    Возвращает элемент для включения в urlpatterns
    
    1. Аргумент route должен быть строкой или gettext_lazy(), содержащей шаблон URL. 
       
       1.1. Строка может содержать угловые скобки (как <username>), чтобы захватить часть URL и отправить ее в качестве 
       аргумента ключевого слова в представление. 
       1.2. Угловые скобки могут включать спецификацию конвертера (например, int часть <int:section>), 
       которая ограничивает совпадающие символы, а также может изменить тип переменной, передаваемой представлению. 
       Например, <int:section> соответствует строке десятичных цифр и преобразует значение в int.
       
    2. Аргумент view является функцией представления или результатом as_view() для представлений на основе классов. 
    Он также может быть django.urls.include().
    
    3. Аргумент kwargs должен быть словарем дополнительных ключевых аргументов для передачи в функцию представление.  
    
    4. Аргумент name - Обратное разрешение URL-адресов. Так задается имя для маршрута.
    
    ===================================================================================================================
    
    from django.urls import include, path

    urlpatterns = [
        path("index/", views.index, name="main-view"),
        path("bio/<username>/", views.bio, name="bio"),
        path("articles/<slug:title>/", views.article, name="article-detail"),
        path("articles/<slug:title>/<int:section>/", views.section, name="article-section"),
        path("blog/", include("blog.urls")),
        ...,
    ]
```

### re_path(route, view, kwargs=None, name=None)
```
    Возвращает элемент для включения в urlpatterns
    
    1. route - регулярное выражение.
    
    Аргументы view, kwargs и name такие же, как и для path(). 
    
    ===================================================================================================================
    
    from django.urls import include, re_path

    urlpatterns = [
        re_path(r"^index/$", views.index, name="index"),
        re_path(r"^bio/(?P<username>\w+)/$", views.bio, name="bio"),
        re_path(r"^blog/", include("blog.urls")),
        ...,
    ]
```

### include()
```
    include(module, namespace=None)
    include(pattern_list)
    include((pattern_list, app_namespace), namespace=None)
    
    Функция, принимающая полный путь импорта Python к другому модулю URLconf, который должен быть «включен» в это место.
    
    module              – Модуль URLconf (или имя модуля)
    namespace (str)     – Пространство имен экземпляра для включаемых записей URL
    pattern_list        – Итерабельность экземпляров path() и/или re_path().
    app_namespace (str) – Пространство имен приложения для включаемых записей URL
```

### reverse().
```
    Текущее приложение можно указать с помощью аргумента current_app функции reverse().(Реверсирование пространств имён URL)
```