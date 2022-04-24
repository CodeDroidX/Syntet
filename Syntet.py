import googletrans
import random
from colorama import Fore,init
init()
translator = googletrans.Translator()
from Levenshtein import distance
print(Fore.YELLOW+"░██████╗██╗░░░██╗███╗░░██╗████████╗███████╗████████╗\n██╔════╝╚██╗░██╔╝████╗░██║╚══██╔══╝██╔════╝╚══██╔══╝\n╚█████╗░░╚████╔╝░██╔██╗██║░░░██║░░░█████╗░░░░░██║░░░\n░╚═══██╗░░╚██╔╝░░██║╚████║░░░██║░░░██╔══╝░░░░░██║░░░\n██████╔╝░░░██║░░░██║░╚███║░░░██║░░░███████╗░░░██║░░░\n╚═════╝░░░░╚═╝░░░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝░░░╚═╝░░░"+Fore.RESET)
f=input("Перетащите сюда исходный текстовый файл> ")
with open(f,"r",encoding="utf-8") as f:
    src=f.read()
print()
print("1. "+Fore.GREEN+"Light Edit Sample"+Fore.RESET+" (небольшое синонимизирование, небольшая перестановка членов предложения)")
print("2. "+Fore.CYAN+"Medium Change Sample"+Fore.RESET+" (двуязычная конвертация, слияние и разделение предложений, возможны неточности.)")
print("3. "+Fore.MAGENTA+"Hard Retell Sample"+Fore.RESET+" (многоязычная конвертация, полный перефраз)")
print("4. "+Fore.RED+"Extreme Full Sample"+Fore.RESET+" (конвертация через все языки, высокая неточность, сильная потеря смысла!!!)")
case=input("\nКакую силу алгоритма вы выберите?> ")
#lang=list(googletrans.LANGUAGES.keys())
if case=="1":
    lang=["ru","en"]

elif case=="2":
    lang=["ru","en","ja"]

elif case=="3":
    lang=["ru","en","ja","fr","zh-cn"]

elif case=="4":
    lang=list(googletrans.LANGUAGES.keys())
out=src
def unirate(new,old):
    return distance(new,old)/len(old)*100
while 1:
    ru=translator.translate(out,dest="ru").text
    print(str(int(unirate(ru,src)))+"% изменений",end='\r')
    with open("new.txt","w",encoding="utf-8") as f:
        f.write(ru)
    out=translator.translate(out,dest=random.choice(lang)).text
