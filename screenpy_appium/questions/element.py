"""Investigate an element on the browser page."""

from __future__ import annotations

from typing import TYPE_CHECKING

from screenpy.pacing import beat

from ..exceptions import TargetingError

if TYPE_CHECKING:
    from screenpy import Actor
    from selenium.webdriver.remote.webelement import WebElement

    from ..target import Target


class Element:
    """Ask to retrieve a specific element.

    Abilities Required:
        :class:`~screenpy_appium.abilities.UseAnAndroidDevice`
        :class:`~screenpy_appium.abilities.UseAnIOSDevice`

    Examples::

        the_actor.should(See.the(Element(SURVEY_RESULT), IsVisible()))
    """

    def describe(self) -> str:
        """Describe the Question."""
        return f"The {self.target}."

    @beat("{} inspects the {target}.")
    def answered_by(self, the_actor: Actor) -> WebElement | None:
        """Direct the Actor to find the element."""
        try:
            return self.target.found_by(the_actor)
        except TargetingError:
            return None

    def __init__(self, target: Target) -> None:
        self.target = target
