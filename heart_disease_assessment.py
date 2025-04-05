from fuzzy_logic import compute_risk
from utils import validate_input

def get_input(prompt, valid_type, valid_range=None):
    """
    A helper function to validate and get correct input from the user.
    """
    while True:
        user_input = input(prompt)
        try:
            # Try to cast input to the valid type
            user_input = valid_type(user_input)

            # If there is a valid range, check if the input is within that range
            if valid_range and user_input not in valid_range:
                print(f"Invalid input! Please enter a value between {valid_range[0]} and {valid_range[-1]}")
                continue
            return user_input
        except ValueError:
            print(f"Invalid input! Please enter a valid {valid_type._name_}.")
            continue

def main():
    print("Welcome to the Heart Disease Risk Assessment System")
    
    # Collecting input from the user
    age = get_input("Enter age: ", float, valid_range=[0, 120])
    sex = get_input("Enter sex (0 = female, 1 = male): ", int, valid_range=[0, 1])
    cp = get_input("Enter chest pain type (0-3): ", int, valid_range=[0, 3])
    trestbps = get_input("Enter resting blood pressure: ", float)
    chol = get_input("Enter cholesterol level: ", float)
    fbs = get_input("Enter fasting blood sugar (0 = False, 1 = True): ", int, valid_range=[0, 1])
    restecg = get_input("Enter resting ECG results (0-2): ", int, valid_range=[0, 2])
    thalach = get_input("Enter  maximum heart rate achieved: ", float)
    exang = get_input("Enter exercise-induced angina (0 = No, 1 = Yes): ", int, valid_range=[0, 1])
    oldpeak = get_input("Enter oldpeak: ", float)
    slope = get_input("Enter slope (0-2): ", int, valid_range=[0, 2])
    ca = get_input("Enter number of major vessels (0-3): ", int, valid_range=[0, 3])
    thal = get_input("Enter thalassemia type (0-3): ", int, valid_range=[0, 3])
    
    # Validate input ranges (using helper function)
    validate_input(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
 # Compute the risk using fuzzy logic
    risk_level = compute_risk(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

    # Display the result
    print(f"Heart Disease Risk Level: {risk_level}")


