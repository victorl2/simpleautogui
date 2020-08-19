wmctrl -ir $1 -b remove,maximized_horz
wmctrl -ir $1 -b remove,maximized_vert
xdotool windowmove $1 $2 $3