import os

pesquisa = "homem aranha sem volta para casa"
pesquisa = pesquisa.split()
print(pesquisa)

pesquisa = "+".join(pesquisa) 

print(pesquisa)

src = "https://www.google.com/search?q="+str(pesquisa)

os.system(f"start {src}")
