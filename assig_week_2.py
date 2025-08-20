# [1] 
name = "Taher"
age = "21"
country = "Egypt"
print("\"Hello \'"+name+'\',How you doing \\ """ Your age is "'+age+'"" + And Your Country Is: '+country)

# [2]
print("\"Hello \'"+name+'\',How you doing \\ \n""" Your age is "'+age+'"" + \nAnd Your Country Is: '+country)

# [3] 
name = 'Elzero'
print ('Second letter IS "'+name[1]+'"\nThird letter IS "'+name[2]+'"\nlast letter Is "'+name[-1]+'"')

# [4]
name = 'Elzero'
print ('"'+name[1:4]+'"\n"'+name[:5:2]+'"\n"'+name[-2::-2]+'"')

# [5]
name = "#@#@Elzero#@#@"
print (name.strip("#@"))

# [6]
num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"
print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

# [7]
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))

# [8]
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())

# [9]
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

# [10]
name = "Elzero"
print(name.index("z"))

# [11]
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love",1))

# [12]
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love"))

# [13]
name = "Taher"
age = 21
country = "Egypt"
print("My Name Is {:s}, And My Age Is {:d}, And My Country Is {:s}".format(name,age,country))
  