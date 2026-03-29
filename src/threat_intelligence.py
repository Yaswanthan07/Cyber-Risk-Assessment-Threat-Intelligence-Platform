"""
Threat Intelligence module
Integrates with VirusTotal and Shodan APIs
"""

import requests
import pandas as pd
from typing import Dict, Optional
from src.config import Config


def check_virustotal(ip: str) -> str:
    """
    Check IP reputation using VirusTotal API
    
    Args:
        ip (str): IP address to check
        
    Returns:
        str: Risk level - "Low", "Medium", "High", or "Unknown"
    """
    if not Config.VT_API_KEY:
        return "Unknown"
    
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": Config.VT_API_KEY}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            return "Unknown"
        
        data = response.json()
        malicious = data["data"]["attributes"]["last_analysis_stats"]["malicious"]
        
        if malicious > 5:
            return "High"
        elif malicious > 0:
            return "Medium"
        else:
            return "Low"
    
    except requests.exceptions.RequestException as e:
        print(f"✗ VirusTotal API error for {ip}: {e}")
        return "Unknown"


def check_shodan(ip: str) -> Dict[str, any]:
    """
    Check IP information using Shodan API
    
    Args:
        ip (str): IP address to check
        
    Returns:
        dict: Dictionary with shodan_country, shodan_vuln_count, and shodan_ports
    """
    default_response = {
        "shodan_country": "N/A",
        "shodan_vuln_count": 0,
        "shodan_ports": "N/A"
    }
    
    if not Config.SHODAN_API_KEY:
        return default_response
    
    url = f"https://api.shodan.io/shodan/host/{ip}?key={Config.SHODAN_API_KEY}"
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            return default_response
        
        data = response.json()
        
        # Extract country
        country = data.get("country_name", "Unknown")
        
        # Extract vulnerability count
        vulns = data.get("vulns", [])
        if isinstance(vulns, list):
            vuln_count = len(vulns)
        elif isinstance(vulns, dict):
            vuln_count = len(vulns.keys())
        else:
            vuln_count = 0
        
        # Extract ports
        ports = data.get("ports", [])
        shodan_ports = ", ".join(map(str, ports)) if ports else "N/A"
        
        return {
            "shodan_country": country,
            "shodan_vuln_count": vuln_count,
            "shodan_ports": shodan_ports
        }
    
    except requests.exceptions.RequestException as e:
        print(f"✗ Shodan API error for {ip}: {e}")
        return default_response


def enrich_with_threat_intelligence(df: pd.DataFrame) -> pd.DataFrame:
    """
    Enrich scan results with threat intelligence from VirusTotal and Shodan
    
    Args:
        df (pd.DataFrame): DataFrame with scan results
        
    Returns:
        pd.DataFrame: Enriched DataFrame with threat intelligence columns
    """
    if df.empty:
        return df
    
    # Check VirusTotal for each unique IP
    print("📊 Checking VirusTotal...")
    df["vt_reputation"] = df["ip"].apply(check_virustotal)
    
    # Check Shodan for each unique IP
    print("📊 Checking Shodan...")
    unique_ips = df["ip"].unique()
    shodan_results = []
    
    for i, ip in enumerate(unique_ips, 1):
        print(f"  [{i}/{len(unique_ips)}] Checking {ip}...")
        shodan_data = check_shodan(ip)
        shodan_results.append({"ip": ip, **shodan_data})
    
    df_shodan = pd.DataFrame(shodan_results)
    df = pd.merge(df, df_shodan, on="ip", how="left")
    
    # Fill missing values
    df = df.fillna({
        "shodan_country": "N/A",
        "shodan_vuln_count": 0,
        "shodan_ports": "N/A"
    })
    
    return df
