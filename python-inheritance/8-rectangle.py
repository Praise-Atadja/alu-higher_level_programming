#!/usr/bin/python3
""" class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """new rectangle.
        Args:
            width (int): The width.            height (int): The height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
