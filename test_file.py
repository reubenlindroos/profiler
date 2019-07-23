from __future__ import division
import numpy as np 
import line_profiler
def func():
	arr = np.random.rand(512,512,512)
	for i in range(10):
		print(i)
		arr += np.random.rand(512,512,512)
	return arr 
func()
