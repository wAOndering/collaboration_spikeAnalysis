### python on how to read data binaries
fname = r"Y:\Jessie\e3 - Data Analysis\e3 Data\2019-05-15_16-21-30\output\2019-05-15_16-21-30__S1.2__ap\2019-05-15_16-21-30__S1.2__ap.dat"
fname = r"Y:\Jessie\e3 - Data Analysis\e3 Data\2019-05-15_16-21-30\output\2019-05-15_16-21-30__S1.2__lfp.dat"
f = open(fname)
a = array.array("L")
a.fromfile(f, 3)


import numpy as np

def readLfp(fname, nchannels=64):
	'''
	this function is to be able to read the binaries registred with matlab
	in matlab int16=>single enable to fill up the matrix with 0 if not fully
	completed same is performed here 
	probably need to go back and quadruple check from the row binaries

	fname (str): correspond to the file name
	nchannels (int): correspond to the number of channel on the probes by default it is 64

	'''
	with open(fname, 'rb') as fid:
		print(fid)
	    data_array = np.fromfile(fid, np.int16)
	    if data_array/nchannels is not int:
	    	tmpLen = ((len(data_array)//nchannels)+1)*nchannels
	    	toAppend = tmpLen-len(data_array)
	    	data_array = np.append(data_array, np.zeros(toAppend))

	    data_array = data_array.reshape((-1, nchannels)).T

	return data_array




