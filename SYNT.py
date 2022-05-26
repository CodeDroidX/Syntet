import googletrans
import random
import os
from colorama import Fore,init
init()
t = googletrans.Translator()
from Levenshtein import ratio

lang_rating=["be","uk","en","bg","cs","pl","pt","fr","nl","tr","fi","ar","ko","ja"]

def diff(str1,str2):
    return 1-ratio(str1,str2)
def color(name):
    print(eval("Fore."+name),end="")
def translate_bigdata(data,lang):
    lines=data
    groups=[]
    element=""
    for line_n in range(len(lines)):
        if len(element+lines[line_n])<15000:
            element+=lines[line_n]
        else:
            groups.append(element)
            element=""
    if element:
        groups.append(element)
    ret=[]
    for i in groups:
        ret.append(t.translate(i,dest=lang).text)
    return ret
color("MAGENTA")
print("\n░██████╗██╗░░░██╗███╗░░██╗████████╗\n██╔════╝╚██╗░██╔╝████╗░██║╚══██╔══╝\n╚█████╗░░╚████╔╝░██╔██╗██║░░░██║░░░\n░╚═══██╗░░╚██╔╝░░██║╚████║░░░██║░░░\n██████╔╝░░░██║░░░██║░╚███║░░░██║░░░\n╚═════╝░░░░╚═╝░░░╚═╝░░╚══╝░░░╚═╝░░░\n")
color("YELLOW")
file=input("Перетащите сюда исходный текстовый файл> ").strip("\"")
name = os.path.basename(file)
data=open(file,encoding="utf8").readlines()
color("CYAN")
d=int(input("Процент отличия результата от исходных данных> "))
color("MAGENTA")
acc=int(input("Процент аккуратности (чем больше - тем дольше)> "))
color("GREEN")
print("Перефраз запущен, подождите")
color("YELLOW")
out=data
langs=["ru"]

langs.append(lang_rating[0])
lang_rating.pop(0)
dif=0
times=0
random.seed("".join(data))
while 1:
    times+=1
    if times%(acc*len(langs))==0 and len(langs)>0:
        langs.append(lang_rating[0])
        lang_rating.pop(0)
        times=0
    ru=translate_bigdata(out,"ru")
    dif=(dif+dif+dif+diff("".join(ru),"".join(out)))/4
    #dif=diff(ru,out)
    print("~ Отличие "+str(round(dif*100))+"%","выборка из",len(langs),"языков",end='\r')
    if dif*100>=d:
        with open(os.path.expanduser('~')+"\\desktop\\"+"Новый "+name,"w",encoding="utf-8") as f:
            f.write("".join(ru))
        print()
        break
    """
    with open("new.txt","w",encoding="utf-8") as f:
        f.write(ru)
    """

    out=translate_bigdata(out,random.choice(langs))
color("GREEN")
print("Работа завершена, файл сохранен на рабочем столе")