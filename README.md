Sure, here is the updated `README.md` with the changes and format similar to the one you provided:

```markdown
# Iris Flower Classification Project

## Overview

The Iris Flower Classification project involves developing a machine learning model to classify Iris flowers into three species: Iris-setosa, Iris-versicolor, and Iris-virginica. The model uses a Logistic Regression algorithm trained on the Iris dataset. This project includes a GUI application built with Tkinter to interactively input flower measurements and obtain classification results.

## Project Structure

- **Data**: The dataset containing Iris flower measurements (iris.csv).
- **Model Training**: Python script (`train_model.py`) to train and save the model.
- **GUI Application**: Python script (`app.py`) that provides a graphical user interface for classifying Iris flowers based on user input.
- **Model Files**: Saved model file (`logistic_regression_model.pkl`).
- **Flower Images**: JPEG files for displaying images of the Iris flowers (iris_setosa.jpg, iris_versicolor.jpg, iris_virginica.jpg).

## Objectives

1. [Load and Explore the Dataset](#load-and-explore-the-dataset)
2. [Data Preprocessing](#data-preprocessing)
3. [Train-Test Split](#train-test-split)
4. [Model Training](#model-training)
5. [Model Evaluation](#model-evaluation)
6. [GUI Application](#gui-application)

## Getting Started

### Prerequisites

- Python 3.x
- `pandas`
- `scikit-learn`
- `joblib`
- `tkinter`
- `Pillow`

You can install the required packages using pip:

```bash
pip install pandas scikit-learn joblib Pillow
```

### Training the Model

1. Ensure `iris.csv` is in the project directory.
2. Run `train_model.py` to train and save the model:

   ```bash
   python train_model.py
   ```

### Running the GUI Application

1. Ensure `logistic_regression_model.pkl` and image files (`iris_setosa.jpg`, `iris_versicolor.jpg`, `iris_virginica.jpg`) are in the same directory as `app.py`.
2. Run `app.py`:

   ```bash
   python app.py
   ```

   This will open a GUI application where you can input flower measurements and get a classification result along with the corresponding flower image.

## Usage

1. Enter sepal length, sepal width, petal length, and petal width into the GUI.
2. Click "Predict" to see the classification result and the image of the predicted flower species.

## Troubleshooting

- **Deprecation Warnings**: Update your packages if you see warnings about deprecated features.
- **Input Issues**: Ensure that you are entering numerical values for the flower measurements. Invalid input will trigger an error message.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## Acknowledgments

This project utilizes the Iris dataset for classification and leverages Logistic Regression and Tkinter for model training and GUI development.

## Contact

For questions or feedback, please contact [Issa El Mousleh](mailto:issaelmousleh@outlook.com).
