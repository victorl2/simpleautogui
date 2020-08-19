from subprocess import PIPE, STDOUT, Popen

SCRIPT_DIR = '/scripts/'


def script_path(script_name):
    """Return the path to the file inside the main scripts folder"""
    if script_name[0] == '/':
        return SCRIPT_DIR + script_name[1:]
    return SCRIPT_DIR + script_name


def enable_always_on_top(window_id):
    """Enable window always on top"""
    Popen(["/bin/bash", script_path('scripts/always_on_top.sh'),
           window_id, 'enable'], stderr=STDOUT, stdout=PIPE)


def disable_always_on_top(window_id):
    """Disable window always on top"""
    Popen(["/bin/bash", script_path('always_on_top.sh'),
           window_id, 'disable'], stderr=STDOUT, stdout=PIPE)


def resize_window(window_id, width, height):
    """Resize the window to the given width x height"""
    Popen(["/bin/bash", script_path('resize_window.sh'), window_id,
           str(width), str(height)], stderr=STDOUT, stdout=PIPE)


def press_key(key):
    """Press and hold a given keyboard key"""
    Popen(["/bin/bash", script_path('press_key.sh'), key], stderr=STDOUT, stdout=PIPE)


def release_key(key):
    """Release a pressed keyboard key"""
    Popen(["/bin/bash", script_path('release_key.sh'), key], stderr=STDOUT, stdout=PIPE)


def press_key_once(key):
    """Press a keyboard key one time without holding it"""
    Popen(["/bin/bash", script_path('press_key_once.sh'), key], stderr=STDOUT, stdout=PIPE)


def send_message(window_id, text_message):
    """Type a message and sends with the enter key on the keyboard"""
    Popen(["/bin/bash", script_path('send_message.sh'), window_id,
           text_message], stderr=STDOUT, stdout=PIPE)


def click(window_id, x, y):
    """ Click in a position on the current window, the position is relative to the current window """
    Popen(["/bin/bash", script_path('move_mouse.sh'), window_id,
           str(x), str(y)], stderr=STDOUT, stdout=PIPE)


def activate_window(window_id):
    """Activate the window"""
    Popen(["/bin/bash", script_path('activate_window.sh'), window_id]
          , stderr=STDOUT, stdout=PIPE)


def move_window(window_id, x, y):
    """ Move the app window to the position (x,y) """
    Popen(["/bin/bash", script_path('window_move.sh'),
           window_id, str(x), str(y)], stderr=STDOUT, stdout=PIPE)

