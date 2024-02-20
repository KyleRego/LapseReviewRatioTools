from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *


def show_lapse_review_ratio_widget() -> None:
    card_count = mw.col.cardCount()
    showInfo("Card count: %d (hello world)" % card_count)


action = QAction("Lapse Review Ratio", mw)
qconnect(action.triggered, show_lapse_review_ratio_widget)
mw.form.menuTools.addAction(action)
