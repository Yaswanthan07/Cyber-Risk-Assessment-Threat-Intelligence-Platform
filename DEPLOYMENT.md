# Deployment Guide

This guide covers deploying CyberScan Pro to various platforms.

## Local Deployment

### Prerequisites
- Python 3.8+
- Nmap installed
- API keys configured

### Steps

1. **Clone repository**
   ```bash
   git clone https://github.com/yourusername/CyberScan-Pro.git
   cd CyberScan-Pro
   ```

2. **Setup environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run**
   ```bash
   streamlit run app.py
   ```

## Heroku Deployment

### Prerequisites
- Heroku account
- Heroku CLI installed
- Git repository

### Steps

1. **Create Procfile**
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Create .streamlit/config.toml**
   ```toml
   [client]
   showErrorDetails = false
   
   [logger]
   level = "error"
   ```

3. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

4. **Set environment variables**
   ```bash
   heroku config:set VT_API_KEY=your_key
   heroku config:set SHODAN_API_KEY=your_key
   heroku config:set SENDER_EMAIL=your_email
   heroku config:set APP_PASSWORD=your_password
   heroku config:set RECEIVER_EMAIL=recipient@gmail.com
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

## Docker Deployment

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install Nmap
RUN apt-get update && apt-get install -y nmap && rm -rf /var/lib/apt/lists/*

# Copy files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run

```bash
# Build image
docker build -t cyberscan-pro .

# Run container
docker run -p 8501:8501 \
  -e VT_API_KEY=your_key \
  -e SHODAN_API_KEY=your_key \
  -e SENDER_EMAIL=your_email \
  -e APP_PASSWORD=your_password \
  -e RECEIVER_EMAIL=recipient@gmail.com \
  cyberscan-pro
```

## AWS EC2 Deployment

### Steps

1. **Launch EC2 instance**
   - Ubuntu 22.04 LTS
   - t2.micro (free tier eligible)

2. **Connect and setup**
   ```bash
   sudo apt-get update
   sudo apt-get install -y python3-pip nmap git
   ```

3. **Clone and install**
   ```bash
   git clone https://github.com/yourusername/CyberScan-Pro.git
   cd CyberScan-Pro
   pip3 install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   nano .env  # Edit with your keys
   ```

5. **Run with nohup**
   ```bash
   nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 > app.log 2>&1 &
   ```

6. **Configure security group**
   - Allow inbound on port 8501
   - Restrict to your IP for security

## Railway.app Deployment

1. **Connect GitHub repository**
2. **Create project**
3. **Set environment variables**
4. **Deploy**

Railway automatically detects Python projects.

## Streamlit Cloud Deployment

### Steps

1. **Push to GitHub**
   ```bash
   git push origin main
   ```

2. **Go to https://streamlit.io/cloud**

3. **Click "New app"**

4. **Select repository and branch**

5. **Set secrets**
   - Go to app settings
   - Add API keys and credentials

6. **Deploy**

### Secrets Format in Streamlit Cloud

In the app settings, add:
```
VT_API_KEY = your_key
SHODAN_API_KEY = your_key
SENDER_EMAIL = your_email
APP_PASSWORD = your_password
RECEIVER_EMAIL = recipient@gmail.com
```

## Production Considerations

1. **Use reverse proxy** (Nginx/Apache)
2. **Enable HTTPS** (Let's Encrypt)
3. **Monitor logs** and errors
4. **Rate limit** API calls
5. **Cache results** when possible
6. **Backup scan data** regularly
7. **Use strong passwords** for email
8. **Monitor resource usage**

## Scaling Tips

1. **Cache threat intelligence** results
2. **Batch API calls** efficiently
3. **Use async requests** where possible
4. **Implement request queuing** for scans
5. **Monitor API rate limits**
6. **Optimize database queries**

---

For more help, check README.md or create a GitHub issue.
