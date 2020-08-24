import sys
import os
from PIL import Image 

filePath = ""
pathToFile = ""
fileExtention = ""
fileName = ""

widthDivisions = 3
heightDivisions = 1


for i in range(len(sys.argv)):
  #Asking for help command?
  if sys.argv[i] == "help":
    print ("Use '-p [PATH TO FILE]'")
    print ("Use '-w [N WIDTH DIVISIONS]' default 3")
    print ("Use '-h [N HEIGHT DIVISIONS]' default 1")
    exit(0)

  #Setting width sections
  if sys.argv[i] == "-w":
    widthDivisions = int(sys.argv[i+1])

  if sys.argv[i] == "-h":
    heightDivisions = int(sys.argv[i+1])

  if sys.argv[i] == "-p":
    filePath = str(sys.argv[i+1])
    
if not filePath == "":

  pathArgsList = filePath.split("/")
  if len(pathArgsList) >= 1:
    for i in range(len(pathArgsList)-1):
      pathToFile += str(pathArgsList[i]) + "/"


  fileExtention = filePath.split(".")[-1]
  fileName = filePath.split("/")[-1].split(".")[0]
  try:
      img = Image.open(filePath)
      width, height = img.size

      sizeW = (int)(width/widthDivisions)
      sizeH = (int)(height/heightDivisions)
    
      nTry = 1
      finalPath = pathToFile + fileName

      while os.path.exists(finalPath):
        finalPath = pathToFile + fileName + "(" + str(nTry) + ")"
        nTry += 1
      
      os.makedirs(finalPath)
      
      for w_i in range(widthDivisions):
        for h_i in range(heightDivisions):

          startW = (w_i*sizeW)
          startH = (h_i*sizeH)
          actualArea = (startW, startH, startW+sizeW, startH+sizeH)
          actualCrop = img.crop(actualArea)
          
          newURL = str(w_i)+','+str(h_i)+'.'+str(fileExtention)
          print(finalPath + "/" + newURL)
          actualCrop.save(finalPath + "/" + newURL)

  except IOError:
    pass
else:
  print("Not added file")
  exit()