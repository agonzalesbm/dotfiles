from libqtile.widget import TextBox


def left_arrow(bg_color, fg_color):
    return TextBox(
        text="\ueb6f",
        fontsize=45,
        foreground=fg_color,
        background=bg_color,
        padding=0
    )
