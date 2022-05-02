====================
Additional Abilities
====================

ScreenPy Appium adds three additional abilities,
which enable Actors
to use Appium
to use mobile devices.

One ability,
:class:`~screenpy_appium.abilities.UseAMobileDevice`,
is not an ability to give to an Actor.
This ability is meant to make it easier
for Actions and Questions
to find whichever of the other two abilities
an Actor has.

.. module:: screenpy_appium.abilities

UseAMobileDevice
----------------

.. autoclass:: UseAMobileDevice
    :members:

UseAnAndroidDevice
------------------

.. autoclass:: UseAnAndroidDevice
    :members:

UseAnIOSDevice
--------------

.. autoclass:: UseAnIOSDevice
    :members:
