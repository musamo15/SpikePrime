import json
import random
import pika
import os
from pika.exchange_type import ExchangeType

print('pika version: %s' % pika.__version__)

#Access the CLODUAMQP_URL environment variable and parse it
url = os.environ.get('CLOUDAMQP_URL', 'amqps://zhonslcd:0vJlLr7YxOadAfNEw33pgpyVHPWSJz4I@baboon.rmq.cloudamqp.com/zhonslcd')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

main_channel = connection.channel()

main_channel.exchange_declare(exchange="test_exchange",
                         passive=False,
                         durable=True,
                         auto_delete=False)

tickers = {
    'MXSE.EQBR.LKOH': (1933, 1940),
    'MXSE.EQBR.MSNG': (1.35, 1.45),
    'MXSE.EQBR.SBER': (90, 92),
    'MXSE.EQNE.GAZP': (156, 162),
    'MXSE.EQNE.PLZL': (1025, 1040),
    'MXSE.EQNL.VTBR': (0.05, 0.06)
}


def getticker():
    return list(tickers.keys())[random.randrange(0, len(tickers) - 1)]


_COUNT_ = 10

for i in range(0, _COUNT_):
    ticker = getticker()
    msg = {
        'order.stop.create': {
            'data': {
                'params': {
                    'condition': {
                        'ticker': ticker
                    }
                }
            }
        }
    }
    body = json.dumps(msg)
    print(body)
    main_channel.basic_publish(
        exchange='test_exchange',
        routing_key='Action',
        body=json.dumps(msg),
        properties=pika.BasicProperties(content_type='application/json'))
    print('send ticker %s' % ticker)

connection.close()