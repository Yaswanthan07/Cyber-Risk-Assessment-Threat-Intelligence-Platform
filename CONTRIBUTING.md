# Contributing to CyberScan Pro

Thank you for your interest in contributing to CyberScan Pro! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Report security vulnerabilities responsibly
- Keep discussions constructive and professional

## How to Contribute

### Reporting Bugs

1. Check if the issue already exists
2. Provide detailed reproduction steps
3. Include environment information (OS, Python version, etc.)
4. Attach screenshots or error messages if applicable

### Suggesting Enhancements

1. Clearly describe the enhancement
2. Explain the use case and benefits
3. Provide examples if possible

### Code Contributions

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/CyberScan-Pro.git
   cd CyberScan-Pro
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Follow coding standards**
   - Use PEP 8 style guide
   - Add docstrings to functions
   - Keep functions focused and modular
   - Add type hints where appropriate

4. **Test your changes**
   ```bash
   # Run the app locally
   streamlit run app.py
   ```

5. **Commit with clear messages**
   ```bash
   git commit -m "Add detailed description of changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Describe what you've changed
   - Reference any related issues
   - Test in the provided environment

## Code Style

### Python Style Guide

```python
# ✅ Good
def scan_network(targets: list, timeout: int = 30) -> pd.DataFrame:
    """
    Scan a list of network targets.
    
    Args:
        targets (list): List of target hosts/IPs
        timeout (int): Scan timeout in seconds
        
    Returns:
        pd.DataFrame: Scan results
    """
    # Implementation here
    pass

# ❌ Avoid
def scan(targets, timeout=30):
    # No docstring
    # No type hints
    pass
```

## Project Structure

- `src/` - Core modules
  - `config.py` - Configuration management
  - `scanner.py` - Network scanning
  - `threat_intelligence.py` - API integrations
  - `risk_calculator.py` - Risk assessment
  - `alerter.py` - Email notifications
  - `utils.py` - Utilities
- `app.py` - Main Streamlit application
- `requirements.txt` - Dependencies
- `README.md` - Documentation

## Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env with your API keys
nano .env

# Run the app
streamlit run app.py
```

## Testing

Before submitting a PR:

1. Test the app locally with different targets
2. Verify API integrations work correctly
3. Test email alerts functionality
4. Check error handling and edge cases
5. Ensure no sensitive data is logged

## Documentation

- Update `README.md` for user-facing changes
- Add docstrings to new functions
- Include comments for complex logic
- Update this file if guidelines change

## Security Considerations

- Never commit API keys or passwords
- Use environment variables for sensitive data
- Validate user inputs
- Handle API errors gracefully
- Log securely without exposing sensitive info

## Release Process

1. Update version in `src/__init__.py`
2. Update CHANGELOG (if maintained)
3. Create a git tag
4. Push to main repository
5. Create GitHub Release

## Questions?

- Open a discussion in GitHub Issues
- Check existing documentation first
- Be patient and respectful with responses

---

Thank you for making CyberScan Pro better! 🎉
