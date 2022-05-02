"""
Enable an Actor to use an iOS device.
"""

from appium.webdriver import Remote

from .use_a_mobile_device import UseAMobileDevice


class UseAnIOSDevice(UseAMobileDevice):
    """Enable an Actor to use an iOS device.

    Because of how Appium connects to a hub with desired capabilities,
    you must set up your Android driver ahead of time to give to this
    ability.

    Examples::

        the_actor.can(UseAnIOSDevice.using(ios_driver))
    """

    driver: Remote

    @classmethod
    def using(cls, driver: Remote) -> "UseAnIOSDevice":
        """Supply the Appium driver, connected to an iOS device."""
        return cls(driver)

    def forget(self) -> None:
        """Quit the attached driver."""
        self.driver.quit()

    def __repr__(self) -> str:
        return "Use an iOS device"

    def __init__(self, driver: Remote) -> None:
        self.driver = driver
