# Passo a passo do projeto

# importando as bibliotecas
import pandas as pd     
import pyautogui
import time 


# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

# define o tempo de espera entre os comandos do Pyautogui
pyautogui.PAUSE = 0.3

# Passo 1: entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=801, y=383)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espera o site carregar 
time.sleep(3)

# Passo 2: fazer login 
pyautogui.click(x=831, y=369)
pyautogui.write("joycemuitolinda@gmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenha")
pyautogui.press("tab")
pyautogui.press("enter")


# Passo 3: importar a base de dados
tabela = pd.read_csv("produtos.csv")
print(tabela)


# Passo 4: cadastrar um produto
# aqui precisamos percorrer as linhas da tabela
# para cada linha vamos cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=849, y=249)
    pyautogui.write(str(tabela.loc[linha, "codigo"])) # pega o codigo da tabela e escreve no campo
    pyautogui.press("tab") # passa para o proximo campo
    pyautogui.write(str(tabela.loc[linha, "marca"])) 
    pyautogui.press("tab") 
    pyautogui.write(str(tabela.loc[linha, "tipo"])) 
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"])) 
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"])) 
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"])) 
    pyautogui.press("tab") 
    if not pd.isna(tabela.loc[linha, "obs"]): # verfica se existe info em obs, caso não, pula
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.click(x=646, y=634)
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim







