import os

def dr():
    print("run tree container [1]")
    print("download images [2]")
    i = int(input("What is the opetion do you want to execute>"))
    if i == 1:
       images_run = str(input("which container to run>"))
       os.system(f"docker run -d -p 7000:8080 {images_run}")
       os.system(f"docker run -d -p 8000:8080 {images_run}")
       os.system(f "docker run -d -p 9000:8080 {images_run}")
    elif i == 2:
       images = str(input("Name of images for download>"))
       os.system(f"docker pull {images}")
    else:
       print("Error unkonw this command")
dr()