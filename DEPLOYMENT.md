# Herbo Bueno - Deployment Guide

## 🚀 Free Hosting Options

### Option 1: Railway (Recommended - Easiest)

1. **Sign up** at [railway.app](https://railway.app)
2. **Connect GitHub** and select your repository
3. **Deploy automatically** - Railway will detect Django and deploy
4. **Get free domain** - You'll get a `.railway.app` domain
5. **Custom domain** - Add your own domain in Railway dashboard

**Steps:**
```bash
# 1. Push your code to GitHub
git add .
git commit -m "Ready for deployment"
git push origin main

# 2. Go to railway.app and connect your GitHub repo
# 3. Railway will automatically deploy your Django app
```

### Option 2: Heroku (Classic Choice)

1. **Sign up** at [heroku.com](https://heroku.com)
2. **Install Heroku CLI**
3. **Deploy using Git**

**Steps:**
```bash
# 1. Install Heroku CLI
# 2. Login to Heroku
heroku login

# 3. Create Heroku app
heroku create herbo-bueno-app

# 4. Set environment variables
heroku config:set SECRET_KEY=your-secret-key-here
heroku config:set DEBUG=False

# 5. Deploy
git push heroku main

# 6. Run migrations
heroku run python manage.py migrate
```

### Option 3: Vercel (For Static + API)

1. **Sign up** at [vercel.com](https://vercel.com)
2. **Connect GitHub** repository
3. **Deploy automatically**

**Note:** Vercel works best with Django as an API backend. For full Django apps, Railway or Heroku are better.

## 🌐 Free Domain Options

### Option 1: Freenom (Free .tk, .ml, .ga domains)
1. Go to [freenom.com](https://freenom.com)
2. Search for available domains
3. Register for free (1 year)
4. Point DNS to your hosting provider

### Option 2: GitHub Pages + Custom Domain
1. Use GitHub Pages for static version
2. Add custom domain in repository settings
3. Point your domain to GitHub Pages

### Option 3: Netlify + Custom Domain
1. Deploy to Netlify
2. Add custom domain in Netlify dashboard
3. Configure DNS settings

## 🔧 Environment Variables

Set these in your hosting platform:

```
SECRET_KEY=your-very-secure-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
```

## 📱 Mobile App Deployment

For the mobile app mentioned in your website:
1. **React Native** - Deploy to App Store/Google Play
2. **Flutter** - Deploy to app stores
3. **PWA** - Make your website installable as an app

## 🎯 Recommended Setup

**Best Free Setup:**
1. **Hosting**: Railway.app (free tier)
2. **Domain**: Freenom free domain (.tk, .ml, .ga)
3. **Database**: Railway PostgreSQL (free tier)
4. **CDN**: Cloudflare (free)

## 🚀 Quick Deploy Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

## 📞 Support

If you need help with deployment, check:
- Railway documentation
- Heroku documentation
- Django deployment guide

Your Herbo Bueno website is now ready for deployment! 🎉
