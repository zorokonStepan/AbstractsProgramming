```
    Использовать SQLAlchemy можно на нескольких уровнях.
    
    1. Уровень движка. 
       Самый низкий уровень управляет пулами соединений с базами данных, выполняет команды SQL и возвращает результат. 
       Это ближе всего к DB-API.
    
    2. Язык выражений SQL.
       Следующий уровень — язык выражений SQL, который позволяет вам выражать запросы более Python-ориентированным 
       способом.
       
    3. ORM.
       Самый высокий уровень — это ORM (Object Relational Model — объектно-реляционная модель), который использует язык 
       выражений SQL Expression Language и связывает код приложения с реляционными структурами данных.
```

### 1. Уровень движка. 
```
    import sqlalchemy as sa
    
    conn = sa.create_engine('sqlite://')
    
    conn.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)''')
    
    # **************************************************
    
    ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
    conn.execute(ins, 'duck', 10, 0.0) 
    conn.execute(ins, 'bear', 2, 1000.0)
    conn.execute(ins, 'weasel', 1, 2000.0)

    rows = conn.execute('SELECT * FROM zoo')
    
    for row in rows:
        print(row)
```

### 2. Язык выражений SQL.
```
    import sqlalchemy as sa
    
    conn = sa.create_engine('sqlite://')

    meta = sa.MetaData()
    
    zoo = sa.Table(
                'zoo', 
                meta,
                sa.Column('critter', sa.String, primary_key=True),
                sa.Column('count', sa.Integer),
                sa.Column('damages', sa.Float)
            )
    meta.create_all(conn)
    
    # **************************************************
    
    conn.execute(zoo.insert(('bear', 2, 1000.0)))
    conn.execute(zoo.insert(('weasel', 1, 2000.0)))
    conn.execute(zoo.insert(('duck', 10, 0)))
    
    result = conn.execute(zoo.select())
    
    rows = result.fetchall()
    print(rows)  # [('bear', 2, 1000.0), ('weasel', 1, 2000.0), ('duck', 10, 0.0)
```

### 3. ORM.
```
    import sqlalchemy as sa
     
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker


    conn = sa.create_engine('sqlite:///zoo.db')
    
    Session = sessionmaker(bind=conn)
    session = Session()
    
    Base = declarative_base()
 
    class Zoo(Base):
        __tablename__ = 'zoo'
        critter = sa.Column('critter', sa.String, primary_key=True)
        count = sa.Column('count', sa.Integer)
        damages = sa.Column('damages', sa.Float)
        
        def __init__(self, critter, count, damages):
            self.critter = critter
            self.count = count
            self.damages = damages
        
        def __repr__(self):
            return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)
            
    Base.metadata.create_all(conn)


    first = ('duck', 10, 0.0)
    second = Zoo('bear', 2, 1000.0)
    third = Zoo('weasel', 1, 2000.0)
    
    session.add(first)
    session.add_all([second, third])
    
    session.commit()
```