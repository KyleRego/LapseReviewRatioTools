from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *
from . import lapse_review_ratio_widget

action = QAction("Lapse Review Ratio", mw)
qconnect(action.triggered, lapse_review_ratio_widget.show_widget)
mw.form.menuTools.addAction(action)
