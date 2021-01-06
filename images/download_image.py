import cv2
import time
import os

img_source = 'http://96.56.250.139:8200/mjpg/video.mjpg#.X9pWjjXS-8w.link'
target_path = './images'
history_path = 'history.txt'
log_path = 'log.txt'

img_number = 0
try:
    history_file = open(target_path + '/' + history_path, 'r+')
    img_number = sum(1 for line in history_file)
except:
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    history_file = open(target_path + '/' + history_path, 'w')


try:
    cap = cv2.VideoCapture(img_source)
    ret, frame = cap.read()
    if ret:
        cur_time = time.time()
        cv2.imwrite(target_path + '/' + str(img_number) + ".jpg", frame)
        
        if img_number != 0:
            history_file.write('\n')
        history_file.write(str(cur_time))
        
        print("Image saved sucsessfully")
    else:
        raise Exception('Capture return was wrong: image was not saved');
    cap.release()
    
except Exception as e:
    with open(target_path + '/' + log_path, 'a') as log:
        date = time.strftime("%b %d %Y %H:%M:%S", time.localtime(time.time()))
        log.write(date + '; ')
        log.write(str(e) + '\n')

history_file.close()