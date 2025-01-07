from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

def wait_and_click(driver, xpath, wait_time=10):
    element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

def wait_and_send_keys(driver, xpath, value, wait_time=10):
    element = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element.send_keys(value)

current_dir = os.path.dirname(os.path.abspath(__file__))
chromedriver_path = os.path.join(current_dir, "chormedv", "chromedriver.exe")
service = Service(chromedriver_path)

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=service, options=options)

def get_machine_choice():
    while True:
        try:
            print("ESCOLHA AS OPÇÕES:")
            print("1 - Maquina 1")
            print("2 - Maquina 2")
            choice = int(input("Selecione sua opção: "))
            if choice in [1, 2]:
                return choice
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

def login():
    driver.get("https://admin02.autosky.cloud/")
    wait_and_send_keys(driver, '//*[@id="email"]', "----------")
    wait_and_send_keys(driver, '//*[@id="password"]', "------------")
    wait_and_click(driver, '//*[@id="submit-button"]/span[1]')
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

def select_account(machine_choice):
    wait_and_click(driver, '//*[@id="select-partner"]/span[1]/p')
    account_xpath = '//*[@id="option-list-dc7e0ef5-cf5c-4e0a-8af9-3ce8946cecb4"]/td[2]/div' if machine_choice == 1 else '//*[@id="option-list-616dc64a-5295-4f55-800c-b4c92e20dbed"]/td[2]/div'
    wait_and_click(driver, account_xpath)

def publish_update():
    wait_and_click(driver, '//*[@id="btn-options-envs-0"]/span[1]')
    wait_and_click(driver, '//*[@id="btn-servers"]/p')
    wait_and_click(driver, '//*[@id="button-group-label"]/span[1]')
    wait_and_click(driver, '//*[@id="btn-publications"]/span[1]')
    wait_and_click(driver, '//*[@id="root"]/div/div/div[3]/div/div/div[4]/div[3]/div[2]/div[3]/div[3]')
    
    wait_and_send_keys(driver, '//*[@id="operator_name"]', "SSSOLUCOES")
    wait_and_send_keys(driver, '//*[@id="outlined-basic"]', "suporte@sistemasunion.com.br")
    wait_and_send_keys(driver, '//*[@id="root"]/div/div/div[3]/div/div/div[4]/div[3]/div[2]/div[4]/div[1]/div[2]/div/div[4]/div/div/textarea[1]', "ATUALIZAÇÃO SISTEMICA COMBINADA NECESSÁRIA!")
    
    wait_and_click(driver, '//*[@id="submit-button"]')

def main():
    machine_choice = get_machine_choice()
    login()
    select_account(machine_choice)
    publish_update()

    time.sleep(5)

    driver.quit()

if __name__ == "__main__":
    main()
