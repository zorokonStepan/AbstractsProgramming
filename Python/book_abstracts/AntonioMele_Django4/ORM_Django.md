```
    Встроенный в Django ORM-преобразователь основан на итерируемых наборах запросов QuerySet. 
    
    Итерируемый набор запросов QuerySet – это коллекция запросов к базе данных, предназначенных для извлечения объектов 
    из базы данных. К наборам запросов можно применять фильтры, чтобы сужать результаты запросов на основе заданных 
    параметров.
        
    Наборы запросов QuerySet в Django являются ленивыми, то есть они вычисляются только тогда, когда это приходится 
    делать. Подобное поведение придает наборам запросов QuerySet большую эффективность. Если не назначать набор 
    запросов QuerySet переменной, а вместо этого писать его непосредственно в оболочке Python, то инструкция SQL 
    набора запросов будет исполняться, потому что вы побуждаете ее генерировать результат    
```

```
    class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def __str__(self):
        return self.title
```

#### Создание записи
```
     post = Post(title='Another post', slug='another-post', body='Post body.', author=user)
     post.save()
     
     или
     
     Post.objects.create(title='One more post', slug='one-more-post', body='Post body.', author=user)
```

#### Обновление записи
```
    post.title = 'New title'
    post.save()
```

#### Извлечение записи
```
    all_posts = Post.objects.all()
    
    Post.objects.get()
```


#### Применение метода filter()
```
    Post.objects.filter(publish__year=2022, author__username='admin')
    или то же самое
    Post.objects.filter(publish__year=2022).filter(author__username='admin')
    
    Запросы с операциями поиска в полях формируются с использованием двух знаков подчеркивания, 
    например publish__year, но те же обозначения также используются для обращения к полям ассоциированных моделей, 
    например author__username
```