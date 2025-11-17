#!/bin/bash

# Health Risk Predictor - Quick Deployment Script
echo "🚀 Health Risk Predictor Deployment Helper"
echo "==========================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
    git add .
    git commit -m "Health Risk Predictor - Ready for deployment"
    echo "✅ Git initialized and first commit created"
else
    echo "📁 Adding files to Git..."
    git add .
    echo "Enter commit message:"
    read -r commit_msg
    git commit -m "$commit_msg"
    echo "✅ Changes committed"
fi

echo ""
echo "🔗 Next Steps:"
echo "1. Create a new repository on GitHub"
echo "2. Copy the repository URL"
echo "3. Run these commands (replace YOUR_USERNAME with your GitHub username):"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/health-risk-predictor.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "4. Go to render.com and deploy from your GitHub repository"
echo ""
echo "🎉 Your app will be live shortly after deployment!"