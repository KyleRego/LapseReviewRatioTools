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
        self.window.resize(320, 240)
        self.window.setWindowTitle("Lapse Review Ratio Tools")

        layout = QVBoxLayout()
        avg = lapse_review_ratio_calculations.average_lapse_review_ratio(mw)
        avg_text = f"The average review lapse ratio (average of per card reviews/lapses) in your collection is {avg}."
        avg_text_widget = QLabel(avg_text)
        layout.addWidget(avg_text_widget)

        self.window.setLayout(layout)

    def show(self):
        self.window.show()
