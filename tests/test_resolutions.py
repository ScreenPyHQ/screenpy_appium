from unittest import mock

from screenpy.resolutions.base_resolution import BaseResolution
from screenpy_appium.resolutions import IsTappable, IsVisible
from appium.webdriver.webelement import WebElement
from hamcrest.core.string_description import StringDescription
from dataclasses import dataclass


@dataclass
class ExpectedDescriptions:
    describe_to: str
    describe_match: str
    describe_mismatch: str
    describe_none: str


def _assert_descriptions(
    obj: BaseResolution, element: WebElement, expected: ExpectedDescriptions
):
    describe_to = StringDescription()
    describe_match = StringDescription()
    describe_mismatch = StringDescription()
    describe_none = StringDescription()

    obj.describe_to(describe_to)
    obj.describe_match(element, describe_match)
    obj.describe_mismatch(element, describe_mismatch)
    obj.describe_mismatch(None, describe_none)

    assert describe_to.out == expected.describe_to
    assert describe_match.out == expected.describe_match
    assert describe_mismatch.out == expected.describe_mismatch
    assert describe_none.out == expected.describe_none


class TestIsTappable:
    def test_can_be_instantiated(self):
        ic = IsTappable()

        assert isinstance(ic, IsTappable)

    def test_matches_a_Tapable_element(self):
        element = mock.Mock(spec=WebElement)
        element.is_enabled.return_value = True
        element.is_displayed.return_value = True
        ic = IsTappable()

        assert ic._matches(element)

    def test_does_not_match_untapable_element(self):
        invisible_element = mock.Mock(spec=WebElement)
        invisible_element.is_displayed.return_value = False
        invisible_element.is_enabled.return_value = True
        inactive_element = mock.Mock(spec=WebElement)
        inactive_element.is_displayed.return_value = True
        inactive_element.is_enabled.return_value = False
        ic = IsTappable()

        assert not ic._matches(None)  # element was not found by Element()
        assert not ic._matches(invisible_element)
        assert not ic._matches(inactive_element)

    @mock.patch("appium.webdriver.webelement.WebElement", spec=WebElement)
    def test_descriptions(self, element):
        expected = ExpectedDescriptions(
            describe_to="the element is enabled/tappable",
            describe_match="it was enabled/tappable",
            describe_mismatch="was not enabled/tappable",
            describe_none="was not even present",
        )

        _assert_descriptions(IsTappable(), element, expected)


class TestIsVisible:
    def test_can_be_instantiated(self):
        iv = IsVisible()

        assert isinstance(iv, IsVisible)

    def test_matches_a_visible_element(self):
        element = mock.Mock(spec=WebElement)
        element.is_displayed.return_value = True
        iv = IsVisible()

        assert iv._matches(element)

    def test_does_not_match_invisible_element(self):
        invisible_element = mock.Mock(spec=WebElement)
        invisible_element.is_displayed.return_value = False
        iv = IsVisible()

        assert not iv._matches(None)  # element was not found by Element()
        assert not iv._matches(invisible_element)

    def test_descriptions(self):
        element = mock.Mock(spec=WebElement)
        expected = ExpectedDescriptions(
            describe_to="the element is visible",
            describe_match="it was visible",
            describe_mismatch="was not visible",
            describe_none="was not even present",
        )

        _assert_descriptions(IsVisible(), element, expected)
