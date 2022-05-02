from unittest import mock

import pytest

from screenpy import AnActor
from screenpy_appium.abilities import UseAnAndroidDevice, UseAnIOSDevice


@pytest.fixture(scope="function")
def AndroidTester() -> AnActor:
    """Provide an Actor with mocked web browsing abilities."""
    UseAnAndroidDevice_Mocked = mock.Mock(spec=UseAnAndroidDevice)
    UseAnAndroidDevice_Mocked.driver = mock.Mock()

    return AnActor.named("Android Tester").who_can(UseAnAndroidDevice_Mocked)


@pytest.fixture(scope="function")
def IOSTester() -> AnActor:
    """Provide an Actor with mocked web browsing abilities."""
    UseAnIOSDevice_Mocked = mock.Mock(spec=UseAnIOSDevice)
    UseAnIOSDevice_Mocked.driver = mock.Mock()

    return AnActor.named("iOS Tester").who_can(UseAnIOSDevice_Mocked)
