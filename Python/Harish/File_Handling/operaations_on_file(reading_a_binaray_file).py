fptr=open("photo.jpg", "rb")
image1=fptr.read()
#print(image1)
fptr2=open("photo1.jpg", "wb")
fptr2.write(image1)
print("image is created in new file")
fptr.close()
fptr2.close()