def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    scale = input("Enter 'C' for Celsius or 'F' for Fahrenheit: ").strip().upper()
    temp = float(input("Enter temperature: "))

    if scale == 'C':
        print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
    elif scale == 'F':
        print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
    else:
        print("Invalid scale. Please enter 'C' or 'F'.")


