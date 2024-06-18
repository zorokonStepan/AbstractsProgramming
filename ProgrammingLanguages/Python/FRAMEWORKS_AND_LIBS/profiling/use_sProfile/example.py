import cProfile
import pstats
import io


def write_to_file_profiling_result(filename):
    def wrapper(func):
        def inner(*args, **kwargs):
            pr = cProfile.Profile()
            pr.enable()

            func(*args, **kwargs)

            pr.disable()
            s = io.StringIO()
            ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
            ps.print_stats()

            with open(filename, 'w+') as f:
                f.write(s.getvalue())

        return inner
    return wrapper

# view report: snakeviz filename.prof
