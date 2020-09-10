#########################################################################
# 								 	                                    
#   Swiss crypto tool is created purely in python.It supports	        
#   different hashing algorithm and different encryption algorithm      
#   too.User can also send a secure email by encrypting their body      
#   with private key using this tool.	   
#   This script is compatible with python2.7.
#   Before running this script please install pycrypto library and try 
#   to resolve all dependencies issues.
#               Author : JK                   		                    
#	           		                    
#########################################################################


import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from Crypto.Cipher import ARC4
from Crypto.Cipher import DES
from Crypto.Cipher import AES
from Tkinter import *
import tkMessageBox
import Tkinter
import base64
import hashlib
import os
import sys

#Functions for hashing,encryption and decryption.
def clicked1():
    mEntry=Entry(root,textvariable=text1,text="Enter text to convert=").pack(side=TOP)
    global mtext
    mtext=text1.get()
    B4=Tkinter.Button(root,text="Convert",command=clicked1_convert)
    B4.pack(side=BOTTOM)
def md5():
     md5L=Label(root,text="Enter data to convert:",fg="blue",font=("arial",15))
     md5L.pack()
     global mtext
     mEntry=Entry(root,textvariable=text1).pack(side=TOP)
     mtext=text1.get()
     B4=Tkinter.Button(root,text="Convert",command=md52) 
     B4.pack(side=TOP)
def md52():
    md5=hashlib.md5(mtext).hexdigest()
    md5L2=Label(root,text="MD5="+md5,bg="#F5DEB3",font=("arial",15))
    md5L2.pack()
    print "\nMD5:"+md5

def sha1():
     shaL=Label(root,text="Enter data to convert:",fg="blue",font=("arial",15))
     shaL.pack()
     global mtext
     mEntry=Entry(root,textvariable=text1).pack(side=TOP)
     mtext=text1.get()
     B4=Tkinter.Button(root,text="Convert",command=shaa1)
     B4.pack(side=TOP)

def shaa1():
    sha1=hashlib.sha1()
    sha1.update(mtext)
    shA1=sha1.hexdigest()
    SHA1L=Label(root,text="SHA1="+shA1,bg="#F5DEB3",font=("arial",15))
    SHA1L.pack()
    print "\nSHA1:"+shA1
    
def sha224():
     sha224=Label(root,text="Enter data to convert:",fg="blue",font=("arial",15))
     sha224.pack()
     global mtext
     mEntry=Entry(root,textvariable=text1).pack(side=TOP)
     mtext=text1.get()
     B4=Tkinter.Button(root,text="Convert",command=shA224)
     B4.pack(side=TOP)

def shA224():
    sha224=hashlib.sha224()
    sha224.update(mtext)
    shA224=sha224.hexdigest()
    SHA224L=Label(root,text="SHA224="+shA224,bg="#F5DEB3",font=("arial",15))
    SHA224L.pack()
    print '\nSHA224:'+shA224

def sha256():
     sha256=Label(root,text="Enter data to convert:",fg="blue",font=("arial",15))
     sha256.pack()
     global mtext
     mEntry=Entry(root,textvariable=text1).pack(side=TOP)
     mtext=text1.get()
     B4=Tkinter.Button(root,text="Convert",command=shA256)
     B4.pack(side=TOP)

def shA256():
    sha256=hashlib.sha256()
    sha256.update(mtext)
    shA256=sha256.hexdigest()
    SHA256L=Label(root,text="SHA256="+shA256,bg="#F5DEB3",font=("arial",15))
    SHA256L.pack()
    print "\nSHA256:"+shA256

def sha384():
     sha384=Label(root,text="Enter data to convert:",fg="blue",font=("arial",15))
     sha384.pack()
     global mtext
     mEntry=Entry(root,textvariable=text1).pack(side=TOP)
     mtext=text1.get()
     B4=Tkinter.Button(root,text="Convert",command=shA384)
     B4.pack(side=TOP)
def shA384():
    sha384=hashlib.sha384()
    sha384.update(mtext)
    shA384=sha384.hexdigest()
    SHA384L=Label(root,text="SHA384="+shA384,bg="#F5DEB3",font=("arial",15))
    SHA384L.pack()
    print'\nSHA384:'+shA384

def sha512():
     sha512=Label(root,text="Enter data to convert:",fg="blue",font=("arial",15))
     sha512.pack()
     global mtext
     mEntry=Entry(root,textvariable=text1).pack(side=TOP)
     mtext=text1.get()
     B4=Tkinter.Button(root,text="Convert",command=shA512)
     B4.pack(side=TOP)

def shA512():
     sha512=hashlib.sha512()
     sha512.update(mtext)
     shA512=sha512.hexdigest()
     SHA512L=Label(root,text="SHA512="+shA512,bg="#F5DEB3",font=("arial",15))
     SHA512L.pack()
     print "\nSHA512:"+shA512


def clicked2():
    text3=StringVar()
    label3=Label(root,textvariable=text3,bd="4",fg="brown",bg="grey")
    text3.set("Select Ciphers :")
    label3.pack()
    var = IntVar()
    R1 = Radiobutton(root, text="Block Cipher", variable=var, value=1,command=clicked3)
    R1.pack()
    R2 = Radiobutton(root, text="Stream Cipher", variable=var, value=2,command=clicked15)
    R2.pack()

def clicked3():
    text4=StringVar()
    label4=Label(root,textvariable=text4,bd="4",fg="brown",bg="grey")
    text4.set("Select Encryption:")
    label4.pack()
    R3 = Radiobutton(root, text="AES (Advanced Encryption Standard)", variable=var, value=1,command=clicked8)
    R3.pack()
    R4 = Radiobutton(root, text="DES (Data Encryption Standard)", variable=var, value=2,command=clicked4)
    R4.pack()

def clicked4():
    DESL=Label(root,text="Enter Data To Convert:",font=("arial",15))
    DESL.pack()
    global text3
    text3=StringVar()
    mEntry2=Entry(root,textvariable=text3,width=50).pack()
    B5=Tkinter.Button(root,text="OK",command=clicked5)
    B5.pack(side=BOTTOM)

def clicked5():
    global mText2
    mText2=(text3.get())
    print "Data to be converted :"+mText2
    BlockSize=8
    key=("12345678")
    des = DES.new(key, DES.MODE_ECB)
    cipher_text = (des.encrypt(mText2))
    bcipher_text=cipher_text.encode('hex')
    print "Key:"+key
    print "Encrypted Text:"+bcipher_text
    text5=StringVar()
    label5=Label(root,textvariable=text5,bd="4",fg="brown",bg="grey",font=("arial",15))
    text5.set("Key:"+key)
    label5.pack()
    text6=StringVar()
    label6=Label(root,textvariable=text6,bd="4",fg="brown",bg="grey",font=("arial",15))
    text6.set("Encrypted text:"+bcipher_text)
    label6.pack()

def clicked6():
        R5 = Radiobutton(root, text="AES (Advanced Encryption Standard)",value=0,command=clicked12)
        R5.pack()
        R6 = Radiobutton(root, text="DES (Data Encryption Standard)", value=1,command=clicked11)
        R6.pack()
        R20=Radiobutton(root,text="ARC4",value=2,command=clicked18)
        R20.pack()
        
        
        

def clicked7():
        des2 = DES.new(text7.get(), DES.MODE_ECB)
        hdecrypt=text8.get()
        hexdecrypt=hdecrypt.decode('hex')
        decrypted=des2.decrypt(hexdecrypt)
        label7=Label(root,text="Decrypted_Data="+decrypted,fg="brown",bg="grey",font=("arial",15))
        label7.pack()
        print "Decrypted Data:"+decrypted

def clicked8():
    AESL=Label(root,text="Enter Text To Convert:")
    AESL.pack()
    global text9
    text9=StringVar()
    mEntry5=Entry(root,textvariable=text9,text="Enter data to be converted",fg="brown",bg="grey",width=50)
    mEntry5.pack()
    B8=Tkinter.Button(root,text="OK",command=clicked9)
    B8.pack()
    
def clicked9():
    global data
    data=text9.get()
    print "Data to be comverted:"+data
    B9=Tkinter.Button(root,text="Convert",command=clicked10(data))
    B9.pack()
    
def clicked10(privateInfo):
    BlockSize=32
    Padding='{'
    pad=lambda s:s+(BlockSize-len(s)%BlockSize)*Padding
    EncodeAES=lambda c,s:base64.b64encode(c.encrypt(pad(s)))
    Secret=os.urandom(BlockSize)
    HexSecret=Secret.encode('hex')
    label10=Label(root,text="Key="+HexSecret,fg="brown",bg="grey",font=("arial",15))
    label10.pack()
    print 'encrypted_key=='+HexSecret
    Cipher=AES.new(Secret)
    encoded=EncodeAES(Cipher,privateInfo)
    HexEncoded=encoded.encode('hex')
    label11=Label(root,text="Encrypted_Text="+HexEncoded,fg="brown",bg="grey",font=("arial",15))
    label11.pack()
    print 'Encrypted_String=='+HexEncoded
    
    
def clicked11():
    DESD=Label(root,text="Enter Key To Decrypt")
    DESD.pack()
    global text7
    text7=StringVar()
    mEntry3=Entry(root,textvariable=text7,text="Enter Key here",fg="brown",bg="grey")
    mEntry3.pack()
    DESD2=Label(root,text="Enter Encrypted Text Here:",font=("arial",15))
    DESD2.pack()
    global text8
    text8=StringVar()
    mEntry4=Entry(root,textvariable=text8,text="Enter Encrypted Text Here:",fg="brown",bg="grey")
    mEntry4.pack()
    B7=Tkinter.Button(root,text="Decrypt",command=clicked7)
    B7.pack()

def clicked12():
    AESD=Label(root,text="Enter Key to decrypt:",font=("arial",15))
    AESD.pack()
    global text11
    text11=StringVar()
    global text12
    text12=StringVar()
    mEntry11=Entry(root,textvariable=text11,text="Enter Key Here")
    mEntry11.pack()
    AESD2=Label(root,text="Enter Data To Decrypt",font=("arial",15))
    AESD2.pack()
    mEntry12=Entry(root,textvariable=text12,text="Enter Text Here")
    mEntry12.pack()
    B11=Tkinter.Button(root,text="Ok",command=clicked13)
    B11.pack()

def clicked13():
    global key2
    global hexEncrypted_text2
    key3=text11.get()
    hexEncrypted_text2=text12.get()
    B13=Tkinter.Button(root,text="Decrypt",command=clicked14(key3,hexEncrypted_text2))
    B13.pack()

def clicked14(key2,hexEncrypted_text):
    Padding='{'
    DecodeAES=lambda c,e:c.decrypt(base64.b64decode(e)).rstrip(Padding)
    key4=key2.decode('hex')
    Cipher=AES.new(key4)
    encrypted_text=hexEncrypted_text.decode('hex')
    decoded=DecodeAES(Cipher,encrypted_text)
    label14=Label(root,text="Decrypted_Text="+decoded,fg="brown",bg="grey",font=("arial",15))
    label14.pack()
    print "Decrypted Data="+decoded

def clicked15():
    labeL15=Label(root,text="Select Encryption Algorithm :",fg="brown",bg="grey",font=("arial",15))
    labeL15.pack()
    R15 = Radiobutton(root, text="ARC4", variable=var, value=0,command=clicked16)
    R15.pack()

def clicked16():
    global text15
    global text16
    text15=StringVar()
    text16=StringVar()
    CLICK16=Label(root,text="Enter Key and Data To Convert:",font=("arial",15))
    CLICK16.pack()
    mEntry15=Entry(root,textvariable=text15,text="Enter Key:")
    mEntry15.pack()
    mEntry16=Entry(root,textvariable=text16,text="Enter Data")
    mEntry16.pack()
    B15=Tkinter.Button(root,text="Convert",command=clicked17)
    B15.pack()

def clicked17():
    key=text15.get()
    data15=text16.get()
    obj1 = ARC4.new(key)
    cipher_text15 = obj1.encrypt(data15)
    hex_cipher_text15=cipher_text15.encode('hex')
    label15=Label(root,text="Encrypted_Data="+hex_cipher_text15,fg="brown",bg="grey",font=("arial",15))
    label15.pack()
    print "Encrypted_Data="+hex_cipher_text15
    global text17
    global text18


    
    
def clicked18():
    ARC4D=Label(root,text="Enter Key To Decrypt",font=("arial",15))
    ARC4D.pack()
    global text17
    global text18
    text17=StringVar()
    text18=StringVar()
    mEntry17=Entry(root,textvariable=text17,text="Enter Key")
    mEntry17.pack()
    ARC4D2=Label(root,text="Enter Encrypted Data:")
    ARC4D2.pack()
    mEntry18=Entry(root,textvariable=text18,text="Enter Data")
    mEntry18.pack()
    mButton17=Tkinter.Button(root,text="Ok",command=clicked19)
    mButton17.pack()

def clicked19():
    key16=text17.get()
    hex_data16=text18.get()
    data16=hex_data16.decode('hex')
    obj2 = ARC4.new(key16)
    decrypted16=obj2.decrypt(data16)
    label18=Label(root,text="Decrypted_Text="+decrypted16,fg="brown",bg="grey",font=("arial",15))
    label18.pack()
    print "Decrypted text="+decrypted16

def clicked20():
    global Semail
    global Temail
    global body
    global user_name
    global password
    global encrypted_body
    Semail=StringVar()
    Temail=StringVar()
    body=StringVar()
    user_name=StringVar()
    password=StringVar()
    encrypted_body=StringVar()
    EMAILL=Label(root,text="Enter your email:",font=("arial",18),bg="skyblue")
    EMAILL.pack()
    mEntryS=Entry(root,textvariable=Semail,text="Enter your Email")
    mEntryS.pack()
    TOEMAIL=Label(root,text="To Email=",bg="skyblue",font=("arial",18))
    TOEMAIL.pack()
    mEntryT=Entry(root,textvariable=Temail,text="Enter Reciever Email")
    mEntryT.pack()
    MESSAGE=Label(root,text="Enter your message=",bg="skyblue",font=("arial",18))
    MESSAGE.pack()
    mEntryB=Entry(root,textvariable=body,text="Enter your message")
    mEntryB.pack()
    USER=Label(root,text="Enter your User_Name=",bg="skyblue",font=("arial",18))
    USER.pack()
    mEntryU=Entry(root,textvariable=user_name,text="Enter you user_name")
    mEntryU.pack()
    PASS=Label(root,text="Enter your password=",bg="skyblue",font=("arial",18))
    PASS.pack()
    mEntryP=Entry(root,textvariable=password,text="Enter your Password",show="*")
    mEntryP.pack()
    B19=Tkinter.Button(root,text="Convert and Send",command=clicked21,font=("arial",13))
    B19.pack()
    
def clicked21():
    global msg
    msg=MIMEMultipart()
    global sa
    sa=Semail.get()
    msg['From']=sa
    global ta
    ta=Temail.get()
    msg['To']=ta
    msg['Subject']="Encrypted Email"
    uname=user_name.get()
    pwd=password.get()
    global privateBody
    privateBody=body.get()
    BlockSize2=32
    Padding='{'
    pad=lambda s:s+(BlockSize2-len(s)%BlockSize2)*Padding
    EncodeAES2=lambda c,s:base64.b64encode(c.encrypt(pad(s)))
    Secret2=os.urandom(BlockSize2)
    HexSecret2=Secret2.encode('hex')
    label20=Label(root,text="Key="+HexSecret2,fg="brown",bg="grey",font=("arial",15))
    label20.pack()
    print 'encrypted_key=='+HexSecret2
    Cipher2=AES.new(Secret2)
    encoded2=EncodeAES2(Cipher2,privateBody)
    HexEncoded2=encoded2.encode('hex')
    label21=Label(root,text="Encrypted_Text="+HexEncoded2,fg="brown",bg="grey",font=("arial",15))
    label21.pack()
    print 'Encrypted_String=='+HexEncoded2
    msg.attach(MIMEText(HexEncoded2))
    server=smtplib.SMTP('SMTP.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(uname,pwd)
    server.sendmail(sa,ta,msg.as_string())
    server.quit()
    
    

# graphical part
root=Tk()
root.title("Secure Mail")
frame = Frame(root)
frame.pack()
frame.configure(bg="#F5DEB3")
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
global text1
text1=StringVar()
var = StringVar()
label = Label( frame, textvariable=var,bg="#F4A460",bd=5,width=80,height=3,fg="black",font=("arial",15))
var.set("Secure Messaging System")
label.pack(side=TOP)
#B1 = Tkinter.Button(frame, text ="Hash Converter",pady=10,width=30,activebackground="pink",fg="Brown",command=clicked1)
#B1.pack(side = LEFT)
#B2 = Tkinter.Button(frame, text ="Encryption",pady=10,width=30,activebackground="pink",fg="Brown",command=clicked2)
#B2.pack(side = LEFT)
#B6 = Tkinter.Button(frame, text ="Decryption",pady=10,width=30,activebackground="pink",fg="Brown",command=clicked6)
#B6.pack(side = LEFT)
#B3 = Tkinter.Button(frame, text ="Secure Messaging",pady=10,width=30,activebackground="pink",fg="Brown",command=clicked20)
#B3.pack(side = LEFT)
mb=Menubutton ( frame, text="Hash Converter", relief=RAISED,width=35,height=3,bg="cyan")
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
mb.menu.add_checkbutton ( label="MD5",command=md5 ,font=("arial",13))
mb.menu.add_checkbutton ( label="SHA1",command=sha1,font=("arial",13))
mb.menu.add_checkbutton ( label="SHA224",command=sha224,font=("arial",13))
mb.menu.add_checkbutton ( label="SHA256",command=sha256,font=("arial",13))
mb.menu.add_checkbutton ( label="SHA384",command=sha384,font=("arial",13))
mb.menu.add_checkbutton ( label="SHA512",command=sha512,font=("arial",13))
mb.pack(side=LEFT)
mb2=  Menubutton ( frame, text="Encryption", relief=RAISED,width=35,height=3,bg="cyan")
mb2.menu  =  Menu ( mb2, tearoff = 0 )
mb2["menu"]  =  mb2.menu
mb2.menu.add_checkbutton ( label="Symmetric Encryption",command=clicked2)
mb2.menu.add_checkbutton ( label="Assymetric Encryption")
mb2.pack(side=LEFT)
mb3=  Menubutton ( frame, text="Decryption", relief=RAISED,width=35,height=3,bg="cyan")
mb3.menu  =  Menu ( mb3, tearoff = 0 )
mb3["menu"]  =  mb3.menu
mb3.menu.add_checkbutton ( label="Symmetric Encryption",command=clicked6)
mb3.menu.add_checkbutton ( label="Assymetric Encryption")
mb3.pack(side=LEFT)
mb4=  Menubutton ( frame, text="Secure Email", relief=RAISED,width=35,height=3,bg="cyan")
mb4.menu  =  Menu ( mb4, tearoff = 0 )
mb4["menu"]  =  mb4.menu
mb4.menu.add_checkbutton ( label="Symmetric Encryption",command=clicked20)
mb4.menu.add_checkbutton ( label="Assymetric Encryption")
mb4.pack(side=LEFT)
root.mainloop()
##############################################################################################################################
