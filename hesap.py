def toplama(x,y):
   return x + y

def cıkarma(x,y):
    return x - y

def carpma(x,y):
    return x * y

def bolme(x,y):
    return x / y

def modAlma(x,y):
    return (x*100)/y

while True:
    islem = input("Lütfen yapmak istediğiniz işlemi seçiniz (+, -, *, /, %):")
    
    while islem not in ['+', '-', '*', '/', '%']:
        print ("Gecersiz İslem Secimi!")
        islem=input("Lütfen yapmak istediğiniz işlemi seçiniz (+, -, *, /, %):")
    x = float(input("Lütfen ilk sayiyi girin:"))
    y = float(input("Lütfen ikini sayıyı girin:"))
#Hesaplama
    if islem == '+':
       result = x + y
    elif islem == '-':
       result = x - y
    elif islem == '*':
       result = x * y
    elif islem == '/':
       result = x / y
    elif islem == '%':
       result = (x / 100)* y  
    else:         
       continue
    print("Sonuc:", result)

    choice = input("devam etmek istiyor musun? (E/H):")
    if choice.lower() != 'e':
       break
 
