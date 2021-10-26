
import cv2 
import numpy as np 
import glob
import random


class readnet_webimage_detector: 


  def __init__(self, yolo_weights, yolo_config): 
    self.net = cv2.dnn.readNet(yolo_weights, yolo_config)

  def set_classes(self, class_list):
    self.classes = class_list

  def set_image_path(self, path): 
    # The images could be in a jpg or png format
    self.images_path = glob.glob(str(path)+"/*.jpg") + glob.glob(str(path)+"/*.png") 

  def get_objects(self, threshold = 0.3, resize = False): 

    layer_names = self.net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(self.classes), 3))

    # Insert here the path of your images
    random.shuffle(self.images_path)

    objects = []

    # loop through all the images
    for img_path in self.images_path:

      # Loading image
      img = cv2.imread(img_path) # img is a numpy array 
      
      if resize == True: 
        img = cv2.resize(img, None, fx=0.4, fy=0.4)
        
      height, width, channels = img.shape

      # Detecting objects
      blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False) # This is also a numpy array 

      self.net.setInput(blob)
      outs = self.net.forward(output_layers)

      for out in outs:

        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > threshold:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                  # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                crop_img = img[y:y+h, x:x+w]
                objects.append({'img':crop_img, 
                                'label':class_id})
        
    return objects  
    
