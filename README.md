# Cockpit preset for [Starship](https://starship.rs/)

This is a preset for the [Starship](https://starship.rs/) cross-shell prompt.

![Starship Cockpit Demo](./assets/demo.png)

## Requirements

Install and enable a [Nerd Font](https://www.nerdfonts.com/) in your terminal.

Install [Starship](https://starship.rs/) and configure your shell to use it.

> [!TIP]
> More information about Starship installation and configuration can be found [here](https://starship.rs/guide/#%F0%9F%9A%80-installation).

## Installation

Copy the `starship.toml` file to your Starship configuration directory.

> [!TIP]
> More information about Starship configuration files can be found [here](https://starship.rs/config/#configuration).

## Palettes

This preset includes predefined palettes that you can enable by setting the `palette` value in your `starship.toml` file.

> [!NOTE]
> Background color is not included in the palette. You can set it in your terminal settings.

### Default

![Starship Cockpit Default Palette](./assets/palettes/default.png)

```toml
palette = "default"
```

> [!IMPORTANT]
> The default palette uses standard terminal colors, ensuring it blends with your terminal color scheme. In the image you can see the [Catppuccin Mocha](https://raw.githubusercontent.com/mbadolato/iTerm2-Color-Schemes/master/schemes/catppuccin-mocha.itermcolors) iTerm2 color scheme.

### Gruvbox Dark

![Starship Cockpit Gruvbox Dark Palette](./assets/palettes/gruvbox_dark.png)

```toml
palette = "gruvbox_dark"
```

### Gruvbox Light

![Starship Cockpit Gruvbox Light Palette](./assets/palettes/gruvbox_light.png)

```toml
palette = "gruvbox_light"
```

## Configuration

### Battery

Environment variables:

| Variable | Default | Description  |
| -------- | ------- | ------------ |
| `STARSHIP_COCKPIT_BATTERY_ENABLED` | `false` | Enable or disable the battery module. |
| `STARSHIP_COCKPIT_BATTERY_THRESHOLD` | `100` | Set the battery threshold. |

Example configuration:
```bash
export STARSHIP_COCKPIT_BATTERY_ENABLED=true
export STARSHIP_COCKPIT_BATTERY_THRESHOLD=10
```

### Keyboard Layout

> [!NOTE]
> Currently, the keyboard layout module is only supported on macOS. Support for other operating systems may be added in the future.

Environment variables:

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `STARSHIP_COCKPIT_KEYBOARD_LAYOUT_ENABLED` | `false` | Enable or disable the keyboard layout module. |
| `STARSHIP_COCKPIT_KEYBOARD_LAYOUT_[LAYOUT_ID]` | - | Custom alias for layout. |

Example configuration:
```bash
export STARSHIP_COCKPIT_KEYBOARD_LAYOUT_ENABLED=true
export STARSHIP_COCKPIT_KEYBOARD_LAYOUT_ABC=ENG
export STARSHIP_COCKPIT_KEYBOARD_LAYOUT_UKRAINIAN=UKR
```
