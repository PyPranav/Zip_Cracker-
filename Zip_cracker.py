import zipfile, string
b = string.printable[:94]+" " 
a="qwertyuiopasdfghjklzxcvbnm1234567890"
list_char = list(a) # for all possibilities use b (like space,special charecters and capitals)
passw = REPASS = ""
name = input("Enter Zip Filname(along with extension): ")
d=0
def formaker(l):
    for z in range(l):
        if z == 0:
            forstr = "for a0 in list_char:\n"
        else:
            forstr += ("   "*z)+f"for a{z} in list_char:\n"+"   "*(z+1)+"if d==10:\n"+"   "*(z+2)+"break\n"
    forstr += ("   "*l)+"passw="
    for z in range(l):
        if z != l-1:
            forstr += f"a{z}+"
        else:
            forstr += f"a{z}"
    forstr += "\n"+("   " * l) + "passw=passw.encode(encoding='UTF-8')"
    forstr += "\n"+("   " * l)+"try:\n"+("   " * (l+1))+"with zipfile.ZipFile(f'{name}', 'r') as zf:\n"+(
            "   " * (l+2))+"zf.extractall(pwd=passw)\n"+("   " * (l+2))+"print(f'password found: {passw}')\n"+("   " * (l+2))+"d=10\n"+("   " * (l+2))+"REPASS = passw\n"+("   " * (l+2))+"break\n"+(
            "   " * l)+"except:\n"+("   " * (l+1))+"print(f'{passw.decode(\"UTF-8\")} didnt work')\n"+("   " * l)+"if d==10:\n"+("   " * (l+1))+"break"
    return forstr
for z in range (1, 8): # to change the max length of the password or to specify a certain length change the range accordingly.(Currently its set to start from a len of 1 to a try till a max len of 7) 
    if d!=10:
        exec(formaker(z))
    else:
        break

print("*"*20+"\n"+f"Password = {REPASS.decode('UTF-8')}\n"+"*"*20)
f = open("pass.txt", "w")
f.write("*"*20+"\n"+f"Password = {REPASS.decode('UTF-8')}\n"+"*"*20)
f.close()
