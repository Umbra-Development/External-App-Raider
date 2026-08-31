"""PyInstaller entry point for the combined Umbra application."""

import sys

from external_app_raider import PACKAGED_BOT_ARGUMENT


def main() -> None:
    if PACKAGED_BOT_ARGUMENT in sys.argv[1:]:
        sys.argv.remove(PACKAGED_BOT_ARGUMENT)
        from external_app_raider import main as run_bot

        run_bot()
        return

    from umbra_gui import main as run_gui

    run_gui()


if __name__ == "__main__":
    main()
