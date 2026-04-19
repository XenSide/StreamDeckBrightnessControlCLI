# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "streamdeck",
# ]
# ///

import os
import sys

# Must add the script's directory to the DLL search path before importing
# StreamDeck so Windows can locate hidapi.dll placed alongside this script.
if sys.platform == "win32":
    os.add_dll_directory(os.path.dirname(os.path.abspath(__file__)))

from StreamDeck.DeviceManager import DeviceManager


def main() -> None:
    brightness = 10
    args = sys.argv[1:]
    for i, arg in enumerate(args):
        if arg == "--brightness" and i + 1 < len(args):
            brightness = max(0, min(100, int(args[i + 1])))

    manager = DeviceManager()
    decks = manager.enumerate()

    if not decks:
        print("No Stream Deck devices found.")
        sys.exit(1)

    for deck in decks:
        deck.open()
        deck.set_brightness(brightness)
        deck.close()

    print(f"Stream Deck brightness set to {brightness}%.")


if __name__ == "__main__":
    main()
