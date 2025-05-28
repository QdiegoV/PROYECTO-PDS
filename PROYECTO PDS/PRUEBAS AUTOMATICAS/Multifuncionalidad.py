from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Configurar navegador
options = Options()
options.add_argument("--start-maximized")

# Iniciar driver
driver = webdriver.Chrome(service=Service(), options=options)

# Ruta del archivo INICIO.html (AJUSTA si está en otra carpeta)
inicio_path = os.path.abspath("INICIO.html")
inicio_url = f"file:///{inicio_path}"

try:
    # 1. Abrir la página de inicio
    driver.get(inicio_url)
    time.sleep(2)

    # 2. Hacer clic en la noticia de Xabi Alonso
    xabi_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'Xavialonso.html')]"))
    )
    xabi_link.click()
    time.sleep(2)

    # 3. Tomar pantallazo
    driver.save_screenshot("pantallazo_xabi_alonso.png")

    # 4. Volver a la página de inicio
    driver.back()
    time.sleep(2)

finally:
    driver.quit()
