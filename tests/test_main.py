from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_exchange_by_currency_and_date():
    response = client.get('/exchanges/gbp/2023-01-02')
    assert response.status_code == 200
    assert response.text == '5.2768'


def test_get_exchange_by_currency_and_date_bad_currency():
    response = client.get('/exchanges/aaa/2023-01-02')
    assert response.status_code == 404


def test_get_exchange_by_currency_and_date_holiday_date():
    response = client.get('/exchanges/aaa/2023-01-01')
    assert response.status_code == 404


def test_get_minmax_by_currency_and_date():
    response = client.get('/exchanges/minmax/gbp/100')
    assert response.status_code == 200
    assert response.json() == {'min': 5.2086, 'max': 5.4638}


def test_get_minmax_by_currency_and_date_bad_currency():
    response = client.get('/exchanges/minmax/aaa/100')
    assert response.status_code == 404


def test_get_minmax_by_currency_and_date_range_too_big():
    response = client.get('/exchanges/minmax/gbp/256')
    assert response.status_code == 400


def test_get_minmax_bid_differences_by_currency():
    response = client.get('/exchanges/differences/gbp/100')
    assert response.status_code == 200


def test_get_minmax_bid_differences_by_currency_bad_currency():
    response = client.get('/exchanges/minmax/aaa/100')
    assert response.status_code == 404


def test_get_minmax_bid_differences_by_currency_range_too_big():
    response = client.get('/exchanges/minmax/gbp/256')
    assert response.status_code == 400
