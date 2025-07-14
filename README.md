# Cancer Diagnosis and Image Classification Project

This project implements a pipeline for cancer diagnosis prediction using tabular data and image classification of lung cancer types using convolutional neural networks (CNNs) with TensorFlow/Keras. It combines classical machine learning models with deep learning and transfer learning techniques.

---

## Project Structure

- **Data Loading and Exploration**  
  Loading clinical tabular data for cancer diagnosis, checking missing values, exploring feature correlations, and visualizing diagnosis distributions.

- **Data Preprocessing and Feature Scaling**  
  Scaling numerical attributes and preparing labels for classical ML models.

- **Classical Machine Learning Models**  
  Training and evaluating Logistic Regression, Decision Tree, Random Forest, Support Vector Machine, and Gradient Boosting classifiers on tabular data.

- **Ensemble Modeling**  
  Combining Random Forest and Gradient Boosting with a soft voting ensemble.

- **Model Evaluation**  
  Performance metrics including accuracy, precision, recall, F1-score, ROC AUC, confusion matrices, and ROC curves.

- **Image Data Preparation**  
  Organizing lung cancer scan images, mapping classes to labels, resizing images, and normalization.

- **Image Data Augmentation and Generators**  
  Using `ImageDataGenerator` for augmentation and normalization, creating train/validation/test generators.

- **CNN Model Definition and Training**  
  Building CNN models from scratch and using transfer learning with MobileNetV2.

- **Hyperparameter Tuning**  
  Using Keras Tuner to optimize model architecture and training parameters.

---

## Setup and Requirements

### Libraries

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- tensorflow (including keras)
- keras-tuner
- pillow
- google.colab (if using Colab)
- IPython widgets (optional)

Install via pip if needed:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow keras-tuner pillow ipywidgets
