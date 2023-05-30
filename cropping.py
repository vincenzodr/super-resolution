import os
import tensorflow as tf

train_path = r'E:/Download/archive/DIV2K_train_HR/DIV2K_train_HR'
output_path = r'E:/Download/archive/DIV2K_crop'
crop_height = 256
crop_width = 256

def cropping(path, crop_height, crop_width,k):
    y = tf.keras.utils.load_img(path)
    y = tf.keras.utils.img_to_array(y)
    
    for i in range(y.shape[0] // crop_height):
        for j in range(y.shape[1] // crop_height):
            cropped_image = y[i*crop_height:(i+1)*crop_height,j*crop_width:(j+1)*crop_width,:]
            
            # Crop
            output = str(k) + '.png'
            path = os.path.join(output_path,output)
            print("Saved image " + output)
            tf.keras.utils.save_img(path,cropped_image)
            
            # Horizontal flipped crop
            output = str(k) + '_hflip.png'
            path = os.path.join(output_path,output)
            print("Saved image " + output)
            tf.keras.utils.save_img(path,tf.image.flip_left_right(cropped_image))
            
            # Vertical flipped crop
            output = str(k) + '_vflip.png'
            path = os.path.join(output_path,output)
            print("Saved image " + output)
            tf.keras.utils.save_img(path,tf.image.flip_up_down(cropped_image))
            
            k += 1
    return k

k = 0
for dirname, _, filenames in os.walk(train_path):
    for filename in filenames:
        img_path = os.path.join(dirname, filename)
        
        k = cropping(img_path, crop_height, crop_width,k)
        