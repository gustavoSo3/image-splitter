import sys
from PIL import Image 

filePath = ""
widthDivisions = 3
heightDivisions = 1
fileExtention = ""

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
  fileExtention = filePath.split(".")[-1]
  try:
      img = Image.open(filePath)
      width, height = img.size

      sizeW = (int)(width/widthDivisions)
      sizeH = (int)(height/heightDivisions)
      
      for w_i in range(widthDivisions):
        for h_i in range(heightDivisions):

          startW = (w_i*sizeW)
          startH = (h_i*sizeH)
          actualArea = (startW, startH, startW+sizeW, startH+sizeH)
          actualCrop = img.crop(actualArea)
          
          newURL = str(w_i)+','+str(h_i)+'.'+str(fileExtention)
          actualCrop.save(newURL)

  except IOError:
    pass
else:
  print("Not added file")
  exit()