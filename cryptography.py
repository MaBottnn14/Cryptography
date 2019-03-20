"""
cryptography.py
Author: maBottnn14
Credit: Andrew Enelow, https://www.youtube.com/watch?v=9-Yw434IbVM  This video taught me the overview of encryption but didn't give it away as the example used in this video was very different than the one in this project,https://www.dreamincode.net/forums/topic/214465-add-two-lists/ 

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md

Enter e to encrypt, d to decrypt, or q to quit: z
Did not understand command, try again.
Enter e to encrypt, d to decrypt, or q to quit: e
Message: Two plus two = Five
Key: Lorem ipsum
+KF;B(CH=NIZ}m;R\Dt
Enter e to encrypt, d to decrypt, or q to quit: d
Message: +KF;B(CH=NIZ}m;R\Dt
Key: Lorem ipsum
Two plus two = Five
Enter e to encrypt, d to decrypt, or q to quit: q
Goodbye!
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
def loop():
    txt = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    for q in txt:
        
        w=[]
        e=[]
        s=" "
#encrypt
        if txt=="e":
            lmao=list(input("Message: "))
            lol=len(lmao)
            rip=list(input("Key: "))
            ggboys=rip*lol
            for r in lmao:
                gg=associations.find(r)
                w.append(gg)
            for o in ggboys:
                ggboys=associations.find(o)
                e.append(ggboys)
            hi=[(w+e) for w, e in zip(w,e)]
            for t in hi:
                e="".join([associations[x % len(associations)] for x in hi])
            print(e)
            loop( )
#decrypt
        elif txt=="d":
            lmao=list(input("Message: "))
            lol=len(lmao)
            rip=list(input("Key: "))
            ggboys=rip*lol
            for r in lmao:
                gg=associations.find(r)
                w.append(gg)
            for o in ggboys:
                ggboys=associations.find(o)
                e.append(ggboys)
            hi=[(w-e) for w, e in zip(w,e)]
            for d in hi:
                e="".join([associations[x % len(associations)] for x in hi])
            print(e)
            loop( )
#saying goobye :(
        elif txt == "q":
            print("Goodbye!")
        else:
            print("Did not understand command, try again.")
            loop()
loop()