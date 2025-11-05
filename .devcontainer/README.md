# 🛠️ DevContainer Setup for Chess Academy

This devcontainer configuration allows you to develop the Chess Academy Odoo project in a fully containerized environment using Visual Studio Code.

## 🎯 What's Included

### Development Environment
- **Odoo 17** with development mode enabled
- **PostgreSQL 15** database
- **Python 3.11** with debugging support
- **Git** for version control
- **Vim** for quick edits
- Development tools: `pylint-odoo`, `debugpy`, `ipython`

### VS Code Extensions
Pre-installed extensions:
- Python language support with Pylance
- Python debugger
- Odoo snippets and syntax highlighting
- Jinja2 template support
- XML formatting
- Docker support

### Ports
Automatically forwarded ports:
- **8069**: Odoo web interface
- **5432**: PostgreSQL database
- **5678**: Python debugger (for remote debugging)

## 🚀 Getting Started

### Prerequisites
1. **Visual Studio Code** installed
2. **Docker Desktop** running
3. **Remote - Containers** extension installed in VS Code

### Open in DevContainer

#### Method 1: Command Palette
1. Open this project in VS Code
2. Press `F1` or `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
3. Type and select: **"Remote-Containers: Reopen in Container"**
4. Wait for the container to build and start (~5-10 minutes first time)

#### Method 2: Notification
1. Open this project in VS Code
2. Click **"Reopen in Container"** from the notification popup
3. Wait for initialization

### First Time Setup

Once the container is running:

1. **Open Terminal** in VS Code (`Ctrl+``)
2. **Verify Odoo is running:**
   ```bash
   ps aux | grep odoo
   ```
3. **Access Odoo:** Open http://localhost:8069 in your browser
4. **Create Database:**
   - Master Password: `admin123`
   - Database Name: `chess_academy_dev`
   - Load demo data: Optional

## 💻 Development Workflow

### File Structure
```
/mnt/extra-addons/          # Your custom modules (mounted)
├── chess_academy/          # Chess Academy module
│   ├── __manifest__.py
│   ├── models/
│   ├── views/
│   └── security/
```

### Making Changes

#### Edit Code
All files in the `addons/` directory are mounted and can be edited:
- Changes to `.py` files require Odoo restart (with `--dev=all` they auto-reload)
- Changes to `.xml` files require module upgrade
- Changes to `__manifest__.py` require module upgrade

#### Restart Odoo
```bash
# Inside the container
pkill odoo
odoo --dev=all
```

Or restart the container from VS Code:
- `F1` → "Remote-Containers: Rebuild Container"

#### Update/Upgrade Module
```bash
# Install/Upgrade Chess Academy module
odoo -d chess_academy_dev -u chess_academy --stop-after-init

# Or via Odoo UI:
# Apps → Chess Academy → Upgrade
```

### Debugging

#### Python Debugging
The devcontainer includes `debugpy` for debugging.

**Launch Configuration** (`.vscode/launch.json`):
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Odoo: Attach",
      "type": "python",
      "request": "attach",
      "port": 5678,
      "host": "localhost",
      "pathMappings": [
        {
          "localRoot": "${workspaceFolder}/addons",
          "remoteRoot": "/mnt/extra-addons"
        }
      ]
    }
  ]
}
```

To debug:
1. Set breakpoints in your Python code
2. Start Odoo with debugpy: `python -m debugpy --listen 0.0.0.0:5678 /usr/bin/odoo`
3. Attach debugger from VS Code (F5)

#### View Logs
```bash
# Inside container terminal
tail -f /var/log/odoo/odoo.log

# Or check Docker logs
docker logs -f chess_academy_odoo_dev
```

## 🔧 Common Tasks

### Install Python Packages
```bash
# Inside container
pip install --user package-name
```

### Access PostgreSQL
```bash
# Inside container
psql -h postgres -U odoo -d chess_academy_dev
```

### Run Odoo Commands
```bash
# List databases
odoo --list-databases

# Initialize module
odoo -d chess_academy_dev -i chess_academy --stop-after-init

# Update module
odoo -d chess_academy_dev -u chess_academy --stop-after-init

# Run with dev mode (auto-reload)
odoo --dev=all

# Run with specific log level
odoo --log-level=debug
```

### Database Management
```bash
# Backup database
pg_dump -h postgres -U odoo chess_academy_dev > backup.sql

# Restore database
psql -h postgres -U odoo chess_academy_dev < backup.sql

# Drop and recreate database
dropdb -h postgres -U odoo chess_academy_dev
createdb -h postgres -U odoo chess_academy_dev
```

## 📂 Devcontainer Files

- `.devcontainer/devcontainer.json` - Main devcontainer configuration
- `.devcontainer/docker-compose.dev.yml` - Docker Compose for development
- `Dockerfile.dev` - Development Docker image with extra tools

## 🔍 Troubleshooting

### Container Won't Start
```bash
# Clean up containers
docker-compose -f .devcontainer/docker-compose.dev.yml down -v

# Rebuild container
F1 → "Remote-Containers: Rebuild Container"
```

### Port Already in Use
Stop the production containers first:
```bash
docker-compose down
```

### Module Not Loading
1. Check if module is in `/mnt/extra-addons`
2. Update apps list: Settings → Apps → Update Apps List
3. Check Odoo logs for errors

### Permission Issues
```bash
# Inside container, fix permissions
sudo chown -R odoo:odoo /mnt/extra-addons
```

## 🎓 Tips & Best Practices

### 1. Development Mode
The devcontainer runs Odoo with `--dev=all` which enables:
- Auto-reload on Python file changes
- Better error messages
- Debug mode
- Asset auto-compilation

### 2. Code Quality
Use the pre-installed linting:
```bash
pylint --load-plugins=pylint_odoo addons/chess_academy
```

### 3. Testing
```bash
# Run tests for your module
odoo -d chess_academy_dev -u chess_academy --test-enable --stop-after-init
```

### 4. Git Workflow
Git is available in the container:
```bash
git status
git add .
git commit -m "Your message"
git push
```

### 5. Multiple Databases
You can create multiple databases for different testing scenarios:
- `chess_academy_dev` - Main development
- `chess_academy_test` - Testing
- `chess_academy_demo` - Demo with sample data

## 📚 Resources

- [VS Code DevContainers Docs](https://code.visualstudio.com/docs/remote/containers)
- [Odoo Development Documentation](https://www.odoo.com/documentation/17.0/developer.html)
- [Docker Compose Reference](https://docs.docker.com/compose/)

## 🆘 Getting Help

If you encounter issues:
1. Check Odoo logs: `docker logs chess_academy_odoo_dev`
2. Check PostgreSQL: `docker logs chess_academy_db_dev`
3. Rebuild container: `F1` → "Rebuild Container"
4. Clean restart: Stop containers, delete volumes, rebuild

---

**Happy Coding! 🎉**


