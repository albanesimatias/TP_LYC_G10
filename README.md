# TP COMPILADOR UNLaM 2024

## Integrantes
- Integrante 1: Matias Albanesi
- Integrante 2: Matias Gallues
- Integrante 3: Agustin Federico

## Instalacion y ejecución

**Requisitos**
   -Python 3.12
   -pip
   -'ply'

Para ejecutar el codigo, sigue los siguientes pasos:

1. **Descargar el zip del tag 1.0.0**

2. **Instalar dependencias**

   ```bash
   pip install ply
   ```

3. **Ejecutar**

   lyc-compiler.exe

   El mismo ejecutara en primera instancia un test del lexico donde verificamos que reconosca los tokens correctamente y luego se ejecutara automaticamente el parser con su propio test el cual mostrara las reglas que se van aplicando. Los archivo de tests estan dentro de la carpeta /TESTS/

   Tambien se puede ejecutar directamente el lyc-compiler.py con el siguiente comando por consola.
   ```bash
   python lyc-compiler.py
   ```