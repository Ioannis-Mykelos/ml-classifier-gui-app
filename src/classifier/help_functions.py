""" This module contains helper functions for the classifier application. """

from pathlib import Path
from typing import Any, Tuple

import numpy as np
from classes import class_names
from PIL import Image
from tensorflow.keras import models

# Get absolute path to project root
project_root = Path(__file__).resolve().parent.parent.parent
model_path = project_root / "src" / "model" / "baseline_one.h5"
print("-----------------")

print(f"Project root: {project_root}")
print(f"Model path: {model_path}")
print(f"Model exists: {model_path.exists()}")
print("-----------------")

if not model_path.exists():
    raise FileNotFoundError(f"Model not found at {model_path}")

my_model = models.load_model(str(model_path))


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
