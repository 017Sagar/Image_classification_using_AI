import os


os.chdir('dataset\\train\\3\\')
i=1
for file in os.listdir():
    src=file
    dst="4"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1


