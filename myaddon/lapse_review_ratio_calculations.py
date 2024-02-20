from aqt import AnkiQt


def average_lapse_review_ratio(mw: AnkiQt):
    cards_data = mw.col.db.all("select id, lapses from cards;")
    ratio_sum_holder = 0
    for card_data in cards_data:
        card_id = card_data[0]
        card_lapse_count = card_data[1]
        review_count = mw.col.db.first("select count(*) from revlog where cid = ?", card_id)[0]
        if review_count == 0:
            continue
        lapse_review_ratio = card_lapse_count / review_count
        ratio_sum_holder += lapse_review_ratio
    card_count = mw.col.db.first("select count(*) from cards")[0]
    return ratio_sum_holder / card_count
