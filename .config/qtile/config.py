# # # # #
#
#  This is a customized config for the Qtile window manager.
#
#  For a list previous contributors and increased comment-based documentation,
#  please refer to the default config file at: ~/usr/share/doc/qtile/default_config.py.
#
# # # # #


from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4" # Otherwise known as "the Windows key"
terminal = guess_terminal()

accentColour = "#00506b"

keys = [

    # Move the selector
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move the selected window
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Resize the selected window
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # misc
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Launch programs; change these at your will
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch a terminal"),
    Key([mod], "f", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key([mod], "c", lazy.spawn("code"), desc="Launch Visual Studio Code"),
    Key([mod], "n", lazy.spawn("pcmanfm"), desc="Launch Pcmanfm"),
    Key([mod], "d", lazy.spawn("discord"), desc="Launch Discord"),
]

groups = [Group(i) for i in "123456789"]
for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.Columns(border_width=2, margin=2, border_focus=accentColour),
    layout.Max(),
    layout.Floating(border_width=1),
]

widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=5),
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(background=accentColour),
                widget.Chord(chords_colors={"launch": ("#ff0000", "#ffffff")}, name_transform=lambda name: name.upper()),

                widget.Spacer(length=10),
                widget.CheckUpdates(initial_text='Checking for updates...', display_format="Updates: {updates}", no_update_string="All Packages Up-to-date", execute="sudo pacman -Syy", update_interval=10),
                widget.Spacer(length=9),
                widget.Sep(),
                widget.Systray(),
                widget.Sep(),
                widget.Spacer(length=7),
                widget.Clock(format="%A, %B %d, %Y - %H:%M %p"),
                widget.Spacer(length=5),
                widget.QuickExit(default_text="[Logout]", countdown_format= "[{} secs]"),
            ],
            30, # the vertical size of the bar
        ),
        wallpaper='~/Pictures/Wallpapers/wallpaper.jpg',
        wallpaper_mode='stretch',
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
