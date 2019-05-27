#!/usr/bin/env python2


STRING = '    hello world today   '

print 'replace ......... "' + STRING.replace('world','') + '"'
print 'strip   ......... "' + STRING.strip() + '"'
print 'lstrip  ......... "' + STRING.lstrip() + '"'
print 'rstrip  ......... "' + STRING.rstrip() + '"'

SEPARATOR = ''
OUTPUT = [ x.replace('o','x') for x in STRING ]

print SEPARATOR.join(OUTPUT)

# --- end ---

