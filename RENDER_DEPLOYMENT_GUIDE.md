# 🚀 Complete Guide: Deploy Health Risk Predictor to Render

## 📋 Prerequisites
- ✅ Your enhanced Health Risk Predictor app is ready
- ✅ Render account (free tier available)
- ✅ GitHub account (for code repository)

## 🎯 Step 1: Prepare Your Code Repository

### 1.1 Create GitHub Repository
1. Go to [GitHub.com](https://github.com) and login
2. Click **"New Repository"** (green button)
3. Repository settings:
   - **Repository name:** `health-risk-predictor` (or your preferred name)
   - **Description:** "AI-powered health risk assessment for diabetes and heart disease"
   - **Visibility:** Public (required for free Render hosting)
   - **Initialize with:** ❌ Don't check any boxes (we have existing files)
4. Click **"Create repository"**

### 1.2 Upload Your Files
**Option A: Using GitHub Web Interface (Easiest)**

1. On your new repository page, click **"uploading an existing file"** link
2. Upload ALL these files from your workspace:
   ```
   ├── app.py
   ├── models.py
   ├── requirements.txt
   ├── Procfile
   ├── railway.json (optional, Render doesn't need it)
   ├── README.md
   ├── DEPLOYMENT_GUIDE.md
   ├── static/
   │   └── css/
   │       └── style.css
   ├── templates/
   │   ├── base.html
   │   ├── index.html
   │   ├── about.html
   │   ├── heart_disease.html
   │   ├── diabetes.html
   │   ├── heart_result.html
   │   └── diabetes_result.html
   ├── models/
   │   ├── heart_model.pkl
   │   ├── diabetes_model.pkl
   │   ├── heart_scaler.pkl
   │   ├── diabetes_scaler.pkl
   │   └── diabetes_encoders.pkl
   └── user_input_files/
       ├── heart.csv
       └── diabetes.csv
   ```

3. **For multiple file uploads:**
   - Drag and drop all files/folders
   - Or select all files using Ctrl+A (Cmd+A on Mac)
   - Upload them in batches if needed

4. Commit message: `"Initial commit: Health Risk Predictor app"`

5. Click **"Commit changes"**

**Option B: Using Git Commands (Advanced)**

```bash
# Navigate to your project folder
cd /path/to/your/health-risk-predictor

# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Health Risk Predictor app"

# Add GitHub repository as origin (replace with your actual repo URL)
git remote add origin https://github.com/YOUR_USERNAME/health-risk-predictor.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## 🎯 Step 2: Deploy to Render

### 2.1 Create Render Account
1. Go to [Render.com](https://render.com)
2. Click **"Get Started for Free"**
3. Sign up using:
   - **GitHub account** (recommended - easier integration)
   - **Email and password**
   - Or **Google account**

### 2.2 Connect GitHub Repository
1. After login, you'll see the Render dashboard
2. Click **"New +"** button
3. Select **"Web Service"**
4. Connect your GitHub account if prompted
5. Find and select your repository:
   - **Repository:** `health-risk-predictor` (your repo name)
   - **Branch:** `main`

### 2.3 Configure Web Service
Fill in these settings:

**Basic Settings:**
- **Name:** `health-risk-predictor` (or your preferred name)
- **Region:** Choose closest to your users (e.g., `Oregon (US West)`)
- **Branch:** `main`
- **Root Directory:** Leave empty (files are in root)
- **Runtime:** `Python 3`

**Build and Deploy Settings:**
- **Build Command:** Leave empty (Render auto-detects)
- **Start Command:** Leave empty (we have Procfile)

**Auto-Deploy:** ✅ Yes (recommended for updates)

### 2.4 Environment Variables (IMPORTANT!)
Click **"Advanced"** tab and add these environment variables:

```
FLASK_ENV=production
PORT=5000
PYTHON_VERSION=3.12.0
```

**If you see additional settings:**
- **Instance Type:** Free tier is selected by default
- **Auto-Deploy:** Enabled

### 2.5 Deploy
1. Click **"Create Web Service"**
2. Render will automatically:
   - Detect it's a Python app
   - Install dependencies from `requirements.txt`
   - Run your `Procfile`
   - Deploy your app

## 🎯 Step 3: Monitor Deployment

### 3.1 Build Process
Render will show real-time logs. You should see:
```
✓ Build completed successfully
✓ Deploy started
✓ Service is live
```

### 3.2 Deployment URL
After successful deployment, you'll get a URL like:
```
https://health-risk-predictor.onrender.com
```
**This is your live app URL!**

## 🎯 Step 4: Test Your Live App

### 4.1 Accessibility Test
1. Open your Render URL in browser
2. Check that the home page loads
3. Test navigation between pages
4. Test both prediction forms

### 4.2 Functionality Test
1. **Heart Disease Prediction:**
   - Fill out the form with test data
   - Submit and check results display

2. **Diabetes Prediction:**
   - Fill out the form with test data
   - Submit and check results display

## 🎯 Step 5: Custom Domain (Optional)

### 5.1 Free Custom Subdomain
1. Go to your service dashboard on Render
2. Click **"Settings"** tab
3. Scroll to **"Custom Domains"**
4. Add your desired subdomain: `myapp.render.com`

### 5.2 Custom Domain (Advanced)
If you own a domain:
1. Add CNAME record in your DNS settings
2. Point to your Render app URL
3. Add domain in Render settings

## 🎯 Step 6: Continuous Deployment

### 6.1 Auto-Deploy Updates
When you make changes to your code:
1. Push updates to your GitHub repository
2. Render automatically detects changes
3. Rebuilds and deploys your app
4. Updates are live within 2-3 minutes

### 6.2 Manual Redeploy
1. Go to your service dashboard
2. Click **"Manual Deploy"** → **"Deploy latest commit"**

## 🚨 Troubleshooting Common Issues

### Issue 1: Build Fails
**Error:** `No module named 'flask'`
**Solution:** 
- Check `requirements.txt` exists and has correct dependencies
- Ensure all imports are available

### Issue 2: App Doesn't Start
**Error:** `Application failed to start`
**Solution:**
- Verify `Procfile` content: `web: python app.py`
- Check `app.py` uses `PORT` environment variable correctly

### Issue 3: Models Not Loading
**Error:** `FileNotFoundError: models/heart_model.pkl`
**Solution:**
- Ensure all model files are uploaded to repository
- Check file paths are correct

### Issue 4: Port Binding Error
**Solution:** Ensure `app.py` has:
```python
port = int(os.environ.get('PORT', 5000))
app.run(debug=False, host='0.0.0.0', port=port)
```

### Issue 5: Memory Issues (Free Tier)
**Error:** Out of memory
**Solutions:**
- Use smaller models
- Optimize data processing
- Consider upgrading to paid tier

## 📊 Render Free Tier Limits
- ✅ **750 hours/month** of compute time
- ✅ **0.5 GB RAM** per instance
- ✅ **100 GB bandwidth** per month
- ✅ **Automatic SSL** certificates
- ✅ **Custom domains** support
- ⚠️ **Sleeps after 15 minutes** of inactivity (wakes up on request)
- ⚠️ **Cold starts** may take 30 seconds

## 🎯 Next Steps After Deployment

1. **Share your app URL** with users
2. **Monitor usage** in Render dashboard
3. **Update regularly** with improvements
4. **Consider paid tier** if needed (starts at $7/month)

## 📞 Support Resources

- **Render Documentation:** https://render.com/docs
- **Render Status Page:** https://status.render.com
- **Community Discord:** https://discord.gg/render

---

**🎉 Congratulations! Your Health Risk Predictor app is now live on Render!**

Your app URL: `https://YOUR_APP_NAME.onrender.com`