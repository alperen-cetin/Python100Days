print("""\
                  
  /\  /\___ _   _ 
 / /_/ / _ \ | | |
/ __  /  __/ |_| |
\/ /_/ \___|\__, |
            |___/ """)
print("Welcome to my useless alter ego creator\n" )
name = input("Write your real name:\n" )
friendName = input("Name of your best friend:\n" )
food = input("Your favourite food:\n" )
stringLen = len(name)
stringLen2 = len(name)
stringLen3 = len(name)
slicedStr = name[stringLen::-3]
slicedStr2 = name[stringLen2::-5]
slicedStr3 = name[stringLen3::-3]
alterEgo = slicedStr + slicedStr2 + slicedStr3
print(alterEgo)




