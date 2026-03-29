#!/bin/bash

# CyberScan Pro - Setup Script
# This script automates the setup process

set -e  # Exit on error

echo "🛡️  CyberScan Pro Setup"
echo "======================="
echo ""

# Check Python version
echo "✓ Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "✗ Python 3 is required but not installed."
    echo "  Please install Python 3.8 or higher"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "  Found Python $PYTHON_VERSION"
echo ""

# Check Nmap
echo "✓ Checking Nmap installation..."
if command -v nmap &> /dev/null; then
    NMAP_VERSION=$(nmap --version | head -1)
    echo "  Found $NMAP_VERSION"
else
    echo "⚠️  Nmap is not installed!"
    echo "  Installation instructions:"
    echo "  - Ubuntu/Debian: sudo apt-get install nmap"
    echo "  - macOS: brew install nmap"
    echo "  - Windows: Download from https://nmap.org/download.html"
    echo ""
    read -p "Continue without Nmap? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi
echo ""

# Create virtual environment
echo "✓ Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "  Virtual environment created in ./venv"
else
    echo "  Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate || . venv/Scripts/activate 2>/dev/null
echo "  Virtual environment activated"
echo ""

# Upgrade pip
echo "✓ Upgrading pip..."
pip install --quiet --upgrade pip
echo "  pip upgraded"
echo ""

# Install dependencies
echo "✓ Installing Python dependencies..."
pip install -r requirements.txt
echo "  Dependencies installed"
echo ""

# Setup environment file
echo "✓ Setting up environment configuration..."
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "  Created .env file from .env.example"
        echo "  ⚠️  IMPORTANT: Edit .env with your API keys!"
    else
        echo "  .env.example not found"
    fi
else
    echo "  .env already exists"
fi
echo ""

# Create necessary directories
echo "✓ Creating data directories..."
mkdir -p scan_xml data logs
echo "  Directories created: scan_xml/, data/, logs/"
echo ""

echo "=================================="
echo "✅ Setup Complete!"
echo "=================================="
echo ""
echo "Next steps:"
echo "1. Edit .env file with your API keys"
echo "2. Run: streamlit run app.py"
echo "3. Open browser to http://localhost:8501"
echo ""
echo "For more info, see README.md"
echo ""
