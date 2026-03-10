""" This file contains the code for the GUI app. """

from taipy import Gui

IMAGE_PATH = "finishedProject/images/app_images/placeholder_image.png"
LOGO_PATH = "finishedProject/images/app_images/logo.png"
CONTENT = ""


# The callback function
# state: holds the current variables of the app
# var_name: the name of the variable that was changed
# var_value: the new value of that variable
def on_change(state, var_name, var_value):
    """
    On change function for the GUI.
    Args:
        state: The state of the app.
        var_name: The name of the variable that was changed.
        var_value: The new value of that variable.
    """
    if var_name == "content":
        # Update the image path displayed on the screen
        state.IMAGE_PATH = var_value


INDEX_PAGE = """
<|text-center|
<|{LOGO_PATH}|image|width=25vw|>

#### Select your image from your file system
<|{CONTENT}|file_selector|extensions=.png,.jpg|>

<|{IMAGE_PATH}|image|width=25vw|>
|>
"""

app = Gui(page=INDEX_PAGE)

if __name__ == "__main__":
    app.run(use_reloader=True, port=5000)
