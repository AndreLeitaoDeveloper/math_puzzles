## Author: Andre Leitao
## version 0.1

import random 
x = 0
l = [1.,2.,3.,4.,5.,6.,7.,8.,9.]
while x!=66:	
	random.shuffle(l)
	A, B, C, D, E, F, G, H, I = l	
	if ((13 * B) / C)%2 == 0 and ((G * H / I)%2) == 0:
		x = A + ((13 * B) / C) + D + (12 * E) - F - 11 + ((G * H) / I) - 10 
		if x == 66:
			print l
			break
