"""Matches a tappable WebElement. (Yes, they're still WebElements on mobile.)."""

from screenpy.resolutions.base_resolution import BaseResolution

from .custom_matchers import is_tappable_element


class IsTappable(BaseResolution):
    """Match on a tappable element.

    Abilities Required:
        :class:`~screenpy_appium.abilities.UseAnAndroidDevice`
        :class:`~screenpy_appium.abilities.UseAnIOSDevice`

    Examples::

        the_actor.should(See.the(Element(LOGIN_BUTTON), IsTappable()))
    """

    line = "tappable"
    matcher_function = is_tappable_element
