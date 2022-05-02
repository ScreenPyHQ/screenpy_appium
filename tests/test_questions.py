from unittest import mock

import pytest

from screenpy.exceptions import UnableToAnswer
from appium.webdriver.webdriver import WebDriverException

from screenpy_appium import Target
from screenpy_appium.abilities import UseAnAndroidDevice
from screenpy_appium.questions import (
    Attribute,
    Element,
    List,
    Number,
    Text,
)


class TestAttribute:
    def test_can_be_instantiated(self):
        a1 = Attribute("")
        a2 = Attribute("").of_the(None)

        assert isinstance(a1, Attribute)
        assert isinstance(a2, Attribute)

    def test_raises_error_if_no_target(self, AndroidTester):
        with pytest.raises(UnableToAnswer):
            Attribute("").answered_by(AndroidTester)

    def test_of_all_sets_multi(self):
        assert Attribute("").of_all(None).multi

    def test_uses_get_attribute(self, AndroidTester):
        fake_target = Target.the("fake").located_by("//html")
        attr = "foo"
        value = "bar"
        mocked_driver = AndroidTester.ability_to(UseAnAndroidDevice).driver
        mocked_element = mock.Mock()
        mocked_element.get_attribute.return_value = value
        mocked_driver.find_element.return_value = mocked_element

        assert Attribute(attr).of_the(fake_target).answered_by(AndroidTester) == value
        mocked_driver.find_element.assert_called_once_with(*fake_target)
        mocked_element.get_attribute.assert_called_once_with(attr)

    def test_uses_get_attribute_multi(self, AndroidTester):
        fake_target = Target.the("fake").located_by("//html")
        attr = "foo"
        value = "bar"
        mocked_driver = AndroidTester.ability_to(UseAnAndroidDevice).driver
        mocked_elements = [mock.Mock() for _ in range(3)]
        for mocked_element in mocked_elements:
            mocked_element.get_attribute.return_value = value
        mocked_driver.find_elements.return_value = mocked_elements

        attrs = Attribute(attr).of_all(fake_target).answered_by(AndroidTester)

        assert attrs == [value] * len(mocked_elements)
        mocked_driver.find_elements.assert_called_once_with(*fake_target)
        mocked_element.get_attribute.assert_called_once_with(attr)


class TestElement:
    def test_can_be_instantiated(self):
        e = Element(None)

        assert isinstance(e, Element)

    def test_question_returns_none_if_no_element_found(self, AndroidTester):
        test_target = Target.the("foo").located_by("//bar")
        mocked_driver = AndroidTester.ability_to(UseAnAndroidDevice).driver
        mocked_driver.find_element.side_effect = WebDriverException

        assert Element(test_target).answered_by(AndroidTester) is None

    def test_ask_for_element(self, AndroidTester):
        fake_target = Target.the("fake").located_by("//html")
        mocked_driver = AndroidTester.ability_to(UseAnAndroidDevice).driver
        mocked_element = mock.Mock()
        mocked_driver.find_element.return_value = mocked_element

        assert Element(fake_target).answered_by(AndroidTester) is mocked_element
        mocked_driver.find_element.assert_called_once_with(*fake_target)


class TestList:
    def test_can_be_instantiated(self):
        l1 = List.of(None)
        l2 = List.of_all(None)

        assert isinstance(l1, List)
        assert isinstance(l2, List)

    def test_ask_for_list(self, AndroidTester):
        fake_target = Target.the("fake").located_by("//xpath")
        return_value = ["a", "b", "c"]
        mocked_driver = AndroidTester.ability_to(UseAnAndroidDevice).driver
        mocked_driver.find_elements.return_value = return_value

        assert List.of(fake_target).answered_by(AndroidTester) == return_value
        mocked_driver.find_elements.assert_called_once_with(*fake_target)


class TestNumber:
    def test_can_be_instantiated(self):
        n1 = Number.of(None)

        assert isinstance(n1, Number)

    def test_ask_for_number(self, AndroidTester):
        fake_target = Target.the("fake").located_by("//xpath")
        return_value = [1, 2, 3]
        mocked_driver = AndroidTester.ability_to(UseAnAndroidDevice).driver
        mocked_driver.find_elements.return_value = return_value

        assert Number.of(fake_target).answered_by(AndroidTester) == len(return_value)
        mocked_driver.find_elements.assert_called_once_with(*fake_target)


class TestText:
    def test_can_be_instantiated(self):
        t1 = Text.of(None)
        t2 = Text.of_all(None)

        assert isinstance(t1, Text)
        assert isinstance(t2, Text)

    def test_of_all_sets_multi(self):
        assert Text.of_all(None).multi

    def test_ask_for_text(self, AndroidTester):
        fake_target = Target.the("fake").located_by("//xpath")
        mocked_driver = AndroidTester.ability_to(UseAnAndroidDevice).driver
        expected_text = "spam and eggs"
        mocked_element = mock.Mock(text=expected_text)
        mocked_driver.find_element.return_value = mocked_element

        assert Text.of_the(fake_target).answered_by(AndroidTester) == expected_text
        mocked_driver.find_element.assert_called_once_with(*fake_target)

    def test_ask_for_all_text(self, AndroidTester):
        fake_target = Target.the("fakes").located_by("//xpath")
        mocked_driver = AndroidTester.ability_to(UseAnAndroidDevice).driver
        expected_texts = ["spam", "eggs", "baked beans"]
        mocked_elements = [mock.Mock(text=text) for text in expected_texts]
        mocked_driver.find_elements.return_value = mocked_elements

        assert Text.of_all(fake_target).answered_by(AndroidTester) == expected_texts
        mocked_driver.find_elements.assert_called_once_with(*fake_target)
