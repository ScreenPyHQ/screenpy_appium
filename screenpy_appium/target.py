"""
Combine a string with a locator to describe an element in an app.

Target attempts to figure out a couple logical defaults for locators, e.g.
if the string begins with a "/" or a "(", it's probably an XPATH locator.
Otherwise, the default is accessibility ID.
"""

from typing import Iterator, List, Optional, Tuple, Union

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriverException
from appium.webdriver.webelement import WebElement
from screenpy import Actor

from .abilities import UseAMobileDevice
from .exceptions import TargetingError


class Target:
    """Describe an element with a human-readable string and a locator.

    Abilities Required:
        :class:`~screenpy_appium.abilities.UseAnAndroidDevice`
        :class:`~screenpy_appium.abilities.UseAnIOSDevice`

    Examples::

        # assumes by Accessibility ID
        Target.the("accept button").located_by('"Accept" Button')

        # assumes by XPATH
        Target.the("username field").located_by("//android.widget.EditText")

        Target.the('"Log In" button').located((AppiumBy.NAME, "login"))
    """

    locator: Optional[Tuple[str, str]]

    @classmethod
    def the(cls, description: str) -> "Target":
        """Provide a human-readable description for the element."""
        return cls(description)

    def located_by(self, locator: Union[Tuple[str, str], str]) -> "Target":
        """Set the locator for this Target.

        Possible values for locator:
            * A tuple of an AppiumBy classifier and a string
              (e.g. ``(AppiumBy.NAME, "welcome")``)
            * An Accessibility ID string (e.g. ``"Accept Button"``)
            * An XPATH string (e.g. ``"//div/h3"``)
        """
        if isinstance(locator, tuple):
            self.locator = locator
        elif locator[0] in ("(", "/"):
            self.locator = (AppiumBy.XPATH, locator)
        else:
            self.locator = (AppiumBy.ACCESSIBILITY_ID, locator)

        return self

    located = located_by

    def get_locator(self) -> Tuple[str, str]:
        """Return the stored locator.

        Raises:
            TargetingError: if no locator was set.
        """
        if self.locator is None:
            raise TargetingError(
                f"Locator was not supplied to the {self} target. Make sure to use "
                "either .located() or .located_by() to supply a locator."
            )
        return self.locator

    def found_by(self, the_actor: Actor) -> WebElement:
        """Retrieve the |WebElement| as viewed by the Actor."""
        driver = the_actor.ability_to(UseAMobileDevice).driver
        try:
            return driver.find_element(*self)
        except WebDriverException as e:
            raise TargetingError(f"{e} raised while trying to find {self}.") from e

    def all_found_by(self, the_actor: Actor) -> List[WebElement]:
        """Retrieve a list of |WebElement| objects as viewed by the Actor."""
        driver = the_actor.ability_to(UseAMobileDevice).driver
        try:
            return driver.find_elements(*self)
        except WebDriverException as e:
            raise TargetingError(f"{e} raised while trying to find {self}.") from e

    def __repr__(self) -> str:
        return self.target_name

    __str__ = __repr__

    def __iter__(self) -> Iterator[str]:
        return self.get_locator().__iter__()

    def __getitem__(self, index: int) -> str:
        return self.get_locator()[index]

    def __init__(self, description: str) -> None:
        self.target_name = description
        self.locator = None
