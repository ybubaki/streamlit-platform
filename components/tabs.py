import streamlit as st
import pandas as pd
from .summary_tab import summary_view
from .financial_statement_tab import financial_statement_view
from .conpany_info_tab import company_info_view

def main_tabs():
    company_info_tab, trade_tab, pep_tab, crime_tab= st.tabs(["Company Info", "Trade", "PEP", "Crime"])

    with company_info_tab:
        company_info_view()
        sub_tabs()


def sub_tabs():
    summary_tab, finance_tab, ownership_tab, quantitative_tab = st.tabs(["Summary", "Financial statement", "Ownership", "Quantitative disclosure"])

    with summary_tab:
        summary_view()
    
    with finance_tab:
        financial_tabs()
        financial_statement_view()


def financial_tabs():
    cash_flow_tab, income_tab, balance_tab = st.tabs(["Cash flow", "Income statements", "Balance sheet"])

    with cash_flow_tab:
        cash_flow_data = {
            "Description": [
                "Net Income",
                "Depreciation & Amortization",
                "Change in Working Capital",
                "Cash from Operations",
                "Capital Expenditures",
                "Cash from Investing Activities",
                "Dividends Paid",
                "Cash from Financing Activities",
                "Net Change in Cash"
            ],
            "Amount": [
                "$120,000",
                "$30,000",
                "$10,000",
                "$160,000",
                "$-20,000",
                "$-10,000",
                "$-5,000",
                "$-15,000",
                "$110,000"
            ]
        }

        cash_flow_df = pd.DataFrame(cash_flow_data)

        st.markdown("### Cash Flow Statement")
        st.table(cash_flow_df)
        

    with income_tab:

        income_statement_data = {
            "Description": [
                "Revenue",
                "Cost of Goods Sold",
                "Gross Profit",
                "Operating Expenses",
                "Operating Income",
                "Other Income",
                "Net Income Before Tax",
                "Income Tax Expense",
                "Net Income"
            ],
            "Amount": [
                "$500,000",
                "$300,000",
                "$200,000",
                "$50,000",
                "$150,000",
                "$10,000",
                "$160,000",
                "$40,000",
                "$120,000"
            ]
        }

        income_statement_df = pd.DataFrame(income_statement_data)

        st.markdown("### Income Statement")
        st.table(income_statement_df)