import re 

# May have to give entire file path 

ListStr = []  # empty list 

f = open("fileName.txt", "r")

for x in f:
  x.append(ListStr)
  
  
for item in ListStr:
  re.split('<<span>, </span>', item)
  
  
  f.close()
  


