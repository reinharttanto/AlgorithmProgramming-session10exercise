def convert_to_celsius(t):
    c = (5 / 9) * (t - 32)
    return c


def convert_to_kelvin(t):
    k = t + 273.15
    return k


def convert_temp():
    f = int(input("Enter a temperature in Fahrenheit: "))

    c = convert_to_celsius(f)
    k = convert_to_kelvin(c)

    print("")
    print("The temperature in Fahrenheit is:", f)
    print("The temperature in Celsius is:", c)
    print("The temperature in Kelvin is:", k)


