#!/bin/bash
# Script to use sample data for quick testing

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -f "$SCRIPT_DIR/mrds.geojson" ]; then
    echo "⚠️  Warning: mrds.geojson already exists!"
    echo "This script will overwrite it with sample data."
    read -p "Continue? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Cancelled."
        exit 1
    fi
fi

echo "📋 Copying sample data to mrds.geojson..."
cp "$SCRIPT_DIR/mrds_sample.geojson" "$SCRIPT_DIR/mrds.geojson"

if [ $? -eq 0 ]; then
    echo "✅ Sample data installed successfully!"
    echo "   You can now run: python3 -m http.server 8000"
    echo "   Then open: http://localhost:8000"
    echo ""
    echo "📝 Note: This is sample data with only 10 points for testing."
    echo "   To use full USGS MRDS data (304,613 points), follow instructions in data/README.md"
else
    echo "❌ Error copying sample data"
    exit 1
fi
