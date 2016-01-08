#!/bin/sh
EXTERNAL_IP=$(./get_external_ip.sh)
curl --basic --user "innocuous_news:flowersandkittens" --data-ascii "status=awesome+new+article+about+love+and+happiness+at+http://$EXTERNAL_IP/love.html" http://twitter.com/statuses/update.json
