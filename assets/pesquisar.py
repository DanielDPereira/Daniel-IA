import os

pesquisa = "pesquisar homem aranha sem volta para casa"
pesquisa = pesquisa.split()

print(pesquisa)
pesquisa.pop(0)
print(pesquisa)

pesquisa = "+".join(pesquisa) 

url = "https://www.google.com/search?q="+str(pesquisa)

os.system(f"start {url}")
