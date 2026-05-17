# Generated from Quimica.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,41,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,1,1,1,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,
        1,2,1,3,3,3,30,8,3,1,3,1,3,1,3,3,3,35,8,3,1,3,1,3,1,4,1,4,1,4,0,
        0,5,0,2,4,6,8,0,1,1,0,3,9,39,0,11,1,0,0,0,2,21,1,0,0,0,4,23,1,0,
        0,0,6,29,1,0,0,0,8,38,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,
        1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,15,1,0,0,0,15,16,5,0,0,1,
        16,1,1,0,0,0,17,22,3,4,2,0,18,19,3,6,3,0,19,20,5,12,0,0,20,22,1,
        0,0,0,21,17,1,0,0,0,21,18,1,0,0,0,22,3,1,0,0,0,23,24,5,18,0,0,24,
        25,5,11,0,0,25,26,3,6,3,0,26,27,5,12,0,0,27,5,1,0,0,0,28,30,3,8,
        4,0,29,28,1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,32,5,1,0,0,32,34,
        5,2,0,0,33,35,3,8,4,0,34,33,1,0,0,0,34,35,1,0,0,0,35,36,1,0,0,0,
        36,37,5,10,0,0,37,7,1,0,0,0,38,39,7,0,0,0,39,9,1,0,0,0,4,13,21,29,
        34
    ]

class QuimicaParser ( Parser ):

    grammarFileName = "Quimica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'de'", "'mono'", "'di'", 
                     "'tri'", "'tetra'", "'penta'", "'hexa'", "'hepta'", 
                     "<INVALID>", "'='", "';'", "','", "'('", "')'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "FUNCION", "CONECTOR", "MONO", "DI", 
                      "TRI", "TETRA", "PENTA", "HEXA", "HEPTA", "ELEMENTO", 
                      "ASIGNACION", "PUNTO_COMA", "COMA", "PAREN_IZQ", "PAREN_DER", 
                      "LLAVE_IZQ", "LLAVE_DER", "ID", "ID_INVALIDO", "NUMERO_FLOAT", 
                      "NUMERO_INT", "WS", "ERROR" ]

    RULE_programa = 0
    RULE_instruccion = 1
    RULE_asignacion = 2
    RULE_compuesto = 3
    RULE_prefijo = 4

    ruleNames =  [ "programa", "instruccion", "asignacion", "compuesto", 
                   "prefijo" ]

    EOF = Token.EOF
    FUNCION=1
    CONECTOR=2
    MONO=3
    DI=4
    TRI=5
    TETRA=6
    PENTA=7
    HEXA=8
    HEPTA=9
    ELEMENTO=10
    ASIGNACION=11
    PUNTO_COMA=12
    COMA=13
    PAREN_IZQ=14
    PAREN_DER=15
    LLAVE_IZQ=16
    LLAVE_DER=17
    ID=18
    ID_INVALIDO=19
    NUMERO_FLOAT=20
    NUMERO_INT=21
    WS=22
    ERROR=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(QuimicaParser.EOF, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuimicaParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(QuimicaParser.InstruccionContext,i)


        def getRuleIndex(self):
            return QuimicaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = QuimicaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.instruccion()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 263162) != 0)):
                    break

            self.state = 15
            self.match(QuimicaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(QuimicaParser.AsignacionContext,0)


        def compuesto(self):
            return self.getTypedRuleContext(QuimicaParser.CompuestoContext,0)


        def PUNTO_COMA(self):
            return self.getToken(QuimicaParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return QuimicaParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)




    def instruccion(self):

        localctx = QuimicaParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.asignacion()
                pass
            elif token in [1, 3, 4, 5, 6, 7, 8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.compuesto()
                self.state = 19
                self.match(QuimicaParser.PUNTO_COMA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(QuimicaParser.ID, 0)

        def ASIGNACION(self):
            return self.getToken(QuimicaParser.ASIGNACION, 0)

        def compuesto(self):
            return self.getTypedRuleContext(QuimicaParser.CompuestoContext,0)


        def PUNTO_COMA(self):
            return self.getToken(QuimicaParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return QuimicaParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = QuimicaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(QuimicaParser.ID)
            self.state = 24
            self.match(QuimicaParser.ASIGNACION)
            self.state = 25
            self.compuesto()
            self.state = 26
            self.match(QuimicaParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompuestoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(QuimicaParser.FUNCION, 0)

        def CONECTOR(self):
            return self.getToken(QuimicaParser.CONECTOR, 0)

        def ELEMENTO(self):
            return self.getToken(QuimicaParser.ELEMENTO, 0)

        def prefijo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuimicaParser.PrefijoContext)
            else:
                return self.getTypedRuleContext(QuimicaParser.PrefijoContext,i)


        def getRuleIndex(self):
            return QuimicaParser.RULE_compuesto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompuesto" ):
                listener.enterCompuesto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompuesto" ):
                listener.exitCompuesto(self)




    def compuesto(self):

        localctx = QuimicaParser.CompuestoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_compuesto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1016) != 0):
                self.state = 28
                self.prefijo()


            self.state = 31
            self.match(QuimicaParser.FUNCION)
            self.state = 32
            self.match(QuimicaParser.CONECTOR)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1016) != 0):
                self.state = 33
                self.prefijo()


            self.state = 36
            self.match(QuimicaParser.ELEMENTO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrefijoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MONO(self):
            return self.getToken(QuimicaParser.MONO, 0)

        def DI(self):
            return self.getToken(QuimicaParser.DI, 0)

        def TRI(self):
            return self.getToken(QuimicaParser.TRI, 0)

        def TETRA(self):
            return self.getToken(QuimicaParser.TETRA, 0)

        def PENTA(self):
            return self.getToken(QuimicaParser.PENTA, 0)

        def HEXA(self):
            return self.getToken(QuimicaParser.HEXA, 0)

        def HEPTA(self):
            return self.getToken(QuimicaParser.HEPTA, 0)

        def getRuleIndex(self):
            return QuimicaParser.RULE_prefijo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefijo" ):
                listener.enterPrefijo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefijo" ):
                listener.exitPrefijo(self)




    def prefijo(self):

        localctx = QuimicaParser.PrefijoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_prefijo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1016) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





