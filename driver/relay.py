"""
This implementation does its best to follow the Robert Martin's Clean code guidelines.
The comments follows the Google Python Style Guide:
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__author__ = "Lorenzo Carnevale <lcarnevale@unime.it>"
__license__ = "MIT License"
__description__ = "Relay MicroPython driver"

from machine import Pin

class Relay(object):
    """
    """
    __instance = None

    def __new__(self) -> __instance:
        """Implement class object.
        
        Returns
            (Relay) instance of the class
        """
        self.__instance = super(Relay, self).__new__(self)
        return self.__instance

    def build_pin(self, pin_number) -> __instance:
        """Build the pin variable.

        Args:
            pin_number(int): custom pin number

        Returns
            (Relay) instance of the class
        """
        self.__pin = Pin(pin_number, Pin.OUT)
        return self.__instance

    
    def high(self) -> None:
        """Set the relay value as high (1)
        """
        self.__pin.value(1)

    def low(self) -> None:
        """Set the relay value as low (0)
        """
        self.__pin.value(0)