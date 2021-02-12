import pyupbit
import datetime

# orderbook (bid and ask)
orderbook = pyupbit.get_orderbook("KRW-BTC")
ms = int(orderbook[0]["timestamp"])

dt = datetime.datetime.fromtimestamp(ms/1000)

print(orderbook)
# [{'market': 'KRW-BTC', 'timestamp': 1613126053872, 'total_ask_size': 1.70739473, 'total_bid_size': 3.17927152,
#   'orderbook_units': [{'ask_price': 51452000.0, 'bid_price': 51440000.0, 'ask_size': 0.22338449, 'bid_size': 0.37101067},
#                       {'ask_price': 51453000.0, 'bid_price': 51439000.0, 'ask_size': 0.15511314, 'bid_size': 0.03135925},
#                       {'ask_price': 51465000.0, 'bid_price': 51438000.0, 'ask_size': 0.15629131, 'bid_size': 0.00097204},
#                       {'ask_price': 51466000.0, 'bid_price': 51435000.0, 'ask_size': 0.02337201, 'bid_size': 0.035037},
#                       {'ask_price': 51467000.0, 'bid_price': 51434000.0, 'ask_size': 0.04024893, 'bid_size': 0.2005},
#                       {'ask_price': 51468000.0, 'bid_price': 51433000.0, 'ask_size': 0.00026, 'bid_size': 0.28458274},
#                       {'ask_price': 51470000.0, 'bid_price': 51432000.0, 'ask_size': 0.00777295, 'bid_size': 0.21730537},
#                       {'ask_price': 51476000.0, 'bid_price': 51431000.0, 'ask_size': 0.09230321, 'bid_size': 0.38260844},
#                       {'ask_price': 51477000.0, 'bid_price': 51430000.0, 'ask_size': 0.00086, 'bid_size': 0.28817829},
#                       {'ask_price': 51480000.0, 'bid_price': 51429000.0, 'ask_size': 0.05391774, 'bid_size': 0.1943},
#                       {'ask_price': 51484000.0, 'bid_price': 51427000.0, 'ask_size': 0.00076, 'bid_size': 1.13154232},
#                       {'ask_price': 51495000.0, 'bid_price': 51425000.0, 'ask_size': 0.1881, 'bid_size': 0.03138088},
#                       {'ask_price': 51496000.0, 'bid_price': 51423000.0, 'ask_size': 0.05542172, 'bid_size': 0.00194465},
#                       {'ask_price': 51499000.0, 'bid_price': 51419000.0, 'ask_size': 0.45659441, 'bid_size': 0.00232625},
#                       {'ask_price': 51500000.0, 'bid_price': 51417000.0, 'ask_size': 0.25299482, 'bid_size': 0.00622362}
#                       ]
#   }
#  ]
