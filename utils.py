def validate_input(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    if not (0 <= age <= 100):
        raise ValueError("Age must be between 0 and 100.")
    if sex not in [0, 1]:
        raise ValueError("Sex must be either 0 (female) or 1 (male).")
    if not (0 <= cp <= 3):
        raise ValueError("Chest pain type must be between 0 and 3.")
    if not (90 <= trestbps <= 200):
        raise ValueError("Resting blood pressure must be between 90 and 200.")
    if not (100 <= chol <= 600):
        raise ValueError("Cholesterol level must be between 100 and 600.")
    if fbs not in [0, 1]:
        raise ValueError("Fasting blood sugar must be either 0 or 1.")
    if not (0 <= restecg <= 2):
        raise ValueError("Resting ECG results must be between 0 and 2.")
    if not (60 <= thalach <= 220):
         raise ValueError("Maximum heart rate achieved must be between 60 and 220.")
    if exang not in [0, 1]:
        raise ValueError("Exercise-induced angina must be either 0 or 1.")
    if not (-6 <= oldpeak <= 6):
        raise ValueError("Oldpeak must be between -6 and 6.")
    if not (0 <= slope <= 2):
        raise ValueError("Slope must be between 0 and 2.")
    if not (0 <= ca <= 3):
        raise ValueError("Number of major vessels must be between 0 and 3.")
    if not (0 <= thal <= 3):
        raise ValueError("Thalassemia type must be between 0 and 3.")