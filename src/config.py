"""
Configuration module for CyberScan Pro
Handles all environment variables and constants
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for CyberScan Pro"""
    
    # Scan Configuration
    TARGETS = [
        "testasp.vulnweb.com",
        "testphp.vulnweb.com",
        "zero.webappsecurity.com"
    ]
    SCAN_OUTPUT_DIR = "scan_xml"
    
    # API Keys (Load from environment variables for security)
    VT_API_KEY = os.getenv("VT_API_KEY", "")
    SHODAN_API_KEY = os.getenv("SHODAN_API_KEY", "")
    
    # Email Configuration
    SENDER_EMAIL = os.getenv("SENDER_EMAIL", "")
    APP_PASSWORD = os.getenv("APP_PASSWORD", "")
    RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL", "")
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    
    # Risk Assessment Configuration
    HIGH_RISK_SERVICES = {
        "ftp": 3,
        "telnet": 4,
        "ssh": 1
    }
    
    # Risk Score Thresholds
    CRITICAL_RISK_THRESHOLD = 8
    HIGH_RISK_THRESHOLD = 4
    MEDIUM_RISK_THRESHOLD = 2
    
    # Data storage
    DATA_DIR = "data"
    SCAN_RESULTS_FILE = os.path.join(DATA_DIR, "scan_results.csv")
    
    @staticmethod
    def validate_api_keys():
        """Validate that required API keys are configured"""
        return {
            "vt_configured": bool(Config.VT_API_KEY),
            "shodan_configured": bool(Config.SHODAN_API_KEY),
            "email_configured": bool(Config.SENDER_EMAIL and Config.APP_PASSWORD and Config.RECEIVER_EMAIL)
        }
