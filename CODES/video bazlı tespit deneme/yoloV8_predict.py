from ultralytics import YOLO
from PIL import Image

from roboflow import Roboflow
rf = Roboflow(api_key="gGsQ42EvK9CktMAILWyO")
project = rf.workspace().project("domates_tespit")
model = project.version(1).model


# load a pretrained YOLOv8n detection model
# model = YOLO('yolov8n.pt') 

""" 
# resim dosyası üzerinde nesne tanıma 
image1 = Image.open("_23frame55.jpg")
sonuc = model.predict(source = image1 , save = True)  # save ile kaydededer.

image2 = Image.open("_23frame65.jpg")
sonuc = model.predict(source = image2 , save = True)  # save ile kaydededer.

image3= Image.open("_23frame75.jpg")
sonuc = model.predict(source = image3 , save = True)  # save ile kaydededer.

image4 = Image.open("_23frame110.jpg")
sonuc = model.predict(source = image4 , save = True)  # save ile kaydededer.

image5= Image.open("_23frame140.jpg")
sonuc = model.predict(source = image5 , save = True)  # save ile kaydededer.

"""

# print(f"{len(sonuc)} adet nesneyi buldu.")

# web-cam açılarak nesne tanıma yapan sistem
#sonuc2 = model.predict(source=0)

sonuc_video = model.predict(source = "DJI_0021.MP4" , show=True)