#!/usr/bin/env python3
"""
Railway Network Error Diagnostic Tool
Run this to identify the exact cause of your Railway deployment issues
"""

import os
import time
import subprocess
import sys
from pathlib import Path

def check_file_sizes():
    """Check if any files are too large for Railway"""
    print("🔍 CHECKING FILE SIZES")
    print("-" * 40)
    
    large_files = []
    models_dir = Path("models")
    
    if models_dir.exists():
        for file in models_dir.glob("*.pkl"):
            size_mb = file.stat().st_size / (1024 * 1024)
            print(f"📄 {file.name}: {size_mb:.1f} MB")
            if size_mb > 50:  # Railway often has issues with files > 50MB
                large_files.append(file.name)
    
    if large_files:
        print(f"\n❌ PROBLEM FOUND: Large files detected:")
        for file in large_files:
            print(f"   • {file} (may cause Railway timeouts)")
        return False
    else:
        print(f"\n✅ File sizes look good")
        return True

def check_startup_time():
    """Test app startup time"""
    print("\n⏱️  TESTING STARTUP TIME")
    print("-" * 40)
    
    try:
        start_time = time.time()
        
        # Test basic import
        from models import HealthRiskPredictor
        predictor = HealthRiskPredictor()
        
        # Test model loading
        if os.path.exists('models/heart_model.pkl'):
            predictor.load_models()
            print("✅ Models loaded successfully")
        else:
            print("⚠️  Models not found - would need training on startup")
        
        startup_time = time.time() - start_time
        print(f"⏰ Startup time: {startup_time:.2f} seconds")
        
        if startup_time > 10:
            print(f"❌ PROBLEM: Startup time {startup_time:.1f}s may cause Railway health check timeouts")
            return False
        else:
            print(f"✅ Startup time {startup_time:.1f}s should work on Railway")
            return True
            
    except Exception as e:
        print(f"❌ Startup test failed: {e}")
        return False

def test_health_endpoints():
    """Test if health endpoints work"""
    print("\n🏥 TESTING HEALTH ENDPOINTS")
    print("-" * 40)
    
    try:
        from app import app
        
        # Test with Flask test client
        with app.test_client() as client:
            response = client.get('/healthz')
            if response.status_code == 200 and response.data == b'OK':
                print("✅ /healthz endpoint working")
            else:
                print(f"❌ /healthz endpoint failed: {response.status_code}")
                return False
                
            response = client.get('/health')
            if response.status_code == 200:
                print("✅ /health endpoint working")
            else:
                print(f"❌ /health endpoint failed: {response.status_code}")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Health endpoint test failed: {e}")
        return False

def generate_recommendations():
    """Generate deployment recommendations based on test results"""
    print("\n" + "=" * 50)
    print("🎯 DEPLOYMENT RECOMMENDATIONS")
    print("=" * 50)
    
    print("\n📋 DIAGNOSTIC SUMMARY:")
    
    file_ok = check_file_sizes()
    startup_ok = check_startup_time() 
    health_ok = test_health_endpoints()
    
    print(f"\n📊 Results:")
    print(f"   File sizes: {'✅ OK' if file_ok else '❌ ISSUES'}")
    print(f"   Startup time: {'✅ OK' if startup_ok else '❌ SLOW'}")
    print(f"   Health endpoints: {'✅ OK' if health_ok else '❌ BROKEN'}")
    
    if file_ok and startup_ok and health_ok:
        print(f"\n🎉 ALL TESTS PASSED!")
        print(f"Your app should work on both Railway and PythonAnywhere.")
        print(f"\nRecommendation: Try Railway again with the optimized files I created.")
        
    elif not file_ok:
        print(f"\n🚨 LARGE FILE DETECTED")
        print(f"Your diabetes_model.pkl is too large for Railway.")
        print(f"\nRecommendation: Switch to PythonAnywhere immediately.")
        print(f"PythonAnywhere handles large files much better than Railway.")
        
    elif not startup_ok:
        print(f"\n🐌 SLOW STARTUP DETECTED")
        print(f"Your app takes too long to start up.")
        print(f"\nRecommendation: Use the railway-optimized app I created.")
        print(f"Or switch to PythonAnywhere for better performance.")
        
    elif not health_ok:
        print(f"\n❌ HEALTH ENDPOINT ISSUES")
        print(f"Your health endpoints aren't working properly.")
        print(f"\nRecommendation: Use the app_railway.py file I created.")
        print(f"It has optimized health endpoints for Railway.")
    
    print(f"\n🚀 NEXT STEPS:")
    
    if not file_ok:
        print(f"1. 🏃‍♂️ URGENT: Switch to PythonAnywhere (handles large files)")
        print(f"   → Go to https://www.pythonanywhere.com and upload your files")
        
    elif not startup_ok:
        print(f"1. 🔧 Use Railway-optimized files:")
        print(f"   → Replace app.py with app_railway.py")
        print(f"   → Replace requirements.txt with requirements_railway.txt")
        print(f"   → Replace Procfile with Procfile_railway")
        
    elif not health_ok:
        print(f"1. 🔧 Use Railway-optimized files:")
        print(f"   → The health endpoints in app_railway.py are optimized")
        
    else:
        print(f"1. 🔧 Try Railway with optimized files:")
        print(f"   → Use app_railway.py, requirements_railway.txt, Procfile_railway")
        print(f"2. 🏃‍♂️ OR: Switch to PythonAnywhere (recommended for reliability)")
        
    print(f"\n📞 Need help? Let me know what the tests show!")

if __name__ == "__main__":
    print("🔍 Railway Network Error Diagnostic Tool")
    print("This will help identify why Railway deployment keeps failing\n")
    
    generate_recommendations()