# intro-to-python

Introduction to Python course, part of the AI Academy

## How to run the notebooks

This repository contains Jupyter notebooks that teach Python fundamentals for data science and geoscience applications. Here are the different ways you can run them:

### Option 1: Local Installation (Recommended)

1. **Prerequisites**: Make sure you have Python 3.8+ installed
2. **Clone the repository**:
   ```bash
   git clone https://github.com/ingehap/intro-to-python.git
   cd intro-to-python
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Launch Jupyter**:
   ```bash
   jupyter notebook
   ```
5. **Navigate to the `course/` folder** and open any notebook (`.ipynb` file)

### Option 2: Using GitHub Codespaces

1. Click the green "Code" button on GitHub
2. Select "Codespaces" tab
3. Click "Create codespace on main"
4. Wait for the environment to load, then run:
   ```bash
   pip install -r requirements.txt
   jupyter notebook --allow-root
   ```

### Option 3: Using Dev Container (VS Code)

1. Open the repository in VS Code
2. Install the "Dev Containers" extension
3. Press `Ctrl+Shift+P` and select "Dev Containers: Reopen in Container"
4. Once loaded, the dependencies will be installed automatically
5. Open a terminal and run: `jupyter notebook --allow-root`

### Option 4: Google Colab

You can run individual notebooks in Google Colab by:
1. Uploading the `.ipynb` files to your Google Drive
2. Opening them with Google Colab
3. Note: You may need to install some packages by adding cells with `!pip install package_name`

## Course Content

The `course/` folder contains the following notebooks:

- **`Data.ipynb`** - Python fundamentals: collections, iteration, and NumPy basics
- **`Intro_to_Pandas_and_Series.ipynb`** - Introduction to Pandas Series
- **`Intro_to_Pandas_DataFrames.ipynb`** - Working with Pandas DataFrames
- **`Intro_to_Pandas_exercises.ipynb`** - Hands-on exercises with geoscience data
- **`Pandas_for_timeseries.ipynb`** - Time series analysis with Pandas
- **`Intro_to_matplotlib.ipynb`** - Data visualization with matplotlib

## Requirements

All required packages are listed in `requirements.txt`. Key dependencies include:
- Jupyter for running notebooks
- Pandas for data manipulation
- NumPy for numerical computing
- Matplotlib and Seaborn for plotting
- Various scientific computing packages

## Troubleshooting

**Problem**: Package installation fails
- **Solution**: Try updating pip: `pip install --upgrade pip` then retry

**Problem**: Jupyter won't start
- **Solution**: Make sure it's installed: `pip install jupyter` then try again

**Problem**: Import errors in notebooks
- **Solution**: Ensure all requirements are installed: `pip install -r requirements.txt`

**Problem**: Permission denied errors
- **Solution**: Try using virtual environment or use `pip install --user -r requirements.txt`

I recommend keeping your work in the `course` folder.
