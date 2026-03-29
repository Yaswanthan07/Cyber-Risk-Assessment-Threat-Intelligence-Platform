"""
Network scanning module using Nmap
Handles nmap scans and XML parsing
"""

import os
import subprocess
import xml.etree.ElementTree as ET
import pandas as pd
from src.config import Config


def run_nmap_scan(targets: list = None) -> None:
    """
    Run Nmap scan on specified targets and save results as XML
    
    Args:
        targets (list): List of target hosts/IPs to scan. Defaults to Config.TARGETS
    """
    if targets is None:
        targets = Config.TARGETS
    
    # Create scan output directory if it doesn't exist
    os.makedirs(Config.SCAN_OUTPUT_DIR, exist_ok=True)
    
    for target in targets:
        output_file = os.path.join(Config.SCAN_OUTPUT_DIR, f"{target}.xml")
        
        cmd = [
            "nmap",
            "-sV",  # Service version detection
            "-oX",  # XML output
            output_file,
            target
        ]
        
        print(f"🔍 Scanning {target}...")
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"✓ Successfully scanned {target}")
        except subprocess.CalledProcessError as e:
            print(f"✗ Error scanning {target}: {e}")
        except FileNotFoundError:
            print("✗ Nmap not found. Please install nmap: apt-get install nmap")


def parse_nmap_xml(xml_file: str) -> list:
    """
    Parse Nmap XML output and extract host and port information
    
    Args:
        xml_file (str): Path to the Nmap XML output file
        
    Returns:
        list: List of dictionaries containing IP, port, and service info
    """
    results = []
    
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        for host in root.findall("host"):
            # Extract IP address
            address = host.find("address")
            if address is None:
                continue
            
            ip = address.get("addr")
            
            # Extract ports
            ports = host.find("ports")
            if ports is None:
                continue
            
            for port in ports.findall("port"):
                port_id = port.get("portid")
                
                # Extract service name
                service = port.find("service")
                service_name = service.get("name") if service is not None else "unknown"
                
                # Extract service version if available
                service_version = service.get("product", "") if service is not None else ""
                
                results.append({
                    "ip": ip,
                    "port": port_id,
                    "service": service_name,
                    "version": service_version
                })
    
    except ET.ParseError as e:
        print(f"✗ Error parsing {xml_file}: {e}")
    except FileNotFoundError:
        print(f"✗ File not found: {xml_file}")
    
    return results


def load_all_scan_results(targets: list = None) -> pd.DataFrame:
    """
    Load and combine scan results from all target files
    
    Args:
        targets (list): List of targets to load. Defaults to Config.TARGETS
        
    Returns:
        pd.DataFrame: Combined scan results
    """
    if targets is None:
        targets = Config.TARGETS
    
    all_results = []
    
    for target in targets:
        xml_file = os.path.join(Config.SCAN_OUTPUT_DIR, f"{target}.xml")
        
        if os.path.exists(xml_file):
            results = parse_nmap_xml(xml_file)
            all_results.extend(results)
        else:
            print(f"⚠️ Scan file not found for {target}: {xml_file}")
    
    if not all_results:
        return pd.DataFrame()
    
    df = pd.DataFrame(all_results)
    return df
