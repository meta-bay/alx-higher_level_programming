#!/usr/bin/node
const thefs = require('fs');
const i = thefs.readFileSync(process.argv[2], 'utf8');
const j = thefs.readFileSync(process.argv[3], 'utf8');
thefs.writeFileSync(process.argv[4], i + j);
