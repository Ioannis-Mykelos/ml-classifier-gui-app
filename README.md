# Machine Learning GUI App
Simple machine learning image classifier GUI app.

## Introduction

In this repository you will find how to create a beautiful GUI application that can classify images of animals and vehicles!

<img src="https://github.com/MariyaSha/ml_gui_app/assets/32107652/4925650b-9ee5-4b55-ab7c-415b772762c1" width=600px>

## Finished Project

Includes the complete application, along with 2 jupyter notebooks with plenty of information to help you customize your own image classifying neural networks.
<br>
The complete app is also live and running on Taipy's cloud: https://classifier.taipy.cloud/

## Requirements
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
uv init
uv add pre-commit fastapi requests jinja2 python-multipart uvicorn
uv lock
uv sync
```

3. Activate your `.venv` environment (created by `uv sync`):
- Windows use `.venv\Scripts\activate`
- Linux `source .venv/bin/activate`


## Screenshot

<img src="https://raw.githubusercontent.com/MariyaSha/ml_gui_app/main/finishedProject/wireframe.png" width=600px>

