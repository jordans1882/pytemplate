"""
The template module:

This module has example classes to showcase how to write classes, methods and documentation for the
python-template package. See the Template class and the template function.
"""


class Template:
    """
    A class to represent a template.

    Attributes
    ----------
       val : numeric
           The answer to everything
       val2 : numeric
           I'm feeling lucky
    """

    def __init__(self, val=42, val2=7):
        """
        Constructs all the necessary attributes for the template object.

        Parameters
        ----------
            val : numeric
                The answer to everything
            val2 : numeric
                I'm feeling lucky
        """
        self.val = val
        self.val2 = val2
        self.val3 = None

    def hello_world(self):
        """
        A simple function to print hello world
        """
        print("Hello world!!")
        print(f"The secret number is: {self.val}")

    def hello_world_v2(self):
        """
        A simple function to print hello world
        """
        print("Hello world!!")
        print(f"The other secret number is: {self.val2}")

    def identity(self, val: float) -> float:
        """
        A simple identity function
        """
        self.val3 = val
        return val


def template():
    """
    A simple function to print hello world
    """
    print("Hello World!!")
