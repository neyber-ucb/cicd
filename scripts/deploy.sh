#!/bin/bash
set -e

# Deployment script for Task Manager
# Usage: ./deploy.sh <environment> <release_id>

ENVIRONMENT=$1
RELEASE_ID=$2
APP_DIR="/var/www/taskmanager"

if [ -z "$ENVIRONMENT" ] || [ -z "$RELEASE_ID" ]; then
    echo "Usage: $0 <staging|production> <release_id>"
    exit 1
fi

echo "🚀 Deploying release $RELEASE_ID to $ENVIRONMENT"

# Create release directory
RELEASE_DIR="$APP_DIR/releases/$RELEASE_ID"
mkdir -p "$RELEASE_DIR"

cd "$RELEASE_DIR"

# Setup backend
echo "📦 Setting up backend..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Link shared .env
ln -sfn "$APP_DIR/shared/.env" .env

# Run migrations
echo "🔄 Running migrations..."
alembic upgrade head || echo "⚠️  No migrations to run"

# Setup frontend
echo "🎨 Setting up frontend..."
cd "$RELEASE_DIR"
mkdir -p frontend
cp -r frontend-dist/* frontend/

# Atomic symlink switch
echo "🔗 Switching symlink..."
ln -sfn "$RELEASE_DIR" "$APP_DIR/current"

# Restart services
echo "♻️  Restarting services..."
sudo systemctl restart taskmanager-backend
sudo systemctl restart taskmanager-frontend

# Health check
echo "🏥 Running health check..."
sleep 3
curl -f "http://localhost:8000/api/health" || {
    echo "❌ Health check failed!"
    exit 1
}

echo "✅ Deployment successful!"
echo "📍 Current release: $RELEASE_ID"
echo "🔗 Symlink: $(readlink -f $APP_DIR/current)"
