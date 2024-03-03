from urllib import request
try:
    request.urlopen('https://www.shopee.com.br/')
except:
    print('\033[1;31mNão foi possível acessar o site da Shopee :(')
else:
    print('\033[1;32mSucesso! Consegui acessar o site da Shopee.\033[m')
