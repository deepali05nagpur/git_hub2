def upper(func):
    def  wrapper():
        function=func()
        return function.upper()
    return wrapper
@upper
def display():
    return "python is programming language"

print(display())
