"""
Investigate how many of an element are present on the page.
"""

from screenpy import Actor
from screenpy.pacing import beat

from ..target import Target


class Number:
    """Ask how many of a certain element are on the page.

    Note that in Android, this will only retrieve elements which are currently
    included in the viewport. On iOS, this will retrieve every element.

    Abilities Required:
        :class:`~screenpy_appium.abilities.UseAnAndroidDevice`
        :class:`~screenpy_appium.abilities.UseAnIOSDevice`

    Examples::

        the_actor.should(See.the(Number.of(SEARCH_RESULTS), IsEqualTo(4)))
    """

    @classmethod
    def of(cls, target: Target) -> "Number":
        """Target the element to be counted."""
        return cls(target=target)

    def describe(self) -> str:
        """Describe the Question."""
        return f"The number of {self.target}."

    @beat("{} counts the number of {target}.")
    def answered_by(self, the_actor: Actor) -> int:
        """Direct the Actor to count the elements."""
        return len(self.target.all_found_by(the_actor))

    def __init__(self, target: Target) -> None:
        self.target = target
