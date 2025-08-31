# Yaz kampi: Veri Bilimine Giris - Odev 02

#Bolum - 1: Sayı Analizi

num1 = int(input("Bir sayi girin:"))

if num1 %2 ==0 and num1>0:
    print("Pozitif cift")
elif num1 %2 ==0 and num1<0:
    print("Negatif cift")
elif num1 %2 !=0 and num1>0:
    print("Pozitif tek")
elif num1 %2 !=0 and num1<0:
    print("Negatif tek")
else:
    print("Sayı notr yani sıfır")

#Bolum - 2: Harf Frekansı (String)

word = input("Lutfen kelimeyi girin:")
letterCounter = {} # {key:value}

for letter in word:
    if letter in letterCounter:
        letterCounter[letter] += 1
    else:
        letterCounter[letter] = 1

print(letterCounter)

#Bolum - 3: Şifre Kontrolü (String Metotları)

password = input("Lutfen sifrenizi girin:")

lenght = len(password) >=8
upperLetherControl = any(char.isupper()for char in password)
digitControl = any(char.isdigit()for char in password)

if lenght and upperLetherControl and digitControl:
    print("Sifre gecerli.")
else:
    print("Sifre gecersiz.")
    if not lenght:
        print("Sifre en az 8 karakter olmalidir.")
    if not upperLetherControl:
        print("Sifre en az 1 buyuk harf icermelidir.")
    if not digitControl:
        print("Sifre en az 1 rakam icermelidir.")

#Bolum - 4: Liste İşlemleri

numbers = [12,4,9,25,30,7,18]
bigNumbers = []
total1 = 0
avg1 = 0
for num in numbers:
    total1 += num
avg1 = total1/len(numbers)
for num in numbers:
    if num > avg1:
        bigNumbers.append(num)
print(bigNumbers)
print(avg1)

#Bolum - 5: Nested Loop (Desen)

rows = int(input("Kac satir yildiz olacagini girin:"))
for i in range(1,rows+1):
    print("*"*i)

#Bolum - 6 : While Döngüsü

num2 = 1
total2 = 0
counter1 = 0
while num2 !=0:
    num2 = int(input("Bir sayi girin (0 ile cikis): "))
    if num2 != 0:
        total2 += num2
        counter1 += 1

print("Toplam:",total2)
if counter1 >0:
    print("Ortalam:",total2/counter1)
else:
    print("Hic sayi girilmedi.")


#Bolum - 7: Palindrom Kontrolü

paliWord = input("Lutfen kelimeyi girin:")
if paliWord == paliWord[::-1]:
    print("Kelime palindromdur.")
else:
    print("Kelime palindrom değildir.")


#Bolum - 8: List Comprehension

list1 = [i*i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(list1)

#   list1 = []
#   for i in range(101):
#       if i%3 == 0 and i %5 == 0:
#           list1.append(i*i)
#   print(list1)

#Bolum - 9: String İşlemleri

text = input("Lutfen cumleyi girin:")
words = text.split(" ")
words = [w[0].upper()+w[1:] for w in words]
#    for w in range(len(words)):
#        words[w] = words[w][0].upper() + words[w][1:] # --> w. kelimenin 0. indeksi
sentnc = ""
for word in words:
    sentnc += word + " "
print(sentnc)

#Mini Proje: Film Yorumu Analizi

#Kaç yorum var
#Kaç tane yorumda iyi geçiyor
#Her yorumun uzunluğu

comments = []      # Yorumları tutacak liste
cmtLength = []     # Yorumların karakter uzunlukları
goodCounter = 0    # "iyi" geçen yorum sayısı

# Yorumları alma kısmı
while True:
    sentence = input("Lütfen film hakkındaki yorumunuzu girin (0 ile çıkış): ")
    if sentence == "0":
        break
    comments.append(sentence)
    cmtLength.append(len(sentence))

    # "iyi" kelimesi kontrolü
    words = sentence.split()
    for w in words:
        if w.lower() == "iyi": # İyi ve iyi ikisinide saymak için
            goodCounter += 1
            break  # sadece bir kez saymak için döngü kırılır

# Toplam yorum sayısı
totalComments = len(comments)

# En uzun ve en kısa yorumu bulma
if totalComments > 0:
    longest = comments[0]
    shortest = comments[0]

    totalLength = 0

    for i in range(totalComments):
        # Ortalama için toplam uzunluk
        totalLength += cmtLength[i]

        # En uzun
        if len(comments[i]) > len(longest):
            longest = comments[i]

        # En kısa
        if len(comments[i]) < len(shortest):
            shortest = comments[i]

    avgLength = totalLength / totalComments

    # Sonuçları yazdır
    print("\nToplam yorum sayısı:", totalComments)
    print('"iyi" geçen yorum sayısı:', goodCounter)
    print("En uzun yorum:", longest)
    print("En kısa yorum:", shortest)
    print("Ortalama uzunluk:", round(avgLength, 1), "karakter")
else:
    print("Hiç yorum girilmedi.")







