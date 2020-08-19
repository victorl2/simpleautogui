if [ $2 == "enable" ]; then
    wmctrl -ir $1 -b add,above
else
    wmctrl -ir $1 -b remove,above
fi