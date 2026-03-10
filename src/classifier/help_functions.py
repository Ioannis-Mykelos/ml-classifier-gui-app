""" This module contains helper functions for the classifier application. """

from typing import Any, Tuple

import numpy as np
from classes import class_names
from PIL import Image
from tensorflow.keras import models

# Load model
my_model = models.load_model("../model/baseline_one.keras")


def predict_image(model: Any = my_model, path_to_img: str = "") -> Tuple[float, str]:
    """
    Predict the image class using the given trained model and a file path to an image.

    Args:
        model: The trained Keras model used for prediction.
        path_to_img: String path to the input image file.

    Returns:
        top_prob (float): The probability of the most likely class (between 0 and 1).
        top_pred (str): The name of the predicted class.
    """
    img = Image.open(path_to_img)
    img = img.convert("RGB")
    img = img.resize((32, 32))
    data = np.asarray(img)
    data = data / 255
    probs = model.predict(np.array([data])[:1])

    top_prob = probs.max()
    top_pred = class_names[np.argmax(probs)]

    return top_prob, top_pred
