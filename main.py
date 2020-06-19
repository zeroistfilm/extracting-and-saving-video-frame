import cv2
vidcap = cv2.VideoCapture('DJI_0002.MP4')
success,image = vidcap.read()
count = 0
success = True
while success:
  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))  
  success,image = vidcap.read()
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1