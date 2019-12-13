import os
import time

os.chdir(r"C:\Users\bytedance")
#print(os.getcwd())
os.system('adb kill-server')
os.system('adb start-serverr')
os.system('adb devices')
os.system('adb shell am start -n com.mediatek.camera/com.android.camera.CameraActivity')

T = 1
while T <= 100:
    time.sleep(2)
    print('即将拍摄第'+str(T)+'张\n')
    os.system('adb shell input tap 400 540')
    time.sleep(1)
    os.system('adb shell input tap 440 1350')
    #time.sleep(1)
    T += 1

time.sleep(1)

#### 查看当前文件夹下文件数

os.system('adb shell "cd sdcard/DCIM/Camera && ls -l | grep "^-" | wc -l"')

#### 循环结束 导出图片后删除

pd = os.system(r'adb pull /sdcard/DCIM/Camera D:\byte_data\1212_card')

while pd != 0:
    print('等待导出完毕。。。')
    time.sleep(1)

print('已成功导出图片')

os.system('adb shell "cd sdcard/DCIM/Camera && rm -r *.*"')
print('已删除图片')