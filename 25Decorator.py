import random
import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Executing {func.__name__} took {end_time - start_time} seconds.")
        return result
    return wrapper

@log_execution_time
def simulate_long_task():
    time.sleep(random.randint(1, 3))
    print("Task completed.")


simulate_long_task()    