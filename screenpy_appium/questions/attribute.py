"""Investigate an attribute of a Target."""

from __future__ import annotations

from typing import TYPE_CHECKING

from screenpy.exceptions import UnableToAnswer
from screenpy.pacing import beat

if TYPE_CHECKING:
    from screenpy import Actor

    from ..target import Target


class Attribute:
    """Ask about an attribute on an element.

    Abilities Required:
        :class:`~screenpy_appium.abilities.UseAnAndroidDevice`
        :class:`~screenpy_appium.abilities.UseAnIOSDevice`

    Examples::

        the_actor.should(
            See.the(
                Attribute("value").of_the(NAME_INPUT), ReadsExactly("Jessica Walters")),
            ),
            See.the(
                Attribute("aria-label").of_the(BALLOONS), ContainsTheText("balloon")),
            ),
        )
    """

    target: Target | None

    def of_the(self, target: Target) -> Attribute:
        """Target the element to get the attribute from."""
        self.target = target
        return self

    of = of_the_first_of_the = of_the

    def of_all(self, target: Target) -> Attribute:
        """Target the elements, plural, to get the attribute from."""
        self.target = target
        self.multi = True
        return self

    def describe(self) -> str:
        """Describe the Question."""
        return f'The "{self.attribute}" attribute of the {self.target}.'

    @beat('{} examines the "{attribute}" attribute of the {target}...')
    def answered_by(
        self, the_actor: Actor
    ) -> str | dict | list[str | dict | None] | None:
        """Direct the actor to investigate the attribute on the element."""
        if self.target is None:
            msg = (
                "No Target given to Attribute to investigate. Supply a Target"
                " with the `.of()`, `.of_the()`, or `.of_all()` method."
            )
            raise UnableToAnswer(msg)

        if self.multi:
            elements = self.target.all_found_by(the_actor)
            return [element.get_attribute(self.attribute) for element in elements]
        return self.target.found_by(the_actor).get_attribute(self.attribute)

    def __init__(self, attribute: str) -> None:
        self.attribute = attribute
        self.multi = False
        self.target = None
