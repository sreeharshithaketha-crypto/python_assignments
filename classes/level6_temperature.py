# Q10: Convert Celsius to Fahrenheit and Fahrenheit to Celsius.
class Temperature:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

temperature = Temperature()
print(temperature.celsius_to_fahrenheit(25))
print(temperature.fahrenheit_to_celsius(77))
