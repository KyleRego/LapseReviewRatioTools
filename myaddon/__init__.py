import aqt
from aqt import mw, gui_hooks
from aqt.utils import showInfo, qconnect
from aqt.qt import *
from . import lapse_review_ratio_widget
from . import lapse_review_ratio_calculations

from anki.cards import Card
from anki.notes import Note

from .lapse_review_ratio_calculations import lr_ratio_for_card, lr_ratio_for_note

action = QAction("Lapse Review Ratio Tools", mw)
qconnect(action.triggered, lapse_review_ratio_widget.show_widget)
mw.form.menuTools.addAction(action)


def on_browser_did_fetch_columns(columns):
    columns["lapseReviewRatio"] = aqt.browser.Column(
        key="lapseReviewRatio",
        cards_mode_label="Lapse review ratio",
        notes_mode_label="Average card lapse review ratio",
        uses_cell_font=False,
        alignment=aqt.browser.Columns.ALIGNMENT_CENTER,
    )


def on_browser_did_fetch_row(card_or_note_id, is_note, row, columns):
    for index, key in enumerate(columns):
        if key == "lapseReviewRatio":
            if is_note:
                row.cells[index].text = lr_ratio_for_note(mw, card_or_note_id)
            else:
                row.cells[index].text = lr_ratio_for_card(mw, card_or_note_id)


gui_hooks.browser_did_fetch_columns.append(on_browser_did_fetch_columns)
gui_hooks.browser_did_fetch_row.append(on_browser_did_fetch_row)
