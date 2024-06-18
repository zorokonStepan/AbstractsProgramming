import yappi


def write_to_file_profiling_result_use_yappi(filename_pstats, filename_callgrind):
    def wrapper(func):
        def inner(*args, **kwargs):
            yappi.start()  # Здесь начинается наблюдение за выполняемым кодом

            func(*args, **kwargs)

            func_stats = yappi.get_func_stats()  # Собираем статистику выполненных функций
            func_stats.print_all()  # Выведем в консоль собранную статистику
            func_stats.save(filename_pstats, 'PSTAT')  # Сохраняем в формате pstat
            func_stats.save(filename_callgrind, 'CALLGRIND')  # Сохраняем в формате callgrind
            yappi.stop()  # Останавливаем наблюдение
            yappi.clear_stats()  # Очищаем статистику
        return inner
    return wrapper


# view report: snakeviz filename_pstats.pstats
