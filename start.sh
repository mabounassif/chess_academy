#!/bin/bash

echo "🏁 Starting Chess Academy Odoo Setup..."
echo ""

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Start services
echo "🚀 Starting Docker containers..."
docker-compose up -d

# Wait for services to be ready
echo "⏳ Waiting for services to initialize..."
sleep 5

# Check if Odoo is running
if docker ps | grep -q chess_academy_odoo; then
    echo "✅ Odoo is running!"
    echo ""
    echo "🌐 Access Odoo at: http://localhost:8069"
    echo ""
    echo "📝 Next steps:"
    echo "   1. Open http://localhost:8069 in your browser"
    echo "   2. Create database with master password: admin123"
    echo "   3. Install required modules (see INSTALL.md)"
    echo ""
    echo "📖 Full documentation: README.md"
    echo ""
    echo "🛑 To stop: docker-compose down"
else
    echo "❌ Failed to start Odoo. Check logs with: docker-compose logs"
    exit 1
fi

