"""
Optional, only for those who are training the model on GPU and facing "CUDA_error:ran_out_of_memory" problem.
"""


import tensorflow as tf

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
