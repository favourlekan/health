import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

class HealthRiskPredictor:
    def __init__(self):
        self.heart_model = None
        self.diabetes_model = None
        self.heart_scaler = StandardScaler()
        self.diabetes_scaler = StandardScaler()
        self.diabetes_encoders = {}
        self.is_trained = False
    
    def prepare_heart_data(self, df):
        """Prepare heart disease data for training"""
        # Clean column names
        df.columns = df.columns.str.strip()
        
        # Features and target
        feature_cols = ['age', 'sex', 'chest pain type', 'resting blood pressure', 
                       'serum cholestoral', 'fasting blood sugar', 
                       'resting electrocardiographic results', 'max heart rate',
                       'exercise induced angina', 'oldpeak', 'ST segment', 
                       'major vessels', 'thal']
        
        X = df[feature_cols].copy()
        y = df['heart disease'].copy()
        
        # Convert target to binary (1=no disease->0, 2=disease->1)
        y = (y == 2).astype(int)
        
        return X, y, feature_cols
    
    def prepare_diabetes_data(self, df):
        """Prepare diabetes data for training"""
        # Features and target
        feature_cols = ['gender', 'age', 'hypertension', 'heart_disease', 
                       'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level']
        
        X = df[feature_cols].copy()
        y = df['diabetes'].copy()
        
        # Encode categorical variables
        categorical_cols = ['gender', 'smoking_history']
        
        for col in categorical_cols:
            if col not in self.diabetes_encoders:
                self.diabetes_encoders[col] = LabelEncoder()
            X[col] = self.diabetes_encoders[col].fit_transform(X[col])
        
        return X, y, feature_cols
    
    def train_models(self):
        """Train both heart disease and diabetes prediction models"""
        print("Loading datasets...")
        
        # Load datasets
        heart_df = pd.read_csv('user_input_files/heart.csv')
        diabetes_df = pd.read_csv('user_input_files/diabetes.csv')
        
        print("Preparing heart disease data...")
        X_heart, y_heart, heart_features = self.prepare_heart_data(heart_df)
        
        print("Preparing diabetes data...")
        X_diabetes, y_diabetes, diabetes_features = self.prepare_diabetes_data(diabetes_df)
        
        # Scale features
        X_heart_scaled = self.heart_scaler.fit_transform(X_heart)
        X_diabetes_scaled = self.diabetes_scaler.fit_transform(X_diabetes)
        
        # Train heart disease model
        print("Training heart disease model...")
        X_train_heart, X_test_heart, y_train_heart, y_test_heart = train_test_split(
            X_heart_scaled, y_heart, test_size=0.2, random_state=42, stratify=y_heart
        )
        
        self.heart_model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.heart_model.fit(X_train_heart, y_train_heart)
        
        # Evaluate heart disease model
        heart_pred = self.heart_model.predict(X_test_heart)
        heart_accuracy = accuracy_score(y_test_heart, heart_pred)
        print(f"Heart disease model accuracy: {heart_accuracy:.3f}")
        
        # Train diabetes model
        print("Training diabetes model...")
        X_train_diabetes, X_test_diabetes, y_train_diabetes, y_test_diabetes = train_test_split(
            X_diabetes_scaled, y_diabetes, test_size=0.2, random_state=42, stratify=y_diabetes
        )
        
        self.diabetes_model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
        self.diabetes_model.fit(X_train_diabetes, y_train_diabetes)
        
        # Evaluate diabetes model
        diabetes_pred = self.diabetes_model.predict(X_test_diabetes)
        diabetes_accuracy = accuracy_score(y_test_diabetes, diabetes_pred)
        print(f"Diabetes model accuracy: {diabetes_accuracy:.3f}")
        
        # Save models
        self.save_models()
        self.is_trained = True
        
        return {
            'heart_accuracy': heart_accuracy,
            'diabetes_accuracy': diabetes_accuracy,
            'heart_features': heart_features,
            'diabetes_features': diabetes_features
        }
    
    def predict_heart_disease(self, features):
        """Predict heart disease risk"""
        if not self.is_trained:
            self.load_models()
        
        # Expected feature order for heart disease
        feature_names = ['age', 'sex', 'chest_pain_type', 'resting_bp', 
                        'cholesterol', 'fasting_bs', 'resting_ecg', 'max_hr',
                        'exercise_angina', 'oldpeak', 'st_segment', 'major_vessels', 'thal']
        
        # Convert features to numpy array in correct order
        feature_array = np.array([features[name] for name in feature_names]).reshape(1, -1)
        
        # Scale features
        feature_scaled = self.heart_scaler.transform(feature_array)
        
        # Predict
        risk_probability = self.heart_model.predict_proba(feature_scaled)[0][1]
        risk_class = self.heart_model.predict(feature_scaled)[0]
        
        # Enhanced risk level categorization
        if risk_probability > 0.7:
            risk_level = 'High'
        elif risk_probability > 0.3:
            risk_level = 'Medium'
        else:
            risk_level = 'Low'
        
        return {
            'risk_probability': float(risk_probability),
            'risk_class': int(risk_class),
            'risk_level': risk_level
        }
    
    def predict_diabetes(self, features):
        """Predict diabetes risk"""
        if not self.is_trained:
            self.load_models()
        
        # Prepare features
        feature_dict = features.copy()
        
        # Encode categorical variables
        if 'gender' in feature_dict:
            try:
                feature_dict['gender'] = self.diabetes_encoders['gender'].transform([feature_dict['gender']])[0]
            except ValueError:
                # Handle unseen categories
                feature_dict['gender'] = 0
        
        if 'smoking_history' in feature_dict:
            try:
                feature_dict['smoking_history'] = self.diabetes_encoders['smoking_history'].transform([feature_dict['smoking_history']])[0]
            except ValueError:
                # Handle unseen categories
                feature_dict['smoking_history'] = 0
        
        # Expected feature order for diabetes
        feature_names = ['gender', 'age', 'hypertension', 'heart_disease', 
                        'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level']
        
        # Convert features to numpy array in correct order
        feature_array = np.array([feature_dict[name] for name in feature_names]).reshape(1, -1)
        
        # Scale features
        feature_scaled = self.diabetes_scaler.transform(feature_array)
        
        # Predict
        risk_probability = self.diabetes_model.predict_proba(feature_scaled)[0][1]
        risk_class = self.diabetes_model.predict(feature_scaled)[0]
        
        # Enhanced risk level categorization
        if risk_probability > 0.7:
            risk_level = 'High'
        elif risk_probability > 0.3:
            risk_level = 'Medium'
        else:
            risk_level = 'Low'
        
        return {
            'risk_probability': float(risk_probability),
            'risk_class': int(risk_class),
            'risk_level': risk_level
        }
    
    def save_models(self):
        """Save trained models and preprocessors"""
        os.makedirs('models', exist_ok=True)
        
        joblib.dump(self.heart_model, 'models/heart_model.pkl')
        joblib.dump(self.diabetes_model, 'models/diabetes_model.pkl')
        joblib.dump(self.heart_scaler, 'models/heart_scaler.pkl')
        joblib.dump(self.diabetes_scaler, 'models/diabetes_scaler.pkl')
        joblib.dump(self.diabetes_encoders, 'models/diabetes_encoders.pkl')
        
        print("Models saved successfully!")
    
    def load_models(self):
        """Load trained models and preprocessors"""
        try:
            self.heart_model = joblib.load('models/heart_model.pkl')
            self.diabetes_model = joblib.load('models/diabetes_model.pkl')
            self.heart_scaler = joblib.load('models/heart_scaler.pkl')
            self.diabetes_scaler = joblib.load('models/diabetes_scaler.pkl')
            self.diabetes_encoders = joblib.load('models/diabetes_encoders.pkl')
            self.is_trained = True
            print("Models loaded successfully!")
        except FileNotFoundError:
            print("Models not found. Please train the models first.")
            return False
        return True

if __name__ == "__main__":
    # Train models if running this file directly
    predictor = HealthRiskPredictor()
    results = predictor.train_models()
    print("\nTraining completed!")
    print(f"Heart Disease Model Accuracy: {results['heart_accuracy']:.3f}")
    print(f"Diabetes Model Accuracy: {results['diabetes_accuracy']:.3f}")
