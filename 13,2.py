def outer_function(outer_variable):
    def inner_function(inner_variable):
        
        result = outer_variable + inner_variable
        return result


    return inner_function

outer_instance = outer_function(10)

result = outer_instance(5)

print(result)
