FROM odoo:17.0

USER root

# Install PostgreSQL client for health checks
RUN apt-get update && apt-get install -y postgresql-client curl && rm -rf /var/lib/apt/lists/*

# Copy custom addons
COPY ./addons /mnt/extra-addons

# Copy entrypoint script (configuration passed via command-line args)
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set proper permissions
RUN chown -R odoo:odoo /mnt/extra-addons

USER odoo

# Expose port
EXPOSE 8069

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD curl -f http://localhost:8069/web/health || exit 1

# Use custom entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Start Odoo
CMD ["odoo"]

