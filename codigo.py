import pyautogui
import time

# pyauthogui.click -> clicar em algum lugar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever algo
# pyautogui.hotkey -> pressionar uma combinação de teclas

pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema da empresa
# abrir o Chrome

pyautogui.press("win")
pyautogui.write("chrome") 
pyautogui.press("enter")

# digitar o site

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(3)

# Passo 2: Fazer login no sistema 

# Preencher email
pyautogui.click(x=704, y=380)
pyautogui.write("pythonimpressLogitech@gmail.com")

# preencher a senha
pyautogui.press("tab")
pyautogui.write("123456789")

# botão logar 

pyautogui.press("tab")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(3)

# Passo 3: importar a base de dados para o sistema
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto

for linha in tabela.index:
  pyautogui.click(x=703, y=257)

  codigo = tabela.loc[linha, "codigo"]
  pyautogui.write(codigo)

  pyautogui.press("tab")
  marca = tabela.loc[linha, "marca"]
  pyautogui.write(marca)

  pyautogui.press("tab")
  tipo = tabela.loc[linha, "tipo"]
  pyautogui.write(tipo)

  pyautogui.press("tab")
  categoria = str(tabela.loc[linha, "categoria"])
  pyautogui.write(categoria)

  pyautogui.press("tab")
  preco_unitario = str(tabela.loc[linha, "preco_unitario"])
  pyautogui.write(preco_unitario) 

  pyautogui.press("tab")
  custo = str(tabela.loc[linha, "custo"])
  pyautogui.write(custo)

  pyautogui.press("tab")
  obs = str(tabela.loc[linha, "obs"])
  
  if obs != "nan":  
      pyautogui.write(obs)

  pyautogui.press("tab")
  pyautogui.press("enter")


  pyautogui.scroll(10000)


# Passo 5: Repetir todos os produtos

