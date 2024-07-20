# Iris Flower Classification Project

## Overview

The Iris Flower Classification project involves developing a machine learning model to classify Iris flowers into three species: Iris-setosa, Iris-versicolor, and Iris-virginica. This is achieved using a Logistic Regression model trained on the Iris dataset. The project includes a GUI application built with Tkinter to interactively classify flowers based on user input.

## Project Structure

- **Data**: The Iris dataset in CSV format (`iris.csv`).
- **Model Training**: Python script (`train_model.py`) to train and save the model.
- **GUI Application**: Python script (`app.py`) that provides a graphical user interface for classifying Iris flowers.
- **Images**: Photos of Iris flowers used for displaying predictions (`iris_setosa.jpg`, `iris_versicolor.jpg`, `iris_virginica.jpg`).

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
