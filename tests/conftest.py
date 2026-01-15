"""икстуры для тестов"""
import pytest


@pytest.fixture
def sample_transactions():
    """икстура с тестовыми транзакциями"""
    return [
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2023-12-01T12:00:00.000000',
            'amount': '100.00',
            'currency': {'name': 'USD'},
            'description': 'Payment',
            'from': 'Visa Platinum 1234567812345678',
            'to': 'Счет 12345678901234567890'
        },
        {
            'id': 2,
            'state': 'PENDING',
            'date': '2023-11-15T09:30:00.000000',
            'amount': '50.00',
            'currency': {'name': 'EUR'}
        }
    ]
