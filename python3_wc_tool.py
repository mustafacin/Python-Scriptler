#!/usr/bin/python3

#Bu program wc toolunun yaptiklarini yapmaktadir.

wordlist = input("Input your file : ")

lines = open(wordlist)
harfsayisi= 0
kelimesayisi = 0
satirsayisi = 0

for line in lines:
    dosya = line.split()  #liste bicimine atar.Kelime sayisi icin
    satirsayisi += 1
    kelimesayisi += len(dosya)
    harfsayisi += len(line)

print("Line : ",satirsayisi," Word : " , kelimesayisi ," char : ",harfsayisi)
