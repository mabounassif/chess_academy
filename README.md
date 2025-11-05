# Chess Academy - Odoo Setup

A minimalistic Odoo setup for managing a Chess Academy with student enrollment, lesson scheduling, coach management, and more.

## 📋 Overview

This setup includes:
- **Docker-based Odoo 17** with PostgreSQL database
- **Custom Chess Academy module** with models for Students, Coaches, and Lessons
- **Pre-configured dependencies** for CRM, Sales, Calendar, Events, and Marketing

## 🚀 Deployment Options

### 🚂 Railway (Cloud Deployment - Recommended)
Deploy to Railway in minutes with automatic PostgreSQL setup and SSL certificates.

**See detailed guide: [DEPLOY_RAILWAY.md](DEPLOY_RAILWAY.md)**

Quick deploy:
1. Push this repo to GitHub
2. Create a Railway project from your repo
3. Add PostgreSQL database
4. Set environment variables
5. Deploy! 🎉

### 💻 Local Development (Docker)

#### Prerequisites
- Docker and Docker Compose installed on your system
- Port 8069 available for Odoo web interface
- Port 5432 available for PostgreSQL

#### Installation

1. **Start the services**
```bash
docker-compose up -d
```

2. **Wait for initialization** (first time takes ~2 minutes)
```bash
docker logs -f chess_academy_odoo
```

3. **Access Odoo**
- Open browser: http://localhost:8069
- Create your first database when prompted

### Database Creation

When accessing Odoo for the first time:
1. **Master Password**: `admin123`
2. **Database Name**: `chess_academy` (or your choice)
3. **Email**: Your admin email
4. **Password**: Your admin password
5. **Language**: Select your language
6. **Country**: Select your country
7. **Demo Data**: Choose "Create demo data" for testing or leave unchecked for production

## 📦 Module Installation

After database creation:

### 1. Install Core Modules

Go to **Apps** menu and install these modules in order:

**Essential (Install First):**
- Contacts
- CRM
- Sales
- Invoicing
- Calendar
- Appointments

**Additional (Install After Essential):**
- Project
- Website
- Portal
- Events
- Email Marketing
- SMS Marketing
- Marketing Automation

### 2. Install Chess Academy Module

1. Go to **Apps** menu
2. Remove the "Apps" filter
3. Search for "Chess Academy"
4. Click **Install**

If you don't see the Chess Academy module:
1. Activate Developer Mode (Settings → Activate Developer Mode)
2. Go to Apps → Update Apps List
3. Search for "Chess Academy" and install

## 🎓 Using the Chess Academy Module

### Students Management
- Navigate to **Chess Academy → Students**
- Create student records with:
  - Personal information (name, age, parent/guardian)
  - Chess rating and skill level
  - Track enrollment date and lessons

### Coaches Management
- Navigate to **Chess Academy → Coaches**
- Add coach profiles with:
  - Contact information
  - FIDE title and rating
  - Specialization and hourly rate

### Lesson Scheduling
- Navigate to **Chess Academy → Lessons**
- Schedule lessons with:
  - Student and coach assignment
  - Date, time, and duration
  - Lesson type (individual, group, online, tournament prep)
  - Track progress notes and homework
- View lessons in calendar view for easy scheduling

## 🔧 Configuration

### Odoo Configuration
Edit `config/odoo.conf` to customize:
- Admin password
- Database settings
- Add-ons path
- Performance settings

### Adding More Modules
Place custom modules in the `addons/` directory and update the apps list in Odoo.

## 📊 Key Features by Module

| Module Category | Features Enabled |
|----------------|------------------|
| **CRM & Contacts** | Lead management, parent/guardian contacts, partner schools |
| **Sales & Billing** | Lesson packages, invoicing, payment tracking |
| **Calendar** | Lesson scheduling, coach availability, room bookings |
| **Project** | Student progress tracking, curriculum management |
| **Website & Portal** | Parent/student login, lesson videos, online booking |
| **Events** | Tournament organization, camps, special sessions |
| **Marketing** | Email campaigns, SMS reminders, automated renewals |

## 🛠️ Useful Commands

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker logs -f chess_academy_odoo

# Restart Odoo (after config changes)
docker-compose restart odoo

# Database backup
docker exec chess_academy_db pg_dump -U odoo chess_academy > backup.sql

# Database restore
cat backup.sql | docker exec -i chess_academy_db psql -U odoo chess_academy
```

## 📁 Project Structure

```
chess_academy/
├── docker-compose.yml          # Docker services configuration
├── config/
│   └── odoo.conf              # Odoo configuration
├── addons/
│   └── chess_academy/         # Custom Chess Academy module
│       ├── __manifest__.py    # Module definition
│       ├── models/            # Data models (Student, Coach, Lesson)
│       ├── views/             # UI views and menus
│       └── security/          # Access rights
└── README.md                  # This file
```

## 🔐 Security Notes

**Important:** Change these defaults in production:
- Master password in `config/odoo.conf` (currently: `admin123`)
- PostgreSQL password in `docker-compose.yml` (currently: `odoo`)
- Restrict network access to your Odoo instance

## 🆘 Troubleshooting

### Module not appearing?
1. Enable Developer Mode
2. Apps → Update Apps List
3. Clear browser cache

### Port already in use?
Edit `docker-compose.yml` to change port mappings:
```yaml
ports:
  - "8070:8069"  # Change 8070 to any available port
```

### Database connection issues?
Check if PostgreSQL is running:
```bash
docker ps | grep postgres
docker logs chess_academy_db
```

## 📚 Next Steps

1. **Configure Company Settings**: Settings → General Settings
2. **Set Up Email**: Settings → Technical → Outgoing Mail Servers
3. **Customize Website**: Website → Configuration
4. **Create Lesson Products**: Sales → Products (for selling lesson packages)
5. **Set Up Payment Methods**: Invoicing → Configuration → Payment Acquirers
6. **Configure Calendar**: Calendar → Configuration

## 📖 Additional Resources

- [Odoo Documentation](https://www.odoo.com/documentation/17.0/)
- [Odoo Developer Guide](https://www.odoo.com/documentation/17.0/developer.html)
- [Docker Compose Reference](https://docs.docker.com/compose/)

## 📄 License

This custom module is licensed under LGPL-3.

---

**Note**: This is a minimal setup designed for quick deployment. For production use, consider:
- Using environment variables for sensitive data
- Setting up SSL/TLS certificates
- Implementing backup automation
- Configuring proper firewall rules
- Using a reverse proxy (nginx)

