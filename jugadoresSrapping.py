import pandas
from bs4 import BeautifulSoup as bs
import requests

num=0
listacompleta=[]

while True:

    url = 'https://sofifa.com/teams?offset='+str(num)
    page = requests.get(url)
    
    if page and num!=960:
        
        links=[]
        soup = bs(page.content, 'html.parser')
        eq = soup.find_all('a')
        string = str(eq)
        while True:
            try:
                indice = string.index("href")
            except:
                break
            i=indice+6
            link=""
            while string[i]!='"':
                link=link+string[i]
                i=i+1
            links.append(link)
            string=string[i:len(string)]

        lenlin = len(links)
        for x in range(lenlin-1, -1, -1):
            if ("?" in links[x]) or "team" not in links[x] or len(links[x])<8:
                links.pop(x)
        
        for x in range(len(links)):
            print(links[x])
            url = 'https://sofifa.com'+links[x]
            page = requests.get(url)

            if page:
         
                linkjug=[]
                soup = bs(page.content, 'html.parser')
                eq = soup.find_all('a', class_='tooltip')
                string = str(eq)
                while True:
                    try:
                        indice = string.index("href")
                    except:
                        break
                    i=indice+6
                    link=""
                    while string[i]!='"':
                        link=link+string[i]
                        i=i+1
                    linkjug.append(link)
                    string=string[i:len(string)]
 
                lenlin = len(linkjug)
                for i in range(lenlin-1,-1,-1):
                    if "player" not in linkjug[i]:
                        linkjug.pop(i)
                for i in range(len(linkjug)):
                    url = 'https://sofifa.com'+linkjug[i]
                    page = requests.get(url)
                    soup = bs(page.content, 'html.parser')
                    
                    listajug=[]
                    
                    name= soup.find_all('div', class_='info')
                    
                    juga=name[0].text
                    
                    indeex=0
                    
                    while(juga[indeex]!="\n"):
                        indeex=indeex+1
                        
                    esta=False

                    for q in range(len(listacompleta)):
                        if juga[:indeex] == str(listacompleta[q][0]):
                            esta=True
                    
                    if not esta:
                    
                        #Variable 0
                        listajug.append(juga[:indeex])
                        
                        jug1=soup.find_all('div', class_='columns')
                        jug2=jug1[0].find_all('div', class_='column col-12')
                        jug3=jug2[2].find_all('div', class_='column col-3')
                        seleccion=False
                        if(len(jug3))==4:
                            seleccion=True
                        
                        jug=soup.find_all('div', class_='column col-3')
                        
                        #Variable 1
                        listajug.append(jug[0].text[0:2])
                        
                        #Variable 2
                        listajug.append(jug[1].text[0:2])
                        
                        #Variable 3
                        juga=jug[2].text
                        indeex=juga.index('€')
                        listajug.append("")
                        w=indeex+1
                        while juga[w]!='V':
                            listajug[3]=listajug[3]+juga[w]
                            w=w+1
                            
                        #Variable 4
                        juga=jug[3].text
                        indeex=juga.index('€')
                        listajug.append("")
                        w=indeex+1
                        while juga[w]!='W':
                            listajug[4]=listajug[4]+juga[w]
                            w=w+1
                            
                        #Variables 5 y 6
                        juga=jug[4].text
                        indeex=juga.index('★')
                        w=indeex-2
                        listajug.append(juga[w])
                        juga=juga[indeex+3:len(juga)]
                        indeex=juga.index('★')
                        w=indeex-2
                        listajug.append(juga[w])
                        
                        #Variable 7
                        juga=jug[6].text[2:len(jug[6].text)]
                        indeex=juga.index("\n")
                        listajug.append(juga[0:indeex])
                        
                        ##--
                        z=7
                        if seleccion:
                            z=8
                        ##--
                        #Variables 8,9,10,11,12(Datos de Ataque)
                        juga=jug[z].text
                        cont=0
                        
                        while cont!=5:
                            cad=""
                            ranlen=len(juga)
                            for j in range(ranlen):
                                if juga[j].isdigit():
                                    k=j
                                    while juga[k].isdigit():
                                        cad=cad+juga[k]
                                        k=k+1
                                    listajug.append(cad)
                                    juga=juga[k:len(juga)]
                                    break
                            cont=cont+1
                        z=z+1
                        #Variables 13,14,15,16,17(Datos de Regate)
                        juga=jug[8].text
                        cont=0
                        
                        while cont!=5:
                            cad=""
                            ranlen=len(juga)
                            for j in range(ranlen):
                                if juga[j].isdigit():
                                    k=j
                                    while juga[k].isdigit():
                                        cad=cad+juga[k]
                                        k=k+1
                                    listajug.append(cad)
                                    juga=juga[k:len(juga)]
                                    break
                            cont=cont+1
                        z=z+1
                        #Variables 18,19,20,21,22(Datos de Movimiento)
                        juga=jug[9].text
                        cont=0
                        
                        while cont!=5:
                            cad=""
                            ranlen=len(juga)
                            for j in range(ranlen):
                                if juga[j].isdigit():
                                    k=j
                                    while juga[k].isdigit():
                                        cad=cad+juga[k]
                                        k=k+1
                                    listajug.append(cad)
                                    juga=juga[k:len(juga)]
                                    break
                            cont=cont+1
                        
                        z=z+1
                        #Variables 23,24,25,26,27(Datos de Potencia)
                        juga=jug[10].text
                        cont=0
                        
                        while cont!=5:
                            cad=""
                            ranlen=len(juga)
                            for j in range(ranlen):
                                if juga[j].isdigit():
                                    k=j
                                    while juga[k].isdigit():
                                        cad=cad+juga[k]
                                        k=k+1
                                    listajug.append(cad)
                                    juga=juga[k:len(juga)]
                                    break
                            cont=cont+1
                        z=z+1
                        #Variables 28,29,30,31,32,33(Datos de Mentalidad)
                        juga=jug[11].text
                        cont=0
                        
                        while cont!=6:
                            cad=""
                            ranlen=len(juga)
                            for j in range(ranlen):
                                if juga[j].isdigit():
                                    k=j
                                    while juga[k].isdigit():
                                        cad=cad+juga[k]
                                        k=k+1
                                    listajug.append(cad)
                                    juga=juga[k:len(juga)]
                                    break
                            cont=cont+1
                        z=z+1
                        #Variables 34,35,36(Datos de Defensa)
                        juga=jug[12].text
                        cont=0
                        
                        while cont!=3:
                            cad=""
                            ranlen=len(juga)
                            for j in range(ranlen):
                                if juga[j].isdigit():
                                    k=j
                                    while juga[k].isdigit():
                                        cad=cad+juga[k]
                                        k=k+1
                                    listajug.append(cad)
                                    juga=juga[k:len(juga)]
                                    break
                            cont=cont+1
                        
                        z=z+1
                        #Variables 37,38,39,40,41(Datos de Portero)
                        juga=jug[13].text
                        cont=0
                        
                        while cont!=5:
                            cad=""
                            ranlen=len(juga)
                            for j in range(ranlen):
                                if juga[j].isdigit():
                                    k=j
                                    while juga[k].isdigit():
                                        cad=cad+juga[k]
                                        k=k+1
                                    listajug.append(cad)
                                    juga=juga[k:len(juga)]
                                    break
                            cont=cont+1
                        listacompleta.append(listajug)
        num=num+60
        
        df = pandas.DataFrame(listacompleta)

        df.to_csv('final'+str(num)+'.csv')
    else:      
        break
    


df = pandas.DataFrame(listacompleta)

df.to_csv('final.csv')









