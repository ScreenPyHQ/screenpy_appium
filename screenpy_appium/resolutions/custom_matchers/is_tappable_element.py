"""
A matcher that matches a tappable element. For example:

    assert_that(driver.find_element_by_id("search"), is_tappable_element())
"""
from typing import Optional

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description
from selenium.webdriver.remote.webelement import WebElement


class IsTappableElement(BaseMatcher[Optional[WebElement]]):
    """Matches an element which both ``is_enabled`` and ``is_displayed``."""

    def _matches(self, item: Optional[WebElement]) -> bool:
        """Whether the item is tappable."""
        if item is None:
            return False
        return item.is_displayed() and item.is_enabled()

    def describe_to(self, description: Description) -> None:
        """Describe the passing case."""
        description.append_text("the element is enabled/tappable")

    def describe_match(
        self, _: Optional[WebElement], match_description: Description
    ) -> None:
        """Describe the passing case, when it is unexpected."""
        match_description.append_text("it was enabled/tappable")

    def describe_mismatch(
        self, item: Optional[WebElement], mismatch_description: Description
    ) -> None:
        """Describe the failing case."""
        if item is None or not item.is_displayed():
            mismatch_description.append_text("was not even present")
            return
        mismatch_description.append_text("was not enabled/tappable")


def is_tappable_element() -> IsTappableElement:
    """This matcher matches any element that is visible and enabled."""
    return IsTappableElement()
