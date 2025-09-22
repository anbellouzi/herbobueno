# Herbo Bueno Club

A Django-based website for the Herbo Bueno Club, featuring vendor partnerships, giveaways, and vacation packages.

## Features

- **User Management**: User registration, profiles, and authentication
- **Vendor System**: Vendor registration, product listings, and purchase tracking
- **Giveaway System**: Vacation packages and vendor prizes with entry tracking
- **Membership Tiers**: Different membership levels with varying benefits
- **Patreon-inspired Design**: Modern, responsive UI with Bootstrap 5

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Visit `http://127.0.0.1:8000/` to access the website
2. Create an account or login
3. Browse vendors and make purchases to earn giveaway entries
4. Enter giveaways for a chance to win vacation packages or vendor prizes
5. Upgrade your membership for additional benefits

## Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/` to:
- Manage vendors and products
- Create vacation packages and vendor prizes
- Set up giveaways
- Configure membership tiers
- View user data and purchases

## Project Structure

```
herbo_bueno/
├── core/           # Core app with user profiles
├── vendors/        # Vendor management and purchases
├── giveaways/      # Giveaway system and prizes
├── memberships/    # Membership tiers and benefits
├── templates/      # HTML templates
├── static/         # CSS, JS, and images
└── media/          # User uploaded files
```

## Technologies Used

- Django 4.2.7
- Bootstrap 5
- Font Awesome
- SQLite (development)
- Pillow (image handling)
- Crispy Forms
