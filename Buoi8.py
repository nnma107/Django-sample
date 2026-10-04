
import random
thuong="abcdefghijklmnopqrstuvwxyz"
HOA="ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
so="0123456789"
dac_biet="!@#$%^&*" 
tat_ca=thuong + HOA+ so+ dac_biet 
do_dai=int(input("Do dai mat khau: ")) #Bat buoc moi nhom co it nhat 1 ki tu dac bit 

if do_dai<8:
    print("Need at least 8 char")
else:
    print("Do dai hop le, bat dau tao mat khau...")

    mk =[ random.choice(thuong),random.choice(HOA),random.choice(so),random.choice(dac_biet)] #them phan con lai tu tat ca
    for _ in range(do_dai-4): 
        mk.append(random.choice(tat_ca)) 
    random.shuffle(mk)  #tron random
    print("".join(mk))
