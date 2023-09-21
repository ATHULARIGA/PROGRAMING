def print_msg():
    x="hello everyone"

    return x

    
def outer(ptr1):
    print("entering outer")
    def inner():
        print("entering inner")
        ref=ptr1
        y=ref()
        newstr=""
        i=0
        while( i < len(y)):
            data=y[i]
            asciiv=ord(data)
            if ( asciiv >= 97 and asciiv <= 122 ):
                newasciiv=asciiv-32
                newascii=chr(newasciiv)
                newstr+=newascii
            elif ( asciiv >= 65 and asciiv <= 90 ):
                newasciiv=asciiv+32
                newascii=chr(newasciiv)
                newstr+=newascii
            else:
                newstr+=data
            i+=1
        
        print(newstr)
        ref=ptr1
        ref()
        print("leaving inner")
    return inner
ptr1=print_msg
ptr2=outer(ptr1)
ptr2()
print("pgm end")