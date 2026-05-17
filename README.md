\# \[cite\_start]LexQuimica - Analizador Léxico \[cite: 115]

\[cite\_start]Este proyecto consiste en el diseño e implementación de un analizador léxico funcional para el lenguaje de dominio específico LexQuimica, especializado en el procesamiento y traducción de nomenclatura química sistemática (IUPAC) a flujos de tokens estructurados\[cite: 116].



\## \[cite\_start]Información del Curso \[cite: 117]

\* \[cite\_start]\*\*Materia:\*\* Programación de Sistemas de Base 1\[cite: 118].

\* \[cite\_start]\*\*Institución:\*\* Universidad Autónoma de Tamaulipas\[cite: 118].

\* \[cite\_start]\*\*Semestre:\*\* 2026-1\[cite: 119].

\* \*\*Profesor:\*\* Dr. \[cite\_start]Dante Adolfo Muñoz Quintero\[cite: 120].



\## \[cite\_start]Integrantes del Equipo \[cite: 121]

\* \[cite\_start]Perez Castan Alejandro Emmanuel - \[Matrícula]2223330182 \[cite: 122]

\* \[cite\_start]Sanchez Garcia Gael Antonio - \[Matrícula]2223330195 \[cite: 122]

\* \[cite\_start]Alejandre Mar Sergio Adrian - \[Matrícula]2223330133 \[cite: 122]



\## \[cite\_start]Descripción del Lenguaje \[cite: 123]

LexQuimica es un lenguaje de programación de dominio específico diseñado con fines educativos para permitir la asignación lógica de variables y el análisis gramatical de compuestos químicos inorgánicos continuos. \[cite\_start]Sigue una sintaxis imperativa rígida donde cada declaración e instrucción científica debe concluir de forma explícita con un delimitador de punto y coma\[cite: 124].



\## \[cite\_start]Tokens Reconocidos \[cite: 125]

\[cite\_start]El analizador léxico clasifica los componentes válidos en las siguientes categorías de tokens estándar\[cite: 126]:

\* \[cite\_start]`P\_Reservada`: Prefijos numéricos griegos, conectores de enlace y funciones químicas base\[cite: 126].

\* \[cite\_start]`ID`: Identificadores válidos para variables formados por combinaciones de letras, dígitos o guiones bajos\[cite: 126].

\* \[cite\_start]`OPERADOR`: Símbolos de asignación y transferencia de datos (`=`)\[cite: 126].

\* \[cite\_start]`DELIMITADOR`: Caracteres de puntuación y control de alcance espacial (`;`, `,`, `(`, `)`, `{`, `}`)\[cite: 126].

\* \[cite\_start]`NUMERO`: Constantes numéricas para valores numéricos enteros o decimales de punto flotante\[cite: 126].



\## \[cite\_start]Cómo ejecutar \[cite: 127]



\### Prerrequisitos

Es necesario contar con Python 3 instalado y el entorno runtime de ANTLR v4 para Python. \[cite\_start]Puedes instalar la librería necesaria mediante el siguiente comando en la terminal:

```bash

pip install antlr4-python3-runtime

