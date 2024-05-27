import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Replace this with your manually calculated confusion matrix
# Example confusion matrix for illustration purposes
cm = np.array([[6, 6, 1], [0, 111, 1], [0, 18, 134]])

# Function to plot confusion matrix
def plot_confusion_matrix(cm, classes):
    plt.figure(figsize=(8, 8))
    sns.set(font_scale=1.2)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=classes, yticklabels=classes)
    plt.title("MI' Confusion Matrix", pad=20)
    plt.xlabel('Annotated by an Expert')
    plt.ylabel('Predicted by GPT-4')
    plt.show()

# Define class labels (replace with your actual class labels)
class_labels = ['Immidiate', 'Non-immidiate', 'Not TSD']

# Plot confusion matrix
plot_confusion_matrix(cm, class_labels)