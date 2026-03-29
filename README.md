# 🔐 Cyber Risk Assessment & Threat Intelligence Platform

An advanced Python-based cybersecurity project that performs automated vulnerability scanning, threat intelligence analysis, and risk assessment using real-world tools like Nmap, VirusTotal, and Shodan. The system also provides a visual dashboard and automated email alerts for high-risk findings.

---

## 🚀 Features

* 🔍 **Automated Network Scanning**

  * Uses Nmap to scan target systems
  * Extracts open ports, services, and vulnerabilities

* 🧠 **Threat Intelligence Integration**

  * VirusTotal API for IP reputation analysis
  * Shodan API for external exposure insights

* ⚠️ **Risk Scoring System**

  * Assigns risk scores based on detected services
  * Classifies severity levels (Low, Medium, High)

* 📊 **Interactive Dashboard**

  * Built using Streamlit
  * Visualizes scan results using Plotly charts

* 📧 **Email Alert System**

  * Sends alerts for high-risk vulnerabilities
  * Automated notification system

* 📁 **Data Processing**

  * Parses XML scan results
  * Converts data into structured Pandas DataFrames

---

## 🛠️ Tech Stack

* **Programming Language:** Python

* **Tools & Libraries:**

  * Nmap
  * Pandas
  * Streamlit
  * Plotly
  * Requests
  * XML Parsing (ElementTree)
  * SMTP (Email Alerts)

* **APIs Used:**

  * VirusTotal API
  * Shodan API

---

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

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/cyber-risk-platform.git
cd cyber-risk-platform
```

### 2. Install Dependencies

```bash
pip install pandas streamlit plotly requests python-nmap fpdf
```

### 3. Install Nmap

#### Linux:

```bash
sudo apt-get update
sudo apt-get install nmap
```

#### Windows:

Download and install from: https://nmap.org/download.html

---

## 🔑 API Configuration

Update the following variables in your code:

```python
VT_API_KEY = "your_virustotal_api_key"
SHODAN_API_KEY = "your_shodan_api_key"
```

---

## 🎯 How It Works

1. **Target Definition**

   * User provides target IP/domain

2. **Network Scanning**

   * Nmap scans the target system

3. **Data Extraction**

   * XML results are parsed into structured data

4. **Threat Intelligence**

   * VirusTotal checks malicious reputation
   * Shodan identifies exposed services

5. **Risk Assessment**

   * Risk scores are calculated
   * Severity classification is assigned

6. **Visualization**

   * Dashboard displays analytics using charts

7. **Alerting**

   * Email alerts sent for high-risk vulnerabilities

---

## 📊 Running the Dashboard

```bash
streamlit run dashboard.py
```

Optional (for public access):

```bash
cloudflared tunnel --url http://localhost:8501
```

---

## 📧 Email Alert Configuration

Update email credentials:

```python
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
RECEIVER_EMAIL = "receiver_email@gmail.com"
```

---

## ⚠️ Disclaimer

This project is intended for **educational and ethical cybersecurity purposes only**. Do not perform scans on systems without proper authorization.

---

## 📌 Future Enhancements

* 🤖 Machine Learning-based risk prediction
* 🌐 Real-time monitoring system
* 🔐 User authentication for dashboard
* ☁️ Cloud deployment (AWS / Azure)
* 🔗 Integration with additional threat intelligence APIs

---
