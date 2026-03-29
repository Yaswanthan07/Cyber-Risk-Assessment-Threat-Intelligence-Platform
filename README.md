# CyberScan Pro

A powerful and comprehensive **Network Security Dashboard** for reconnaissance, threat intelligence, and vulnerability assessment.

## 🎯 Features

- **🔍 Network Scanning**: Automated Nmap scanning for port and service discovery
- **🛡️ Threat Intelligence**: Integration with VirusTotal & Shodan APIs
- **📊 Risk Assessment**: Intelligent risk scoring and severity assignment
- **📧 Security Alerts**: Automated email notifications for high-risk findings
- **📈 Analytics Dashboard**: Comprehensive visualizations and reporting
- **💾 Data Export**: Multiple export formats (CSV, JSON)
- **🎨 Modern UI**: Interactive Streamlit dashboard with real-time updates

## 📋 Requirements

- Python 3.8+
- Nmap (system dependency)
- API Keys:
  - VirusTotal API (free tier available)
  - Shodan API (free tier available)
- Email account (for alerts, tested with Gmail)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/CyberScan-Pro.git
cd CyberScan-Pro
```

### 2. Create Virtual Environment

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install Python packages
pip install -r requirements.txt

# Install Nmap (system dependency)
# Ubuntu/Debian
sudo apt-get install nmap

# macOS (with Homebrew)
brew install nmap

# Windows - Download from https://nmap.org/download.html
```

### 4. Configure API Keys

```bash
# Copy the example configuration
cp .env.example .env

# Edit .env with your API keys and credentials
nano .env
```

**Required API Keys:**

1. **VirusTotal API**
   - Sign up: https://www.virustotal.com/gui/home/upload
   - Free tier provides 4 requests/minute

2. **Shodan API**
   - Sign up: https://www.shodan.io/
   - Free tier provides 1 query/month

3. **Gmail App Password** (for email alerts)
   - Enable 2FA on your Google account
   - Generate app password: https://myaccount.google.com/apppasswords

### 5. Run the Application

```bash
streamlit run app.py
```

The dashboard will open at `http://localhost:8501`

## 📁 Project Structure

```
CyberScan-Pro/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── streamlit.toml             # Streamlit configuration
├── README.md                  # This file
│
├── src/                       # Source code modules
│   ├── __init__.py
│   ├── config.py             # Configuration management
│   ├── scanner.py            # Nmap scanning functionality
│   ├── threat_intelligence.py # VirusTotal & Shodan integration
│   ├── risk_calculator.py    # Risk scoring logic
│   ├── alerter.py            # Email alert system
│   └── utils.py              # Utility functions
│
├── scan_xml/                 # Nmap scan output (XML files)
├── data/                     # Exported scan results (CSV/JSON)
└── logs/                     # Application logs
```

## 💻 Usage Guide

### Running a Network Scan

1. Click **"Run Scan"** in the sidebar
2. Select targets or use default targets
3. Wait for scan to complete (time depends on number of targets)
4. View results in the dashboard

### Understanding Risk Scores

Risk scores are calculated based on:
- **Open Port**: Base risk of 1
- **Service Type**: FTP (+3), Telnet (+4), SSH (+1)
- **VirusTotal Reputation**: Medium (+2), High (+4)
- **Shodan Vulnerabilities**: +1 per vulnerability (capped at 5)

**Severity Levels:**
- **Critical** 🔴 - VT High + Risk Score ≥ 6
- **High** 🟠 - VT High OR Risk Score ≥ 4
- **Medium** 🟡 - VT Medium OR Risk Score ≥ 2
- **Low** 🟢 - Everything else

### Sending Security Alerts

1. Review **"High-Risk Findings"** tab
2. Click **"Send Email Alert"** button
3. Verify email delivery to configured recipient

### Exporting Data

- Download as **CSV** for spreadsheet analysis
- Download as **JSON** for API integration
- Save to **Local Storage** for archival

## 🔐 Security Best Practices

1. **Never commit API keys** - Use `.env` file (already in `.gitignore`)
2. **Use environment variables** - All sensitive data loaded from `.env`
3. **Restrict file permissions** - Limit access to scan results
4. **Regular backups** - Save important scan reports
5. **Keep dependencies updated** - Run `pip install --upgrade -r requirements.txt`

## 🔧 Configuration Options

Edit `src/config.py` to customize:

```python
# Default scan targets
TARGETS = ["target1.com", "target2.com"]

# Risk scoring thresholds
CRITICAL_RISK_THRESHOLD = 8
HIGH_RISK_THRESHOLD = 4

# High-risk services
HIGH_RISK_SERVICES = {
    "ftp": 3,
    "telnet": 4,
    "ssh": 1
}
```

## 📊 Dashboard Tabs

### 📊 Risk Overview
- Risk score distribution histogram
- Vulnerability severity pie chart

### 📋 Scan Results
- Full table of all found ports
- Filter by severity, service, risk score
- Sort and search capabilities

### 🚨 High-Risk Findings
- Detailed view of critical and high-risk entries
- Send email alerts directly to stakeholders
- Expandable details for each finding

### 📈 Analytics
- Top 10 services by port count
- Services ranked by average risk score
- VirusTotal reputation distribution
- Risk score correlation analysis

### 💾 Export
- Download results in CSV format
- Download results in JSON format
- Save to local database for archival

## 🐛 Troubleshooting

### Nmap not found
```bash
# Linux
sudo apt-get install nmap

# macOS
brew install nmap

# Windows - Download from https://nmap.org/download.html
```

### API Key errors
- Verify API keys in `.env` file
- Check API quotas and rate limits
- Test API keys independently

### Email alert failures
- Enable 2FA on Gmail account
- Generate new app password
- Check firewall/proxy settings

### Streamlit port already in use
```bash
streamlit run app.py --server.port 8502
```

## 📝 Example Workflow

```
1. Clone repository & setup environment
2. Configure API keys in .env
3. Run: streamlit run app.py
4. Click "Run Scan" button
5. Review findings in dashboard
6. Send email alerts for high-risk entries
7. Export results for reporting
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

CyberScan Pro is designed for **authorized security testing only**. Users are responsible for:
- Obtaining proper authorization before scanning networks
- Complying with all applicable laws and regulations
- Using this tool ethically and responsibly

Unauthorized network scanning may be illegal. Always get written permission before testing.

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review troubleshooting section

## 🙏 Acknowledgments

- Nmap - Network scanning
- VirusTotal - IP reputation checking
- Shodan - Internet-connected device search
- Streamlit - Interactive dashboard framework
- Plotly - Data visualization

---

**Made with ❤️ for cybersecurity professionals**
