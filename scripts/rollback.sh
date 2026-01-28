#!/bin/bash
set -e

# Rollback script for Task Manager
# Usage: ./rollback.sh [release_id]

APP_DIR="/var/www/taskmanager"
TARGET_RELEASE=$1

cd "$APP_DIR/releases"

if [ -z "$TARGET_RELEASE" ]; then
    # Get previous release (second most recent)
    TARGET_RELEASE=$(ls -1dt */ | sed -n '2p' | tr -d '/')
    
    if [ -z "$TARGET_RELEASE" ]; then
        echo "❌ No previous release found"
        exit 1
    fi
    
    echo "🔄 Rolling back to previous release: $TARGET_RELEASE"
else
    echo "🔄 Rolling back to specified release: $TARGET_RELEASE"
    
    if [ ! -d "$TARGET_RELEASE" ]; then
        echo "❌ Release $TARGET_RELEASE not found"
        exit 1
    fi
fi

# Atomic symlink switch
echo "🔗 Switching symlink..."
ln -sfn "$APP_DIR/releases/$TARGET_RELEASE" "$APP_DIR/current"

# Restart services
echo "♻️  Restarting services..."
sudo systemctl restart taskmanager-backend
sudo systemctl restart taskmanager-frontend

# Health check
echo "🏥 Running health check..."
sleep 3
curl -f "http://localhost:8000/api/health" || {
    echo "❌ Health check failed after rollback!"
    exit 1
}

echo "✅ Rollback successful!"
echo "📍 Current release: $TARGET_RELEASE"
echo "🔗 Symlink: $(readlink -f $APP_DIR/current)"
