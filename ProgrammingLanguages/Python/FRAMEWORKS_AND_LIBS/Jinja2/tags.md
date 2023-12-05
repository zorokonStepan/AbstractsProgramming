# {% with %}
```
    Шаблонный тег {% with %} полезен тем, что он позволяет избегать многократного обращения к базе данных или 
    к дорогостоящим методам.
    
    {% with comments.count as total_comments %}
        <h2>{{ total_comments }} comment{{ total_comments|pluralize }}</h2>
    {% endwith %}
```
