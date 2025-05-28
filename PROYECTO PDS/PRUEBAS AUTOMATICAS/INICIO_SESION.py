from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

# Crear carpeta para screenshots si no existe
os.makedirs("Screenshots Proyecto Sesion", exist_ok=True)

# Configuración del navegador
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

try:
    # Cargar tu sitio local
    driver.get("http://127.0.0.1:3000/SESION.html")
    time.sleep(1)

    # Asegurarse de que el formulario de login esté visible (por defecto lo está)
    # Llenar campos del formulario de inicio de sesión
    driver.find_element(By.ID, "email-login").send_keys("ana.gomez@gmail.com")
    driver.find_element(By.ID, "password-login").send_keys("MiContraseñaSegura123")

    # Tomar screenshot antes de enviar
    driver.save_screenshot("Screenshots Proyecto Sesion/formulario_login_lleno.png")

    # Enviar formulario de inicio de sesión
    driver.find_element(By.CSS_SELECTOR, "#form-login button[type='submit']").click()

    # Esperar a que se procese el inicio de sesión
    time.sleep(2)

    # Tomar screenshot luego del envío
    driver.save_screenshot("Screenshots Proyecto Sesion/formulario_login_enviado.png")

finally:
    input("Presiona Enter para cerrar...")
    driver.quit()
