#!/bin/bash

# MSSQL MCP Server Installation Script

echo "🚀 Installing MSSQL MCP Server..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python $python_version is installed, but Python $required_version or higher is required."
    exit 1
fi

echo "✅ Python $python_version detected"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Make server executable
chmod +x src/server.py

echo "✅ Installation complete!"
echo ""
echo "📋 Next steps:"
echo "1. Copy env.example to .env and configure your database settings"
echo "2. Run the server with: python src/server.py"
echo "3. Or activate the virtual environment and run: source venv/bin/activate && python src/server.py"
echo ""
echo "📖 For Claude Desktop integration, see README.md" 