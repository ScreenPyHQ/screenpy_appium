"""
A matcher that matches a visible element. For example:

    assert_that(driver.find_element_by_id("search"), is_visible_element())
"""


from typing import Optional

from appium.webdriver.webelement import WebElement
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description


class IsVisibleElement(BaseMatcher[Optional[WebElement]]):
    """
    Matches an element whose ``is_displayed`` method returns True.
    """

    def _matches(self, item: Optional[WebElement]) -> bool:
        """Whether the element is visible."""
        if item is None:
            return False
        return item.is_displayed()

    def describe_to(self, description: Description) -> None:
        """Describe the passing case."""
        description.append_text("the element is visible")

    def describe_match(
        self, _: Optional[WebElement], match_description: Description
    ) -> None:
        """Describe the passing case, when it is unexpected."""
        match_description.append_text("it was visible")

    def describe_mismatch(
        self, item: Optional[WebElement], mismatch_description: Description
    ) -> None:
        """Describe the failing case."""
        if item is None:
            mismatch_description.append_text("was not even present")
            return
        mismatch_description.append_text("was not visible")


def is_visible_element() -> IsVisibleElement:
    """This matcher matches any element that is visible."""
    return IsVisibleElement()
