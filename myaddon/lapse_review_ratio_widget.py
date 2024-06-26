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
        avg_text = f"The average number of lapses / reviews for cards in your collection is {avg}."
        avg_text_widget = QLabel(avg_text)
        layout.addWidget(avg_text_widget)

        standard_deviation = lapse_review_ratio_calculations.standard_deviation_of_lapse_review_ratio(mw)
        standard_deviation_text = F"The standard deviation is {standard_deviation}."
        standard_deviation_text_widget = QLabel(standard_deviation_text)
        layout.addWidget(standard_deviation_text_widget)

        median = lapse_review_ratio_calculations.median_lapse_review_ratio(mw)
        median_text = f"The median number of lapses / reviews for cards in your collection is {median}"
        median_text_widget = QLabel(median_text)
        layout.addWidget(median_text_widget)

        mode = lapse_review_ratio_calculations.mode_lapse_review_ratio(mw)
        mode_text = f"The mode is {mode}"
        mode_text_widget = QLabel(mode_text)
        layout.addWidget(mode_text_widget)

        skewness = lapse_review_ratio_calculations.skewness(mw)
        skewness_text = f"The skewness is {skewness}"
        skewness_text_widget = QLabel(skewness_text)
        layout.addWidget(skewness_text_widget)

        self.window.setLayout(layout)

    def show(self):
        self.window.show()
