class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32


check_temperature = TemperatureConverter.celsius_to_fahrenheit(30)
lets_check = f"\nTemperature in Fahrenheit: {check_temperature} F.\n"
print(lets_check)
