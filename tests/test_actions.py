from __future__ import annotations

from typing import TYPE_CHECKING
from unittest import mock

import pytest
from screenpy.exceptions import UnableToAct

from screenpy_appium.actions import Clear, Enter, Tap

if TYPE_CHECKING:
    from screenpy import Actor


def get_mocked_target_and_element() -> tuple[mock.Mock, mock.Mock]:
    """Get a mocked target which returns a mocked element."""
    target = mock.Mock()
    element = mock.Mock()
    target.found_by.return_value = element

    return target, element


class TestClear:
    def test_can_be_instantiated(self) -> None:
        c1 = Clear(None)
        c2 = Clear.the_text_from_the(None)

        assert isinstance(c1, Clear)
        assert isinstance(c2, Clear)

    def test_perform_clear(self, AndroidTester: Actor, IOSTester: Actor) -> None:
        android_target, android_element = get_mocked_target_and_element()
        ios_target, ios_element = get_mocked_target_and_element()

        Clear.the_text_from(android_target).perform_as(AndroidTester)
        Clear.the_text_from(ios_target).perform_as(IOSTester)

        android_target.found_by.assert_called_once_with(AndroidTester)
        ios_target.found_by.assert_called_once_with(IOSTester)
        android_element.clear.assert_called_once()
        ios_element.clear.assert_called_once()


class TestEnter:
    def test_can_be_instantiated(self) -> None:
        e1 = Enter.the_text("test")
        e2 = Enter.the_text("test").into(None)
        e3 = Enter.the_keys("test").into(None)
        e4 = Enter.the_text("test").into_the(None)
        e5 = Enter.the_text("test").on(None)
        e6 = Enter.the_keys("test").on(None)
        e7 = Enter.the_secret("test")

        assert isinstance(e1, Enter)
        assert isinstance(e2, Enter)
        assert isinstance(e3, Enter)
        assert isinstance(e4, Enter)
        assert isinstance(e5, Enter)
        assert isinstance(e6, Enter)
        assert isinstance(e7, Enter)

    def test_secret_masks_text(self) -> None:
        """the_secret sets text_to_log to [CENSORED]"""
        text = "Keep it a secret to everybody"
        e = Enter.the_secret(text)

        assert e.text == text
        assert e.text_to_log == "[CENSORED]"

    def test_perform_enter(self, AndroidTester: Actor) -> None:
        target, element = get_mocked_target_and_element()
        text = 'Speak "Friend" and Enter'

        Enter.the_text(text).into_the(target).perform_as(AndroidTester)

        target.found_by.assert_called_once_with(AndroidTester)
        element.send_keys.assert_called_once_with(text)

    def test_perform_without_target_raises(self, AndroidTester: Actor) -> None:
        with pytest.raises(UnableToAct):
            Enter.the_text("woops!").perform_as(AndroidTester)


class TestTap:
    def test_can_be_instantiated(self) -> None:
        c1 = Tap.on(None)
        c2 = Tap.on_the(None)

        assert isinstance(c1, Tap)
        assert isinstance(c2, Tap)

    def test_perform_click(self, AndroidTester: Actor, IOSTester: Actor) -> None:
        android_target, android_element = get_mocked_target_and_element()
        ios_target, ios_element = get_mocked_target_and_element()

        Tap.on(android_target).perform_as(AndroidTester)
        Tap.on(ios_target).perform_as(IOSTester)

        android_target.found_by.assert_called_once_with(AndroidTester)
        android_element.click.assert_called_once()
        ios_target.found_by.assert_called_once_with(IOSTester)
        ios_element.click.assert_called_once()
