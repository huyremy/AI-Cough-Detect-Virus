import tensorflow 
from tensorflow.keras.layers import *
from tensorflow.keras.preprocessing import image  
from tensorflow.keras.models import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import warnings
warnings.simplefilter("ignore", DeprecationWarning)
warnings.filterwarnings('ignore')
cough = load_model('cough.hdf5')
def output(model,img_path,size):
    img_path=img_path
    img = image.load_img(img_path,target_size=size)
    img_arr = image.img_to_array(img,dtype='double')
    img_arr=img_arr/255
    img_arr=np.expand_dims(img_arr,axis=0)
    result = np.argmax(model.predict(img_arr), axis=-1)
    if result==1:
        print("Dương tính")
    elif result==0:
        print("Âm tính")
