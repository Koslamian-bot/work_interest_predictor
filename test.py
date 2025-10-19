import joblib
import pandas as pd

# ------------------------------
# Load the trained model
# ------------------------------
model = joblib.load("health_tester.joblib")   # make sure this file is in same folder

# ------------------------------
# Define input columns
# ------------------------------
columns = ['Gender', 'Country', 'Occupation', 'Days_Indoors']

# ------------------------------
# Take user input
# ------------------------------
user_data = {}
for col in columns:
    user_data[col] = input(f"Enter {col}: ")

# Convert inputs into a DataFrame
df = pd.DataFrame([user_data])

# ------------------------------
# Convert string inputs to numbers (same mapping used while training)
# You can customize these mappings based on your dataset’s original encoding
# ------------------------------
def str_to_num(value):
    # Try converting to int/float; if not, assign dummy numeric value
    try:
        return int(value)
    except:
        return hash(value) % 10  # rough fallback if string, just to avoid errors

for col in columns:
    df[col] = df[col].apply(str_to_num)

# ------------------------------
# Predict using the loaded model
# ------------------------------
pred = model.predict(df.values)

# ------------------------------
# Map numerical predictions to string labels
# ------------------------------
def decode_prediction(value):
    if value == 0:
        return "Maybe"
    elif value == 1:
        return "No"
    elif value == 2:
        return "Yes"
    else:
        return f"Unknown({value})"

# If you have two outputs (like Work_Interest, Social_Weakness)
# handle them as a tuple/list
if len(pred.shape) > 1 and pred.shape[1] > 1:
    decoded = [decode_prediction(p) for p in pred[0]]
    print("\n🎯 Predicted Work_Interest:", decoded[0])
    print("🎯 Predicted Social_Weakness:", decoded[1])
else:
    print("\n🎯 Predicted Output:", decode_prediction(pred[0]))
