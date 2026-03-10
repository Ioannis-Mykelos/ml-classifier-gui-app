# Machine Learning GUI App
Simple machine learning image classifier GUI app.

## Screenshot

<img src="https://raw.githubusercontent.com/MariyaSha/ml_gui_app/main/finishedProject/wireframe.png" width=700px>


## Introduction

In this repository you will find how to create a beautiful GUI application that can classify images of animals and vehicles!

## Project

Includes the complete application, along with 2 jupyter notebooks with plenty of information to help you customize your own image classifying neural networks.


## Quick Start

### Requirements
1. Clone this repository on your local system, and navigate to project folder:
```
https://github.com/Ioannis-Mykelos/ml-classifier-gui-app.git
cd ml-classifier-gui-app
```

> [!NOTE]
> This project uses the `uv` Python package manager for dependency management.
> Follow the instructions from the [official documentation](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer) if you want to run the app locally without Docker.

2. Create a virtual environment with `uv` and install dependencies (uv + WSL example):
```
uv venv
uv lock
uv sync
```

3. Activate your `.venv` environment (created by `uv sync`):
- Windows use `.venv\Scripts\activate`
- Linux `source .venv/bin/activate`

4. Create a juputer kernel from your new virtual environment (under `Jupyter kernel`)
```
# Create the kernel
python -m ipykernel install --user --name=ml-classifier-gui-app --display-name "ml-classifier-gui-app-env"
```

5. Run the App
```
python src/classifier/classifier.py
```

## Play with your web app

You can find your GUI application in `http://127.0.0.1:5000/`.

## Extend your Deep Learning model, by training it in a bigger sample, with more images, or try other image classification uses. It is up to you.


