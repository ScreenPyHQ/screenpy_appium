from __future__ import annotations

from screenpy_appium.abilities import (
    UseAMobileDevice,
    UseAnAndroidDevice,
    UseAnIOSDevice,
)
from tests.useful_mocks import get_mocked_webdriver


class TestUseAnAndroidDevice:
    def test_can_be_instantiated(self) -> None:
        uaad = UseAnAndroidDevice.using(get_mocked_webdriver())

        assert isinstance(uaad, UseAnAndroidDevice)

    def test_is_instance_of_use_a_mobile_device(self) -> None:
        uaad = UseAnAndroidDevice.using(get_mocked_webdriver())

        assert isinstance(uaad, UseAMobileDevice)

    def test_forget_quits_the_driver(self) -> None:
        driver = get_mocked_webdriver()

        UseAnAndroidDevice.using(driver).forget()

        driver.quit.assert_called_once()


class TestUseAnIOSDevice:
    def test_can_be_instantiated(self) -> None:
        uaid = UseAnIOSDevice.using(get_mocked_webdriver())

        assert isinstance(uaid, UseAnIOSDevice)

    def test_is_instance_of_use_a_mobile_device(self) -> None:
        uaid = UseAnIOSDevice.using(get_mocked_webdriver())

        assert isinstance(uaid, UseAMobileDevice)

    def test_forget_quits_the_driver(self) -> None:
        driver = get_mocked_webdriver()

        UseAnIOSDevice.using(driver).forget()

        driver.quit.assert_called_once()
