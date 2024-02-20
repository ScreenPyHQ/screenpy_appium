from __future__ import annotations

from unittest import mock

from appium.webdriver import Remote

from screenpy_appium import Target


def get_mock_target_class() -> type:
    class FakeTarget(Target):
        def __new__(cls, *args: object, **kwargs: object) -> FakeTarget:  # noqa: ARG003
            return mock.create_autospec(FakeTarget, instance=True)

    return FakeTarget


def get_mocked_webdriver() -> mock.Mock:
    return mock.create_autospec(Remote, instance=True)
