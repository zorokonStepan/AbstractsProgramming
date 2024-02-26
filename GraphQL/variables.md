```
        Вместо того чтобы иметь дело со строками, давайте применять имена переменных, которым в GraphQL всегда 
    предшествует символ $:

    mutation createSong($title:String! $numberOne:Int $by:String!) {
        addSong(title:$title, numberOne:$numberOne, performerName:$by)
            {
                id
                title
                numberOne
            }
        }
```