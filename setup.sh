#!/bin/bash
# Simple setup script for intro-to-python

echo "🐍 Setting up intro-to-python environment..."
echo "================================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check Python version
python_version=$(python3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
echo "✓ Python $python_version detected"

# Install requirements
echo ""
echo "📦 Installing required packages..."
if python3 -m pip install -r requirements.txt; then
    echo "✓ All packages installed successfully!"
else
    echo "❌ Failed to install packages. Try:"
    echo "   pip install --user -r requirements.txt"
    echo "   or"
    echo "   python3 -m pip install --user -r requirements.txt"
    exit 1
fi

# Check for notebooks
if [ -d "course" ]; then
    notebook_count=$(find course -name "*.ipynb" | wc -l)
    echo "📚 Found $notebook_count notebooks in course/ directory"
fi

echo ""
echo "🚀 Setup complete! To start:"
echo "   1. Run: jupyter notebook"
echo "   2. Navigate to the 'course' folder"  
echo "   3. Open any .ipynb file to start learning!"
echo ""
echo "💡 Tip: Start with 'Data.ipynb' for Python fundamentals"