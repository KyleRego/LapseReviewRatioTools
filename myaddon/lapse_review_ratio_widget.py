from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo

from . import lapse_review_ratio_calculations

def show_widget() -> None:
    mw.lapse_review_ratio_widget = widget = LapseReviewRatioWidget()
    widget.show()


class LapseReviewRatioWidget:
    def __init__(self):
        self.window = QWidget()
        self.window.setWindowTitle("Lapse Review Ratio Tools")
        layout = QVBoxLayout()

        card_count = lapse_review_ratio_calculations.average_lapse_review_ratio(mw)
        card_count_text = f"There are {card_count} cards in your collection."
        card_count_text_widget = QLabel(card_count_text)
        layout.addWidget(card_count_text_widget)

        self.window.setLayout(layout)

    def show(self):
        self.window.show()
