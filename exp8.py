def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        celsius_temp = float(input("Enter temperature in Celsius: "))
        fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
        print(f"{celsius_temp}°C is equal to {fahrenheit_temp:.2f}°F")
    elif choice == '2':
        fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
        celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
        print(f"{fahrenheit_temp}°F is equal to {celsius_temp:.2f}°C")
    elif choice == '3':
        print("Exiting the Temperature Converter. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
