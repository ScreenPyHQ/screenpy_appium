from unittest import mock

import pytest
from appium.webdriver import Remote
from screenpy import AnActor

from screenpy_appium.abilities import UseAnAndroidDevice, UseAnIOSDevice


@pytest.fixture()
def AndroidTester() -> AnActor:
    """Provide an Actor with mocked web browsing abilities."""
    UseAnAndroidDevice_Mocked = mock.create_autospec(UseAnAndroidDevice, instance=True)
    UseAnAndroidDevice_Mocked.driver = mock.create_autospec(Remote, instance=True)

    return AnActor.named("Android Tester").who_can(UseAnAndroidDevice_Mocked)


@pytest.fixture()
def IOSTester() -> AnActor:
    """Provide an Actor with mocked web browsing abilities."""
    UseAnIOSDevice_Mocked = mock.create_autospec(UseAnIOSDevice, instance=True)
    UseAnIOSDevice_Mocked.driver = mock.create_autospec(Remote, instance=True)

    return AnActor.named("iOS Tester").who_can(UseAnIOSDevice_Mocked)
