from PIL import Image,ImageColor
import binascii
from flask import render_template
def decode(passw, filename):
    #open image
    im = Image.open("images/new/"+filename)
    pix = im.load()

    #open image

    #info
    #print(im.size[0],im.size[1]) x,y değerleri


    #info

    #width,height
    width = im.size[0]
    height = im.size[1]
    #width,height

    user_password = passw

    pass_var = (width*height)-(2)
    red = []
    green =[]
    blue = []
    red_binary = []
    green_binary = []
    blue_binary = []
    encoded_text_binary = []
    encoded_password_binary = []



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

    encoded_text_length = red_binary[(height*width)-1]
    encoded_text_length = int(encoded_text_length, 2)

    encoded_password_length = green_binary[(height*width)-1]
    encoded_password_length = int(encoded_password_length, 2)

    mod = int((encoded_text_length*8) % 3)
    remain = int((encoded_text_length*8) / 3)

    mod2 = int((encoded_password_length*8) % 3)
    remain2 = int((encoded_password_length*8) / 3)

    if (mod == 0):
        for i in range(0,remain,1):
            var = red_binary[i]
            var = var[7:8]
            encoded_text_binary.append(var)
            var = green_binary[i]
            var = var[7:8]
            encoded_text_binary.append(var)
            var = blue_binary[i]
            var = var[7:8]
            encoded_text_binary.append(var)

    if (mod == 1):
        for i in range(0,remain,1):
            var = red_binary[i]
            var = var[7:8]
            encoded_text_binary.append(var)
            var = green_binary[i]
            var = var[7:8]
            encoded_text_binary.append(var)
            var = blue_binary[i]
            var = var[7:8]
            encoded_text_binary.append(var)

        var = red_binary[remain +1]
        var = var[7:8]
        encoded_text_binary.append(var)

    if (mod == 2):
        for i in range(0,remain,1):
            var = red_binary[i]
            var = var[7:8]
            encoded_text_binary.append(var)
            var = green_binary[i]
            var = var[7:8]
            encoded_text_binary.append(var)
            var = blue_binary[i]
            var = var[7:8]
            encoded_text_binary.append(var)

        var = red_binary[remain+1]
        var = var[7:8]
        encoded_text_binary.append(var)

        var = green_binary[remain+1]
        var = var[7:8]
        encoded_text_binary.append(var)

    if mod2 == 0:
        for i in range(pass_var, pass_var-remain2, -1):
            var = blue_binary[i]
            var = var[7:8]
            encoded_password_binary.append(var)
            var = green_binary[i]
            var = var[7:8]
            encoded_password_binary.append(var)
            var = red_binary[i]
            var = var[7:8]
            encoded_password_binary.append(var)

    if mod2 == 1:
        for i in range(pass_var, pass_var-remain2, -1):
            var = blue_binary[i]
            var = var[7:8]
            encoded_password_binary.append(var)
            var = green_binary[i]
            var = var[7:8]
            encoded_password_binary.append(var)
            var = red_binary[i]
            var = var[7:8]
            encoded_password_binary.append(var)

        var = blue_binary[pass_var - remain2]
        var = var[7:8]
        encoded_password_binary.append(var)

    if mod2 == 2:
        for i in range(pass_var, pass_var-remain2, -1):
            var = blue_binary[i]
            var = var[7:8]
            encoded_password_binary.append(var)
            var = green_binary[i]
            var = var[7:8]
            encoded_password_binary.append(var)
            var = red_binary[i]
            var = var[7:8]
            encoded_password_binary.append(var)

        var = blue_binary[pass_var - remain2]
        var = var[7:8]
        encoded_password_binary.append(var)

        var = green_binary[pass_var - remain2]
        var = var[7:8]
        encoded_password_binary.append(var)
    resim_sifre = ""
    resim_text = ""
    for i in range(0,len(encoded_password_binary),1):
        resim_sifre += encoded_password_binary[i]
    print(resim_sifre)
    resim_sifre = int(resim_sifre, 2)
    resim_sifre = binascii.unhexlify('%x' % resim_sifre)

    resim_sifre = str(resim_sifre).split("'")[1]

    for i in range(0,len(encoded_text_binary),1):
        resim_text += encoded_text_binary[i]
    print(resim_text)
    resim_text = int(resim_text, 2)
    resim_text = binascii.unhexlify('%x' % resim_text)

    resim_text = str(resim_text).split("'")[1]

    if user_password == resim_sifre:
        print(resim_text)
        return resim_text
    else:
        print("Parola Yanlış Ajan mısınız? Polis Aranıyor.")

