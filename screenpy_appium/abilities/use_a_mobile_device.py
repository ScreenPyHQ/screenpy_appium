"""
A common base class for the specific device abilities, which will help when
using the Actor's `has_ability_to` and `uses_ability_to` methods.
"""


class UseAMobileDevice:
    """A common base to make ability discovery easier.

    This Ability should not be granted directly.

    There are some Actions or Questions which can be performed/asked whether
    the Actor can :class:`~screenpy_appium.abilities.UseAnIOSDevice` or
    :class:`~screenpy_appium.abilities.UseAnAndroidDevice`, so it doesn't
    matter which of them we use. In those cases, we can do this::

        the_actor.has_ability_to(UseAMobileDevice)

        the_actor.uses_ability_to(UseAMobileDevice)
    """
