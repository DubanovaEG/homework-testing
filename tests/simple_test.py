def test_masks():
    """ростой тест для проверки работы"""
    import sys
    sys.path.insert(0, "src")
    
    import masks
    
    # Тест маскировки карты
    result = masks.get_mask_card_number("1234567812345678")
    expected = "1234 56** **** 5678"
    assert result == expected, f"жидалось '{expected}', получено '{result}'"
    print("✅ test_masks: get_mask_card_number работает")
    
    # Тест маскировки счета
    result = masks.get_mask_account("12345678901234567890")
    expected = "**7890"
    assert result == expected, f"жидалось '{expected}', получено '{result}'"
    print("✅ test_masks: get_mask_account работает")

if __name__ == "__main__":
    test_masks()
    print("се тесты прошли успешно!")
