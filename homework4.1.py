string1 = 'helloworld'
if len(string1) < 2:
    result1 = "Empty String"
else:
    result1 = string1[:2] + string1[-2:]
print(result1)  

string2 = 'my'
if len(string2) < 2:
    result2 = "Empty String"
else:
    result2 = string2[:2] + string2[-2:]
print(result2)

string3 = 'x'
if len(string3) < 2:
    result3 = "Empty String"
else:
    result3 = string3[:2] + string3[-2:]
print(result3)
