from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

# Configurar el driver de Chrome automáticamente
chrome_options = Options()
chrome_options.add_argument("--headless")  # Modo sin interfaz gráfica
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Configurar WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Ir a la página de inicio de sesión
driver.get("https://schoolpack.smart.edu.co/idiomas/alumnos.aspx")  # 🔹 Reemplaza con la URL real

# Esperar a que el campo de usuario esté disponible
wait = WebDriverWait(driver, 10)

usuario = wait.until(EC.presence_of_element_located((By.ID, "vUSUCOD")))
contraseña = wait.until(EC.presence_of_element_located((By.ID, "vPASS")))

# Ingresar datos
usuario.send_keys("1034785253")
contraseña.send_keys("Ti1034785253")

# Presionar Enter en el campo de contraseña
contraseña.send_keys(Keys.ENTER)

# ✅ Esperar a que la página de inicio cargue después del login

print("✅ Inicio de sesión exitoso")

# 🔹 Esperar a que aparezca el anuncio (máx. 10 seg) y cerrarlo
try:
    anuncio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "gxp0_cls"))  # 🔹 Cambia esto con el ID real del botón "X"
    )
    anuncio.click()
    print("✅ Anuncio cerrado")
except:
    print("⚠ No apareció ningún anuncio")
#esperar a la iamgen programacion
try:
    imagen = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "IMAGE18"))  # 🔹 Cambia esto con el ID real del botón "X"
    )
    imagen.click()
    print("✅ Programacion Abierta")
    #Programar la clase para el siguiente dia a las 4
    azul = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "W0030Grid1ContainerRow_0001"))  # 🔹 Cambia esto con el ID real del botón "X"
    )
    azul.click()
    print("✅ Estudiante seleccionado")
    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "W0030BUTTON1"))  # 🔹 Cambia esto con el ID real del botón "X"
    )
    boton.click()
    print("✅ Horario Abierto")
    #entrar a la otra ventana
    # Esperar a que el iframe aparezca
    iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "gxp0_ifrm"))
    )

    # Cambiar el foco al iframe
    driver.switch_to.frame(iframe)
    # Esperar a que el select esté disponible
      
    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "vTPEAPROBO"))
    )

  

  
    # Seleccionar la opción "Pendientes por programar"
    select = Select(select_element)
    select.select_by_visible_text("Pendientes por programar")

    #seleccionar la clase siguiente
    time.sleep(1)
    
    clase = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Grid1ContainerRow_0001"))
    )
    clase.click()
    #Click en asignar
    asignar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "BUTTON1"))
    )
    asignar.click()
    driver.switch_to.default_content()
    #asignar dia
    #entrar a la otra ventana
    # Esperar a que el iframe aparezca
    iframe2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "gxp1_ifrm"))
    )

    # Cambiar el foco al iframe
    driver.switch_to.frame(iframe2)
    # Esperar a que el select esté disponible
      
    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "vDIA"))
    )

    # Seleccionar la opción "del segundo dia"
    select = Select(select_element)
    opciones = []
    for option in select.options:
        valor = option.get_attribute("value")
        
        opciones.append(valor)
    
    select.select_by_value(opciones[1])
    if opciones[1]=="7":
        #seleccionar el horario de 3 el sabado
        hora = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Grid1ContainerRow_0006"))
    )
    else:
        
        #seleccionar el horario de 4 y media
        hora = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "Grid1ContainerRow_0006"))
        )
    
    hora.click()
    #confirmar
    confirmar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "BUTTON1"))
    )
    confirmar.click()
    driver.switch_to.default_content()
    print("Clase Programada")
    
    
except:
    print("⚠ No se entro a la programacion")

   
    
    

# 🔹 Mantén el navegador abierto por unos segundos (opcional)
time.sleep(1)

# Cerrar el navegador
driver.quit()
