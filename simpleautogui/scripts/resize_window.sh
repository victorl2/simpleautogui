#https://www.semicomplete.com/projects/xdotool/
#https://stackoverflow.com/questions/49755831/wmctrl-moving-a-fullscreen-window
wmctrl -ir $1 -b remove,maximized_horz
wmctrl -ir $1 -b remove,maximized_vert
xdotool windowsize $1 $2 $3