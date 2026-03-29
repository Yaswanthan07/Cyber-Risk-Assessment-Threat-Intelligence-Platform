"""
Risk assessment and calculation module
Calculates risk scores and assigns severity levels
"""

import pandas as pd
from src.config import Config


def calculate_risk_score(row: pd.Series) -> int:
    """
    Calculate risk score based on multiple factors
    
    Args:
        row (pd.Series): DataFrame row with scan and threat intel data
        
    Returns:
        int: Risk score
    """
    score = 1  # Base score
    
    # Add points for high-risk services
    if row["service"] in Config.HIGH_RISK_SERVICES:
        score += Config.HIGH_RISK_SERVICES[row["service"]]
    
    # Add points based on Shodan vulnerability count
    if "shodan_vuln_count" in row and row["shodan_vuln_count"] > 0:
        score += min(row["shodan_vuln_count"], 5)  # Cap at 5 points
    
    # Add points based on VirusTotal reputation
    if row.get("vt_reputation") == "Medium":
        score += 2
    elif row.get("vt_reputation") == "High":
        score += 4
    
    return score


def assign_severity(row: pd.Series) -> str:
    """
    Assign severity level based on risk score and threat intel
    
    Args:
        row (pd.Series): DataFrame row with risk_score and vt_reputation
        
    Returns:
        str: Severity level - "Critical", "High", "Medium", or "Low"
    """
    risk_score = row.get("risk_score", 0)
    vt_reputation = row.get("vt_reputation", "Low")
    
    # Critical threshold
    if vt_reputation == "High" and risk_score >= 6:
        return "Critical"
    
    # High threshold
    if vt_reputation == "High" or risk_score >= Config.HIGH_RISK_THRESHOLD:
        return "High"
    
    # Medium threshold
    if vt_reputation == "Medium" or risk_score >= Config.MEDIUM_RISK_THRESHOLD:
        return "Medium"
    
    return "Low"


def assess_risks(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform full risk assessment on scan results
    
    Args:
        df (pd.DataFrame): DataFrame with scan and threat intel data
        
    Returns:
        pd.DataFrame: DataFrame with risk_score and severity columns added
    """
    if df.empty:
        return df
    
    print("⚠️ Calculating risk scores...")
    df["risk_score"] = df.apply(calculate_risk_score, axis=1)
    
    print("🎯 Assigning severity levels...")
    df["severity"] = df.apply(assign_severity, axis=1)
    
    return df


def get_risk_summary(df: pd.DataFrame) -> dict:
    """
    Generate a summary of risk statistics
    
    Args:
        df (pd.DataFrame): Assessed DataFrame
        
    Returns:
        dict: Risk summary statistics
    """
    if df.empty:
        return {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "total": 0,
            "avg_risk_score": 0
        }
    
    return {
        "critical": len(df[df["severity"] == "Critical"]),
        "high": len(df[df["severity"] == "High"]),
        "medium": len(df[df["severity"] == "Medium"]),
        "low": len(df[df["severity"] == "Low"]),
        "total": len(df),
        "avg_risk_score": df["risk_score"].mean(),
        "max_risk_score": df["risk_score"].max()
    }
