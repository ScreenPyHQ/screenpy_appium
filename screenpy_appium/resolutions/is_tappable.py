"""Matches a tappable WebElement. (Yes, they're still WebElements on mobile.)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from screenpy import beat

from .custom_matchers import is_tappable_element

if TYPE_CHECKING:
    from .custom_matchers.is_tappable_element import IsTappableElement


class IsTappable:
    """Match on a tappable element.

    Abilities Required:
        :class:`~screenpy_appium.abilities.UseAnAndroidDevice`
        :class:`~screenpy_appium.abilities.UseAnIOSDevice`

    Examples::

        the_actor.should(See.the(Element(LOGIN_BUTTON), IsTappable()))
    """

    def describe(self) -> str:
        """Describe the Resolution's expectation."""
        return "tappable"

    @beat("... hoping it's tappable.")
    def resolve(self) -> IsTappableElement:
        """Produce the Matcher to make the assertion."""
        return is_tappable_element()
