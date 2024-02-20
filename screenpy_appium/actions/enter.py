"""Enter text into an input field, or press keys."""

from __future__ import annotations

from typing import TYPE_CHECKING

from appium.webdriver.webdriver import WebDriverException
from screenpy.exceptions import DeliveryError, UnableToAct
from screenpy.pacing import beat

from ..common import pos_args_deprecated

if TYPE_CHECKING:
    from screenpy import Actor

    from ..target import Target


class Enter:
    """Enter text into an input field, or press specific keys.

    Abilities Required:
        :class:`~screenpy_appium.abilities.UseAnAndroidDevice`
        :class:`~screenpy_appium.abilities.UseAnIOSDevice`

    Examples::

        the_actor.attempts_to(
            Enter.the_text("Hello world!").into_the(COMMENT_FIELD)
        )
    """

    target: Target | None

    @staticmethod
    def the_text(text: str) -> Enter:
        """Provide the text to enter into the field."""
        return Enter(text)

    the_keys = the_text

    @staticmethod
    def the_secret(text: str) -> Enter:
        """
        Provide the text to enter into the field, but mask it in logging.

        The text will appear as "[CENSORED]".
        """
        return Enter(text, mask=True)

    the_password = the_secret

    def into_the(self, target: Target) -> Enter:
        """Target the element to enter text into."""
        self.target = target
        return self

    on = into = into_the_first_of_the = into_the

    def describe(self) -> str:
        """Describe the Action in present tense."""
        return f'Enter "{self.text_to_log}" into the {self.target}.'

    @beat('{} enters "{text_to_log}" into the {target}.')
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the Actor to enter the text into the element."""
        if self.target is None:
            msg = (
                "Target was not supplied for Enter. Provide a Target by using either "
                "the .into(), .into_the(), or .on() method."
            )
            raise UnableToAct(msg)

        element = self.target.found_by(the_actor)

        try:
            element.send_keys(self.text)
        except WebDriverException as e:
            msg = (
                "Encountered an issue while attempting to enter text into "
                f"{self.target}: {e.__class__.__name__}"
            )
            raise DeliveryError(msg) from e

    @pos_args_deprecated("mask")
    def __init__(self, text: str, mask: bool = False) -> None:  # noqa: FBT001, FBT002
        self.text = text
        self.target = None

        if mask:
            self.text_to_log = "[CENSORED]"
        else:
            self.text_to_log = self.text
