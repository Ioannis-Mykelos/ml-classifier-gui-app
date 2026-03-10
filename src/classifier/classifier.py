""" This file contains the code for the classifier GUI app."""

from pathlib import Path
from typing import Any

from help_functions import load_model, predict_image
from taipy.gui import Gui

# Get absolute path to project root
project_root = Path(__file__).resolve().parent.parent.parent
model_path = project_root / "src" / "model" / "baseline.keras"
image_path = project_root / "src" / "images" / "app_images" / "placeholder_image.png"
logo_path = project_root / "src" / "images" / "app_images" / "logo.png"
content = ""
prob = 0
pred = ""

my_model = load_model(the_model_path=model_path)

index = """
<|text-center|
<|{logo_path}|image|width=25vw|>

<|{content}|file_selector|extensions=.png,.jpg|>
select an image from your file system

<|{pred}|>

<|{image_path}|image|>

<|{prob}|indicator|value={prob}|min=0|max=100|width=25vw|>
|>
"""


def on_change(state: Any, var_name: str, var_val: Any) -> None:
    """
    Callback function that handles changes in the state of the GUI app.

    Args:
        state: The current state object of the app, used to store and update UI variables.
        var_name (str): The name of the variable in the app whose value has changed.
        var_val: The new value assigned to the variable.

    This function is typically triggered by interactions in the GUI, such as selecting an image file.
    When the 'content' variable changes (corresponding to image file selection), it processes
    the selected image using the pre-trained model, updates the prediction and probability displays,
    and refreshes the image shown in the GUI.
    """
    print("---------------------------------------------")
    if var_name == "content":
        top_prob, top_pred = predict_image(model=my_model, path_to_img=var_val)
        state.prob = round(top_prob * 100)
        state.pred = "this is a " + top_pred
        state.image_path = var_val
    print(f" - The Var name = {var_name}")
    print(f" - The Var value = {var_val}")


app = Gui(page=index)

if __name__ == "__main__":
    app.run(use_reloader=True)
