# Streamlit Secrets Configuration

## 📝 Local Development

1. **Edit `.streamlit/secrets.toml`** and add your actual API keys:
   - `APP_PASSWORD` - Your app access password
   - `ANTHROPIC_API_KEY` - Your Anthropic Claude API key (required)
   - Optional: Add other AI provider keys if needed

2. **Restart your Streamlit app** after making changes

3. **This file is safe** - it's in `.gitignore` and won't be committed to Git

## 🚀 Deployment (Streamlit Cloud)

**IMPORTANT:** For deployment, you DON'T use this file!

Instead, use Streamlit Cloud's built-in Secrets management:

1. Go to your app on [share.streamlit.io](https://share.streamlit.io)
2. Click **⚙️ Settings** → **Secrets**
3. Copy the contents from `secrets.toml.example` (or this file)
4. Paste into Streamlit Cloud Secrets
5. Replace placeholder values with your actual keys
6. Click **Save**

The app will automatically restart with the new secrets.

## 🔐 Security Notes

- ✅ `secrets.toml` is in `.gitignore` - safe from Git commits
- ✅ Streamlit Cloud Secrets are encrypted and secure
- ❌ Never commit API keys to Git
- ❌ Never share your `secrets.toml` file

## 📚 More Information

See `DEPLOYMENT.md` in the project root for complete deployment instructions.

