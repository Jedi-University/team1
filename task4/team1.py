def super_range(i):
   x = 0
   while x < i:
	   yield x
	   x += 1

for x in super_range(100):
   print(x)