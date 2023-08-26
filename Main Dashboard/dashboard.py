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

class Dashboard(App):
    CSS_PATH = "dash_layout.css"

    def compose(self) -> ComposeResult:

        def on_mount(self) -> None:
            self.Header.styles.background = "#9932CC"
            
if __name__ == "__main__":
    app = Dashboard()
    app.run()
