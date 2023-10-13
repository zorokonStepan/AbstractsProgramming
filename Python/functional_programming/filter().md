```
    >>> filter (bool, ['spam', '', 'ni'])
    <filter object at 0x00000000029B7B70>
    
    >>> list(filter(bool, ['spam', '', 'ni']))
    ['spam', 'ni']
```