"""Investigate one or more elements."""

from __future__ import annotations

from typing import TYPE_CHECKING

from screenpy.pacing import beat

if TYPE_CHECKING:
    from appium.webdriver import WebElement
    from screenpy import Actor

    from ..target import Target


class List:
    """Ask for a list of elements.

    Abilities Required:
        :class:`~screenpy_appium.abilities.UseAnAndroidDevice`
        :class:`~screenpy_appium.abilities.UseAnIOSDevice`

    Examples::

        the_actor.should(See.the(List.of(CONFETTI), IsEmpty()))
    """

    @staticmethod
    def of_the(target: Target) -> List:
        """Target the element(s) to list."""
        return List(target)

    of_all_the = of_all = of = of_the

    def describe(self) -> str:
        """Describe the Question."""
        return f"The list of {self.target}."

    @beat("{} lists off the {target}.")
    def answered_by(self, the_actor: Actor) -> list[WebElement]:
        """Direct the Actor to rattle off the specified elements."""
        return self.target.all_found_by(the_actor)

    def __init__(self, target: Target) -> None:
        self.target = target
