from roboflow import Roboflow
rf = Roboflow(api_key="gGsQ42EvK9CktMAILWyO")
project = rf.workspace("saciducak").project("hastalikli_domates")
model = project.version(1).model
# dataset = version.download("yolov9")

# infer on a local image
#cprint(model.predict("_23frame75.jpg", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("_54frame1380.jpg", confidence=40, overlap=30).save("prediction6.jpg")
# another exapmle prediction
# model.predict("_23frame75.jpg", confidence=40, overlap=30).save("prediction5.jpg")


# model.predict("DJI_0021.MP4", confidence=40, overlap=30).save("VİDEO.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())   