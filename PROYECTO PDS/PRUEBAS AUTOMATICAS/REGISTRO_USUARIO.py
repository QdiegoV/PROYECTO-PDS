from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

# Crear carpeta para screenshots si no existe
os.makedirs("Screenshots Proyecto Registro", exist_ok=True)

# Configuración del navegador
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

try:
    # Cargar tu sitio local
    driver.get("http://127.0.0.1:3000/SESION.html")
    time.sleep(1)  # Espera ligera para que cargue bien

    # Mostrar formulario de registro haciendo clic en el enlace "Regístrate"
    driver.find_element(By.ID, "mostrar-registro").click()
    time.sleep(1)

    # Llenar campos del formulario de registro
    driver.find_element(By.ID, "nombre").send_keys("Ana Gómez")
    driver.find_element(By.ID, "email").send_keys("ana.gomez@gmail.com")
    driver.find_element(By.ID, "password").send_keys("MiContraseñaSegura123")

    # Tomar screenshot antes de enviar
    driver.save_screenshot("Screenshots Proyecto Registro/formulario_registro_lleno.png")

    # Enviar formulario
    driver.find_element(By.CSS_SELECTOR, "#form-registro button[type='submit']").click()

    # Esperar un poco para que se procese el envío (simulación)
    time.sleep(2)

    # Tomar screenshot luego del envío
    driver.save_screenshot("Screenshots Proyecto Registro/formulario_registro_enviado.png")

finally:
    input("Presiona Enter para cerrar...")
    driver.quit()

    