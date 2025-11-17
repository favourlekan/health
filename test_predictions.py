#!/usr/bin/env python3
"""
Test script to demonstrate the prediction functionality
"""
from models import HealthRiskPredictor

def test_heart_disease_prediction():
    """Test heart disease prediction with sample data"""
    print("=== Testing Heart Disease Prediction ===")
    
    predictor = HealthRiskPredictor()
    predictor.load_models()
    
    # Sample test case - moderate risk profile
    heart_features = {
        'age': 55,
        'sex': 1,  # Male
        'chest_pain_type': 2,  # Atypical angina
        'resting_bp': 140,
        'cholesterol': 200,
        'fasting_bs': 0,
        'resting_ecg': 0,
        'max_hr': 150,
        'exercise_angina': 0,
        'oldpeak': 1.0,
        'st_segment': 2,
        'major_vessels': 1,
        'thal': 7
    }
    
    result = predictor.predict_heart_disease(heart_features)
    
    print(f"Risk Probability: {result['risk_probability']:.3f}")
    print(f"Risk Level: {result['risk_level']}")
    print(f"Risk Class: {result['risk_class']}")
    
    # High risk test case
    print("\n--- High Risk Test Case ---")
    high_risk_features = heart_features.copy()
    high_risk_features.update({
        'age': 70,
        'chest_pain_type': 4,  # Asymptomatic
        'resting_bp': 180,
        'cholesterol': 300,
        'exercise_angina': 1,
        'oldpeak': 3.0,
        'major_vessels': 3
    })
    
    result_high = predictor.predict_heart_disease(high_risk_features)
    print(f"Risk Probability: {result_high['risk_probability']:.3f}")
    print(f"Risk Level: {result_high['risk_level']}")

def test_diabetes_prediction():
    """Test diabetes prediction with sample data"""
    print("\n=== Testing Diabetes Prediction ===")
    
    predictor = HealthRiskPredictor()
    predictor.load_models()
    
    # Sample test case - moderate risk profile
    diabetes_features = {
        'gender': 'Male',
        'age': 45.0,
        'hypertension': 0,
        'heart_disease': 0,
        'smoking_history': 'never',
        'bmi': 28.5,
        'HbA1c_level': 5.9,
        'blood_glucose_level': 110
    }
    
    result = predictor.predict_diabetes(diabetes_features)
    
    print(f"Risk Probability: {result['risk_probability']:.3f}")
    print(f"Risk Level: {result['risk_level']}")
    print(f"Risk Class: {result['risk_class']}")
    
    # High risk test case
    print("\n--- High Risk Test Case ---")
    high_risk_features = diabetes_features.copy()
    high_risk_features.update({
        'age': 65.0,
        'hypertension': 1,
        'smoking_history': 'current',
        'bmi': 35.0,
        'HbA1c_level': 6.8,
        'blood_glucose_level': 180
    })
    
    result_high = predictor.predict_diabetes(high_risk_features)
    print(f"Risk Probability: {result_high['risk_probability']:.3f}")
    print(f"Risk Level: {result_high['risk_level']}")

if __name__ == "__main__":
    test_heart_disease_prediction()
    test_diabetes_prediction()
    print("\n=== Testing Complete ===")
    print("Web application is running at http://127.0.0.1:5000")
    print("You can now access the interactive interface!")
