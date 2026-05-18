\# LexQuimica - Analizador Léxico

Este proyecto consiste en el diseño e implementación de un analizador léxico funcional para el lenguaje de dominio específico LexQuimica, especializado en el procesamiento y traducción de nomenclatura química sistemática (IUPAC) a flujos de tokens estructurados.



\## Información del Curso

\* \*\*Materia:\*\* Programación de Sistemas de Base 1

\* \*\*Institución:\*\* Universidad Autónoma de Tamaulipas

\* \*\*Semestre:\*\* 2026-1

\* \*\*Profesor:\*\* Dr. Dante Adolfo Muñoz Quintero



\## Integrantes del Equipo

* Perez Castan Alejandro Emmanuel - 2223330182

\* Sanchez Garcia Gael Antonio - 2223330195

\* Alejandre Mar Sergio Adrian - 2223330133



\## Descripción del Lenguaje

LexQuimica es un lenguaje de programación de dominio específico diseñado con fines educativos para permitir la asignación lógica de variables y el análisis gramatical de compuestos químicos inorgánicos continuos. Sigue una sintaxis imperativa rígida donde cada declaración e instrucción científica debe concluir de forma explícita con un delimitador de punto y coma.



\## Tokens Reconocidos

El analizador léxico classifies los componentes válidos en las siguientes categorías de tokens estándar:

\* `P\_Reservada`: Prefijos numéricos griegos, conectores de enlace y funciones químicas base.

\* `ID`: Identificadores válidos para variables formados por combinaciones de letras, dígitos o guiones bajos.

\* `OPERADOR`: Símbolos de asignación y transferencia de datos (`=`).

\* `DELIMITADOR`: Caracteres de puntuación y control de alcance espacial (`;`, `,`, `(`, `)`, `{`, `}`).

\* `NUMERO`: Constantes numéricas para valores numéricos enteros o decimales de punto flotante.





\### Prerrequisitos

Es necesario contar con Python 3 instalado y el entorno runtime de ANTLR v4 para Python. Puedes instalar la librería necesaria mediante el siguiente comando en la terminal:

```bash

pip install antlr4-python3-runtime



\## Cómo ejecutar

Si realizas modificaciones en las reglas léxicas, regenera los archivos del compilador ejecutando el comando de ANTLR dentro de la carpeta del proyecto:

antlr4 -Dlanguage=Python3 grammar/Quimica.g4 -o src/



Para ejecutar el analizador léxico sobre tu archivo de pruebas químicas, invoca el script principal desde tu consola de comandos pasando la ruta del archivo de texto como argumento:

python src/main.py tests/valid/quimica.txt



