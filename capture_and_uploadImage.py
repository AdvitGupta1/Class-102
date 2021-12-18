import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        img_name = "img" + str(number) + ".png"
        ret, frame = videoCaptureObject.read()
        cv2.imwrite("NewImage1.jpg", frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    accessToken:""
    file = accessToken
    file_from = file
    file_to = "/testFile/" + (img_name)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overWrite)
        print("files uploaded")

def main():
    while(True):
        if((time.time()- start_time)>=5):
           name = take_snapshot()
           upload_files(name)

main()