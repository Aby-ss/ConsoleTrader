import re
import requests
import asciichartpy

from rich import print, box
from rich.panel import Panel
from rich.layout import Layout
from rich.traceback import install
install(show_locals=True)

from textual.app import App, ComposeResult
from textual.containers import HorizontalScroll, VerticalScroll
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Placeholder, Static
from textual.widgets import Header, Footer

class Header(Placeholder):
    DEFAULT_CSS = """
    Header {
        height: 3;
        dock: top;
    }
    """
    
class Footer(Placeholder):
    DEFAULT_CSS = """
    Footer {
        height: 3;
        dock: bottom;
    }
    """

class ConsoleTrader(App):
    CSS_PATH = "layout.css"

    def compose(self) -> ComposeResult:
        
        # --------------------------------------------- Charts ---------------------------------------------
        
        base_url = 'https://www.alphavantage.co/query'
        function = 'TIME_SERIES_DAILY'
        output_size = 'compact'

        chart_params = {
            'function': function,
            'symbol': "AAPL",
            'outputsize': output_size,
            'apikey': "78H5RH2BRNG4G5Z6"
        }

        
        response = requests.get(base_url, params=chart_params)
        data = response.json()

        if 'Error Message' in data:
            print(f"Error: {data['Error Message']}")
        else:
            time_series = data['Time Series (Daily)']
            dates = []
            close_prices = []

            for date, values in time_series.items():
                dates.append(date)
                close_prices.append(float(values['4. close']))

            # Create and display ASCII chart
            chart = asciichartpy.plot(close_prices, {"width": 5, "height": 10, "format": "{:8.2f}"})
            # print(Panel(chart, title=f"Monthly Close Prices for {symbol}", border_style="bold white", box=box.SQUARE))
            
        # --------------------------------------------- Company Overview ---------------------------------------------
        
        company_overview_params = {
        'function': "OVERVIEW",
        'symbol': "AAPL",
        'apikey': "78H5RH2BRNG4G5Z6"
        }
            
        response = requests.get(base_url, params=company_overview_params)
        data = response.json()

        if 'Error Message' in data:
            print(f"Error: {data['Error Message']}")
        else:
            overview_text = ""
            for key, value in data.items():
                overview_text += f"{key}: {value}\n"

            # Extract important variables
            description = re.search(r"Description: (.+)", overview_text).group(1)
            sector = re.search(r"Sector: (.+)", overview_text).group(1)
            industry = re.search(r"Industry: (.+)", overview_text).group(1)
            name = re.search(r"Name: (.+)", overview_text).group(1)
            exchange = re.search(r"Exchange: (.+)", overview_text).group(1)
            currency = re.search(r"Currency: (.+)", overview_text).group(1)
            address = re.search(r"Address: (.+)", overview_text).group(1)
            asset_type = re.search(r"AssetType: (.+)", overview_text).group(1)
            
            company_overview = f"{name}\n\n{description}\n\n\nIndustry: {industry}\nSection: {sector}\nAddress: {address}\ncurrency: {currency}"
            
            
            def get_financial_data(function):
                base_url = 'https://www.alphavantage.co/query'

                params = {
                    'function': function,
                    'symbol': "AAPL",
                    'apikey': "78H5RH2BRNG4G5Z6"
                }

                try:
                    response = requests.get(base_url, params=params)
                    data = response.json()

                    if 'Error Message' in data:
                        print(f"Error: {data['Error Message']}")
                        return None
                    else:
                        return data

                except requests.exceptions.RequestException as e:
                    print(f"Error: {e}")
                    return None
            
            # --------------------------------------------- Balance Sheet ---------------------------------------------
            
            def balance_sheet(api_key, symbol):
                data = get_financial_data('BALANCE_SHEET')
                if data:
                    balance_sheet_data = data.get('annualReports', [])
                    if balance_sheet_data:
                        important_variables = (
                            balance_sheet_data[0].get('fiscalDateEnding', ''),
                            balance_sheet_data[0].get('totalAssets', ''),
                            balance_sheet_data[0].get('totalLiabilities', ''),
                            balance_sheet_data[0].get('totalEquity', ''),
                            balance_sheet_data[0].get('cashAndCashEquivalents', ''),
                            balance_sheet_data[0].get('grossProfit', '')
                        )
                        return important_variables
                    else:
                        print("Balance sheet data not available for this symbol.")
                        return None     
                           
            balance_sheet_data = balance_sheet("78H5RH2BRNG4G5Z6", "AAPL")
            if balance_sheet_data:

                fiscal_date_ending, total_assets, total_liabilities, total_equity, cash_and_equivalents, gross_profit = balance_sheet_data
            
                balance_sheet_variables_text = f"Fiscal Date Ending: {fiscal_date_ending}\nTotal Assets: {total_assets}\nTotal Liabilities: {total_liabilities}\nTotal Equity: {total_equity}\nCash and Cash Equivalents: {cash_and_equivalents}\nGross Profit: {gross_profit}"

            # --------------------------------------------- Cash Flow ---------------------------------------------
            
            def cash_flow(api_key, symbol):
                data = get_financial_data('CASH_FLOW')
                if data:
                    cash_flow_data = data.get('annualReports', [])
                    if cash_flow_data:
                        important_variables = (
                            cash_flow_data[0].get('fiscalDateEnding', ''),
                            cash_flow_data[0].get('operatingCashflow', ''),
                            cash_flow_data[0].get('investingCashflow', ''),
                            cash_flow_data[0].get('financingCashflow', ''),
                            cash_flow_data[0].get('freeCashflow', ''),
                            cash_flow_data[0].get('grossProfit', '')
                        )
                        return important_variables
                    else:
                        print("Cash flow data not available for this symbol.")
                        return None

            cash_flow_data = cash_flow("78H5RH2BRNG4G5Z6", "AAPL")
            if cash_flow_data:
                fiscal_date_ending, operating_cashflow, investing_cashflow, financing_cashflow, free_cashflow, gross_profit = cash_flow_data
                
                cash_flow_variables_text = f"Fiscal Date Ending: {fiscal_date_ending}\nOperating Cash Flow: {operating_cashflow}\nInvesting Cash Flow: {investing_cashflow}\nFinancing Cash Flow: {financing_cashflow}\nFree Cash Flow: {free_cashflow}\nGross Profit: {gross_profit}"

            # --------------------------------------------- Income Statement ---------------------------------------------
            
            def income_statement(api_key, symbol):
                data = get_financial_data('INCOME_STATEMENT')
                if data:
                    income_statement_data = data.get('annualReports', [])
                    if income_statement_data:
                        important_variables = (
                            income_statement_data[0].get('fiscalDateEnding', ''),
                            income_statement_data[0].get('totalRevenue', ''),
                            income_statement_data[0].get('netIncome', ''),
                            income_statement_data[0].get('operatingIncome', ''),
                            income_statement_data[0].get('grossProfit', '')
                        )
                        return important_variables
                    else:
                        print("Income statement data not available for this symbol.")
                        return None

            income_statement_data = income_statement("78H5RH2BRNG4G5Z6", "AAPL")
            if income_statement_data:
                fiscal_date_ending, total_revenue, net_income, operating_income, gross_profit = income_statement_data
                
                income_statement_variables_text = f"Fiscal Date Ending: {fiscal_date_ending}\nTotal Revenue: {total_revenue}\nNet Income: {net_income}\nOperating Income: {operating_income}\nGross Profit: {gross_profit}"


        chart_text = f"{chart}"
        company_overview_text = f"{company_overview}"
        balance_sheet_text = f"{balance_sheet_variables_text}"
        cash_flow_text = f"{cash_flow_variables_text}"
        income_statement_text = f"{income_statement_variables_text}"
        
        financial_statements = f"{balance_sheet}\n\n\n{income_statement_text}"
        
                
        yield Header("ConsoleTrader", classes="Header")
        yield Footer("Empowering Investments, Simplifying Decisions!")
        yield Horizontal(
            Vertical(
                Static(f"{chart_text}"),
                classes="column",
            ),
            Vertical(
                Static(f"{financial_statements}"),
                classes="column"
            )
        )
        yield Horizontal(
            Vertical(
                Static(f"{company_overview_text}"),
                classes="column",
            ),
            Vertical(
                Static("News/Events"),
                classes="column"
            )
        )
        
    
        def on_mount(self) -> None:
            self.Header.styles.background = "#9932CC"

if __name__ == "__main__":
    app = ConsoleTrader()
    app.run()
