"""Tap on an element."""

from __future__ import annotations

from typing import TYPE_CHECKING

from appium.webdriver.webdriver import WebDriverException
from screenpy.exceptions import DeliveryError
from screenpy.pacing import beat

if TYPE_CHECKING:
    from screenpy.actor import Actor

    from ..target import Target


class Tap:
    """Tap on an element!

    Abilities Required:
        :class:`~screenpy_appium.abilities.UseAnAndroidDevice`
        :class:`~screenpy_appium.abilities.UseAnIOSDevice`

    Examples::

        the_actor.attempts_to(Tap.on_the(HAMBURGER_MENU))

        the_actor.attempts_to(Tap.on(THE_BACK_BUTTON))

        the_actor.attempts_to(Tap.on_the_first_of_the(SEARCH_RESULTS))
    """

    @staticmethod
    def on_the(target: Target) -> Tap:
        """Target the element to tap on."""
        return Tap(target)

    on = on_the_first_of_the = on_the

    def describe(self) -> str:
        """Describe the Action in present tense."""
        return f"Tap on the {self.target}."

    @beat("{} taps on the {target}.")
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the Actor to tap on the element."""
        element = self.target.found_by(the_actor)

        try:
            element.click()
        except WebDriverException as e:
            msg = (
                "Encountered an issue while attempting to tap "
                f"{self.target}: {e.__class__.__name__}"
            )
            raise DeliveryError(msg) from e

    def __init__(self, target: Target) -> None:
        self.target = target
        self.description = f" on the {target}" if target is not None else ""
