### используют несколько процессов и/или потоков для обработки одновременных запросов
```
    uwsgi (http://projects.unbit.it/uwsgi);
    cherrypy (http://www.cherrypy.org/);
    pylons (http://www.pylonsproject.org/).
```

### серверы, основанные на событиях, которые пользуются одним процессом, но избегают блокирования любым одиночным запросом
```
     tornado (http://www.tornadoweb.org/);
     gevent (http://gevent.org/);
     gunicorn (http://gunicorn.org/).
```        
