# 🔵 Heroku Deployment Guide (Most Reliable)

## ✅ **Why Heroku?**
- **Most stable platform** for Flask apps
- **Excellent reliability and uptime**
- **Professional hosting with good support**
- **Handles large files well**
- **Generous free tier**
- **Industry standard**

## 🚀 **STEP-BY-STEP: Deploy in 20 Minutes**

### **Step 1: Create Heroku Account**
1. **Go to [Heroku.com](https://heroku.com)**
2. **Click "Get Started for Free"**
3. **Sign up with GitHub** (recommended)
4. **Verify email**
5. **Complete account setup**

### **Step 2: Install Heroku CLI**
**Choose based on your OS:**

**Windows:**
1. **Download Heroku CLI** from heroku.com
2. **Run installer**
3. **Restart command prompt**

**Mac:**
```bash
brew tap heroku/brew && brew install heroku
```

**Linux:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

### **Step 3: Prepare Your Files**
**Create additional files for Heroku:**

**1. Create `runtime.txt`:**
```
python-3.11.0
```

**2. Update `Procfile` (already exists):**
```
web: python app.py
```

**3. Update `requirements.txt` (ensure it includes):**
```
Flask==2.3.3
pandas==2.1.1
numpy==1.26.4
scikit-learn==1.3.0
joblib==1.3.2
Werkzeug==2.3.7
gunicorn==21.2.0
```

### **Step 4: Create GitHub Repository**
**Follow the Render guide steps:**
1. **Create new GitHub repository**
2. **Upload all your files**
3. **Commit with message "Health Risk Predictor for Heroku"**

### **Step 5: Deploy via Heroku CLI**
**Open terminal/command prompt:**

```bash
# Login to Heroku
heroku login

# Create new Heroku app
heroku create your-app-name

# Add GitHub remote (optional, can also use web interface)
git remote add heroku https://git.heroku.com/your-app-name.git

# Push to Heroku
git add .
git commit -m "Deploy Health Risk Predictor to Heroku"
git push heroku main
```

**Alternative: Deploy via Web Interface**
1. **Go to [Heroku Dashboard](https://dashboard.heroku.com)**
2. **Click "New" → "Create new app"**
3. **Choose name:** `your-app-name`
4. **Click "Create app"**
5. **Go to "Deploy" tab**
6. **Connect GitHub** repository
7. **Choose branch:** `main`
8. **Click "Deploy Branch"**

### **Step 6: Configure Environment Variables**
**In Heroku Dashboard:**

1. **Go to Settings tab**
2. **Click "Reveal Config Vars"**
3. **Add these variables:**
   ```
   FLASK_ENV = production
   PORT = 5000
   ```

### **Step 7: Scale Your App**
```bash
# Make sure at least one dyno is running
heroku ps:scale web=1
```

## ✅ **Your Live App URL:**
```
https://your-app-name.herokuapp.com
```

## 🧪 **Test Your App:**
1. **Open the URL in browser**
2. **Test home page loads**
3. **Test heart disease prediction**
4. **Test diabetes prediction**
5. **Verify probability scores display**

## 🔧 **Heroku CLI Commands:**

### **Useful Commands:**
```bash
# View logs
heroku logs --tail

# Restart app
heroku restart

# Open app in browser
heroku open

# Check app status
heroku ps

# View config variables
heroku config

# Set environment variable
heroku config:set FLASK_ENV=production

# Remove environment variable
heroku config:unset VARIABLE_NAME
```

## 🚨 **Troubleshooting Heroku**

### **Build Fails:**
**Check build logs:**
```bash
heroku logs --tail
```

**Common solutions:**
- **Check `requirements.txt`** syntax
- **Verify all imports** are available
- **Ensure file paths** are correct

### **App Won't Start:**
**Check runtime logs:**
```bash
heroku logs --tail
```

**Common solutions:**
- **Verify `Procfile`** exists and is correct
- **Check `runtime.txt`** Python version
- **Ensure port binding** in `app.py`

### **Memory Issues:**
**Heroku Free Tier Limits:**
- **512MB RAM** per dyno
- **550 hours/month** compute time

**Solutions:**
- **Optimize model files**
- **Use paid dynos** if needed

### **Large File Issues:**
**Your 61MB model should work, but if not:**
```bash
# Check if file uploaded
heroku run bash
ls -la models/

# If file too large, consider:
# 1. Optimize model (fewer trees)
# 2. Use paid tier
# 3. External file storage (S3)
```

## 💰 **Heroku Pricing:**

### **Free Tier:**
- ✅ **550 dyno hours/month**
- ✅ **Great for testing**
- ⚠️ **Sleeps after 30 minutes** of inactivity
- ⚠️ **Limited memory**

### **Hobby Dyno ($7/month):**
- ✅ **Always on**
- ✅ **More reliable**
- ✅ **No sleep**
- ✅ **Better performance**

### **Standard-1X Dyno ($25/month):**
- ✅ **2GB RAM**
- ✅ **More compute power**
- ✅ **Professional hosting**

## 🎯 **Benefits of Heroku:**
- ✅ **Most reliable platform**
- ✅ **Excellent documentation**
- ✅ **Great support**
- ✅ **Industry standard**
- ✅ **Easy deployment**
- ✅ **Handles large files**

## 🚀 **Automatic Deployments:**
**Once set up:**
1. **Push code to GitHub**
2. **Heroku automatically deploys**
3. **Updates are live in 2-3 minutes**

## 🎯 **Next Steps:**
1. **Install Heroku CLI**
2. **Create GitHub repository**
3. **Deploy via Heroku CLI or web interface**
4. **Your app will be live in 20 minutes!**

**Ready to try Heroku? It's the most reliable option for your Flask app!**