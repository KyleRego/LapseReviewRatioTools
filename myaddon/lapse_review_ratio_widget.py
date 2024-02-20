from aqt import mw
from aqt.utils import showInfo


def show_widget() -> None:
    card_count = mw.col.cardCount()
    showInfo("Card count: %d (hello world)" % card_count)