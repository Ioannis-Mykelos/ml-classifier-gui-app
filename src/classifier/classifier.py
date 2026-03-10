""" This file contains the code for the classifier GUI app."""

from typing import Any

from help_functions import my_model, predict_image
from taipy.gui import Gui

# from classes import class_names
# from tensorflow.keras import models
# from PIL import Image
# import numpy as np

# model = models.load_model("../model/baseline_one.keras")

# def predict_image(model, path_to_img):
#     """
#     Predict the image class using the given trained model and a file path to an image.

#     Args:
#         model: The trained Keras model used for prediction.
#         path_to_img: String path to the input image file.

#     Returns:
#         top_prob (float): The probability of the most likely class (between 0 and 1).
#         top_pred (str): The name of the predicted class.
#     """
#     img = Image.open(path_to_img)
#     img = img.convert("RGB")
#     img = img.resize((32, 32))
#     data = np.asarray(img)
#     data = data / 255
#     probs = model.predict(np.array([data])[:1])

#     top_prob = probs.max()
#     top_pred = class_names[np.argmax(probs)]

#     return top_prob, top_pred


CONTENT = ""
IMAGE_PATH = "../images/app_images/placeholder_image.png"
IMAGE_LOGO = "../images/app_images/logo.png"
prob = 0
pred = ""

index = """
<|text-center|
<|{IMAGE_LOGO}|image|width=25vw|>

<|{CONTENT}|file_selector|extensions=.png|>
select an image from your file system

<|{pred}|>

<|{IMAGE_PATH}|image|>

<|{prob}|indicator|value={prob}|min=0|max=100|width=25vw|>
>
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
    if var_name == "content":
        top_prob, top_pred = predict_image(my_model, var_val)
        state.prob = round(top_prob * 100)
        state.pred = "this is a " + top_pred
        state.img_path = var_val
    # print(var_name, var_val)


app = Gui(page=index)

if __name__ == "__main__":
    app.run(use_reloader=True)
