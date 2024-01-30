def celsius_converter(value):
    celsius =  (value * 1.8)+32
    return celsius

def fahrenheit_converter(value):
    fahrenheit= (value- 32) * 5/9
    return fahrenheit

print(celsius_converter(32),'C')
print(fahrenheit_converter(89.6),'F')