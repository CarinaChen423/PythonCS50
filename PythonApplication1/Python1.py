
print("Welcome to my world")

name=input("What's your name? ")
#capitalize user's name
name=name.capitalize()
#remove withespace from str
name=name.strip()
#new line
print("Hello,\n" + name, )

#end
print("Hello,", end="??")
print(name)

#with one space
print("Hello,",name)

#spe, no space
print("Hello,",name,sep="???")

#print quotes
print('Hello,"550w"')
print("Hello,'Sophon'")
print("Hello,\"R\"")

#f string
print(f"Hi,{name}")
