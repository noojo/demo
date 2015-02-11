#!/usr/bin/python
import struct
import json
j = []
x = 0
c = 0
r = 0
dim = 0
fw = []
line_width = 11520
lines = 5632
tile = 16

max_x = line_width / tile / 2
max_y = lines / tile


for r in range(0, tile):
	for c in range(0, tile):
		fn = './mora/mo-%03d.%03d.json' % ( c, r)
		print fn
		print "%d x %d" % (max_x, max_y)
		fz = open(fn, 'w')
		#v = 'var mo%03d%03d = [\n' % (c,r)
		v = '{ "depth": ['
		fz.write(v)
		fz.close()
print "writing data"
try:
	with open('modata.raw', 'rb') as f:
		z = 0
		s = 0
		for r in range(0, tile):
			for y in range(0, max_x):
				b= 0
				for c in range(0, tile):
					fn = './mora/mo-%03d.%03d.json' % ( c, r)
					#print fn
					fz = open(fn, 'a')			
					#print "line %d" % y
					for x in range(0,max_x):

						d = f.read(2)
						b = b + 2
						v = struct.unpack('>h', d)
						w = (v[0] / 255.0)
						# open correct output file z, y

						fz.write('%f,' % w)
						
					fz.close()
				
				f.read((line_width*2) - b)
except:
	pass

for r in range(0, tile):
	for c in range(0, tile):
		fn = './mora/mo-%03d.%03d.json' % ( c, r)
		fz = open(fn, 'a')
		fz.write('], "grid": "%04d.%04d" };\n' % (c,r))		
		fz.close()
		






 # LINES                        = 5632
 # LINE_SAMPLES                 = 11520
 # SAMPLE_TYPE                  = MSB_INTEGER
 # SAMPLE_BITS                  = 16
 # UNIT                         = METER