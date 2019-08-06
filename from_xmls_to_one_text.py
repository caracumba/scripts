import glob, re, os

""" Скрипт вынимает из всех xml-файлов содержимое тэга text
и объединяет их все в один текстовый файл
"""
        
num=0
name=input("enter the name of the decease: ") 
name_txt=name+'.txt'
outfile = open(name_txt,'w',encoding='utf-8') # создается файл выдачи 


for files in glob.glob(r"ЗДЕСЬ ПРОПИСЫВАЕТСЯ ПУТЬ К ФАЙЛУ\ПАПКА С XNL\*\*"):
    file=open(files, encoding='utf-8')
    name=re.findall(r"\\([^\\]*)\.xml",str(files))
    name=str(name).strip("''[]\\")
    text=file.read().split("<TEXT>")
    text=text[1].split("</TEXT>")
    num+=1
    file.close()
    outfile = open(name_txt,'r',encoding='utf-8')
    text_outfile=outfile.read()
    outfile.close()
    outfile = open(name_txt,'w',encoding='utf-8')
    outfile.write(text_outfile + "\n" +name + "\n" + str(text[0].strip()) +"\n\n")
    outfile.close()

print(num)
outfile.close()


