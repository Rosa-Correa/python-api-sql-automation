import requests
import sqlite3

def probar_persistencia_datos():
    print("--- Iniciando prueba de datos para Grupo X---")
    
    # 1. Obtener datos de la API
    try:
        url = "https://jsonplaceholder.typicode.com/posts/1"
        respuesta = requests.get(url)
        datos_api = respuesta.json()
    except Exception as e:
        print(f"Error de conexión: {e}")
        return

    # 2. Guardar y verificar en SQL (Demostrando tus certificaciones Oracle)
    try:
        conexion = sqlite3.connect('obras.db')
        cursor = conexion.cursor()
        
        # Reiniciar la tabla para asegurar que no esté vacía en la prueba
        cursor.execute("DROP TABLE IF EXISTS proyectos")
        cursor.execute("CREATE TABLE proyectos (id INTEGER PRIMARY KEY, titulo TEXT, fuente TEXT)")
        
        # Insertar el dato real de la API
        cursor.execute("INSERT INTO proyectos (titulo, fuente) VALUES (?, ?)", 
                       (datos_api['title'], "API Externa"))
        
        conexion.commit()
        
        # 3. AUTO-PRUEBA: Consultar la base de datos de inmediato
        cursor.execute("SELECT * FROM proyectos")
        resultado = cursor.fetchone()
        
        if resultado:
            print(f"ÉXITO: Se encontró el dato en la DB -> {resultado[1]}")
        
        conexion.close()
    except Exception as e:
        print(f"Error en SQL: {e}")

if __name__ == "__main__":
    probar_persistencia_datos()