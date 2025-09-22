#!/bin/bash

echo "🚀 Deploying Herbo Bueno Website..."

# Collect static files
echo "📦 Collecting static files..."
python3 manage.py collectstatic --noinput

# Run migrations
echo "🗄️ Running database migrations..."
python3 manage.py migrate

# Create superuser (optional)
echo "👤 Creating superuser (optional)..."
echo "You can skip this by pressing Ctrl+C"
python3 manage.py createsuperuser

echo "✅ Deployment preparation complete!"
echo ""
echo "🌐 Next steps:"
echo "1. Push your code to GitHub:"
echo "   git add ."
echo "   git commit -m 'Ready for deployment'"
echo "   git push origin main"
echo ""
echo "2. Deploy to Railway:"
echo "   - Go to railway.app"
echo "   - Connect your GitHub repository"
echo "   - Railway will automatically deploy"
echo ""
echo "3. Get a free domain:"
echo "   - Go to freenom.com"
echo "   - Register a free .tk, .ml, or .ga domain"
echo "   - Point it to your Railway app"
echo ""
echo "🎉 Your website will be live at your Railway domain!"
