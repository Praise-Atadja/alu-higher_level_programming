#!/usr/bin/node
const PSecond = require('PS');
const PArg = PS.readFileSync(process.argv[2]).toString();
const SArg = PS.readFileSync(process.argv[3]).toString();
PS.writeFileSync(process.argv[4], PArg + SArg);
