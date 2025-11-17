from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import os
import sys
from models import HealthRiskPredictor

app = Flask(__name__)
app.secret_key = 'health_risk_predictor_secret_key'

# Initialize the predictor
predictor = HealthRiskPredictor()

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/healthz')
def healthz():
    """Simple health check endpoint for Railway - returns 200 OK"""
    return "OK", 200

@app.route('/status')
def status():
    """Status endpoint with app information"""
    return jsonify({
        'app': 'Health Risk Predictor',
        'version': '1.0',
        'status': 'running',
        'endpoints': {
            'home': '/',
            'heart_disease': '/heart_disease',
            'diabetes': '/diabetes',
            'health': '/health',
            'about': '/about'
        }
    })

@app.route('/heart_disease')
def heart_disease_form():
    """Heart disease prediction form"""
    return render_template('heart_disease.html')

@app.route('/diabetes')
def diabetes_form():
    """Diabetes prediction form"""
    return render_template('diabetes.html')

@app.route('/predict_heart', methods=['POST'])
def predict_heart():
    """Handle heart disease prediction"""
    try:
        # Get form data
        features = {
            'age': int(request.form['age']),
            'sex': int(request.form['sex']),
            'chest_pain_type': int(request.form['chest_pain_type']),
            'resting_bp': int(request.form['resting_bp']),
            'cholesterol': int(request.form['cholesterol']),
            'fasting_bs': int(request.form['fasting_bs']),
            'resting_ecg': int(request.form['resting_ecg']),
            'max_hr': int(request.form['max_hr']),
            'exercise_angina': int(request.form['exercise_angina']),
            'oldpeak': float(request.form['oldpeak']),
            'st_segment': int(request.form['st_segment']),
            'major_vessels': int(request.form['major_vessels']),
            'thal': int(request.form['thal'])
        }
        
        # Make prediction
        result = predictor.predict_heart_disease(features)
        
        return render_template('heart_result.html', 
                             result=result, 
                             features=features)
    
    except Exception as e:
        flash(f'Error making prediction: {str(e)}', 'error')
        return redirect(url_for('heart_disease_form'))

@app.route('/predict_diabetes', methods=['POST'])
def predict_diabetes():
    """Handle diabetes prediction"""
    try:
        # Get form data
        features = {
            'gender': request.form['gender'],
            'age': float(request.form['age']),
            'hypertension': int(request.form['hypertension']),
            'heart_disease': int(request.form['heart_disease']),
            'smoking_history': request.form['smoking_history'],
            'bmi': float(request.form['bmi']),
            'HbA1c_level': float(request.form['HbA1c_level']),
            'blood_glucose_level': int(request.form['blood_glucose_level'])
        }
        
        # Make prediction
        result = predictor.predict_diabetes(features)
        
        return render_template('diabetes_result.html', 
                             result=result, 
                             features=features)
    
    except Exception as e:
        flash(f'Error making prediction: {str(e)}', 'error')
        return redirect(url_for('diabetes_form'))

@app.route('/train_models')
def train_models():
    """Train the machine learning models"""
    try:
        flash('Training models... This may take a few minutes.', 'info')
        results = predictor.train_models()
        
        flash(f'Models trained successfully! Heart Disease Accuracy: {results["heart_accuracy"]:.3f}, Diabetes Accuracy: {results["diabetes_accuracy"]:.3f}', 'success')
        
        return redirect(url_for('index'))
    
    except Exception as e:
        flash(f'Error training models: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/health')
def health_check():
    """Health check endpoint for Railway deployment"""
    try:
        # Check if models are loaded
        if predictor.heart_model is not None and predictor.diabetes_model is not None:
            return jsonify({
                'status': 'healthy',
                'message': 'Health Risk Predictor app is running',
                'models_loaded': True,
                'timestamp': '2025-11-17T11:32:34Z'
            }), 200
        else:
            return jsonify({
                'status': 'partial',
                'message': 'App is running but models not fully loaded',
                'models_loaded': False,
                'timestamp': '2025-11-17T11:32:34Z'
            }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Health check failed: {str(e)}',
            'timestamp': '2025-11-17T11:32:34Z'
        }), 500

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

if __name__ == '__main__':
    # Check if models exist, if not, train them
    if not os.path.exists('models/heart_model.pkl'):
        print("Models not found. Training models...")
        try:
            predictor.train_models()
            print("Models trained successfully!")
        except Exception as e:
            print(f"Error training models: {e}")
    else:
        # Load existing models
        predictor.load_models()
        print("Models loaded successfully!")
    
    # Get port from environment (Railway sets this automatically)
    port = int(os.environ.get('PORT', 5000))
    
    app.run(debug=False, host='0.0.0.0', port=port)
