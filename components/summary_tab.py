import streamlit as st

def summary_view():
    firmographics = {
        "Company Name": "Example Corp",
        "Industry": "Technology",
        "Location": "San Francisco, CA",
        "Founded": "2010",
        "Employees": 500,
        "Revenue": "$100M"
    }

    financial_statement = {
        "Total Assets": "$1,000,000",
        "Total Liabilities": "$400,000",
        "Equity": "$600,000",
        "Revenue": "$500,000",
        "Net Income": "$100,000"
    }

    ownership_summary = {
        "Major Shareholder": "John Doe",
        "Ownership Percentage": "25%",
        "Institutional Investors": "ABC Capital, XYZ Investments",
        "Total Shares Outstanding": "1,000,000",
        "Insider Ownership": "15%"
    }

    sections = [
        ("Company Firmographics", firmographics),
        ("Financial Statement", financial_statement),
        ("Ownership Summary", ownership_summary)
    ]

    for title, data in sections:
        with st.container(border=True):
            st.markdown(f"### {title}")
            for key, value in data.items():
                st.write(f"**{key}:** {value}")