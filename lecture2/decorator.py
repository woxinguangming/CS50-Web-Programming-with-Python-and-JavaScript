# 装饰器中，函数可以像值一样作为参数传进来，
# 修改函数，然后在返回修改的函数

def anounce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")
    return wrapper

# hello函数使用装饰器anounce()

@anounce
def hello():
    print("Hello, World!")        

hello()