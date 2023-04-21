from fastapi import FastAPI
from src.models.max_rate_difference import MaxRateDifference
from src.models.minmax_rates import MinmaxRates
from src.utils.service import handle_response

app = FastAPI()


@app.get('/exchanges/{currency}/{date}')
async def exchanges(currency, date):
    url = f'https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}/?format=json'

    data = await handle_response(url)
    exchange_rate = data['rates'][0]
    exchange_rate_value = exchange_rate['mid']
    return exchange_rate_value


@app.get('/exchanges/minmax/{currency}/{last_quotations}', response_model=MinmaxRates)
async def minmax(currency, last_quotations):
    url = f'https://api.nbp.pl/api/exchangerates/rates/a/{currency}/last/{last_quotations}/?format=json'

    data = await handle_response(url)
    exchange_rates = data['rates']
    exchange_rate_values = [value['mid'] for value in exchange_rates]
    max_value = max(exchange_rate_values)
    min_value = min(exchange_rate_values)
    return {'min': min_value, 'max': max_value}


@app.get('/exchanges/differences/{currency}/{last_quotations}', response_model=MaxRateDifference)
async def differences(currency, last_quotations):
    url = f'https://api.nbp.pl/api/exchangerates/rates/c/{currency}/last/{last_quotations}/?format=json'

    data = await handle_response(url)
    rates = data['rates']
    bid_ask_diffs = [rate['ask'] - rate['bid'] for rate in rates]
    bid_ask_diffs = [round(diff, 6) for diff in bid_ask_diffs]
    max_diff = max(bid_ask_diffs)

    return {'max': max_diff}
