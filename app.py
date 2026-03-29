"""
CyberScan Pro - Network Security Dashboard
A powerful tool for network reconnaissance, threat intelligence, and vulnerability assessment.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Import custom modules
from src.config import Config
from src.scanner import run_nmap_scan, load_all_scan_results
from src.threat_intelligence import enrich_with_threat_intelligence
from src.risk_calculator import assess_risks, get_risk_summary
from src.alerter import send_email_alert
from src.utils import (
    save_scan_results, 
    load_scan_results, 
    format_dataframe_for_display,
    get_severity_color,
    get_severity_emoji
)


# =============================
# Page Configuration
# =============================

st.set_page_config(
    page_title="CyberScan Pro",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .metric-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
    }
    .critical { color: #d32f2f; }
    .high { color: #f57c00; }
    .medium { color: #fbc02d; }
    .low { color: #388e3c; }
    </style>
    """, unsafe_allow_html=True)


# =============================
# Sidebar Configuration
# =============================

st.sidebar.title("⚙️ CyberScan Pro Controls")
st.sidebar.markdown("---")

# API Configuration Status
st.sidebar.header("🔑 API Configuration")
api_status = Config.validate_api_keys()

col1, col2 = st.sidebar.columns(2)
with col1:
    if api_status["vt_configured"]:
        st.success("✅ VirusTotal")
    else:
        st.error("❌ VirusTotal")
with col2:
    if api_status["shodan_configured"]:
        st.success("✅ Shodan")
    else:
        st.error("❌ Shodan")

if api_status["email_configured"]:
    st.sidebar.success("✉️ Email Alerts: Configured")
else:
    st.sidebar.warning("⚠️ Email Alerts: Not Configured")

st.sidebar.markdown("---")

# Scan Targets
with st.sidebar.expander("📍 Scan Targets", expanded=True):
    st.write("**Default Targets:**")
    for target in Config.TARGETS:
        st.write(f"• {target}")

st.sidebar.markdown("---")

# Scan Actions
st.sidebar.header("🔍 Scan Actions")

col1, col2 = st.sidebar.columns(2)

with col1:
    if st.button("▶️ Run Scan", use_container_width=True, key="run_scan"):
        with st.spinner("🔄 Running Nmap scans..."):
            run_nmap_scan(Config.TARGETS)
            
            # Load scan results
            df = load_all_scan_results(Config.TARGETS)
            
            if not df.empty:
                st.session_state["df"] = df
                st.success("✅ Scan completed!")
                st.rerun()
            else:
                st.error("❌ No scan results found")

with col2:
    if st.button("🔄 Refresh", use_container_width=True, key="refresh"):
        st.cache_data.clear()
        st.rerun()

# Load or create session data
if "df" not in st.session_state:
    st.session_state["df"] = load_all_scan_results(Config.TARGETS)


# =============================
# Main Content
# =============================

st.title("🛡️ CyberScan Pro")
st.markdown("**Network Reconnaissance • Threat Intelligence • Vulnerability Assessment**")
st.markdown("---")

# Get current data
df = st.session_state.get("df", pd.DataFrame())

# If data exists but not assessed, assess it
if not df.empty and "risk_score" not in df.columns:
    with st.spinner("📊 Enriching with threat intelligence..."):
        df = enrich_with_threat_intelligence(df)
        df = assess_risks(df)
        st.session_state["df"] = df

# Display metrics
if not df.empty:
    st.subheader("📈 Dashboard Overview")
    
    risk_summary = get_risk_summary(df)
    
    metric_cols = st.columns(5)
    
    with metric_cols[0]:
        st.metric("🌐 Total Hosts", df["ip"].nunique())
    
    with metric_cols[1]:
        st.metric("📡 Open Ports", len(df))
    
    with metric_cols[2]:
        st.metric("🔧 Services Found", df["service"].nunique())
    
    with metric_cols[3]:
        st.metric("🔥 Max Risk Score", f"{risk_summary['max_risk_score']:.0f}")
    
    with metric_cols[4]:
        high_risk = risk_summary["critical"] + risk_summary["high"]
        st.metric("⚠️ High-Risk", high_risk, delta=None, delta_color="inverse")
    
    st.markdown("---")
    
    # Risk distribution bar
    risk_cols = st.columns(4)
    with risk_cols[0]:
        st.metric("Critical", risk_summary["critical"], 
                 delta="🔴", delta_color="inverse")
    with risk_cols[1]:
        st.metric("High", risk_summary["high"], 
                 delta="🟠", delta_color="inverse")
    with risk_cols[2]:
        st.metric("Medium", risk_summary["medium"],
                 delta="🟡", delta_color="off")
    with risk_cols[3]:
        st.metric("Low", risk_summary["low"],
                 delta="🟢", delta_color="off")
    
    st.markdown("---")
    
    # Tabs for different views
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Risk Overview",
        "📋 Scan Results",
        "🚨 High-Risk Findings",
        "📈 Analytics",
        "💾 Export"
    ])
    
    # Tab 1: Risk Overview
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            # Risk Score Distribution
            fig = px.histogram(df, x="risk_score", nbins=20, 
                              title="Risk Score Distribution",
                              labels={"risk_score": "Risk Score", "count": "Number of Ports"})
            fig.update_traces(marker_color="#667eea")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Severity Distribution
            fig = px.pie(df, names="severity",
                        title="Vulnerability Severity Distribution",
                        color="severity",
                        color_discrete_map={
                            "Critical": "#d32f2f",
                            "High": "#f57c00",
                            "Medium": "#fbc02d",
                            "Low": "#388e3c"
                        })
            st.plotly_chart(fig, use_container_width=True)
    
    # Tab 2: All Scan Results
    with tab2:
        st.subheader("Full Scan Results")
        
        # Filters
        col1, col2, col3 = st.columns(3)
        
        with col1:
            selected_severity = st.multiselect(
                "Filter by Severity",
                options=df["severity"].unique(),
                default=df["severity"].unique()
            )
        
        with col2:
            selected_services = st.multiselect(
                "Filter by Service",
                options=df["service"].unique(),
                default=df["service"].unique()
            )
        
        with col3:
            min_risk = st.slider("Min Risk Score", 
                               min_value=int(df["risk_score"].min()),
                               max_value=int(df["risk_score"].max()),
                               value=int(df["risk_score"].min()))
        
        # Apply filters
        filtered_df = df[
            (df["severity"].isin(selected_severity)) &
            (df["service"].isin(selected_services)) &
            (df["risk_score"] >= min_risk)
        ]
        
        st.write(f"**Showing {len(filtered_df)} of {len(df)} entries**")
        
        # Display table
        display_df = format_dataframe_for_display(filtered_df)
        st.dataframe(display_df, use_container_width=True, height=400)
    
    # Tab 3: High-Risk Findings
    with tab3:
        st.subheader("⚠️ High & Critical Risk Findings")
        
        high_risk_df = df[df["severity"].isin(["High", "Critical"])]
        
        if not high_risk_df.empty:
            display_df = format_dataframe_for_display(high_risk_df)
            
            for idx, row in high_risk_df.iterrows():
                with st.expander(f"{get_severity_emoji(row['severity'])} {row['ip']}:{row['port']} - {row['service']}"):
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("IP Address", row['ip'])
                    col2.metric("Port", row['port'])
                    col3.metric("Service", row['service'])
                    col4.metric("Risk Score", row['risk_score'])
                    
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("VirusTotal", row.get('vt_reputation', 'Unknown'))
                    col2.metric("Shodan Vulns", row.get('shodan_vuln_count', 0))
                    col3.metric("Country", row.get('shodan_country', 'N/A'))
                    col4.metric("Severity", row['severity'])
            
            # Send alert button
            if st.button("📧 Send Email Alert", use_container_width=True):
                with st.spinner("Sending email alert..."):
                    result = send_email_alert(high_risk_df, "CyberScan Pro - Security Alert")
                    st.success(result)
        else:
            st.info("ℹ️ No high-risk findings detected. Your network is secure!")
    
    # Tab 4: Analytics
    with tab4:
        st.subheader("📊 Detailed Analytics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Top Services
            service_count = df["service"].value_counts().head(10)
            fig = px.bar(service_count, 
                        title="Top 10 Services by Port Count",
                        labels={"value": "Count", "index": "Service"})
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Risk by Service
            risk_by_service = df.groupby("service")["risk_score"].mean().sort_values(ascending=False).head(10)
            fig = px.bar(risk_by_service,
                        title="Top 10 Services by Avg Risk Score",
                        labels={"value": "Avg Risk Score", "index": "Service"})
            st.plotly_chart(fig, use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # VirusTotal Reputation Distribution
            vt_count = df["vt_reputation"].value_counts()
            fig = px.pie(vt_count,
                        title="IP Reputation Distribution (VirusTotal)",
                        names=vt_count.index,
                        values=vt_count.values)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Risk Score by Reputation
            risk_by_reputation = df.groupby("vt_reputation")["risk_score"].mean()
            fig = px.bar(risk_by_reputation,
                        title="Average Risk Score by VirusTotal Reputation",
                        labels={"value": "Avg Risk Score", "index": "Reputation"})
            st.plotly_chart(fig, use_container_width=True)
    
    # Tab 5: Export
    with tab5:
        st.subheader("💾 Export Data")
        
        export_df = format_dataframe_for_display(df)
        
        # CSV Export
        csv = export_df.to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name=f"cyberscan_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True
        )
        
        # JSON Export
        json_data = export_df.to_json(orient="records", indent=2)
        st.download_button(
            label="📥 Download JSON",
            data=json_data,
            file_name=f"cyberscan_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            use_container_width=True
        )
        
        # Save to data folder
        if st.button("💾 Save to Local Storage", use_container_width=True):
            save_scan_results(export_df)
            st.success("✅ Scan results saved to data folder!")

else:
    st.info("👋 Welcome to CyberScan Pro!")
    st.write("""
    ### Getting Started
    
    1. **Configure API Keys**: Set up VirusTotal and Shodan API keys in your `.env` file
    2. **Run Scan**: Click the "Run Scan" button to start network reconnaissance
    3. **Review Results**: Analyze findings across multiple views
    4. **Take Action**: Send alerts and export reports
    
    ### Features
    - 🔍 Network port scanning with Nmap
    - 📊 Threat intelligence integration (VirusTotal + Shodan)
    - 🎯 Automated risk scoring and severity assessment$$
    - 📧 Email alerts for high-risk findings
    - 📈 Comprehensive analytics and visualizations
    - 💾 Data export in multiple formats
    """)

st.sidebar.markdown("---")
st.sidebar.markdown(f"**Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
