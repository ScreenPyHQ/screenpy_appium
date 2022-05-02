=======
Targets
=======

Targets combine
a human-readable string
and a locator.
Together,
this provides us with readable logs
and Appium with a directive
on what element to interact with.

By default,
ScreenPy Appium's Target class
attempts to guess between
an XPATH locator
or an Accessibility ID locator.
If you're using a different strategy,
you will need to supply
the appropriate ``AppiumBy`` value::

    # assumed XPATH locator
    USERNAME_FIELD = Target.the("username field").located_by("//android.widget.EditText")

    # assumed Accessibility ID locator
    HAMBURGER_MENU = Target.the("hamburger menu").located_by("Navigation Menu")

    # specify which strategy to use
    HOME_ADDRESS_ITEM = Target.the("home address item").located((AppiumBy.NAME, "Home Address"))

The value passed into
the Target's :meth:`~screenpy_appium.Target.the` method
will be used during :external+screenpy:ref:`Narration`.
The value passed in
to the :meth:`~screenpy_appium.Target.located_by` method
will be used by Appium.

We can use these Targets
with our Actions::

    the_actor.attempts_to(Enter.the_text("1337_blaze_7331").into_the(USERNAME_FIELD))

    the_actor.attempts_to(Tap.on_the(HAMBURGER_MENU))

    the_actor.should(See.the(Text.of_the(HOME_ADDRESS_ITEM), ReadsExactly("123 Home St.")))
