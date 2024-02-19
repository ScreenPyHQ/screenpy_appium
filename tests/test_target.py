import pytest

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriverException
from screenpy import Actor

from screenpy_appium import Target
from screenpy_appium.abilities import UseAnAndroidDevice
from screenpy_appium.exceptions import TargetingError


def test_can_be_instantiated() -> None:
    t1 = Target.the("test")
    t2 = Target.the("test").located_by("test")

    assert isinstance(t1, Target)
    assert isinstance(t2, Target)


def test_complains_for_no_locator() -> None:
    """Raises if no locator was supplied."""
    target = Target.the("test")

    with pytest.raises(TargetingError):
        target.get_locator()


def test_get_locator() -> None:
    """Returns the locator tuple when asked for it"""
    a11y_id_locator = "Submit Button"
    xpath_locator = '//div[@id="id"]'
    xpath_locator_2 = "(//a)[5]"
    a11y_id_target = Target.the("css element").located_by(a11y_id_locator)
    xpath_target = Target.the("xpath element").located_by(xpath_locator)
    xpath_target_2 = Target.the("xpath element 2").located_by(xpath_locator_2)

    assert a11y_id_target.get_locator() == (AppiumBy.ACCESSIBILITY_ID, a11y_id_locator)
    assert xpath_target.get_locator() == (AppiumBy.XPATH, xpath_locator)
    assert xpath_target_2.get_locator() == (AppiumBy.XPATH, xpath_locator_2)


def test_located() -> None:
    """Uses the provided locator tuple, unaltered"""
    locator = (AppiumBy.NAME, "spam")
    target = Target.the("test").located(locator)

    assert target.get_locator() == locator


def test_can_be_indexed() -> None:
    locator = (AppiumBy.NAME, "eggs")
    target = Target.the("test").located(locator)

    assert target[0] == locator[0]
    assert target[1] == locator[1]


def test_found_by(AndroidTester: Actor) -> None:
    test_locator = (AppiumBy.NAME, "eggs")
    Target.the("test").located(test_locator).found_by(AndroidTester)

    mocked_driver = AndroidTester.ability_to(UseAnAndroidDevice).driver
    mocked_driver.find_element.assert_called_once_with(*test_locator)


def test_found_by_raises(AndroidTester: Actor) -> None:
    test_name = "frobnosticator"
    mocked_driver = AndroidTester.ability_to(UseAnAndroidDevice).driver
    mocked_driver.find_element.side_effect = WebDriverException

    with pytest.raises(TargetingError) as excinfo:
        Target.the(test_name).located_by("*").found_by(AndroidTester)

    assert test_name in str(excinfo.value)


def test_all_found_by(AndroidTester: Actor) -> None:
    test_locator = (AppiumBy.NAME, "baked beans")
    Target.the("test").located(test_locator).all_found_by(AndroidTester)

    mocked_driver = AndroidTester.ability_to(UseAnAndroidDevice).driver
    mocked_driver.find_elements.assert_called_once_with(*test_locator)


def test_all_found_by_raises(AndroidTester: Actor) -> None:
    test_name = "transmogrifier"
    mocked_driver = AndroidTester.ability_to(UseAnAndroidDevice).driver
    mocked_driver.find_elements.side_effect = WebDriverException

    with pytest.raises(TargetingError) as excinfo:
        Target.the(test_name).located_by("*").all_found_by(AndroidTester)

    assert test_name in str(excinfo.value)


def test_iterator() -> None:
    locator = (AppiumBy.NAME, "eggs")
    target = Target.the("test").located(locator)
    it1 = target.__iter__()
    assert next(it1) == locator[0]
    assert next(it1) == locator[1]
    with pytest.raises(StopIteration):
        next(it1)


def test_empty_target_iterator() -> None:
    nulltarget = Target("bogus")
    with pytest.raises(TargetingError):
        iter(nulltarget)
