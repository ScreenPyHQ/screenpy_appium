"""Enable an actor to use an Android device."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .use_a_mobile_device import UseAMobileDevice

if TYPE_CHECKING:
    from appium.webdriver import Remote


class UseAnAndroidDevice(UseAMobileDevice):
    """Enable an Actor to use an Android device.

    Because of how Appium connects to a hub with desired capabilities,
    you must set up your Android driver ahead of time to give to this
    ability.

    Examples::

        the_actor.can(UseAnAndroidDevice.using(android_driver))
    """

    driver: Remote

    @classmethod
    def using(cls, driver: Remote) -> "UseAnAndroidDevice":
        """Supply the Appium driver, connected to an Android device."""
        return cls(driver)

    def forget(self) -> None:
        """Quit the attached driver."""
        self.driver.quit()

    def __repr__(self) -> str:
        """Represents ability to use android driver."""
        return "Use an Android device"

    def __init__(self, driver: Remote) -> None:
        self.driver = driver
