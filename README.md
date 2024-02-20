ScreenPy Appium
===============

[![Build Status](../../actions/workflows/tests.yml/badge.svg)](../../actions/workflows/tests.yml)
[![Build Status](../../actions/workflows/lint.yml/badge.svg)](../../actions/workflows/lint.yml)

[![Supported Versions](https://img.shields.io/pypi/pyversions/screenpy_appium.svg)](https://pypi.org/project/screenpy_appium)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

```
TITLE CARD:
                               "ScreenPy Appium"
TITLE DISAPPEARS.
                                                                      FADE IN:
INT. DOCUMENTATION - MIDNIGHT

Camera fades in on a white, slightly curved wall. AUDIENCE enters from a
hidden door and stumbles, sliding down the smooth surface - this room is
spherical. The door closes and disappears again.

                              AUDIENCE
                              (surprised)
            Whoa! What is this place?

In the center of the sphere floats a many-armed robot, interacting with
dozens of nearby gadgets. They whir, whizz, and flash lights as the robot
twitches knobs and toggles levers.

                              NARRATOR (V.O.)
            This is the Appium extension module. Appium allows you to
            automate many different kinds of devices. This module
            allows your Actors to interact with it.

AUDIENCE observes the robot warily, yet a fascinated expression creeps
onto their face. A beat, then AUDIENCE shakes their head to snap out of
it. AUDIENCE looks around, confused.

                              AUDIENCE
            Uh, so how do we get out of here?

As if summoned by the question, a round aperture opens in the floor
beneath the robot, and an elevator appears. AUDIENCE cautiously steps
onto it and suddenly descends out of frame.

                                                                      FADE OUT
```


Installation
------------
    pip install screenpy_appium

or

    pip install screenpy[appium]


Documentation
-------------
Please check out the [Read The Docs documentation](https://screenpy-appium-docs.readthedocs.io/en/latest/) for the latest information about this module!

You can also read the [ScreenPy Docs](https://screenpy-docs.readthedocs.io/en/latest/) for more information about ScreenPy in general.


Contributing
------------
You want to contribute? Great! Here are the things you should do before submitting your PR:

1. Fork the repo and git clone your fork.
1. `dev` install the project package:
    1. `pip install -e .[dev]`
    1. Optional (poetry users):
        1. `poetry install --extras dev`
1. Run `pre-commit install` once.
1. Run `tox` to perform tests frequently.
1. Create pull-request from your branch.

That's it! :)
