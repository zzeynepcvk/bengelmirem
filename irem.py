meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "overthink" : "aşırı düşünmek",
            "vibe":"öyle bir hissiyat vermek"
            }

word = input("Anlamadığınız bir kelime yazın (CRINGE,LOL,overthink,vibe!): ")


if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(meme_dict[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("eşleşme yok tekrar dene ")
