"""Matches against a visible WebElement. (Yes, they're still WebElements on mobile.)."""

from __future__ import annotations

from screenpy.resolutions.base_resolution import BaseResolution

from .custom_matchers import is_visible_element


class IsVisible(BaseResolution):
    """Match on a visible element.

    Abilities Required:
        :class:`~screenpy_appium.abilities.UseAnAndroidDevice`
        :class:`~screenpy_appium.abilities.UseAnIOSDevice`

    Examples::

        the_actor.should(See.the(Element(WELCOME_CAROUSEL), IsVisible()))
    """

    line = "visible"
    matcher_function = is_visible_element
