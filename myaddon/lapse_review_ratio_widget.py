from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo


def show_widget() -> None:
    mw.lapse_review_ratio_widget = widget = LapseReviewRatioWidget()
    widget.show()


class LapseReviewRatioWidget:
    def __init__(self):
        self.window = QWidget()

    def show(self):
        self.window.show()
