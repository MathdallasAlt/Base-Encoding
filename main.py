import base64

encodingValues=["b32hexencode","b16encode","b85encode","a85encode","encodebytes","b64encode","b32encode"]
while True:
    print("""----------------|
Encoding list-  |
b32hexencode    |
b16encode       |
b85encode       |
a85encode       |
encodebytes     |
b64encode       |
b32encode      |
----------------|""")
    val=input("Enter value to encode:")
    encodeType=input("Enter type of encoding(q to quit): ")
    if encodeType.lower()==encodingValues[0]:
        x=base64.b32hexencode(val.encode())
    elif encodeType.lower()==encodingValues[1]:
        x=base64.b16encode(val.encode())
    elif encodeType.lower()==encodingValues[2]:
        x=base64.b85encode(val.encode())
    elif encodeType.lower()==encodingValues[3]:
        x=base64.a85encode(val.encode())
    elif encodeType.lower()==encodingValues[4]:
        x=base64.encodebytes(val.encode())
    elif encodeType.lower()==encodingValues[5]:
        x=base64.b64encode(val.encode())
    elif encodeType.lower()==encodingValues[6]:
        x=base64.b32encode(val.encode())
    elif encodeType.lower()=="q":
        quit()
    else:
        print("Invalid encoding")
    print(f"\nEncoded value: {x} \n")


