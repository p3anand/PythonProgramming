import time

def time_calculation(func):
    def wrapper():
        start_time=time.time()
        print("Start Time:", start_time)
        func()
        end_time=time.time()
        print("End Time:", end_time)
        print(f"Time taken for execution: {end_time-start_time}")
        print("-----------------")
    return wrapper()

@time_calculation # This is a decorator
def test_time1():
    print("This is from the function")
    time.sleep(3)

@time_calculation # This is a decorator
def test_time2():
    print("This is from the function")
    time.sleep(3)