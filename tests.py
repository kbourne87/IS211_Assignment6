import unittest
import conversions
import conversions_refactored

CelToFahr = ((0, 32.0),
             (32, 89.6),
             (100, 212.0),
             (273.15, 523.67),
             (459.67, 859.41))

CelToKel = ((0, 273.15),
            (32, 305.15),
            (100, 373.15),
            (273.15, 546.3),
            (459.67, 732.82))

FahrToCel = ((0, -17.78),
             (32, 0.0),
             (100, 37.78),
             (273.15, 133.97),
             (459.67, 237.59))

FahrToKel = ((0, 255.37),
             (32, 273.15),
             (100, 310.93),
             (273.15, 407.12),
             (459.67, 510.74))

KelToFahr = ((0, -827.41),
             (32, -769.81),
             (100, -647.41),
             (273.15, -335.74),
             (459.67, 0.0))

KelToCel = ((0, -273.15),
            (32, -241.15),
            (100, -173.15),
            (273.15, 0.0),
            (459.67, 186.52))

FeettoYards = ((1, 0.33),
            (3, 1),
)

class conversionValues(unittest.TestCase):

    def test_CelToFahr(self):
        'Celcius to Fahrenheit conversion should match tested values'

        for integer, numeral in CelToFahr:
            result = conversions.convertCelsiusToFahrenheit(integer)
            self.assertEqual(numeral, result)

    def test_CelToKel(self):
        'Celcius to Kelvin conversion should match tested values'

        for integer, numeral in CelToKel:
            result = conversions.convertCelciusToKelvin(integer)
            self.assertEqual(numeral, result)

    def test_FahrToCel(self):
        'Fahrenheit to Celcius conversion should match tested values'

        for integer, numeral in FahrToCel:
            result = conversions.convertFahrenheitToCelcius(integer)
            self.assertEqual(numeral, result)

    def test_FahrToKel(self):
        'Fahrenheit to Kelvin conversion should match tested values'

        for integer, numeral in FahrToKel:
            result = conversions.convertFahrenheitToKelvin(integer)
            self.assertEqual(numeral, result)

    def test_KelToCel(self):
        'Kelvin to Celcius conversion should match tested values'

        for integer, numeral in KelToCel:
            result = conversions.convertKelvinToCelcius(integer)
            self.assertEqual(numeral, result)

    def test_KelToFahr(self):
        'Kelvin to Fahrenheit conversion should match tested values'

        for integer, numeral in KelToFahr:
            result = conversions.convertKelvinToFahrenheit(integer)
            self.assertEqual(numeral, result)

class ConversionRefactoredValues(unittest.TestCase):

    """Check to see if the error is raised correctly"""
    def test_ConversionFailure(self):
        self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert_units, 'yards', 'celsius', 4)

    """Proof of concept test"""
    def test_FeettoYards(self):
        for integer, numeral in FeettoYards:
            result = conversions_refactored.convert_units('feet', 'yards', integer)
            self.assertEqual(numeral, result)

    """This will fail because of rounding"""
    def test_CanConvertBack(self):
        for integer, numeral in FeettoYards:
            result = conversions_refactored.convert_units('feet', 'yards', integer)
            change_back = conversions_refactored.convert_units('yards', 'feet', result)
            self.assertEqual(change_back, integer)

if __name__ == '__main__':
    unittest.main()

