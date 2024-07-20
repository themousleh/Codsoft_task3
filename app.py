import tkinter as tk
from tkinter import messagebox, Toplevel, Label
from PIL import Image, ImageTk
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Load the pre-trained model and scaler
model = joblib.load('logistic_regression_model.pkl')
scaler = joblib.load('scaler.pkl')

# Define a function to display the result with an image
def show_result_with_image(prediction):
    # Create a new window for the result
    result_window = Toplevel(window)
    result_window.title("Prediction Result")
    result_window.configure(bg='#ffffff')

    # Define a default image path in case of an error
    image_path = None
    
    # Load the image corresponding to the prediction
    if prediction == "Iris-setosa":
        image_path = "Iris-setosa.jpeg"
    elif prediction == "Iris-versicolor":
        image_path = "iris-versicolor.jpeg"
    elif prediction == "Iris-virginica":
        image_path = "iris-verginica.jpeg"
    else:
        messagebox.showerror("Error", "Unknown prediction value.")
        return

    if image_path:
        try:
            img = Image.open(image_path)
            img = img.resize((250, 250), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
        except Exception as e:
            messagebox.showerror("Image Error", f"Error loading image: {e}")
            return

        # Display the prediction text
        label_text = tk.Label(result_window, text=f"The predicted species is: {prediction}", bg='#ffffff', font=('Helvetica', 14))
        label_text.pack(pady=20)
        
        # Display the image
        label_image = tk.Label(result_window, image=img, bg='#ffffff')
        label_image.image = img  # Keep a reference to avoid garbage collection
        label_image.pack(pady=20)
    
    # Center the result window
    result_window.update_idletasks()
    window_width = result_window.winfo_width()
    window_height = result_window.winfo_height()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    result_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


# Function to make predictions
def predict_species():
    try:
        # Get the values from the entry fields
        sepal_length = float(entry_sepal_length.get())
        sepal_width = float(entry_sepal_width.get())
        petal_length = float(entry_petal_length.get())
        petal_width = float(entry_petal_width.get())

        # Create a DataFrame for the input data
        input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                                  columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

        # Standardize the input data without column names
        input_data = scaler.transform(input_data.values)

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Show the result with an image
        show_result_with_image(prediction)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")

# Create the main window
window = tk.Tk()
window.title("Iris Flower Classification")
window.configure(bg='#ffffff')  # White background

# Define the window size
window_width = 650
window_height = 500

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate position to center the window
x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)

# Set the window size and position
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create and place the title label
title_label = tk.Label(window, text="Iris Flower Classification", bg='#ffffff', font=('Helvetica', 20, 'bold'), fg='#4a90e2')
title_label.pack(pady=20)

# Create a frame for form input
frame_form = tk.Frame(window, bg='#ffffff')
frame_form.pack(pady=20)

# Define font styles
label_font = ('Helvetica', 12)
entry_font = ('Helvetica', 12)

# Create and place labels and entry widgets
labels_texts = ["Sepal Length:", "Sepal Width:", "Petal Length:", "Petal Width:"]
entries = []

for i, text in enumerate(labels_texts):
    tk.Label(frame_form, text=text, bg='#ffffff', font=label_font).grid(row=i, column=0, padx=10, pady=10, sticky='e')
    entry = tk.Entry(frame_form, font=entry_font, width=20)
    entry.grid(row=i, column=1, padx=10, pady=10)
    entries.append(entry)

entry_sepal_length, entry_sepal_width, entry_petal_length, entry_petal_width = entries

# Create and place the classify button with styling
btn_classify = tk.Button(window, text="Classify", command=predict_species, font=('Helvetica', 14), bg='#4a90e2', fg='white', padx=20, pady=10, relief='raised', borderwidth=2)
btn_classify.pack(pady=20)

# Add a footer label for additional information or credits
footer_label = tk.Label(window, text="Iris Classification Model - © 2024", bg='#ffffff', font=('Helvetica', 10), fg='#888888')
footer_label.pack(side='bottom', pady=10)

# Add a brief instruction
instruction_label = tk.Label(window, text="Enter the measurements of the Iris flower and click 'Classify'.", bg='#ffffff', font=('Helvetica', 12, 'italic'), fg='#666666')
instruction_label.pack(pady=10)

# Run the application
window.mainloop()
