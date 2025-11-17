#!/usr/bin/env python3
"""
Health Endpoint Test Script for Railway Deployment
Run this locally to verify all endpoints work before deploying to Railway
"""

import requests
import json
import time
from threading import Timer

def test_health_endpoints():
    """Test all health endpoints"""
    base_url = "http://localhost:5000"
    
    print("🏥 Testing Health Risk Predictor - Railway Health Endpoints")
    print("=" * 60)
    
    # Test endpoints
    endpoints = [
        {
            "path": "/healthz",
            "name": "Basic Health Check",
            "expected": "OK",
            "type": "text"
        },
        {
            "path": "/health", 
            "name": "Detailed Health Check",
            "expected": "status",
            "type": "json"
        },
        {
            "path": "/status",
            "name": "App Status", 
            "expected": "app",
            "type": "json"
        },
        {
            "path": "/",
            "name": "Home Page",
            "expected": "Health Risk Predictor",
            "type": "html"
        }
    ]
    
    results = []
    
    for endpoint in endpoints:
        try:
            print(f"\n🔍 Testing {endpoint['name']} ({endpoint['path']})")
            
            response = requests.get(f"{base_url}{endpoint['path']}", timeout=10)
            
            if response.status_code == 200:
                print(f"   ✅ Status Code: {response.status_code}")
                
                if endpoint['type'] == 'json':
                    data = response.json()
                    if endpoint['expected'] in data:
                        print(f"   ✅ JSON Response contains '{endpoint['expected']}': {json.dumps(data, indent=2)}")
                        results.append("✅ PASS")
                    else:
                        print(f"   ❌ JSON Response missing '{endpoint['expected']}': {json.dumps(data, indent=2)}")
                        results.append("❌ FAIL")
                        
                elif endpoint['type'] == 'text':
                    if endpoint['expected'] in response.text:
                        print(f"   ✅ Text Response: '{response.text}'")
                        results.append("✅ PASS")
                    else:
                        print(f"   ❌ Expected '{endpoint['expected']}', got: '{response.text}'")
                        results.append("❌ FAIL")
                        
                elif endpoint['type'] == 'html':
                    if endpoint['expected'] in response.text:
                        print(f"   ✅ HTML Response contains '{endpoint['expected']}'")
                        results.append("✅ PASS")
                    else:
                        print(f"   ❌ HTML Response missing '{endpoint['expected']}'")
                        results.append("❌ FAIL")
            else:
                print(f"   ❌ Status Code: {response.status_code} (Expected: 200)")
                results.append("❌ FAIL")
                
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Request Error: {e}")
            results.append("❌ FAIL")
        except Exception as e:
            print(f"   ❌ Unexpected Error: {e}")
            results.append("❌ FAIL")
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    passed = results.count("✅ PASS")
    total = len(results)
    
    for i, result in enumerate(results):
        print(f"{i+1}. {result}")
    
    print(f"\n🎯 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Your app is ready for Railway deployment.")
        print("\n✅ Railway Health Check Requirements Met:")
        print("   • /healthz endpoint returns 'OK'")
        print("   • /health endpoint provides detailed status")
        print("   • /status endpoint shows app information")
        print("   • Main application endpoints are accessible")
        
        print("\n🚀 Next Steps:")
        print("1. Commit and push your updated code to GitHub")
        print("2. Railway will automatically detect changes and redeploy")
        print("3. Check Railway dashboard - Network > Healthcheck should pass ✅")
        print("4. Test your live app at https://your-app.railway.app/healthz")
        
    else:
        print("⚠️  SOME TESTS FAILED!")
        print("Please fix the issues above before deploying to Railway.")
        print("\nCommon fixes:")
        print("• Make sure Flask app is running: python app.py")
        print("• Check that all dependencies are installed")
        print("• Verify port 5000 is available")

def start_server():
    """Start the Flask server in a separate thread"""
    import os
    import sys
    
    # Add current directory to Python path
    sys.path.insert(0, os.getcwd())
    
    # Import and run the app
    from app import app
    print("🚀 Starting Health Risk Predictor on http://localhost:5000")
    app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)

if __name__ == "__main__":
    print("Starting Health Risk Predictor test...")
    
    # Start server in background
    import threading
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Wait for server to start
    print("Waiting for server to start...")
    time.sleep(3)
    
    # Run tests
    test_health_endpoints()
    
    print("\n🏁 Test completed. Server is still running in background.")
    print("Press Ctrl+C to stop the server.")