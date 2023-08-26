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
    
        chart_text = "test"
        company_overview_text = "test"
        balance_sheet_text = "test"
        cash_flow_variables_text = "test"
        income_statement_text = "test"
        income_statement_variables_text = "test"
        
        yield Header("ConsoleTrader", classes="Header",)
        yield Footer("Empowering Investments, Simplifying Decisions!")
        yield Horizontal(
            Vertical(
                Static(f"{chart_text}"),
                Static(f"{company_overview_text}"),
                classes="column",
            ),
            Vertical(
                Static(f"{balance_sheet_text}"),
                Static(f"{cash_flow_variables_text}"),
                Static(f"{income_statement_variables_text}"),
                classes="column",
            ),
        )
    
        def on_mount(self) -> None:
            self.Header.styles.background = "#9932CC"

if __name__ == "__main__":
    app = ConsoleTrader()
    app.run()
