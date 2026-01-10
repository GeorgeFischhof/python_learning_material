
class ConvertedUnit:
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit


def convert_meters_to_feet(meters) -> ConvertedUnit:
    return ConvertedUnit(value=meters*3.28084, unit="feet")


def convert_feet_to_meters(feet) -> ConvertedUnit:
    return ConvertedUnit(value=feet*0.3048, unit="meters")


def convert_celsius_to_fahrenheit(celsius) -> ConvertedUnit:
    return ConvertedUnit(value=celsius*1.8+32, unit="Fahrenheit")


def convert_fahrenheit_to_celsius(fahrenheit) -> ConvertedUnit:
    return ConvertedUnit(value=fahrenheit-32/1.8, unit="Celsius")


def unit_converter():

    conversion_functions = {
        "c": convert_celsius_to_fahrenheit,
        "f": convert_fahrenheit_to_celsius,
        "m": convert_meters_to_feet,
        "ft": convert_feet_to_meters,
    }

    # Ask for the unit to convert
    unit_to_convert = ""
    while unit_to_convert.lower() not in conversion_functions:
        unit_to_convert = input("Please specify what unit to convert (C|F|m|ft): ")

    # Ask for the value to convert
    value_to_convert = float(input("Please specify the value of " + unit_to_convert + ": "))

    # Print the converted value, by finding a function based on the unit_to_convert value in the dictionary
    converted = conversion_functions[unit_to_convert.lower()](value_to_convert)
    print("{} {} is {} {}"
          .format(value_to_convert,
                  unit_to_convert,
                  converted.value,
                  converted.unit,
                  ))


if __name__ == "__main__":
    unit_converter()
