def calculate_square_divided_by_b():
    try:
        a = float(input("Значення a: "))
        b = float(input("Значення b: "))
        
        result = a**2 / b

        return result

    except ValueError:
        raise ValueError("Числа.")

    except ZeroDivisionError:
        raise ValueError("Значення b не може бути 0.")

try:
    result = calculate_square_divided_by_b()
    print("Результат:", result)

except ValueError as ve:
    print(f"Помилка: {ve}")
