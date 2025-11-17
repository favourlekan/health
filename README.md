# Health Risk Predictor Web Application

A comprehensive web application for predicting diabetes and heart disease risk using machine learning models trained on medical datasets.

## 🌟 Features

- **Heart Disease Risk Assessment**: Predict cardiovascular risk based on 13 clinical parameters
- **Diabetes Risk Assessment**: Evaluate diabetes risk using 8 health indicators
- **Interactive Web Interface**: User-friendly forms with real-time validation
- **Detailed Results**: Risk probability scores with personalized recommendations
- **Educational Content**: Information about risk factors and health parameters
- **Responsive Design**: Works on desktop and mobile devices

## 📊 Model Performance

- **Heart Disease Model**: 81.5% accuracy using Random Forest algorithm
- **Diabetes Model**: 97.0% accuracy with class balancing for improved predictions

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- Required packages (see requirements.txt)

### Installation

1. **Clone/Download the project files**
2. **Install dependencies:**
   ```bash
   pip install flask pandas numpy scikit-learn joblib
   ```

3. **Train the models (if not already done):**
   ```bash
   python models.py
   ```

4. **Start the web application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open your browser and go to `http://localhost:5000`

## 📁 Project Structure

```
health-risk-predictor/
├── app.py                 # Main Flask application
├── models.py              # Machine learning models and training
├── requirements.txt       # Python dependencies
├── test_predictions.py    # Testing script
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── heart_disease.html # Heart disease form
│   ├── diabetes.html     # Diabetes form
│   ├── heart_result.html # Heart disease results
│   ├── diabetes_result.html # Diabetes results
│   └── about.html        # About page
├── static/css/           # Stylesheets
│   └── style.css         # Main CSS file
├── models/               # Trained model files (auto-generated)
│   ├── heart_model.pkl
│   ├── diabetes_model.pkl
│   ├── heart_scaler.pkl
│   ├── diabetes_scaler.pkl
│   └── diabetes_encoders.pkl
└── user_input_files/     # Input datasets
    ├── heart.csv
    └── diabetes.csv
```

## 🩺 Usage Guide

### Heart Disease Assessment

Required parameters:
- **Demographics**: Age, Sex
- **Clinical Measurements**: Blood pressure, cholesterol, max heart rate
- **Symptoms**: Chest pain type, exercise-induced angina
- **Test Results**: ECG findings, ST depression, major vessels, thalassemia

### Diabetes Assessment

Required parameters:
- **Demographics**: Gender, age
- **Medical History**: Hypertension, heart disease, smoking history
- **Physical Measurements**: BMI, HbA1c level, blood glucose level

## 🔬 Technical Details

### Machine Learning Models

- **Algorithm**: Random Forest Classifier
- **Heart Disease Dataset**: 270 patient records with 13 features
- **Diabetes Dataset**: 100,000 patient records with 8 features
- **Preprocessing**: Feature scaling, categorical encoding, class balancing

### Model Training Features

**Heart Disease Model:**
- Age, sex, chest pain type
- Resting blood pressure, cholesterol
- Fasting blood sugar, resting ECG
- Maximum heart rate, exercise angina
- ST depression, ST segment slope
- Major vessels, thalassemia

**Diabetes Model:**
- Gender, age, hypertension
- Heart disease, smoking history
- BMI, HbA1c level, blood glucose

## ⚠️ Important Disclaimers

- **Educational Purpose Only**: This tool is for informational and educational purposes
- **Not Medical Advice**: Cannot replace professional medical consultation
- **Emergency Situations**: Seek immediate medical care for acute symptoms
- **Limitations**: AI predictions have inherent limitations and potential errors

## 🧪 Testing

Run the test script to verify model functionality:

```bash
python test_predictions.py
```

This will test both models with sample data and display prediction results.

## 📝 API Endpoints

- `/` - Home page
- `/heart_disease` - Heart disease assessment form
- `/diabetes` - Diabetes assessment form
- `/predict_heart` - Heart disease prediction (POST)
- `/predict_diabetes` - Diabetes prediction (POST)
- `/train_models` - Retrain models
- `/about` - About page with detailed information

## 🛡️ Privacy & Security

- No personal data is stored permanently
- All calculations performed locally
- Session data cleared on browser close
- No third-party data sharing

## 🔧 Customization

### Adding New Features

1. **Extend models.py** for new prediction algorithms
2. **Update templates** for additional forms or results
3. **Modify app.py** to add new routes
4. **Update CSS** for styling changes

### Model Retraining

Models can be retrained with new data by:
1. Replacing datasets in `user_input_files/`
2. Running `python models.py`
3. Restarting the web application

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed
2. **Model Not Found**: Run `python models.py` to train models
3. **Port Conflicts**: Change port in `app.py` if 5000 is occupied
4. **Performance Issues**: Consider reducing dataset size for faster training

### Debug Mode

The application runs in debug mode by default. To disable:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

## 🤝 Contributing

This application was developed as a demonstration of machine learning in healthcare. Feel free to:
- Improve model accuracy
- Add new prediction models
- Enhance user interface
- Optimize performance

## 📞 Support

For issues or questions about this educational tool, please refer to the about page within the application for additional information about the models and their limitations.

---

**Author**: MiniMax Agent  
**Purpose**: Educational demonstration of ML in healthcare  
**Version**: 1.0  
**Last Updated**: 2025-10-11
