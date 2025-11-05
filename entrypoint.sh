#!/bin/bash
set -e

# Start Odoo with command-line arguments for Railway
# This bypasses the config file variable substitution issue
exec odoo \
  --addons-path=/mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons \
  --data-dir=/var/lib/odoo \
  --db_host="${PGHOST}" \
  --db_port="${PGPORT}" \
  --db_user="${PGUSER}" \
  --db_password="${PGPASSWORD}" \
  --database="${PGDATABASE}" \
  --db_sslmode=require \
  --limit-time-cpu=600 \
  --limit-time-real=1200 \
  --max-cron-threads=1 \
  --workers=2 \
  --log-level=info \
  --xmlrpc-port=8069 \
  --proxy-mode \
  --no-database-list \
  "$@"

