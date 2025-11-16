# 🚀 GoalPath AI - Deployment Guide

**Complete guide to deploying GoalPath AI for mobile access**

---

## 📱 Recommended: Streamlit Cloud (Best for Mobile)

**Why Streamlit Cloud:**
- ✅ **Free tier** - Perfect for personal use
- ✅ **Automatic HTTPS** - Secure by default
- ✅ **Mobile optimized** - Access from anywhere
- ✅ **Auto-updates** - Push to GitHub, app updates automatically
- ✅ **Zero server maintenance** - Just works
- ✅ **Global CDN** - Fast from Chennai or anywhere

---

## 🎯 Step-by-Step Deployment (15 minutes)

### **Step 1: Get Your API Key (5 minutes)**

You need at least ONE AI provider API key. **Anthropic Claude** is recommended:

1. **Go to:** [console.anthropic.com](https://console.anthropic.com/)
2. **Sign up** (if you don't have an account)
3. **Create API key:**
   - Click "Get API Keys"
   - Click "Create Key"
   - **Copy the key** (starts with `sk-ant-`)
   - **Save it somewhere safe** - you'll need it in Step 4

**Cost:** Claude has a generous free tier, then pay-as-you-go (very cheap for personal use)

---

### **Step 2: Push Code to GitHub (3 minutes)**

Your code is already on this branch: `claude/learnpath-ai-setup-014RbK3m8FVjabq96bopm7Ck`

**Option A: Use this branch directly**
```bash
# You're already here - just make sure latest changes are pushed
git status
# If you see uncommitted changes, commit them
git add .
git commit -m "Ready for deployment"
git push
```

**Option B: Merge to main branch (optional)**
```bash
# Switch to main
git checkout main

# Merge your feature branch
git merge claude/learnpath-ai-setup-014RbK3m8FVjabq96bopm7Ck

# Push to main
git push origin main
```

---

### **Step 3: Deploy on Streamlit Cloud (5 minutes)**

1. **Go to:** [share.streamlit.io](https://share.streamlit.io)

2. **Sign in with GitHub**
   - Click "Continue with GitHub"
   - Authorize Streamlit access

3. **Create New App**
   - Click "New app" button
   - **Repository:** Select `AI-Learning-Project`
   - **Branch:** `claude/learnpath-ai-setup-014RbK3m8FVjabq96bopm7Ck` (or `main`)
   - **Main file path:** `app.py`
   - Click "Deploy!"

4. **Wait for deployment** (2-3 minutes)
   - You'll see build logs
   - Wait for "Your app is live!" message

---

### **Step 4: Configure Secrets (2 minutes)**

**IMPORTANT:** Don't skip this step!

1. **In Streamlit Cloud dashboard:**
   - Click your app
   - Click "⚙️ Settings" (top right)
   - Click "Secrets" in sidebar

2. **Add your secrets** (copy-paste this, then edit):

```toml
# REQUIRED: Your app password (choose a strong password!)
APP_PASSWORD = "YourStrongPassword123!Chennai"

# REQUIRED: At least one AI provider API key
ANTHROPIC_API_KEY = "sk-ant-your-actual-key-here"

# Optional: Add more AI providers if you have them
# OPENAI_API_KEY = "sk-your-openai-key"
# GOOGLE_API_KEY = "your-gemini-key"
# DEEPSEEK_API_KEY = "your-deepseek-key"
```

3. **Click "Save"**
   - App will automatically restart with new secrets

---

### **Step 5: Access Your App! 🎉**

Your app is now live at: `https://your-app-name.streamlit.app`

**Example:** `https://goalpath-ai-chennai.streamlit.app`

---

## 📱 Mobile Access Setup

### **Option 1: Save to Home Screen (Recommended)**

**iPhone/iPad:**
1. Open app URL in Safari
2. Tap the Share button (box with arrow)
3. Scroll down and tap "Add to Home Screen"
4. Name it "GoalPath AI"
5. Tap "Add"

**Android:**
1. Open app URL in Chrome
2. Tap the menu (three dots)
3. Tap "Add to Home Screen"
4. Name it "GoalPath AI"
5. Tap "Add"

**Result:** App appears like a native app on your home screen! 🎉

### **Option 2: Bookmark**

Just bookmark the URL for quick access.

---

## 🔐 Security Setup

### **Choose a Strong Password**

Your `APP_PASSWORD` should be:
- **At least 12 characters**
- **Mix of letters, numbers, symbols**
- **Unique** (don't reuse from other sites)

**Good examples:**
- `GoalPath2025!Chennai@Secure`
- `MyGoals#Mobile$2025`

**Bad examples:**
- `password123` ❌
- `12345678` ❌

### **Save Password Securely**

**Options:**
1. **Password manager** (Bitwarden, 1Password, LastPass)
2. **iPhone Keychain** (auto-fills on mobile)
3. **Google Password Manager** (auto-fills on Android)

---

## 🎯 First Login

1. **Open your app URL**
2. **Enter your password** (the APP_PASSWORD you set in secrets)
3. **Check "Remember me"** (stays logged in for 24 hours)
4. **Start creating goals!**

---

## 🔄 Updating Your App

**When you want to add features or fix issues:**

1. **Make changes locally**
2. **Commit and push to GitHub:**
   ```bash
   git add .
   git commit -m "Update: description of changes"
   git push
   ```
3. **Streamlit Cloud auto-deploys** (within 1-2 minutes)
4. **Refresh your browser** to see changes

**That's it!** No manual deployment needed.

---

## 🐛 Troubleshooting

### **Problem: Can't login / "Incorrect password"**

**Solutions:**
- Check `APP_PASSWORD` in Streamlit Cloud Secrets (no extra spaces)
- Password is case-sensitive
- Try clearing browser cookies for the site
- Make sure you clicked "Save" in Secrets

### **Problem: "API key not configured" error**

**Solutions:**
- Check `ANTHROPIC_API_KEY` in Streamlit Cloud Secrets
- Make sure key starts with `sk-ant-`
- Click "Save" after adding secrets
- Wait 30 seconds for app to restart

### **Problem: App is slow or timing out**

**Solutions:**
- Streamlit Cloud free tier has resource limits
- Large goal plans (50+ tasks) may be slower
- Consider upgrading to paid tier if needed
- Most goals (10-30 tasks) work perfectly on free tier

### **Problem: Can't access from mobile**

**Solutions:**
- Check you're using HTTPS (should be automatic)
- Try different browser (Chrome/Safari)
- Clear browser cache
- Disable any VPN temporarily

### **Problem: Database reset / Lost data**

**Cause:** Streamlit Cloud resets on each deployment

**Solution:** Download backups regularly:
- Your SQLite database file is in the app
- Use Advanced Options → Download as PDF for individual plans
- Consider local backup script (advanced)

---

## 💡 Tips for Mobile Use

### **Performance:**
- **WiFi vs Mobile Data:** Both work, WiFi is faster
- **Battery:** Close app when not in use
- **Offline:** Requires internet connection to work

### **Best Practices:**
- **Bookmark frequently used goals** (copy URL from browser)
- **Use voice features** (🎤) for hands-free on mobile
- **Export to calendar** for offline task viewing
- **Save resource links** instead of uploading files

### **Workflow:**
1. **Morning:** Check calendar for today's tasks
2. **Working:** Use timer to track time on mobile
3. **Evening:** Mark tasks complete, check progress
4. **Weekly:** Get AI coaching review

---

## 🔧 Advanced Configuration (Optional)

### **Custom Domain (Paid Feature)**

Streamlit Cloud paid tier allows custom domains:
- `goalpath.yourname.com` instead of `.streamlit.app`
- Requires paid Streamlit plan ($20/month)

### **Environment Variables**

Add more configuration in Secrets:
```toml
# Timezone (optional)
TZ = "Asia/Kolkata"

# Session timeout (optional, in seconds)
SESSION_TIMEOUT = 86400  # 24 hours
```

### **Analytics (Optional)**

Add Google Analytics to track your own usage:
- Not built-in, would require code modification
- Not recommended for personal use

---

## 💰 Cost Breakdown

**Streamlit Cloud:**
- Free tier: $0/month (perfect for you)
- Paid tier: $20/month (only if you need more resources)

**Anthropic Claude API:**
- Free tier: Generous credits
- Pay-as-you-go: ~$0.01-0.05 per goal plan generation
- **Your estimated cost:** $1-3/month for personal use

**Total:** **FREE to $3/month** for complete setup! 🎉

---

## 🆘 Getting Help

**If you get stuck:**

1. **Check Streamlit Cloud logs:**
   - Go to your app in Streamlit Cloud
   - Click "Manage app"
   - View logs for error messages

2. **Common issues covered in Troubleshooting section above**

3. **Streamlit Community:**
   - [discuss.streamlit.io](https://discuss.streamlit.io/)

4. **GitHub Issues:**
   - Check README and FEATURE_SUMMARY.md first

---

## ✅ Deployment Checklist

Before you start:
- [ ] Have Anthropic API key ready
- [ ] Have GitHub account
- [ ] Code is pushed to GitHub
- [ ] Have chosen a strong password

Deployment steps:
- [ ] Signed up for Streamlit Cloud
- [ ] Created new app
- [ ] Added secrets (APP_PASSWORD + API keys)
- [ ] App is live and accessible
- [ ] Tested login with password
- [ ] Added app to mobile home screen
- [ ] Created first goal plan to test

Security:
- [ ] Using strong password
- [ ] Password saved in password manager
- [ ] API keys kept secret (not in code)
- [ ] .env file NOT committed to GitHub

---

## 🎉 You're All Set!

Your GoalPath AI is now:
- ✅ **Live on the internet**
- ✅ **Accessible from mobile**
- ✅ **Secure with HTTPS**
- ✅ **Auto-updating from GitHub**
- ✅ **Ready to help you achieve goals**

**Next steps:**
1. Open app on mobile
2. Add to home screen
3. Create your first goal plan
4. Start tracking your progress!

**Enjoy using GoalPath AI!** 🚀🎯

---

**Questions?** Check the troubleshooting section or README.md for more details.
