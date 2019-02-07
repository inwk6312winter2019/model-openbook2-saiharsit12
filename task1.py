file= open("Street_Centrelines.csv","r")
str = []
name = []
str2 = []
str3 = []
for line in file:
  line=line.split(",")
  str.append(line[2])
  name.append(line[4])
  str2.append(line[6])
  str3.append(line[7])

print(list(zip(str,name,str2,str3)))
