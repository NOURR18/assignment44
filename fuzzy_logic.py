import skfuzzy as fuzz
import numpy as np

# Define fuzzy sets for each input variable and output risk level
def define_membership_functions():
    # Membership functions for age (low, medium, high)
    age = np.arange(0, 101, 1)
    age_low = fuzz.trimf(age, [0, 20, 40])
    age_medium = fuzz.trimf(age, [30, 50, 70])
    age_high = fuzz.trimf(age, [60, 80, 100])

    # Membership functions for cholesterol (low, medium, high)
    chol = np.arange(0, 401, 1)
    chol_low = fuzz.trimf(chol, [0, 100, 200])
    chol_medium = fuzz.trimf(chol, [150, 200, 250])
    chol_high = fuzz.trimf(chol, [200, 300, 400])
 # Membership functions for blood pressure (low, medium, high)
    trestbps = np.arange(0, 201, 1)
    bp_low = fuzz.trimf(trestbps, [0, 80, 120])
    bp_medium = fuzz.trimf(trestbps, [110, 130, 150])
    bp_high = fuzz.trimf(trestbps, [140, 160, 200])

    # Membership functions for risk level (Low, Medium, High)
    risk = np.arange(0, 11, 1)
    risk_low = fuzz.trimf(risk, [0, 0, 5])
    risk_medium = fuzz.trimf(risk, [3, 5, 7])
    risk_high = fuzz.trimf(risk, [5, 8, 10])

    return age, age_low, age_medium, age_high, chol, chol_low, chol_medium, chol_high, trestbps, bp_low, bp_medium, bp_high, risk, risk_low, risk_medium, risk_high
# Define fuzzy rules
def define_fuzzy_rules(age, chol, trestbps):
    # Example rules for risk classification
    rule1 = fuzz.relation_product(age[2], chol[2]) # Risk increases with high age and high cholesterol
    rule2 = fuzz.relation_product(trestbps[2], chol[2]) # Risk increases with high blood pressure and high cholesterol
    
    return rule1, rule2

# Compute risk using fuzzy inference system
def compute_risk(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    # Define fuzzy sets
    age, age_low, age_medium, age_high, chol, chol_low, chol_medium, chol_high, trestbps, bp_low, bp_medium, bp_high, risk, risk_low, risk_medium, risk_high = define_membership_functions()
# Fuzzy inference system for risk level
    if age >= 60 and chol > 240 and trestbps > 140:
        risk_level = "High"
    elif age >= 40 and chol > 200 and trestbps > 130:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return risk_level