import inspect

def sample_function():
    var1 = 10
    var2 = "Hello"
    var3 = [1, 2, 3]

def count_local_variables(func):
    _, _, _, local_vars = inspect.getargvalues(inspect.currentframe())
    return len(local_vars['locals'])

num_locals = count_local_variables(sample_function)
print(f"The number of local variables in the function is: {num_locals}")
