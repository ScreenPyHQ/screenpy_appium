"""
Exceptions used by ScreenPy Appium.
"""

from screenpy.exceptions import ScreenPyError


class TargetingError(ScreenPyError):
    """There is an issue preventing Target acquisition."""
