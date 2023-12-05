https://django.fun/ru/docs/django/4.2/topics/http/urls/

### ROOT_URLCONF
```
    Например: ROOT_URLCONF = 'kenton.urls'
    
    Django определяет используемый корневой модуль URLconf. 
    Обычно это значение параметра ROOT_URLCONF, но если входящий объект HttpRequest имеет атрибут urlconf 
    (установленный промежуточным программным обеспечением), его значение будет использоваться вместо параметра 
    ROOT_URLCONF.
```

### Конвертеры пути
```
    По умолчанию доступны следующие конвертеры пути:

    str - соответствует любой непустой строке, за исключением разделителя пути, '/'. Это значение по умолчанию, 
          если преобразователь не включен в выражение.
    int - соответствует нулю или любому положительному целому числу. Возвращает int.
    slug - соответствует любой строке заголовка, состоящей из букв или цифр ASCII, а также символов дефиса и 
           подчеркивания. Например, build-your-1st-django-site.
    uuid - соответствует форматированному UUID. Чтобы предотвратить сопоставление нескольких URL-адресов с одной и 
           той же страницей, необходимо использовать дефисы, а буквы должны быть строчными. Например, 
           075194d3-6885-417e-a8a8-6c931e272f00. Возвращает экземпляр UUID.
    path - соответствует любой непустой строке, включая разделитель пути, '/'. Это позволяет вам сопоставлять полный 
           путь URL, а не сегмент пути URL, как в случае с str.
```

### Захваченные параметры
```
    from django.urls import path

    from . import views
    
    urlpatterns = [
        path("articles/2003/", views.special_case_2003),
        path("articles/<int:year>/", views.year_archive),
        path("articles/<int:year>/<int:month>/", views.month_archive),
        path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),
    ]
    
    1. Чтобы получить(захватить) значение из URL-адреса, используйте угловые скобки.
    2. Захваченные значения могут дополнительно включать тип преобразователя. 
       Например, используйте <int:name> для захвата целочисленного параметра. 
       Если конвертер не включен, сопоставляется любая строка, за исключением символа /.
    3. Нет необходимости добавлять косую черту в начале, потому что она есть в каждом URL. Например, это articles, 
       а не /articles.   
    4. каждый шаблон требует, чтобы URL-адрес заканчивался косой чертой.   
```

### Использование регулярных выражений
```
    Для этого используйте re_path() вместо path().

    В регулярных выражениях Python для именованных групп регулярных выражений используется синтаксис 
    (?P<name>pattern), где name - имя группы, а pattern - некоторый шаблон для сопоставления.
```

### Включение других URLconfs
```
    В любой момент ваши urlpatterns могут «включать» другие модули URLconf. 
    По сути, это «корень» набора нижестоящих URL-адресов.
    
    from django.urls import include, path
    from . import views
    
    urlpatterns = [
        path(
            "<page_slug>-<page_id>/",
            include(
                [
                    path("history/", views.history),
                    path("edit/", views.edit),
                    path("discuss/", views.discuss),
                    path("permissions/", views.permissions),
                ]
            ),
        ),
    ]
```

### Передача дополнительных параметров функции предствления
```
    Функция path() может принимать необязательный третий аргумент, который должен быть словарем дополнительных 
    ключевых аргументов для передачи в функцию представление.
    
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path("blog/<int:year>/", views.year_archive, {"foo": "bar"}),
    ]
```

### Передача дополнительных параметров в include()
```
    from django.urls import include, path

    urlpatterns = [
        path("blog/", include("inner"), {"blog_id": 3}),
    ]
    
    # inner.py
    from django.urls import path
    from mysite import views
    
    urlpatterns = [
        path("archive/", views.archive),
        path("about/", views.about),
    ]
    
    Обратите внимание, что дополнительные параметры будут всегда передаваться каждой строке во включенном URLconf, 
    независимо от того, действительно ли представление строки принимает эти параметры как действительные. 
    По этой причине этот метод полезен только в том случае, если вы уверены, что каждое представление во включенном 
    URLconf принимает дополнительные параметры, которые вы передаете.
```

### Обратное разрешение URL-адресов
```
    В шаблонах: использование тега шаблона url.
    В коде Python: использование функции reverse().
    В коде более высокого уровня, связанном с обработкой URL-адресов экземпляров модели Django: метод get_absolute_url().
    
    
    from django.urls import path

    from . import views
    
    urlpatterns = [
        # ...
        path("articles/<int:year>/", views.year_archive, name="news-year-archive"),
        # ...
    ]
    
    *** Вы можете получить их в коде шаблона, используя: ***
    
    <a href="{% url 'news-year-archive' 2012 %}">2012 Archive</a>
    {# Or with the year in a template context variable: #}
    <ul>
        {% for yearvar in year_list %}
            <li><a href="{% url 'news-year-archive' yearvar %}">{{ yearvar }} Archive</a></li>
        {% endfor %}
    </ul>
    
    *** Или в коде Python: ***
    
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    
    
    def redirect_to_year(request):
        # ...
        year = 2006
        # ...
        return HttpResponseRedirect(reverse("news-year-archive", args=(year,)))
```

### Пространства имен URL
```
    Пространства имен URL-адресов позволяют однозначно перевернуть именованные URL, даже если разные приложения 
    используют одинаковые имена URL. 
    
    Пространство имен URL состоит из двух частей, каждая из которых является строкой:
    
    1. пространство имен приложения
    Оно описывает имя развертываемого приложения. 
    Каждый экземпляр одного приложения будет иметь одно и то же пространство имен приложения. 
    Например, приложение администратора Django имеет в некоторой степени предсказуемое пространство имен приложения 'admin'.
    
    2. пространство имен экземпляра
    Оно определяет конкретный экземпляр приложения. 
    Пространства имен экземпляров должны быть уникальными для всего вашего проекта. 
    Однако пространство имен экземпляра может быть таким же, как пространство имен приложения. 
    Это используется для указания экземпляра приложения по умолчанию. 
    Например, экземпляром администратора Django по умолчанию имеет пространство имен экземпляра 'admin'.
    
    URL-адреса в пространстве имен указываются с помощью оператора ':'.
    
    Например, ссылка на главную страницу индекса приложения администратора осуществляется с помощью 'admin:index'. 
    Это указывает на пространство имен 'admin' и именованный URL 'index'.
    
    Пространства имен также могут быть вложенными. Именованный URL-адрес 'sports:polls:index' будет искать шаблон с 
    именем 'index' в пространстве имен 'polls', который сам определен в пространстве имен верхнего уровня 'sports'.
```

### Реверсирование пространств имён URL
пример двух экземпляров приложения polls: один под названием 'author-polls', а другой - publisher-polls'.
```    
    from django.urls import include, path

    urlpatterns = [
        path("author-polls/", include("polls.urls", namespace="author-polls")),
        path("publisher-polls/", include("polls.urls", namespace="publisher-polls")),
    ]
    
    *** --- ***
    
    from django.urls import path
    from . import views
    
    app_name = "polls"
    
    urlpatterns = [
        path("", views.IndexView.as_view(), name="index"),
        path("<int:pk>/", views.DetailView.as_view(), name="detail"),
        ...,
    ]
```

### Пространства имен URL и включенные URLconfs
```
    Пространства имен ПРИЛОЖЕНИЙ включенных URLconfs можно указать двумя способами.

    1. установить атрибут app_name во включенном модуле URLconf на том же уровне, что и атрибут urlpatterns. 
    Вы должны передать фактический модуль или строковую ссылку на модуль в include(), а не сам список urlpatterns.
    URL-адреса, определенные в polls.urls, будут иметь пространство имен приложения polls.
    
    polls.urls.py:
    
        from django.urls import path
        from . import views
        
        app_name = "polls"
        
        urlpatterns = [
            path("", views.IndexView.as_view(), name="index"),
            path("<int:pk>/", views.DetailView.as_view(), name="detail"),
            ...,
        ]
    
    urls.py
    
        from django.urls import include, path
    
        urlpatterns = [
            path("polls/", include("polls.urls")),
        ]
        
    2. включить объект, содержащий встроенные данные пространства имен. 
    Если вы include() список экземпляров path() или re_path(), то URL, содержащиеся в этом объекте, будут добавлены в 
    глобальное пространство имен. Однако можно также include() 2-кортеж, содержащий:    
    (<list of path()/re_path() instances>, <application namespace>)
    
    from django.urls import include, path
    from . import views
    
    polls_patterns = (
        [
            path("", views.IndexView.as_view(), name="index"),
            path("<int:pk>/", views.DetailView.as_view(), name="detail"),
        ],
        "polls",
    )
    
    urlpatterns = [
        path("polls/", include(polls_patterns)),
    ]
    
    Это будет включать назначенные шаблоны URL-адресов в заданное пространство имен приложения.
    
    ===================================================================================================================
    
    Пространство имен ЭКЗЕМПЛЯРА можно указать с помощью аргумента namespace для include(). 
    Если пространство имен экземпляра не указано, по умолчанию будет использоваться пространство имен приложения 
    включенного URLconf. Это означает, что он также будет экземпляром по умолчанию для этого пространства имен.
```