import os

pesquisa = "pesquisar homem aranha sem volta para casa"
pesquisa1 = pesquisa.split()

if pesquisa1[0] == "pesquisar":

    print(pesquisa1)
    pesquisa1.pop(0)
    print(pesquisa1)

    pesquisa1 = "+".join(pesquisa1) 

    url = "https://www.google.com/search?q="+str(pesquisa1)

    os.system(f"start {url}")
