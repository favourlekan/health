#!/usr/bin/env python3
"""
Simple launcher script for the Health Risk Predictor Web Application
"""
import os
import sys
import subprocess

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['flask', 'pandas', 'numpy', 'sklearn', 'joblib']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("Install them with: pip install flask pandas numpy scikit-learn joblib")
        return False
    return True

def check_models():
    """Check if models are trained"""
    model_files = [
        'models/heart_model.pkl',
        'models/diabetes_model.pkl',
        'models/heart_scaler.pkl',
        'models/diabetes_scaler.pkl',
        'models/diabetes_encoders.pkl'
    ]
    
    missing_models = [f for f in model_files if not os.path.exists(f)]
    
    if missing_models:
        print("🤖 Models not found. Training models...")
        try:
            subprocess.run([sys.executable, 'models.py'], check=True)
            print("✅ Models trained successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to train models")
            return False
    else:
        print("✅ Models found and ready")
    
    return True

def main():
    """Main launcher function"""
    print("🏥 Health Risk Predictor - Starting Application")
    print("=" * 50)
    
    # Check dependencies
    print("🔍 Checking dependencies...")
    if not check_dependencies():
        sys.exit(1)
    print("✅ All dependencies available")
    
    # Check datasets
    print("\n📊 Checking datasets...")
    if not os.path.exists('user_input_files/heart.csv'):
        print("❌ Heart disease dataset not found: user_input_files/heart.csv")
        sys.exit(1)
    
    if not os.path.exists('user_input_files/diabetes.csv'):
        print("❌ Diabetes dataset not found: user_input_files/diabetes.csv")
        sys.exit(1)
    print("✅ Datasets available")
    
    # Check models
    print("\n🤖 Checking models...")
    if not check_models():
        sys.exit(1)
    
    # Start the application
    print("\n🚀 Starting Flask application...")
    print("📍 Application will be available at: http://localhost:5000")
    print("📍 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
