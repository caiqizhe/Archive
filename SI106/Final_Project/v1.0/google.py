from googlefinance import getQuotes
import json
print json.dumps( getQuotes('GOOG'), indent=2 )

print getQuotes('GOOG')