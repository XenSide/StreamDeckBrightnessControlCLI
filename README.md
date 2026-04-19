# StreamDeckBrightnessControlCLI
Sets the brightness of all connected Stream Deck devices to a specified level. Works with every Stream Deck model (Original, Mini, XL, MK.2, Plus, Neo, etc.) and targets all connected units at once.

## Usage

```
uv run streamdeck_dim.py [--brightness <0-100>]
```

Defaults to 10% if no argument is provided.

## Requirements

`hidapi.dll` must be placed in the same directory as the script (Windows only). The Python dependency (`streamdeck`) is declared inline and handled automatically by `uv`.
