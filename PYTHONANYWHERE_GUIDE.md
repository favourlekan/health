# 🐍 PythonAnywhere Deployment Guide (Easiest Alternative)

## ✅ **Why PythonAnywhere?**
- **Designed specifically for Python apps**
- **Handles large files (your 61MB model) easily**
- **Web-based file manager** (no GitHub required initially)
- **Very reliable hosting**
- **Good free tier**
- **Perfect for Flask apps**

## 🚀 **STEP-BY-STEP: Deploy in 15 Minutes**

### **Step 1: Create PythonAnywhere Account**
1. **Go to [PythonAnywhere.com](https://pythonanywhere.com)**
2. **Click "Start running Python in the cloud"**
3. **Choose "Start running Python online"**
4. **Sign up with email** (or GitHub/Google)
5. **Verify your email**

### **Step 2: Choose Plan**
**For testing (free tier):**
- **"Free Plan"** → **"Start running Python online"**
- **For production:** "Starter Plan" ($5/month) - recommended

### **Step 3: Upload Your Files**
1. **Go to "Files" tab** (left sidebar)
2. **Navigate to `/home/YOUR_USERNAME/`**
3. **Click "Upload a file"**
4. **Upload ALL your files:**
   ```
   ✅ app.py
   ✅ models.py
   ✅ requirements.txt
   ✅ Procfile (optional for PA)
   ✅ static/ folder (with CSS)
   ✅ templates/ folder (all HTML files)
   ✅ models/ folder (all .pkl files)
   ✅ user_input_files/ folder
   ```

**Upload tips:**
- **Create ZIP file first** and upload ZIP
- **Or upload files one by one**
- **Create folders first** (static/, templates/, models/, user_input_files/)

### **Step 4: Create Flask Web App**
1. **Go to "Web" tab** (left sidebar)
2. **Click "Add a new web app"**
3. **Choose "Manual configuration"**
4. **Select Python version:** Python 3.10
5. **Click "Next"**

### **Step 5: Configure Virtual Environment**
1. **In Web tab, scroll to "Virtualenv" section**
2. **Click "Enter the path to a virtualenv"**
3. **Enter:** `/home/YOUR_USERNAME/mysite/venv`
4. **Click "Enter"**
5. **Open bash console** (top right → "Open console")
6. **Create virtual environment:**
   ```bash
   cd ~/mysite
   python3.10 -m venv venv
   source venv/bin/activate
   pip install flask pandas numpy scikit-learn joblib
   ```

### **Step 6: Configure WSGI File**
1. **In Web tab, click the WSGI configuration file link**
2. **Replace contents with:**
   ```python
   import sys
   import os
   import sys
   
   # Add your project directory to sys.path
   project_home = '/home/YOUR_USERNAME/mysite'
   if project_home not in sys.path:
       sys.path.insert(0, project_home)
   
   # Set Flask app
   from app import app as application
   
   if __name__ == "__main__":
       application.run()
   ```
3. **Save file**

### **Step 7: Configure Static Files**
1. **In Web tab, scroll to "Static files"**
2. **Add these entries:**
   ```
   URL: /static/
   Directory: /home/YOUR_USERNAME/mysite/static
   
   URL: /static/css/
   Directory: /home/YOUR_USERNAME/mysite/static/css
   ```
3. **Save**

### **Step 8: Enable Your Web App**
1. **In Web tab, click the green "Reload" button**
2. **Wait 30 seconds**
3. **Visit your app URL** (shown in Web tab)

## ✅ **Your Live App URL:**
```
https://YOUR_USERNAME.pythonanywhere.com
```

## 🧪 **Test Your App:**
1. **Open the URL in browser**
2. **Test home page loads**
3. **Test heart disease prediction**
4. **Test diabetes prediction**
5. **Check probability scores display correctly**

## 🔧 **Troubleshooting PythonAnywhere**

### **If app doesn't load:**
1. **Check Web tab logs** for errors
2. **Verify WSGI file** is correct
3. **Ensure virtualenv** is activated
4. **Check file paths** match exactly

### **If import errors:**
```bash
# In bash console, activate virtualenv
source ~/mysite/venv/bin/activate
pip install -r requirements.txt
```

### **If static files don't load:**
- **Check static file mappings** in Web tab
- **Verify file paths** are correct
- **Ensure files uploaded** to right directories

## 💰 **Pricing Options:**

### **Free Plan Limitations:**
- **Only available when you log in**
- **Good for testing and demos**
- **Limited CPU time**

### **Starter Plan ($5/month):**
- **Always available**
- **Good performance**
- **Professional hosting**

## 🎯 **Alternative: Quick Upload via Git**

### **If you prefer Git:**
1. **In Files tab, click "Open Bash console here"**
2. **Run:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/health-risk-predictor.git
   cd health-risk-predictor
   ```
3. **Continue from Step 5** above

## 🚀 **Benefits of PythonAnywhere:**
- ✅ **No GitHub required** initially
- ✅ **Handles large files** perfectly
- ✅ **Web-based management**
- ✅ **Built-in Python expertise**
- ✅ **Very reliable**
- ✅ **Good documentation**

## 🎯 **Next Steps:**
1. **Sign up for PythonAnywhere**
2. **Upload your files**
3. **Create Flask web app**
4. **Your app will be live in 15 minutes!**

**Ready to try PythonAnywhere? It should handle your large model files without any issues!**