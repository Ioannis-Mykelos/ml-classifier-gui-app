""" This file contains the code for the GUI app. """

from taipy import Gui

img_path = "finishedProject/images/app_images/placeholder_image.png"
logo_path = "finishedProject/images/app_images/logo.png"
content = ""


# The callback function
# state: holds the current variables of the app
# var_name: the name of the variable that was changed
# var_value: the new value of that variable
def on_change(state, var_name, var_value):
    if var_name == "content":
        # Update the image path displayed on the screen
        state.img_path = var_value


index = """
<|text-center|
<|{logo_path}|image|width=25vw|>

#### Select your image from your file system
<|{content}|file_selector|extensions=.png,.jpg|>

<|{img_path}|image|width=25vw|>
|>
"""

app = Gui(page=index)

if __name__ == "__main__":
    app.run(use_reloader=True, port=5000)
