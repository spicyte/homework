def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                
                if not isinstance(arg, type_):
                    print(f"Failed: Argument {arg} is not of type {type_}")
                    return False
                
               
                if isinstance(arg, str) and len(arg) > max_length:
                    print(f"Failed: Length of argument {arg} exceeds the maximum length {max_length}")
                    return False
                
                
                if contains and any(symbol not in arg for symbol in contains):
                    print(f"Failed: Argument {arg} does not contain the required symbols {contains}")
                    return False
            
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('05years') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
