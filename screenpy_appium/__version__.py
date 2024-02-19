"""
    .s5SSSs.  .s5SSSs.  .s5SSSs.  .s5SSSs.  .s5SSSs.  .s    s.  .s5SSSs.  .s5 s.
          SS.       SS.       SS.       SS.       SS.       SS.       SS.     SS.
    sS    `:; sS    `:; sS    S%S sS    `:; sS    `:; sSs.  S%S sS    S%S ssS SSS
    SS        SS        SS    S%S SS        SS        SS`S. S%S SS    S%S SSS SSS
    `:;;;;.   SS        SS .sS;:' SSSs.     SSSs.     SS `S.S%S SS .sS::'  SSSSS
          ;;. SS        SS    ;,  SS        SS        SS  `sS%S SS          SSS
          `:; SS        SS    `:; SS        SS        SS    `:; SS          `:;
    .,;   ;,. SS    ;,. SS    ;,. SS    ;,. SS    ;,. SS    ;,. SS          ;,.
    `:;;;;;:' `:;;;;;:' `:    ;:' `:;;;;;:' `:;;;;;:' :;    ;:' `:          ;:'

                .s5SSSs.  .s5SSSs.  .s5SSSs.  s.  .s    s.  .s5ssSs.
                      SS.       SS.       SS. SS.       SS.    SS SS.
                sS    S%S sS    S%S sS    S%S S%S sS    S%S sS SS S%S
                SS    S%S SS    S%S SS    S%S S%S SS    S%S SS :; S%S
                SSSs. S%S SS .sS::' SS .sS::' S%S SS    S%S SS    S%S
                SS    S%S SS        SS        S%S SS    S%S SS    S%S
                SS    `:; SS        SS        `:; SS    `:; SS    `:;
                SS    ;,. SS        SS        ;,. SS    ;,. SS    ;,.
                :;    ;:' `:        `:        ;:' `:;;;;;:' :;    ;:'
"""

import importlib.metadata

metadata = importlib.metadata.metadata("screenpy_adapter_allure")

__title__ = metadata["Name"]
__description__ = metadata["Summary"]
__url__ = metadata["Home-page"]
__version__ = metadata["Version"]
__author__ = metadata["Author"]
__author_email__ = metadata["Author-email"]
__license__ = metadata["License"]
__copyright__ = f"2019-2024 {__author__}"
