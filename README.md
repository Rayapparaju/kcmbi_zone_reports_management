# KCMBI Zone Report Management

A Django web application for managing church zone reports with role-based access, digital forms, and PDF generation.

## Features

- **Role-based access**: Admin, Team Leader, and Preacher roles with appropriate permissions
- **Four digital forms**: Preacher Personal Info, Team Leader Personal Data, Congregation Update, KCMBI Field Report
- **Full CRUD**: Create, read, update, and delete operations on all records
- **A4 PDF generation**: ReportLab-based PDFs matching form layout with photos and email footer
- **Zone tracking**: Organize and filter data by geographical zones
- **Photo upload**: Support for preacher/congregation/field report photos
- **Search & filter**: Search across records with role-appropriate visibility
- **Preacher approval**: New registrations require admin approval before login
- **Excel export**: Export team leaders, field reports, congregations, and zones to Excel
- **Responsive design**: Bootstrap 5 with mobile-friendly layout

## Tech Stack

- **Backend**: Python, Django 5.x
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript, Font Awesome
- **Database**: SQLite
- **PDF**: ReportLab
- **Excel**: openpyxl

## Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/Rayapparaju/kcmbi_zone_reports_management.git
   cd kcmbi_zone_reports_management
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   # Username: admin
   # Password: admin123
   ```

6. **Seed demo data** (optional)
   ```bash
   python manage.py seed_data
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic --clear
   ```

8. **Run the server**
   ```bash
   python manage.py runserver
   ```

9. Visit `http://127.0.0.1:8000/`

## Demo Accounts

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | admin123 |
| Team Leader | johnleader | johnleader123 |
| Preacher | jamespreacher | james123 |

## Usage

- **Admin**: Full access to all records, user management, preacher approval
- **Team Leader**: Manages own zones, preachers, congregations, and field reports
- **Preacher**: Submits personal info, congregation updates, and field reports (own data only)

## Commands

```bash
# Reset a user's password
python manage.py reset_password <username> <newpassword>

# Seed demo data
python manage.py seed_data
```

## Color Palette

- Primary: `#AA1C41`
- Primary Dark: `#5E244E`
- Primary Light: `#E68457`
- Accent Gold: `#FFE8B4`
