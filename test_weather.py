import pytest
import weather_functions


def test_convert_kelvin_to_celsius():
    validator = weather_functions.convert_kelvin_to_celsius(0)
    expected = -273.15
    assert validator == expected


def test_convert_kelvin_to_celsius2():
    validator = weather_functions.convert_kelvin_to_celsius(100)
    expected = -173.15
    assert validator == expected


def test_convert_kelvin_to_celsius3():
    validator = weather_functions.convert_kelvin_to_celsius(300)
    expected = 26.85
    assert validator == expected
