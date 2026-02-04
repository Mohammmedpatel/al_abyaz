# Al-Abyaz - Luxury Perfume & Attar Store

A premium e-commerce website for perfumes and attars built with Django, featuring WhatsApp integration for orders and UPI payment support.

![Al-Abyaz Logo](static/images/logo.png)

## Features

- **Luxury Design**: Elegant gold and black theme with premium aesthetics
- **Product Management**: Admin-only product addition via Django Admin
- **WhatsApp Integration**: Direct order placement through WhatsApp
- **UPI Payment**: Easy payment via UPI ID
- **Responsive Design**: Mobile-friendly interface
- **Product Categories**: Perfumes, Attars, and Combo deals
- **Featured & Bestseller Products**: Highlight special products
- **SEO Optimized**: Meta tags and structured data

## Tech Stack

- **Backend**: Django 4.2+
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default)
- **Styling**: Custom CSS with CSS Variables
- **Animations**: AOS (Animate On Scroll)
- **Icons**: Font Awesome

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or download the project**
   ```bash
   cd al_abyaz
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the website**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Configuration

### Update Contact Information

Edit `al_abyaz/settings.py` to update your contact details:

```python
# WhatsApp Configuration
WHATSAPP_NUMBER = '7506516067'  # Your WhatsApp number
UPI_ID = 'sobanbalwa0@okhdfcbank'  # Your UPI ID
SHOP_NAME = 'Al-Abyaz'
```

### Security Settings

Before deploying to production, make sure to:

1. Change the `SECRET_KEY` in `al_abyaz/settings.py`
2. Set `DEBUG = False`
3. Add your domain to `ALLOWED_HOSTS`

## Usage

### Adding Products (Admin Only)

1. Log in to the admin panel at `/admin/`
2. Navigate to **Shop** > **Products**
3. Click **Add Product**
4. Fill in the product details:
   - Name, Slug, Category
   - Product Type (Perfume/Attar/Combo)
   - Description, Price, Stock
   - Volume (e.g., 50ml, 100ml)
   - Fragrance Notes
   - Upload product image
   - Mark as Featured/Bestseller if applicable

### Managing Categories

1. Go to **Shop** > **Categories** in the admin panel
2. Add or edit categories as needed
3. Each product must belong to a category

### Placing Orders

Customers can place orders by:

1. Browsing products on the home page
2. Clicking "Buy Now" on any product card
3. This opens WhatsApp with a pre-filled message
4. The admin receives the order details on WhatsApp

## Project Structure

```
al_abyaz/
├── al_abyaz/                 # Project configuration
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL routing
│   ├── wsgi.py
│   └── asgi.py
├── shop/                     # Main application
│   ├── __init__.py
│   ├── admin.py             # Admin configuration
│   ├── apps.py
│   ├── models.py            # Database models
│   ├── tests.py
│   ├── urls.py              # App URL patterns
│   └── views.py             # View functions
├── templates/                # HTML templates
│   ├── base.html            # Base template
│   └── shop/
│       ├── product/
│       │   ├── list.html    # Product listing page
│       │   └── detail.html  # Product detail page
│       ├── about.html       # About page
│       └── contact.html     # Contact page
├── static/                   # Static files (CSS, JS, images)
│   ├── css/
│   │   └── style.css        # Main stylesheet
│   ├── js/
│   │   └── main.js          # Main JavaScript file
│   └── images/
├── media/                    # User-uploaded files
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Customization

### Changing Colors

Edit the CSS variables in `static/css/style.css`:

```css
:root {
    --color-primary: #1a1a1a;        /* Main background */
    --color-accent: #d4af37;          /* Gold accent */
    --color-accent-light: #f4d03f;    /* Light gold */
    --color-accent-dark: #b8860b;     /* Dark gold */
    /* ... */
}
```

### Adding New Pages

1. Create a view in `shop/views.py`
2. Add URL pattern in `shop/urls.py`
3. Create template in `templates/shop/`
4. Add navigation link in `templates/base.html`

## Deployment

### Deploying to PythonAnywhere

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload your project files
3. Create a virtual environment and install requirements
4. Configure the WSGI file
5. Set up static and media files

### Deploying to Heroku

1. Create a `Procfile`:
   ```
   web: gunicorn al_abyaz.wsgi
   ```

2. Add `gunicorn` to requirements.txt

3. Deploy using Git

## License

This project is licensed under the MIT License.

## Support

For support, contact us on WhatsApp: +91 7506516067

---

**Al-Abyaz** - Crafting Memories Through Fragrance ✨
