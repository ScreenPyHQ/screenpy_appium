from unittest import mock

from screenpy_appium.abilities import (
    UseAMobileDevice,
    UseAnAndroidDevice,
    UseAnIOSDevice,
)


class TestUseAnAndroidDevice:
    def test_can_be_instantiated(self):
        uaad = UseAnAndroidDevice.using(None)

        assert isinstance(uaad, UseAnAndroidDevice)

    def test_is_instance_of_use_a_mobile_device(self):
        uaad = UseAnAndroidDevice.using(None)

        assert isinstance(uaad, UseAMobileDevice)

    def test_forget_quits_the_driver(self):
        driver = mock.Mock()

        UseAnAndroidDevice.using(driver).forget()

        driver.quit.assert_called_once()


class TestUseAnIOSDevice:
    def test_can_be_instantiated(self):
        uaid = UseAnIOSDevice.using(None)

        assert isinstance(uaid, UseAnIOSDevice)

    def test_is_instance_of_use_a_mobile_device(self):
        uaid = UseAnIOSDevice.using(None)

        assert isinstance(uaid, UseAMobileDevice)

    def test_forget_quits_the_driver(self):
        driver = mock.Mock()

        UseAnIOSDevice.using(driver).forget()

        driver.quit.assert_called_once()
