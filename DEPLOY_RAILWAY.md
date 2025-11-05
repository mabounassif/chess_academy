# 🚂 Deploy Chess Academy on Railway

This guide will help you deploy your Chess Academy Odoo instance on Railway.

## Prerequisites

- A Railway account (sign up at [railway.app](https://railway.app))
- Git installed on your machine
- This project pushed to a GitHub repository (or use Railway CLI)

## 🚀 Quick Deploy

### Option 1: Deploy from GitHub (Recommended)

#### Step 1: Create a New Project on Railway

1. Go to [Railway Dashboard](https://railway.app/dashboard)
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Select your `chess_academy` repository

#### Step 2: Add PostgreSQL Database

1. In your Railway project, click **"New"**
2. Select **"Database"** → **"Add PostgreSQL"**
3. Railway will automatically create a PostgreSQL instance

#### Step 3: Configure Environment Variables

Click on your Odoo service, go to **"Variables"** tab, and add:

```env
ODOO_ADMIN_PASSWORD=your-secure-admin-password-here
PORT=8069
```

The following variables are automatically provided by Railway when you add PostgreSQL:
- `PGHOST`
- `PGPORT`
- `PGUSER`
- `PGPASSWORD`
- `PGDATABASE`

#### Step 4: Deploy

1. Railway will automatically detect the `Dockerfile` and start building
2. Wait for the build to complete (~5-10 minutes for first deployment)
3. Once deployed, click **"Generate Domain"** to get your public URL

### Option 2: Deploy with Railway CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Link to PostgreSQL
railway add --database postgresql

# Set environment variables
railway variables set ODOO_ADMIN_PASSWORD=your-secure-password

# Deploy
railway up
```

## 🔧 Configuration

### Required Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `ODOO_ADMIN_PASSWORD` | Master password for Odoo | `MySecurePass123!` |
| `PORT` | Port (Railway auto-detects) | `8069` |

### Automatically Provided by Railway PostgreSQL

| Variable | Description |
|----------|-------------|
| `PGHOST` | PostgreSQL host |
| `PGPORT` | PostgreSQL port |
| `PGUSER` | Database user |
| `PGPASSWORD` | Database password |
| `PGDATABASE` | Database name |

## 📦 First Time Setup

After deployment:

1. **Access your Odoo instance**
   - Go to your Railway-generated domain (e.g., `https://your-app.railway.app`)

2. **Create Database**
   - Master Password: Use the `ODOO_ADMIN_PASSWORD` you set
   - Database Name: `chess_academy`
   - Email: Your admin email
   - Password: Your admin password
   - Language & Country: Select appropriate options
   - Demo Data: Leave unchecked for production

3. **Install Modules**
   Follow the module installation order from `INSTALL.md`:
   - Core modules: Contacts, CRM, Sales, Invoicing
   - Scheduling: Calendar, Appointments
   - Additional: Project, Website, Portal, Events
   - Marketing: Email Marketing, SMS, Marketing Automation
   - Finally: **Chess Academy** module

## 💾 Data Persistence

Railway provides persistent storage for PostgreSQL. Your data is safe across deployments!

However, note that:
- Odoo filestore (uploaded files) may be lost on redeployment
- For production, consider using S3-compatible storage for attachments

## 🔒 Security Recommendations

### 1. Strong Admin Password
```bash
railway variables set ODOO_ADMIN_PASSWORD='Generate-A-Strong-Password-Here'
```

### 2. Restrict Database Listing
Already configured in `odoo.railway.conf`:
```ini
list_db = False
```

### 3. Enable HTTPS
Railway automatically provides SSL certificates for your domain.

### 4. Set Up Backup
```bash
# Connect to PostgreSQL and backup
railway connect postgres
# Then run pg_dump commands
```

## 📊 Monitoring

### View Logs
```bash
# Using Railway CLI
railway logs

# Or in Railway Dashboard:
# Project → Service → Deployments → Click on deployment → View logs
```

### Health Checks
The deployment includes automatic health checks:
- Endpoint: `/web/health`
- Interval: 30 seconds
- Timeout: 10 seconds

## 🔄 Updates and Redeployment

### Automatic Deployment
Railway automatically redeploys when you push to your GitHub repository.

### Manual Deployment
```bash
# Using Railway CLI
railway up

# Or trigger from GitHub:
git push origin main
```

## 💰 Costs

Railway pricing (as of 2025):
- **Free Tier**: $5 credit/month (sufficient for development/testing)
- **Pro Plan**: $20/month + usage-based billing

Estimated costs for Chess Academy:
- Small setup (< 50 users): ~$10-15/month
- Medium setup (50-200 users): ~$20-30/month
- Includes: Odoo instance + PostgreSQL database

## 🐛 Troubleshooting

### Build Fails

**Issue**: Docker build fails
```bash
# Check build logs
railway logs --deployment

# Common fixes:
# 1. Ensure all files are committed to git
# 2. Check Dockerfile syntax
# 3. Verify addons directory structure
```

### Database Connection Issues

**Issue**: Can't connect to PostgreSQL
```bash
# Verify PostgreSQL is running
railway status

# Check environment variables
railway variables

# Ensure PostgreSQL service is linked
railway link
```

### Module Installation Fails

**Issue**: Chess Academy module doesn't appear
1. Check deployment logs for errors
2. Verify file permissions in deployment
3. Update apps list in Odoo (Settings → Apps → Update Apps List)

### Performance Issues

**Issue**: Slow response times
```bash
# Scale up your instance
# In Railway Dashboard: Service → Settings → Resources
# Increase memory and CPU allocation
```

## 📈 Scaling

### Vertical Scaling
Increase resources in Railway Dashboard:
- Go to Service → Settings → Resources
- Adjust vCPU and Memory

### Horizontal Scaling
For high traffic:
1. Use Railway's replica feature
2. Consider adding Redis for sessions
3. Set up CDN for static files

## 🔗 Custom Domain

1. Go to your service in Railway
2. Click **"Settings"** → **"Domains"**
3. Add your custom domain
4. Update your DNS records as instructed

## 📚 Additional Resources

- [Railway Documentation](https://docs.railway.app/)
- [Odoo Documentation](https://www.odoo.com/documentation/17.0/)
- [Railway CLI Reference](https://docs.railway.app/develop/cli)

## 🆘 Getting Help

- Railway Discord: [discord.gg/railway](https://discord.gg/railway)
- Railway Forum: [help.railway.app](https://help.railway.app)
- Odoo Forum: [odoo.com/forum](https://www.odoo.com/forum)

---

## 🎯 Quick Checklist

- [ ] Railway account created
- [ ] GitHub repository set up
- [ ] PostgreSQL database added
- [ ] Environment variables configured
- [ ] First deployment successful
- [ ] Domain generated
- [ ] Database created in Odoo
- [ ] Core modules installed
- [ ] Chess Academy module installed
- [ ] Admin password changed
- [ ] First student/coach created

**Your Chess Academy is now live! 🎉**

