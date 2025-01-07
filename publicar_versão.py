from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))
chromedriver_path = os.path.join(current_dir, "chormedv", "chromedriver.exe")
service = Service(chromedriver_path)
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=service, options=options)
liberado = 5
valor = None 
while liberado == 5:
    print("ESCOLHA AS OPÇÕES:")
    print("1 - Maquina 1")
    print("2 - Maquina 2")
    try:
        valor = int(input("Selecione sua opção: "))  
        if valor == 1 or valor == 2:
            liberado = 3  # Sai do loop ao selecionar uma opção válida
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")
 

# Abrir o site
driver.get("https://admin02.autosky.cloud/")

# Aguardar o carregamento do campo de login
campo_login = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="email"]')
    )
)

# Localizar o campo de senha
campo_senha = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="password"]')
    )
)

# Preencher os campos
campo_login.send_keys("----------")
campo_senha.send_keys("------------")

# Localizar o botão de login
botao_login = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="submit-button"]/span[1]')
    )
)



time.sleep(2)



# Clicar no botão de login
botao_login.click()
 
# Aguardar o processamento (opcional)
time.sleep(5)

# Localizar o botão de selecionar conta
botao_selecionarconta= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="select-partner"]/span[1]/p')
    )
)

botao_selecionarconta.click()

time.sleep(2)
botao_SSSolucoes= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="option-list-dc7e0ef5-cf5c-4e0a-8af9-3ce8946cecb4"]/td[2]/div')
    )
)

botao_kaistudo= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="option-list-616dc64a-5295-4f55-800c-b4c92e20dbed"]/td[2]/div')
    )
)


if valor == 1:
    botao_SSSolucoes.click()
else:
    botao_kaistudo.click()

 

time.sleep(2)
# 


trespontos= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="btn-options-envs-0"]/span[1]')
    )
)

trespontos.click()
time.sleep(0.7)


servidores= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="btn-servers"]/p')
    )
)

servidores.click()

time.sleep(4.5)

acoes= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="button-group-label"]/span[1]')
    )
)

acoes.click()

publicacoes= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="btn-publications"]/span[1]')
    )
)
publicacoes.click()

time.sleep(2)


reconexao= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div/div[4]/div[3]/div[2]/div[3]/div[3]')
    )
)
reconexao.click()

seunome= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="operator_name"]')
    )
)
mensagemusuario= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div/div[4]/div[3]/div[2]/div[4]/div[1]/div[2]/div/div[4]/div/div/textarea[1]')
    )
)
email= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="outlined-basic"]')
    )
)

seunome.send_keys("SSSOLUCOES")
email.send_keys("suporte@sistemasunion.com.br")
mensagemusuario.send_keys("ATUALIZAÇÃO SISTEMICA COMBINADA NECESSÁRIA!")

publicar= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="submit-button"]')
    )
)

time.sleep(1.5)
publicar.click()

time.sleep(22222222)
# Fechar o navegador
driver.quit()


