# 🧠 Mental Health Prediction using Decision Tree Classifier

## 📋 Overview

This project predicts a person’s **Work Interest** and **Social Weakness** based on their personal and behavioral traits such as gender, country, occupation, mood swings, and days spent indoors.

It uses a **Decision Tree Classifier** built with **Scikit-learn** and demonstrates a full machine learning pipeline — from data preprocessing to model saving, loading, and real-time prediction.

---

## 🚀 Features

* Loads and preprocesses dataset using **Pandas**
* Encodes categorical data using **LabelEncoder**
* Trains a **Decision Tree Classifier** model
* Exports and saves the trained model using **Joblib**
* Visualizes the trained model using **Graphviz**
* Loads the model for real-time predictions
* Displays predictions as **human-readable strings** (`Yes`, `No`, `Maybe`)

---

## 🧹 Dataset

**Dataset Used:** `Mental Health Dataset.csv`

Each record includes the following attributes:

| Feature         | Description                            |
| --------------- | -------------------------------------- |
| Gender          | Male / Female                          |
| Country         | Country of residence                   |
| Occupation      | Student / Employee / etc.              |
| Days_Indoors    | Number of days typically spent indoors |
| Work_Interest   | Target variable (Yes/No/Maybe)         |
| Social_Weakness | Target variable (Yes/No/Maybe)         |

---

## ⚙️ Project Structure

```
📂 Mental_Health_Predictor
 ├── Mental Health Dataset.csv
 ├── desc.ipynb      # Jupyter notebook for training the model
 ├── health_tester.joblib  # Saved trained model
 ├── test.py   # Loads model and predicts based on user input
 └── README.md
```

---

## 🧠 How It Works

1. **Data Preparation:**

   * Load dataset using `pandas.read_csv()`
   * Split into input features (`X`) and target labels (`Y`)
   * Convert categorical values into numeric codes using `LabelEncoder`

2. **Model Training:**

   * Create and train a `DecisionTreeClassifier` using Scikit-learn
   * Save the trained model using `joblib.dump()`

3. **Visualization:**

   * Visualize the decision tree with `graphviz` for better understanding

4. **Prediction Script:**

   * Load the saved model (`joblib.load()`)
   * Take user input (e.g., gender, country, etc.)
   * Predict `Work_Interest` and `Social_Weakness`
   * Print results as readable strings (`Yes`, `No`, `Maybe`)

---

## 💻 Example Usage

Run the prediction file:

```bash
python predict_user_input.py
```

Example interaction:

```
Enter Gender: Male
Enter Country: India
Enter Occupation: Student
Enter Days Indoors (0-5): 2
Enter Mood Swings (0-5): 3

Predicted Work Interest: Yes
Predicted Social Weakness: Maybe
```

---

## 🧮 Technologies Used

* Python 3
* Pandas
* Scikit-learn
* Graphviz
* Joblib
* Jupyter Notebook

---

## 📈 Future Improvements

* Add data validation for user input
* Improve accuracy with more training data
* Add a simple GUI using Tkinter or Streamlit
* Integrate more mental health indicators

---

## 🧑‍💻 Author

**Ravi Raahul**
aka ROWIN

---

## 🏁 License

This project is for educational purposes only.
Feel free to modify and experiment with the code for your own learning.
