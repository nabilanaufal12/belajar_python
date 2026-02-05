def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Sesuatu terjadi sebelum fungsi dipanggil.") # Logika tambahan
        result = func(*args, **kwargs) # Memanggil fungsi asli
        print("Sesuatu terjadi setelah fungsi dipanggil.") # Logika tambahan
        return result
    return wrapper # Mengembalikan fungsi wrapper
    
@my_decorator # Ini sama dengan 'say_hello = my_decorator(say_hello)'
def say_hello(name):
    print(f"Halo, {name}!")

@my_decorator
def add(a, b):
    print(f"Menambahkan {a} dan {b}")
    return a + b

say_hello("Dunia")
print(f"Hasil penambahan: {add(10, 20)}")


### Decorator dengan Argumen
def repeat(num_times):
    def decorators_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorators_repeat

@repeat(num_times=3) # Decorator dengan argumen
def greet(name):
    print(f"Salam, {name}!")

greet("Python")


### `functools.wraps`
from functools import wraps

def my_decorator(func):
    @wraps(func) # Mempertahankan metadata fungsi asli
    def wrapper(*args, **kwargs):
        """
        Docstring for wrapper
        
        :param args: Description
        :param kwargs: Description
        """
        print("Sebelum fungsi.")
        result = func(*args, **kwargs)
        print("Sesudah fungsi.")
        return result
    return wrapper

@my_decorator
def example_function():
    """
    Docstring for example_function
    """
    print("Fungsi contoh sedang berjalan.")

example_function()
print(f"Nama fungsi: {example_function.__name__}") # Akan mencetak 'example_function'
print(f"Docstring: {example_function.__doc__}") # Akan mencetak 'Ini adalah fungsi contoh'