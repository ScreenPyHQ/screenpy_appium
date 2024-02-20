from __future__ import annotations

from typing import TYPE_CHECKING, cast
from unittest import mock

from appium.webdriver import Remote

from screenpy_appium import Target
from screenpy_appium.abilities import UseAnAndroidDevice

if TYPE_CHECKING:
    from screenpy import Actor


def get_mock_target_class() -> type:
    class FakeTarget(Target):
        def __new__(cls, *args: object, **kwargs: object) -> FakeTarget:  # noqa: ARG003
            return mock.create_autospec(FakeTarget, instance=True)

    return FakeTarget


def get_mocked_webdriver() -> mock.Mock:
    return mock.create_autospec(Remote, instance=True)


def get_mocked_browser(actor: Actor) -> mock.Mock:
    return cast(mock.Mock, actor.ability_to(UseAnAndroidDevice).driver)
