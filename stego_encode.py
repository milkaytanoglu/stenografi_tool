from PIL import Image,ImageColor
import binascii
#open image

def encode(plaintext_form, passw, filename):
    im = Image.open("images/old/"+filename)
    pix = im.load()

    #open image

    #info
    #print(im.size[0],im.size[1]) x,y değerleri

    """print(pix[0,0][0],pix[0,0][1],pix[0,0][2])
    print(pix[1,0][0],pix[1,0][1],pix[1,0][2])
    print(pix[0,1][0],pix[0,1][1],pix[0,1][2])
    print(pix[1,1][0],pix[1,1][1],pix[1,1][2])""" #renk kodları
    #info

    #width,height
    width = im.size[0]
    height = im.size[1]
    #width,height

    #decralation
    red = []
    green =[]
    blue = []
    red_binary = []
    green_binary = []
    blue_binary = []
    plaintext_binary_obo = []
    plaintext_binary = []
    password = passw
    password_binary = []
    password_binary_obo = []
    len_plaintext_binary_obo = 0
    len_password_binary_obo = 0
    mod = 0
    remain = 0
    mod2 = 0
    remain2 = 0
    r = 0
    g = 1
    b = 2
    r2 = 0
    g2 = 1
    b2 = 2
    pass_var = (width*height)-(2)
    img_binary = []
    tupple_binary = []
    #decralation

    #rgb decomposing
    for pixelx in range(0,height,1):
        for pixely in range(0,width,1):
             red.append(pix[pixely,pixelx][0])
             green.append(pix[pixely,pixelx][1])
             blue.append(pix[pixely,pixelx][2])
    #rgb decomposing

    #rgb binary to 8bit binary
    for i in range(0,len(red),1):
        red_binary.append(f'{red[i]:08b}')
        green_binary.append(f'{green[i]:08b}')
        blue_binary.append(f'{blue[i]:08b}')
        print(red_binary[i])
        print(green_binary[i])
        print(blue_binary[i])
    # rgb binary to 8bit binary

    print("adasdasdasdas")

    #text to binary
    plaintext = plaintext_form
    for i in plaintext:
        plaintext_binary.append(str([bin(ord(i))[2:].zfill(8)]).split("'")[1])
    #text to binary

    """for i in range(0,len(plaintext),1):
        print(plaintext_binary[i])"""

    #all binary values to list
    for y in range(0,len(plaintext),1):
        for x in plaintext_binary[y]:
            plaintext_binary_obo.append(x)
    #all binary values to list

    #mod and remain
    len_plaintext_binary_obo = len(plaintext_binary_obo)
    mod = int(len_plaintext_binary_obo % 3)
    remain = int(len_plaintext_binary_obo / 3)
    #mod and remain

    #encoding plaintext
    if mod == 0:
        for i in range(0,remain,1):
            var = red_binary[i]
            var = var[0:7]
            var = var + plaintext_binary_obo[r]
            red_binary[i] = var
            r = r + 3

        for i in range(0,remain,1):
            var = green_binary[i]
            var = var[0:7]
            var = var + plaintext_binary_obo[g]
            green_binary[i] = var
            g = g + 3

        for i in range(0,remain,1):
            var = blue_binary[i]
            var = var[0:7]
            var = var + plaintext_binary_obo[b]
            blue_binary[i] = var
            b = b + 3

    if mod == 1:
        for i in range(0,remain,1):
            var = red_binary[i]
            var = var[0:7]
            var = var + plaintext_binary_obo[r]
            red_binary[i] = var
            r = r + 3

        for i in range(0,remain,1):
            var = green_binary[i]
            var = var[0:7]
            var = var + plaintext_binary_obo[g]
            green_binary[i] = var
            g = g + 3

        for i in range(0,remain,1):
            var = blue_binary[i]
            var = var[0:7]
            var = var + plaintext_binary_obo[b]
            blue_binary[i] = var
            b = b + 3

        var = red_binary[remain+1]
        var = var[0:7]
        var = var + plaintext_binary_obo[len_plaintext_binary_obo - 1]
        red_binary[remain+1] = var

    if mod == 2:
        for i in range(0,remain,1):
            var = red_binary[i]
            var = var[0:7]
            var = var + plaintext_binary_obo[r]
            red_binary[i] = var
            r = r + 3

        for i in range(0,remain,1):
            var = green_binary[i]
            var = var[0:7]
            var = var + plaintext_binary_obo[g]
            green_binary[i] = var
            g = g + 3

        for i in range(0,remain,1):
            var = blue_binary[i]
            var = var[0:7]
            var = var + plaintext_binary_obo[b]
            blue_binary[i] = var
            b = b + 3

        var = red_binary[remain+1]
        var = var[0:7]
        var = var + plaintext_binary_obo[len_plaintext_binary_obo - 2]
        red_binary[remain+1] = var

        var = green_binary[remain+1]
        var = var[0:7]
        var = var + plaintext_binary_obo[len_plaintext_binary_obo - 1]
        green_binary[remain+1] = var
    #encoding plaintext

    print("++++++++")
    plaintext_length = len(plaintext)
    plaintext_length_binary = "{0:08b}".format(plaintext_length)

    red_binary[(height*width)-1] = plaintext_length_binary
    print(red_binary[width*height-1])

    #password to binary
    for i in password:
        password_binary.append(str([bin(ord(i))[2:].zfill(8)]).split("'")[1])
    #password to binary

    password_length = len(password)
    password_length_binary = "{0:08b}".format(password_length)

    green_binary[(height*width)-1] = password_length_binary
    print(green_binary[width*height-1])

    print("asdadasd")

    for i in password_binary:
        print(i)

    #all binary values to list
    for y in range(0,len(password),1):
        for x in password_binary[y]:
            password_binary_obo.append(x)
    #all binary values to list

    #mod and remain
    len_password_binary_obo = len(password_binary_obo)
    mod2 = int(len_password_binary_obo % 3)
    remain2 = int(len_password_binary_obo / 3)
    #mod and remain

    #encoding password

    if mod2 == 0:
        for i in range(pass_var, pass_var-remain2, -1):
            var = blue_binary[i]
            var = var[0:7]
            var = var + password_binary_obo[r2]
            blue_binary[i] = var
            r2 = r2 + 3
            var = None

        for i in range(pass_var, pass_var-remain2, -1):
            var = green_binary[i]
            var = var[0:7]
            var = var + password_binary_obo[g2]
            green_binary[i] = var
            var = None
            g2 = g2 + 3

        for i in range(pass_var, pass_var-remain2, -1):
            var = red_binary[i]
            var = var[0:7]
            var = var + password_binary_obo[b2]
            red_binary[i] = var
            b2 = b2 + 3
            var = None

    if mod2 == 1:
        for i in range(pass_var, pass_var - remain2, -1):
            var = blue_binary[i]
            var = var[0:7]
            var = var + password_binary_obo[r2]
            blue_binary[i] = var
            r2 = r2 + 3
            var = None

        for i in range(pass_var, pass_var - remain2, -1):
            var = green_binary[i]
            var = var[0:7]
            var = var + password_binary_obo[g2]
            green_binary[i] = var
            var = None
            g2 = g2 + 3

        for i in range(pass_var, pass_var - remain2, -1):
            var = red_binary[i]
            var = var[0:7]
            var = var + password_binary_obo[b2]
            red_binary[i] = var
            b2 = b2 + 3
            var = None

        var = blue_binary[pass_var - remain2]
        var = var[0:7]
        var = var + password_binary_obo[len_password_binary_obo - 1]
        blue_binary[pass_var - remain2] = var

    if mod2 == 2:
        for i in range(pass_var, pass_var - remain2, -1):
            var = blue_binary[i]
            var = var[0:7]
            var = var + password_binary_obo[r2]
            blue_binary[i] = var
            r2 = r2 + 3
            var = None

        for i in range(pass_var, pass_var - remain2, -1):
            var = green_binary[i]
            var = var[0:7]
            var = var + password_binary_obo[g2]
            green_binary[i] = var
            g2 = g2 + 3
            var = None

        for i in range(pass_var, pass_var - remain2, -1):
            var = red_binary[i]
            var = var[0:7]
            var = var + password_binary_obo[b2]
            red_binary[i] = var
            b2 = b2 + 3
            var = None

        var = blue_binary[pass_var - remain2]
        var = var[0:7]
        var = var + password_binary_obo[len_password_binary_obo - 2]
        blue_binary[pass_var - remain2] = var

        var = green_binary[pass_var - remain2]
        var = var[0:7]
        var = var + password_binary_obo[len_password_binary_obo - 1]
        green_binary[pass_var - remain2] = var
    #encoding password
    print("xdxdxd")
    for i in range(0,len(red),1):
        print(red_binary[i])
        print(green_binary[i])
        print(blue_binary[i])

    #rgb binary to decimal
    for i in range(0,width*height,1):
        img_binary.append(red_binary[i])
        img_binary.append(green_binary[i])
        img_binary.append(blue_binary[i])
    for i in range(0,width*height*3,1):
        x = int(img_binary[i], 2)
        img_binary[i] = x
    #rgb binary to decimal
    var_xyz = 0
    #decimal to list
    for i in range(0,width*height,1):
        tupple_binary.append((img_binary[var_xyz], img_binary[var_xyz+1], img_binary[var_xyz+2]))
        var_xyz = var_xyz+3
    #decimal to list

    for i in img_binary:
        print(i)
    print(tupple_binary)

    new_im = Image.new("RGB", (width, height))
    new_im.putdata(tupple_binary)
    new_im.save("images/new/"+filename+".png")
    show = Image.open("images/new/"+filename+".png")