grammar Quimica;

// --- REGLAS DEL PARSER ---
// Permite procesar tanto asignaciones a variables como compuestos sueltos
programa : instruccion+ EOF ;

instruccion : asignacion
            | compuesto PUNTO_COMA
            ;

asignacion : ID ASIGNACION compuesto PUNTO_COMA ;

compuesto : prefijo? FUNCION CONECTOR prefijo? ELEMENTO ;

prefijo   : MONO | DI | TRI | TETRA | PENTA | HEXA | HEPTA ;


// --- REGLAS DEL LEXER ---

// Palabras reservadas de Química (Requisito: Palabras reservadas)
FUNCION   : 'oxido' | 'óxido' | 'xido' | 'hidruro' | 'hidroxido' | 'hidróxido' ;
CONECTOR  : 'de' ;

// Prefijos de cantidad
MONO      : 'mono' ;
DI        : 'di' ;
TRI       : 'tri' ;
TETRA     : 'tetra' ;
PENTA     : 'penta' ;
HEXA      : 'hexa' ;
HEPTA     : 'hepta' ;

// Elementos químicos
ELEMENTO  : 'hierro' | 'sodio' | 'calcio' | 'magnesio' | 'aluminio' | 'carbono' | 'cloro' ;

// Operadores y Delimitadores (Requisito: Operadores y Delimitadores)
ASIGNACION : '=' ;
PUNTO_COMA : ';' ;
COMA       : ',' ;
PAREN_IZQ  : '(' ;
PAREN_DER  : ')' ;
LLAVE_IZQ  : '{' ;
LLAVE_DER  : '}' ;

// Identificadores válidos (Requisito: Letras, dígitos o guiones bajos)
ID : [a-zA-Z_][a-zA-Z0-9_]* ;

// Identificadores inválidos (Requisito: Detección de IDs que inician con número)
ID_INVALIDO : [0-9]+[a-zA-Z_][a-zA-Z0-9_]* ;

// Constantes Numéricas (Requisito: Enteros y flotantes)
NUMERO_FLOAT : [0-9]+ '.' [0-9]+ ;
NUMERO_INT   : [0-9]+ ;

// Espacios en blanco e ignorados
WS        : [ \t\r\n]+ -> skip ;

// Símbolos desconocidos (Requisito: Captura de caracteres no permitidos)
ERROR     : . ;