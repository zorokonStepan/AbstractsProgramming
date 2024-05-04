```
    • tmp_path and tmp_path_factory: для временных каталогов
    
    • capsys: для захвата выходных данных
    
    • capfd: Похож на capsys, но захватывает файловые дескрипторы 1 и 2, которые обычно совпадают с stdout и stderr
    
    • capsysbinary: Там, где capsys захватывает текст, capsysbinary захватывает байты.
    
    • capfdbinary: Захватывает байты в файловых дескрипторах 1 и 2
    
    • caplog: Захватывает выходные данные, записанные с помощью logging packag
    
    • monkeypatch: для изменения среды или кода приложения, например, упрощенная форма имитации
        The monkeypatch fixture provides the following functions:
            • setattr(target, name, value, raising=True) — Sets an attribute
            • delattr(target, name, raising=True) — Deletes an attribute
            • setitem(dic, name, value) — Sets a dictionary entry
            • delitem(dic, name, raising=True) — Deletes a dictionary entry
            • setenv(name, value, prepend=None) — Sets an environment variable
            • delenv(name, raising=True) — Deletes an environment variable
            • syspath_prepend(path) — Prepends path to sys.path, which is Python’s list of import locations
            • chdir(path) — Changes the current working directory
            
    • capfd, capfdbinary, capsysbinary — Варианты capsys, которые работают с файловыми дескрипторами и/или двоичным 
      выводом
      
    • caplog — Похож на capsys и ему подобные; используется для сообщений, созданных с помощью системы логирования 
      Python
    
    • cache — Используется для хранения и извлечения значений между запусками pytest. Самая полезная часть этого 
      приспособления заключается в том, что оно позволяет использовать флаги --last-failed, --failed-first и подобные.
    
    • doctest_namespace — Полезно, если вы хотите использовать pytest для запуска тестов в стиле doctest
    
    • pytestconfig — Используется для получения доступа к конфигурационным значениям, pluginmanager и plugin hooks
    
    • record_property, record_testsuite_property — Используется для добавления дополнительных свойств в тест или набор 
      тестов. Особенно полезно для добавления данных в XML-отчет, который будет использоваться инструментами непрерывной
      интеграции
    
    • recwarn — Используется для тестирования предупреждающих сообщений
    
    • request — Используется для предоставления информации о выполняемой тестовой функции. Чаще всего используется при 
      параметризации fixtures
    
    • pytester, testdir — Используется для предоставления временного тестового каталога, помогающего в запуске и 
      тестировании плагинов pytest. pytester - это основанная на pathlib замена testdir на основе py.path.
    
    • tmpdir, tmpdir_factory — Аналогично tmp_path и tmp_path_factory; Используется для возврата объекта py.path.local 
      вместо объекта pathlib.Path
```