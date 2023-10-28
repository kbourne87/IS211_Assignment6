class ConversionNotPossible(Exception):
    pass

def convert_units (fromUnit, toUnit, value):
    """Went back and forth on this one, obviously more unwieldly as the number of units grows"""

    conversion_dict = {
        ('CELSIUS', 'KELVIN'): value + 273.15,
        ('CELSIUS', 'FAHRENHEIT'): value * 9/5 + 32,
        ('FAHRENHEIT', 'KELVIN'): (value + 459.67) * 5/9,
        ('FAHRENHEIT', 'CELSIUS'): (value + 459.67) * 5/9,
        ('KELVIN', 'CELSIUS'): value - 273.15,
        ('KELVIN', 'FAHRENHEIT'): (value - 459.67) * 9/5,
        ('FEET', 'YARDS'): value / 3,
        ('FEET', 'METERS'): value / 3.28,
        ('METERS', 'FEET'): value * 3.28,
        ('METERS', 'YARDS'): value * 1.09,
        ('YARDS', 'METERS'): value / 1.09,
        ('YARDS', 'FEET'): value * 3
    }

    fromString = str(fromUnit).upper()
    toString = str(toUnit).upper()
    dict_check = tuple((fromString, toString))

    if dict_check in conversion_dict.keys():
        return(round(conversion_dict[dict_check], 2))
    else:
        raise ConversionNotPossible('Cannot convert these unit types')
