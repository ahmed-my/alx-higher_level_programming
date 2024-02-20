#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const URL = process.argv[2];
const storedContent = process.argv[3];
request(URL).pipe(fs.createWriteStream(storedContent));
