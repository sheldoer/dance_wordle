import cv2
import numpy

# ============================ 视频处理 分割成一帧帧图片 =======================================
cap = cv2.VideoCapture(r"beauty.mp4")
num = 1
ret, frame = cap.read()
'''
cv2.imwrite(r'E:\allcode\python_note\210207ciyun\picture\one.jpg' , frame)
img = cv2.imread(r"E:\allcode\python_note\210207ciyun\109951165318165554.jpg",cv2.IMREAD_COLOR)
cv2.namedWindow("Image")
cv2.imshow("Image", frame)
cv2.waitKey (0)
cv2.destroyAllWindows()
'''
while True:
    # 逐帧读取视频  按顺序保存到本地文件夹
    ret, frame = cap.read()
    if ret:
        if 88 <= num < 888:
            #cv2.imwrite(f"E:\allcode\python_note\210207ciyun\picture\img_{num}.jpg", frame)   # 保存一帧帧的图片
            cv2.imwrite(f"E:/allcode/python_note/210207ciyun/pictures/img_{num}.jpg", frame)
            print(f'========== 已成功保存第{num}张图片 ==========')
        num += 1
    else:
        break

cap.release()   # 释放资源
