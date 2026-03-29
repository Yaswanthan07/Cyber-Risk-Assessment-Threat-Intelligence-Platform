# Project Structure

CyberScan Pro has been converted from Jupyter Notebook to a professional Streamlit application with proper modular architecture.

## Directory Structure

```
CyberScan-Pro/
│
├── 📄 app.py                          # Main Streamlit application
├── 📋 README.md                       # Project documentation
├── 📝 CHANGELOG.md                    # Version history
├── 🤝 CONTRIBUTING.md                 # Contribution guidelines
├── 🚀 DEPLOYMENT.md                   # Deployment instructions
├── 📄 LICENSE                         # MIT License
│
├── 📦 requirements.txt                # Python dependencies
├── .env.example                       # Environment template (copy to .env)
├── .gitignore                         # Git ignore rules
├── streamlit.toml                     # Streamlit configuration
│
├── 🔧 setup.sh                        # Setup script (Linux/Mac)
├── 🔧 setup.bat                       # Setup script (Windows)
│
├── 📁 src/                            # Source code modules
│   ├── __init__.py                    # Package initializer
│   ├── config.py                      # Configuration management
│   ├── scanner.py                     # Nmap scanning functionality
│   ├── threat_intelligence.py         # VirusTotal & Shodan APIs
│   ├── risk_calculator.py             # Risk scoring logic
│   ├── alerter.py                     # Email alert system
│   └── utils.py                       # Utility functions
│
├── 📂 .github/
│   └── 📁 workflows/
│       └── code-quality.yml           # GitHub Actions CI/CD
│
├── 📂 scan_xml/                       # Nmap XML outputs (generated)
├── 📂 data/                           # Exported scan results (generated)
└── 📂 logs/                           # Application logs (generated)
```

## Module Descriptions

### Core Modules (`src/`)

#### `config.py`
- Centralized configuration management
- Environment variable loading from `.env` file
- API keys, targets, thresholds
- API key validation methods

#### `scanner.py`
- Nmap integration for network scanning
- XML parsing of Nmap output
- Support for multiple targets
- Error handling for network issues

#### `threat_intelligence.py`
- VirusTotal IP reputation checking
- Shodan vulnerability data retrieval
- Multi-threaded API calls
- Error handling and API rate limiting

#### `risk_calculator.py`
- Risk score calculation based on:
  - Service type
  - VirusTotal reputation
  - Shodan vulnerability count
- Severity assignment (Critical, High, Medium, Low)
- Risk summary statistics

#### `alerter.py`
- Email alert generation and sending
- HTML formatted security reports
- Gmail SMTP integration
- Error handling for email failures

#### `utils.py`
- Data file operations (save/load)
- DataFrame formatting for display
- Color and emoji utilities
- Session state management

### Main Application

#### `app.py`
- Streamlit dashboard interface
- Multi-tab layout with different views
- Real-time data visualization
- Interactive filtering and searching
- Data export functionality

## Key Features

### Scanning
```
Network Target → Nmap Scan → XML Output → Parser → DataFrame
```

### Threat Intelligence
```
IP Addresses → VirusTotal API → Reputation (Low/Med/High)
           ↓
           Shodan API → Vulnerability Count & Country
```

### Risk Assessment
```
Port Data + Service Type + VirusTotal + Shodan → Risk Calculator → Risk Score → Severity
```

### Alerting
```
High-Risk Findings → Email Formatter → SMTP → Email Alert
```

### Dashboard
```
Scan Results → Visualization → Multiple Views → Export Options
```

## Data Flow

```
1. User Action (Click "Run Scan")
   ↓
2. scanner.py: Run Nmap scans on targets
   ↓
3. scanner.py: Parse XML output to DataFrame
   ↓
4. threat_intelligence.py: Enrich with VirusTotal & Shodan data
   ↓
5. risk_calculator.py: Calculate risk scores and severity
   ↓
6. app.py: Display in Streamlit dashboard
   ↓
7. User can:
   - View analytics
   - Send email alerts (alerter.py)
   - Export data (utils.py)
   - Save results to disk
```

## Dependencies

See `requirements.txt` for complete list:

```
streamlit==1.28.1       # Web framework
pandas==2.1.0           # Data processing
plotly==5.17.0          # Visualizations
requests==2.31.0        # HTTP library
python-nmap==0.0.1      # Nmap integration
python-dotenv==1.0.0    # Environment variables
fpdf==1.7.2             # PDF generation (future use)
```

## Configuration Flow

```
.env file (secrets)
    ↓
config.py (loads environment variables)
    ↓
All modules (import from config)
```

## Usage Scenarios

### Scenario 1: Quick Scan
1. User clicks "Run Scan"
2. Nmap scans targets
3. Results displayed in dashboard
4. User reviews findings

### Scenario 2: Detailed Analysis
1. Run scan
2. Review risk scores
3. Check threat intelligence
4. Filter high-risk items
5. Send email alerts

### Scenario 3: Reporting
1. Run scan
2. Apply filters
3. Export to CSV/JSON
4. Generate report

## Security Considerations

### Sensitive Data
- API keys in `.env` (not in repo)
- Email credentials encrypted in transit
- No plaintext passwords logged

### Code Security
- Input validation for API calls
- Error handling for edge cases
- Rate limiting awareness
- Proper exception handling

### Deployment Security
- Environment variables from system
- HTTPS recommended in production
- IP whitelisting for access
- Scheduled backups of results

## Extension Points

Developers can extend by:

1. **Adding new threat intel sources**: Extend `threat_intelligence.py`
2. **Custom risk scoring**: Modify `risk_calculator.py`
3. **New alert methods**: Add to `alerter.py` (Slack, Teams, etc.)
4. **Database integration**: Extend `utils.py`
5. **New visualizations**: Add to `app.py` tabs
6. **Custom reports**: Create new export formats

## Testing Recommendations

When modifying code:

1. Test locally before pushing
2. Verify all imports work
3. Test with sample data
4. Check error handling
5. Validate API calls
6. Test email alerts

## Deploying to GitHub

1. Initialize git repo (if not already done)
2. Add all files
3. Create `.env` file (it will be in `.gitignore`)
4. Commit and push
5. Data files (scan results) are ignored by `.gitignore`

```bash
git init
git add .
git commit -m "Initial commit: Convert Jupyter notebook to Streamlit app"
git branch -M main
git remote add origin https://github.com/yourusername/CyberScan-Pro.git
git push -u origin main
```

---

For setup instructions, see [README.md](README.md)
For deployment options, see [DEPLOYMENT.md](DEPLOYMENT.md)
For contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md)
