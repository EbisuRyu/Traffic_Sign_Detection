import cv2
import matplotlib.pyplot as plt
import numpy as np

def convert(frame, src_model = "rgb", dest_model = "hls"):
    
    if src_model == "rgb" and dest_model == "hsv": 
      frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    elif src_model == "rgb" and dest_model == "hls":
      frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HLS)
    elif src_model == "rgb" and dest_model == "yuv":
      frame = cv2.cvtColor(frame, cv2.COLOR_RGB2YUV)
    elif src_model == "rgb" and dest_model == "ycrcb":
      frame = cv2.cvtColor(frame, cv2.COLOR_RGB2YCR_CB)
    elif src_model == "hsv" and dest_model == "rgb":
      frame = cv2.cvtColor(frame, cv2.COLOR_HSV2RGB)
    elif src_model == "hls" and dest_model == "rgb":
      frame = cv2.cvtColor(frame, cv2.COLOR_HLS2RGB)
    elif src_model == "yuv" and dest_model == "yuv":
      frame = cv2.cvtColor(frame, cv2.COLOR_YUV2RGB)
    elif src_model == "ycrcb" and dest_model == "ycrcb":
      frame = cv2.cvtColor(frame, cv2.COLOR_YCR_CB2RGB)
    elif src_model == "rgb" and dest_model == "rgb": 
      frame = frame
    elif src_model == "rgb" and dest_model == "gray":
      frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)      
    else: 
      raise Exception('ERROR:', 'src_model or dest_model not implemented')

    return frame

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def show_images(images, per_row = 3, per_col = 2, W = 10, H = 5, tdpi = 80):
      
  fig, ax = plt.subplots(per_col, per_row, figsize = (W, H), dpi = tdpi)
  ax = ax.ravel()
  
  for i in range(len(images)):
    img = images[i]
    ax[i].imshow(img)
  
  for i in range(per_row * per_col):
    ax[i].axis('off')
  plt.show()


def box_boundaries(box):
  x1, y1 = box[0], box[1]
  x2, y2 = box[2], box[3]  
  return x1, y1, x2, y2

def put_boxes(image, bboxes):
    
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  for bbox in bboxes:
      x_min, y_min, x_max, y_max, class_name, conf_score = bbox
      cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
  return image