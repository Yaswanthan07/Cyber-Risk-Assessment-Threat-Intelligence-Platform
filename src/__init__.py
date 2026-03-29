"""
CyberScan Pro - Network Security Dashboard
This file makes the src directory a Python package
"""

__version__ = "1.0.0"
__author__ = "CyberScan Team"
__description__ = "Network Reconnaissance, Threat Intelligence, and Vulnerability Assessment"

from src.config import Config
from src.scanner import run_nmap_scan, load_all_scan_results
from src.threat_intelligence import enrich_with_threat_intelligence, check_virustotal, check_shodan
from src.risk_calculator import assess_risks, get_risk_summary
from src.alerter import send_email_alert

__all__ = [
    "Config",
    "run_nmap_scan",
    "load_all_scan_results",
    "enrich_with_threat_intelligence",
    "check_virustotal",
    "check_shodan",
    "assess_risks",
    "get_risk_summary",
    "send_email_alert"
]
