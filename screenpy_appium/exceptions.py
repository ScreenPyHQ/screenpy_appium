"""Exceptions used by ScreenPy Appium."""

from __future__ import annotations

from screenpy.exceptions import ScreenPyError


class TargetingError(ScreenPyError):
    """There is an issue preventing Target acquisition."""
