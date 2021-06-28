#Version 1, task 1
#c = open("countries.txt","r")
#def display_info():
#  lines = c.readlines()
#  for aline in lines:
#     print (aline)
#display_info()


def display_info():
  c = open("countries.txt","r")
  lines = c.readlines()
  list_line = lines[a].split(",")
  print(list_line[0],list_line[1].strip(),list_line[2],list_line[3],list_line[4],list_line[10])
  
#send out data Country [1], Region[2], Population[3], Area[4](square mile), Pop[5], Density[6] (per square mile), Phones (per 1000)[12].

a = int(input("Enter a number between 0 and 228 ( not including ) "))

if a < 0 or a > 227:
  a =int(input("Enter a number between 0 and 228 ( not including ) "))
while a > 0 and a <= 227:
  display_info()
  a = int(input("Enter another number between 0 and 228 ( not including ) "))
  if a == -1:
    print("You have exit the program.")
    break




