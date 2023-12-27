# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# ░█████╗░███╗░░██╗██████╗░██╗░░░██╗██╗░██████╗  ░██████╗░████████╗██╗██╗░░░░░███████╗
# ██╔══██╗████╗░██║██╔══██╗╚██╗░██╔╝╚█║██╔════╝  ██╔═══██╗╚══██╔══╝██║██║░░░░░██╔════╝
# ███████║██╔██╗██║██║░░██║░╚████╔╝░░╚╝╚█████╗░  ██║██╗██║░░░██║░░░██║██║░░░░░█████╗░░
# ██╔══██║██║╚████║██║░░██║░░╚██╔╝░░░░░░╚═══██╗  ╚██████╔╝░░░██║░░░██║██║░░░░░██╔══╝░░
# ██║░░██║██║░╚███║██████╔╝░░░██║░░░░░░██████╔╝  ░╚═██╔═╝░░░░██║░░░██║███████╗███████╗
# ╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░░░░╚═════╝░  ░░░╚═╝░░░░░░╚═╝░░░╚═╝╚══════╝╚══════╝
#
# ░█████╗░░█████╗░███╗░░██╗███████╗██╗░██████╗░██╗░░░██╗██████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗
# ██╔══██╗██╔══██╗████╗░██║██╔════╝██║██╔════╝░██║░░░██║██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
# ██║░░╚═╝██║░░██║██╔██╗██║█████╗░░██║██║░░██╗░██║░░░██║██████╔╝███████║░░░██║░░░██║██║░░██║██╔██╗██║
# ██║░░██╗██║░░██║██║╚████║██╔══╝░░██║██║░░╚██╗██║░░░██║██╔══██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║
# ╚█████╔╝╚█████╔╝██║░╚███║██║░░░░░██║╚██████╔╝╚██████╔╝██║░░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
# ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░░░░╚═╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

import os
import forms_generator
import color_palette
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"

# Command line values
terminal = "alacritty"
rofi = "rofi -show-icons -show drun"
down_volume = "pactl -- set-sink-volume 0 -10%"
up_volume = "pactl -- set-sink-volume 0 +10%"
silence_volume = "pactl -- set-sink-volume 0 0%"
down_bright = "brightnessctl set 10%-"
up_bright = "brightnessctl set +10%"
take_screenshot = "flameshot gui"

init_cmd = [
    "feh --bg-fill ~/Pictures/wallpapers/samurai-girl-dragon-back-tattoo.jpg",
    "picom &",
    "flameshot &",
    "pasystray &",
    "blueman-applet &",
    "nm-tray &"
]

for cmd in init_cmd:
    os.system(cmd)

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Shortcuts config
    Key([mod], "p", lazy.spawn(rofi)),
    Key([mod], "i", lazy.spawn(down_volume)),
    Key([mod], "u", lazy.spawn(up_volume)),
    Key([mod], "o", lazy.spawn(silence_volume)),
    Key([mod], "n", lazy.spawn(down_bright)),
    Key([mod], "m", lazy.spawn(up_bright)),
    Key([mod], "s", lazy.spawn(take_screenshot))
]

# Groups layout
groups = [
    Group('1', label="一"),
    Group('2', label="二"),
    Group('3', label="三"),
    Group('4', label="四"),
    Group('5', label="五"),
    Group('6', label="六"),
    Group('7', label="七"),
    Group('8', label="八"),
    Group('9', label="九"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


# Layout config
layouts = [
    layout.Columns(
        border_width=3,
        border_focus=color_palette.white_color,
        border_normal="#403f3e",
        border_on_single=True,
        margin=8
    ),
    layout.Max(
        border_focus="#f2eeed",
        border_width=3,
        margin=8
    )
]

# Font widgets default
widget_defaults = dict(
    font="Agave Nerd Font",
    fontsize=16,
    padding=2,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                # WARNING: if you want to use widgets dependents of psutil lib
                # and you are using pipx like enviroment use "pipx inject qtile psutil"
                widget.GroupBox(
                    highlight_method="block",
                    this_current_screen_border=color_palette.yellow_color,
                    inactive="#9a9c9a",
                    padding_x=1
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                forms_generator.left_arrow(
                    "", color_palette.blue_color),
                widget.Memory(
                    background=color_palette.blue_color,
                    format="{MemUsed: .0f}{mm}"
                ),
                widget.CPU(
                    format=" \uf4bc  {freq_current}GHz {load_percent}%",
                    background=color_palette.blue_color
                ),
                forms_generator.left_arrow(
                    color_palette.blue_color, color_palette.bright_yellow_color),
                widget.Net(
                    format="{down:6.2f}{down_suffix:<2}↓↑{up:6.2f}{up_suffix:<2}",
                    background=color_palette.bright_yellow_color,
                    foreground="#000000"
                ),
                forms_generator.left_arrow(
                    color_palette.bright_yellow_color, color_palette.purple_color),
                widget.Clock(
                    format="\uf073  %Y-%m-%d \uf43a  %I:%M %p",
                    background=color_palette.purple_color
                ),
                forms_generator.left_arrow(
                    color_palette.purple_color, color_palette.green_color),
                widget.Battery(
                    background=color_palette.green_color,
                    format="{char} {percent:2.0%}",
                    discharge_char="\uf240 ",
                    empty_char="",
                    full_char="",
                    charge_char="\uf0e7",
                    low_percentage=0.2,
                    low_foreground=color_palette.red_color,

                ),
            ],
            24,
            background="#00000050"
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of xprop to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
