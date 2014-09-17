sasm
====

[![Build Status](https://travis-ci.org/ymyzk/sasm.svg?branch=master)](https://travis-ci.org/ymyzk/sasm)
[![Coverage Status](https://coveralls.io/repos/ymyzk/sasm/badge.png?branch=master)](https://coveralls.io/r/ymyzk/sasm?branch=master)
[![PyPI version](https://badge.fury.io/py/sasm.svg)](http://badge.fury.io/py/sasm)

Simple Assembler for SIMPLE Architecture

Requirements
------------
* Python 2.7+
* Python 3.2+
* PyPy
* PyPy3

Installation
------------
1. `git clone https://github.com/ymyzk/sasm.git`
2. `cd sasm`
3. `pip install .`

Assemble
--------
1. Write .sasm file
2. `sasm -o test.mif test.sasm`

Sample
------
### Input .sasm file
```
option(address_radix, HEX)
option(data_radix, HEX)
option(depth, 4096)

li(r1, 1)
li(r2, 0x10)

label(loop)
  add(r0, r1)
  cmp(r0, r2)
blt(loop)

hlt()
```

### Output .mif file
```
-- SASM generated Memory Initialization File (.mif)

WIDTH=16;
DEPTH=4096;
ADDRESS_RADIX=HEX;
DATA_RADIX=HEX;

CONTENT BEGIN
         000 : 8101;
         001 : 8210;
         002 : c800;
         003 : d050;
         004 : b9fd;
         005 : c0f0;
         006 : 0000;
         007 : 0000;
         008 : 0000;
         009 : 0000;
```

See [sample](sample) files.
