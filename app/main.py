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
        
        yield Header("ConsoleTrader", classes="Header")
        yield Footer("Empowering Investments, Simplifying Decisions!")
        yield Horizontal(
            Vertical(
                Static("Chart"),
                classes="column",
            ),
            Vertical(
                Static("Income Statement"),
                classes="column"
            )
        )
        yield Horizontal(
            Vertical(
                Static("Enterprise Information"),
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
