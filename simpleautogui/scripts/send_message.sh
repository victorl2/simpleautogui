## PASS WINDOW ID AS THE FIRST ARGUMENT
xdotool type --delay 500 --window $1 $2
xdotool key --delay 250 --window $1 Return