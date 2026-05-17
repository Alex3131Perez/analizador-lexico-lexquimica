import sys
from antlr4 import *
from QuimicaLexer import QuimicaLexer

def main():
    # Validación de argumento de archivo por terminal
    nombre_archivo = sys.argv[1] if len(sys.argv) > 1 else "quimica.txt"
    
    try:
        input_stream = FileStream(nombre_archivo, encoding='utf-8')
        lexer = QuimicaLexer(input_stream)
        token = lexer.nextToken()
        
        tokens_validos = []
        errores_detectados = []
        
        while token.type != Token.EOF:
            nombre_token = lexer.symbolicNames[token.type]
            
            # 1. Manejo de Errores Léxicos 
            if nombre_token == "ERROR":
                errores_detectados.append(
                    f"Linea {token.line}, Columna {token.column}: Símbolo desconocido '{token.text}' detectado."
                )
            elif nombre_token == "ID_INVALIDO":
                errores_detectados.append(
                    f"Linea {token.line}, Columna {token.column}: Identificador inválido '{token.text}'."
                )
            
            # 2. Clasificación y Traducción de Tokens
            elif nombre_token != "WS":
                categoria = nombre_token
                
                # Mapeo de nombres técnicos a las etiquetas 
                if nombre_token in ["FUNCION", "CONECTOR", "MONO", "DI", "TRI", "TETRA", "PENTA", "HEXA", "HEPTA", "ELEMENTO"]:
                    categoria = "P_Reservada"
                elif nombre_token == "ID":
                    categoria = "ID"
                elif nombre_token == "ASIGNACION":
                    categoria = "OPERADOR"
                elif nombre_token in ["PUNTO_COMA", "COMA", "PAREN_IZQ", "PAREN_DER", "LLAVE_IZQ", "LLAVE_DER"]:
                    categoria = "DELIMITADOR"
                elif nombre_token in ["NUMERO_INT", "NUMERO_FLOAT"]:
                    categoria = "NUMERO"
                
                tokens_validos.append((categoria, token.text))
            
            token = lexer.nextToken()
            
        # --- BLOQUES DE SALIDA TRADUCIDOS ---
        print("Lista de Tokens:")  
        for i, (cat, val) in enumerate(tokens_validos, start=1):
            print(f"  {i}: ({cat}, \"{val}\")")
            
        print("\nLista de Errores:")
        if errores_detectados:
            for err in errores_detectados:
                print(f"  {err}")
        else:
            print("  No se encontraron errores lexicos.")
            
    except Exception as e:
        print(f"Error general al procesar el archivo: {e}")

if __name__ == '__main__':
    main()