from aqt import AnkiQt


def average_lapse_review_ratio(mw: AnkiQt):
    card_count = mw.col.db.first("select count(*) from cards;")[0]
    return card_count
