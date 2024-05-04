```
    @pytest.mark.parametrize("start_state", ["done", "in prog", "todo"])
    def test_finish_simple(cards_db, start_state):
        c = Card("write a book", state=start_state)
        index = cards_db.add_card(c)
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == "done"
```

```
    @pytest.fixture(params=["done", "in prog", "todo"])
    def start_state(request):
        return request.param
    
    
    def test_finish(cards_db, start_state):
        c = Card("write a book", state=start_state)
        index = cards_db.add_card(c)
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == "done"
```

```
    def pytest_generate_tests(metafunc):
        if "start_state" in metafunc.fixturenames:
            metafunc.parametrize("start_state", ["done", "in prog", "todo"])
    
    
    def test_finish(cards_db, start_state):
        c = Card("write a book", state=start_state)
        index = cards_db.add_card(c)
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == "done"
```

Результат одинаковый