#!/bin/sh

wget -q -O - http://www.swlink.net/~styma/REMOTE_ADDR.shtml | grep -v '^<'
