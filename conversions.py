"""Simple functions for conversion"""
def convertCelciusToKelvin(temp):
    convertedTemp = temp + 273.15
    return round(convertedTemp, 2)

def convertCelsiusToFahrenheit(temp):
    convertedTemp =  temp * 9/5 + 32
    return round(convertedTemp, 2)

def convertFahrenheitToKelvin(temp):
    convertedTemp = (temp + 459.67) * 5/9
    return round(convertedTemp, 2)

def convertFahrenheitToCelcius(temp):
    convertedTemp = (temp -32) * 5/9
    return round(convertedTemp, 2)

def convertKelvinToCelcius(temp):
    convertedTemp = temp - 273.15
    return round(convertedTemp, 2)

def convertKelvinToFahrenheit(temp):
    convertedTemp = (temp - 459.67) * 9/5
    return round(convertedTemp, 2)
