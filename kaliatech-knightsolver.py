#!/usr/bin/env python3






from string import *
import re



with open('map-test.kn','r') as fp:
	xx = fp.readlines()

xx = [ tt for tt in xx if tt.startswith('#') == False]

# Ignore forbidden letters, replace oO0 with o
xx = [ re.sub('L|l|I|i|\n', '', tt) for tt in xx ]
xx = [ re.sub('o|O|0', 'o', tt) for tt in xx ]

# If not a space or a letter, assume it's a placeholder
xx = [ ''.join([ ii if ii in ascii_letters + '. ' else ' . ' for ii in tt]) for tt in xx ]

## Remove double spaces and trim
xx = [ re.sub(' +',' ',tt.strip()) for tt in xx ]

# Remove empty lines
xx = [ tt for tt in xx if tt != '' ]

## Get cleaned up arrays
xx = [ tt.split(' ') for tt in xx ]





## TESTS!
colSize = len(xx[0])
rowSize = len(xx)

colRow = [ len(tt) for tt in xx]

if len(set(colRow)) != 1:
	print('Column mismatch')

