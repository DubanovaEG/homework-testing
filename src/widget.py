def mask_account_card(info: str) -> str:
    """аскирует номер карты или счета в строке"""
    if not info:
        return ""
    # роверяем на счет
    if "Счет" in info:
        parts = info.split()
        if len(parts) >= 2:
            number = parts[-1]
            if len(number) >= 4:
                return f"{' '.join(parts[:-1])} **{number[-4:]}"
        return info
    # робуем найти номер карты (16 цифр)
    # азделяем на слова
    parts = info.split()
    for i, part in enumerate(parts):
        # сли часть состоит из 16 цифр
        if part.isdigit() and len(part) == 16:
            # аскируем эту часть
            masked = f"{part[:4]} {part[4:6]}** **** {part[-4:]}"
            parts[i] = masked
            return ' '.join(parts)
    return info


def get_date(date_str: str) -> str:
    """реобразует дату из формата 2023-12-01T12:00:00.000000 в 01.12.2023"""
    if not date_str:
        return ""
    try:
        date_part = date_str.split("T")[0]
        year, month, day = date_part.split("-")
        return f"{day}.{month}.{year}"
    except Exception:
        return date_str
