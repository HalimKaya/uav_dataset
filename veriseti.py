from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

resim=7600

for  i in range(1):
    img = Image.open(str(resim)+'.jpg')
    a =np.size(img)
    height =a[1]
    widht=a[0]
    flipped_img = np.fliplr(img)
    plt.imsave(str(resim+1)+".jpg",flipped_img)
    plt.show()
    resim=resim+100
    i=i+1