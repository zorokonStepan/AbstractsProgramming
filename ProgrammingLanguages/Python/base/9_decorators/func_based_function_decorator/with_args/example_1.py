import time


def retry(max_retries):
    def retry_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    func(*args, **kwargs)
                except:
                    time.sleep(1)
        return wrapper
    return retry_decorator


@retry(5)
def might_fail():
    print("might_fail")
    raise Exception


might_fail()
