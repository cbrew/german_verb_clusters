import pandas
from collections import defaultdict
from codecs import open
from sklearn import preprocessing,manifold,cluster
import time
import numpy as np


def read_counts(filename='Distribution/ip-pp.freqs-orig'):
	"""
	Read in Sabine's German frame data...
	"""
	inf = open(filename,'r',encoding='latin1')
	f = defaultdict(dict)
	for line in inf:
		arr = line.split()
		if len(arr) == 1:
			verb = arr[0]
		elif len(arr) == 2:
			frame = arr[0]
			f[frame][verb] = float(arr[1])    
	inf.close()
	frames = f.keys()
	df = pandas.DataFrame({frame: pandas.Series(f[frame]) for frame in frames})
	return df

def mini_batch(df,k=5):
	X = np.array(df)
	X = preprocessing.normalize(X,norm='l2')
	
	
	mbk = cluster.MiniBatchKMeans(init='k-means++', k=k, batch_size=45,
	                      n_init=10, max_no_improvement=10, verbose=0)
	t0 = time.time()
	mbk.fit(X)
	t_mini_batch = time.time() - t0
	mbk_means_labels = mbk.labels_
	mbk_means_cluster_centers = mbk.cluster_centers_
	mbk_means_labels_unique = np.unique(mbk_means_labels)
	centers = pandas.DataFrame(mbk_means_cluster_centers,index=mbk_means_labels_unique,columns=df.columns)
	return pandas.Series(mbk_means_labels,index=df.index),centers