from typing import List, Dict, Any


def filter_by_state(
    operations: List[Dict[str, Any]], 
    state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """ильтрует операции по статусу"""
    if not operations:
        return []
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
    operations: List[Dict[str, Any]], 
    descending: bool = True
) -> List[Dict[str, Any]]:
    """Сортирует операции по дате"""
    if not operations:
        return []
    return sorted(operations, 
                  key=lambda x: x.get("date", ""), 
                  reverse=descending)
