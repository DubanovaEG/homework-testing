def get_mask_card_number(card_number: str) -> str:
    """аскирует номер карты"""
    if not card_number:
        return ""
    card_number = str(card_number).replace(" ", "")
    if len(card_number) < 16:
        return card_number
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """аскирует номер счета"""
    if not account_number:
        return ""
    account_number = str(account_number).replace(" ", "")
    if len(account_number) < 4:
        return account_number
    return f"**{account_number[-4:]}"
