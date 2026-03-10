""" This module contains helper functions for the classifier application. """

from pathlib import Path
from typing import Any, Tuple

import numpy as np
from classes import class_names
from PIL import Image
from tensorflow.keras import models


def load_model(the_model_path: str):
    """
    Loads a trained Keras model from the specified file path.

    Args:
        the_model_path (str): The file path to the trained Keras model.

    Returns:
        model: The loaded Keras model instance if successful, otherwise None.

    Raises:
        FileNotFoundError: If the model file does not exist at the given path.
        Exception: For any other issues encountered during model loading.
    """
    try:
        model_path = Path(the_model_path)
        if not model_path.exists():
            raise FileNotFoundError(f"Model not found at {model_path}")
        model = models.load_model(model_path)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None


def predict_image(model: Any, path_to_img: str) -> Tuple[float, str]:
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
