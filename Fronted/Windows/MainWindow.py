# ╔═════════════════════════════════╗
# ║         📁 Python Project 📁
# ║
# ║  ✨ Team Members ✨
# ║
# ║  🧑‍💻 Elyasaf Cohen 311557227 🧑‍💻
# ║  🧑‍💻 Eldad Cohen   207920711 🧑‍💻
# ║  🧑‍💻 Israel Shlomo 315130344 🧑‍💻
# ║
# ╚══════════════════════════════════╝

from PySide6.QtWidgets import (
    QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from Fronted.Windows.AIChatBotWindow import AIChatBotWindow
from Fronted.Windows.BuyStocksWindow import BuyStocksWindow
from Fronted.Windows.OrderHistoryWindow import OrderHistoryWindow
from Fronted.Windows.PortfolioWindow import PortfolioWindow
from Fronted.Windows.SellStocksWindow import SellStocksWindow


# ======================================== MAIN WINDOW ========================================= #
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("🌿 System for Managing Investments 🌿")
        self.setMinimumSize(900, 600)

        # ====== Set background image ====== #
        self.bg_path = "C:/Users/elyas/PycharmProjects/InvestmentAdvisor/Pictures/background_pic.jpeg"
        self.bg_label = QLabel(self)
        self.bg_label.setScaledContents(True)
        self.bg_label.lower()

        # ====== Central layout setup ====== #
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.setSpacing(18)
        self.central_widget.setLayout(self.layout)

        # ====== Buttons ====== #
        self.buttons = [
            ("🟢 Buy Stocks 🟢", self.on_buy_stocks_clicked),
            (" 🔴 Sell Stocks 🔴", self.on_sell_stocks_clicked),
            (" 📄 Order History 📄", self.show_order_history_windows),
            (" 📁 Portfolio 📁", self.on_portfolio_clicked),
            (" 🤖 Ask the Chatbot 🤖", self.on_askAIChatBot_clicked)
        ]

        for label, slot in self.buttons:
            btn = QPushButton(label)
            btn.setMinimumWidth(200)
            btn.clicked.connect(slot)
            self.layout.addWidget(btn)

        # ====== Style ====== #
        self.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.9);
                color: #003049;
                font-weight: bold;
                font-size: 15px;
                padding: 12px 28px;
                border-radius: 14px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 1);
            }
        """)

    # ========== Resize Event to Fit Background ========== #
    def resizeEvent(self, event):
        pixmap = QPixmap(self.bg_path)
        self.bg_label.setPixmap(pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
        self.bg_label.resize(self.size())
        super().resizeEvent(event)

    # ================= Button Actions ================= #
    def on_buy_stocks_clicked(self):
        self.BuyWindow = BuyStocksWindow()
        self.BuyWindow.show()

    def on_sell_stocks_clicked(self):
        self.SellWindow = SellStocksWindow()
        self.SellWindow.show()

    def show_order_history_windows(self):
        self.OrderHistoryWindow = OrderHistoryWindow()
        self.OrderHistoryWindow.show()

    def on_portfolio_clicked(self):
        self.PortfolioWindow = PortfolioWindow()
        self.PortfolioWindow.show()

    def on_askAIChatBot_clicked(self):
        self.AIChatBotWindow = AIChatBotWindow()
        self.AIChatBotWindow.show()
