# CyberScan Intelligence Dashboard

A comprehensive cybersecurity intelligence analysis and visualization dashboard built with Jupyter Notebook.

## 📋 Overview

CyberScan Intelligence Dashboard is a data-driven tool designed to analyze, process, and visualize cybersecurity intelligence data. This project leverages advanced analytics and interactive visualizations to provide insights into security threats and patterns.

## 🛠️ Technologies & Libraries Used

### Core Libraries
- **Jupyter Notebook** - Interactive notebook environment for analysis and visualization
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing and array operations
- **matplotlib** - Data visualization and plotting
- **seaborn** - Statistical data visualization
- **scikit-learn** - Machine learning algorithms and data processing
- **plotly** - Interactive visualizations
- **requests** - HTTP library for API interactions

## 📦 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Jupyter Notebook

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Yaswanthan07/CyberScan-Intelligence-Dashboard.git
   cd CyberScan-Intelligence-Dashboard
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```

4. **Install required libraries**
   ```bash
   pip install -r requirements.txt
   ```

   Or install individually:
   ```bash
   pip install jupyter pandas numpy matplotlib seaborn scikit-learn plotly requests beautifulsoup4 python-dotenv
   ```

## 🚀 Running the Dashboard

### Using Jupyter Notebook / Google Colab
1. Ensure you're in the project directory with the virtual environment activated
2. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
3. Open `CyberScan Intelligence Dashboard.ipynb` in your browser
4. Run all cells or execute cells individually using Shift+Enter

## 📊 Features

- **Data Analysis**: Comprehensive cybersecurity data analysis
- **Interactive Visualizations**: Dynamic charts and graphs using Plotly
- **Statistical Insights**: Advanced statistical analysis using scikit-learn
- **Data Processing**: Efficient data manipulation with pandas and numpy
- **Web Integration**: API connectivity for real-time threat data
- **Emailing System**: Every Full Scan will triger an automated emailing system.

## 📁 Project Structure

```
CyberScan-Intelligence-Dashboard/
├── CyberScan Intelligence Dashboard.ipynb  # Main notebook file
└── README.md                                # This file
```

## 📝 Usage Notes

- Ensure all dependencies are installed before running
- The notebook requires an active internet connection for API calls
- Large datasets may require additional memory
- Consider using JupyterLab for an enhanced notebook experience