"""
Utility functions for CyberScan Pro
"""

import os
import pandas as pd
from datetime import datetime
from src.config import Config


def ensure_data_dir():
    """Ensure data directory exists"""
    os.makedirs(Config.DATA_DIR, exist_ok=True)


def save_scan_results(df: pd.DataFrame, filename: str = None) -> str:
    """
    Save scan results to CSV file
    
    Args:
        df (pd.DataFrame): Scan results to save
        filename (str): Custom filename. Defaults to scan_results.csv
        
    Returns:
        str: Path to saved file
    """
    ensure_data_dir()
    
    if filename is None:
        filename = f"scan_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    filepath = os.path.join(Config.DATA_DIR, filename)
    df.to_csv(filepath, index=False)
    print(f"💾 Scan results saved: {filepath}")
    return filepath


def load_scan_results(filename: str = None) -> pd.DataFrame:
    """
    Load scan results from CSV file
    
    Args:
        filename (str): Filename to load. Defaults to latest or scan_results.csv
        
    Returns:
        pd.DataFrame: Loaded scan results
    """
    ensure_data_dir()
    
    if filename is None:
        filename = "scan_results.csv"
    
    filepath = os.path.join(Config.DATA_DIR, filename)
    
    if not os.path.exists(filepath):
        return pd.DataFrame()
    
    try:
        df = pd.read_csv(filepath)
        # Convert numeric columns
        for col in ["port", "risk_score", "shodan_vuln_count"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        print(f"📂 Loaded scan results: {filepath}")
        return df
    except Exception as e:
        print(f"✗ Error loading file: {e}")
        return pd.DataFrame()


def get_latest_scan_file() -> str:
    """
    Get the latest scan results file
    
    Returns:
        str: Path to latest scan file or None
    """
    ensure_data_dir()
    
    files = [f for f in os.listdir(Config.DATA_DIR) if f.startswith("scan_results_") and f.endswith(".csv")]
    
    if not files:
        return None
    
    files.sort(reverse=True)
    return os.path.join(Config.DATA_DIR, files[0])


def format_dataframe_for_display(df: pd.DataFrame) -> pd.DataFrame:
    """
    Format DataFrame for Streamlit display
    
    Args:
        df (pd.DataFrame): DataFrame to format
        
    Returns:
        pd.DataFrame: Formatted DataFrame
    """
    if df.empty:
        return df
    
    # Create a copy to avoid modifying original
    display_df = df.copy()
    
    # Reorder columns for better display
    column_order = ["ip", "port", "service", "version", "vt_reputation", 
                    "shodan_country", "shodan_vuln_count", "risk_score", "severity"]
    
    existing_cols = [col for col in column_order if col in display_df.columns]
    other_cols = [col for col in display_df.columns if col not in existing_cols]
    
    display_df = display_df[existing_cols + other_cols]
    
    return display_df


def get_severity_color(severity: str) -> str:
    """
    Get color for severity level for UI display
    
    Args:
        severity (str): Severity level
        
    Returns:
        str: Color code
    """
    colors = {
        "Critical": "#d32f2f",  # Red
        "High": "#f57c00",      # Orange
        "Medium": "#fbc02d",    # Yellow
        "Low": "#388e3c"        # Green
    }
    return colors.get(severity, "#999999")


def get_severity_emoji(severity: str) -> str:
    """
    Get emoji for severity level
    
    Args:
        severity (str): Severity level
        
    Returns:
        str: Emoji
    """
    emojis = {
        "Critical": "🔴",
        "High": "🟠",
        "Medium": "🟡",
        "Low": "🟢"
    }
    return emojis.get(severity, "⚫")
