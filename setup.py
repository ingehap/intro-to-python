#!/usr/bin/env python3
"""
Simple setup script to help users get started with the intro-to-python notebooks.
"""

import subprocess
import sys
import os

def run_command(cmd):
    """Run a command and return True if successful"""
    try:
        subprocess.run(cmd, check=True, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("🐍 Setting up intro-to-python environment...")
    print("=" * 50)
    
    # Check Python version
    python_version = sys.version_info
    print(f"✓ Python {python_version.major}.{python_version.minor}.{python_version.micro} detected")
    
    if python_version < (3, 8):
        print("❌ Python 3.8+ is required. Please upgrade Python.")
        sys.exit(1)
    
    # Install requirements
    print("\n📦 Installing required packages...")
    if run_command("pip install -r requirements.txt"):
        print("✓ All packages installed successfully!")
    else:
        print("❌ Failed to install some packages. Try manually: pip install -r requirements.txt")
        print("   Or try: pip install --user -r requirements.txt")
        return
    
    # Check if in course directory
    if not os.path.exists("course"):
        print("\n📁 Navigate to the course directory to find the notebooks")
    else:
        print(f"\n📚 Found {len([f for f in os.listdir('course') if f.endswith('.ipynb')])} notebooks in course/ directory")
    
    print("\n🚀 Setup complete! To start:")
    print("   1. Run: jupyter notebook")
    print("   2. Navigate to the 'course' folder")
    print("   3. Open any .ipynb file to start learning!")
    print("\n💡 Tip: Start with 'Data.ipynb' for Python fundamentals")

if __name__ == "__main__":
    main()