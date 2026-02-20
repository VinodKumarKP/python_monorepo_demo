#!/bin/bash
set -e

# Configuration - Replace with your bucket name
BUCKET_NAME="your-my-company-packages-bucket"

echo "🚀 Starting build and publish process..."

# 1. Install s3pypi if not present
if ! command -v s3pypi &> /dev/null; then
    echo "📦 Installing s3pypi..."
    uv pip install s3pypi
fi

# 2. Clean previous builds
rm -rf dist/

# 3. Build all packages in the workspace
echo "🏗️ Building packages..."
uv build --all-packages

# 4. Upload to S3
# This creates the PEP 503 'simple' index structure in your bucket
echo "📤 Uploading to S3 bucket: $BUCKET_NAME..."
s3pypi --bucket "$BUCKET_NAME" --dist-path dist/ --put-index

echo "✅ Done! You can now install your packages using:"
echo "pip install <package-name> --extra-index-url https://$BUCKET_NAME.s3.amazonaws.com/"
