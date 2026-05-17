# Generated from Quimica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .QuimicaParser import QuimicaParser
else:
    from QuimicaParser import QuimicaParser

# This class defines a complete listener for a parse tree produced by QuimicaParser.
class QuimicaListener(ParseTreeListener):

    # Enter a parse tree produced by QuimicaParser#programa.
    def enterPrograma(self, ctx:QuimicaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by QuimicaParser#programa.
    def exitPrograma(self, ctx:QuimicaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by QuimicaParser#instruccion.
    def enterInstruccion(self, ctx:QuimicaParser.InstruccionContext):
        pass

    # Exit a parse tree produced by QuimicaParser#instruccion.
    def exitInstruccion(self, ctx:QuimicaParser.InstruccionContext):
        pass


    # Enter a parse tree produced by QuimicaParser#asignacion.
    def enterAsignacion(self, ctx:QuimicaParser.AsignacionContext):
        pass

    # Exit a parse tree produced by QuimicaParser#asignacion.
    def exitAsignacion(self, ctx:QuimicaParser.AsignacionContext):
        pass


    # Enter a parse tree produced by QuimicaParser#compuesto.
    def enterCompuesto(self, ctx:QuimicaParser.CompuestoContext):
        pass

    # Exit a parse tree produced by QuimicaParser#compuesto.
    def exitCompuesto(self, ctx:QuimicaParser.CompuestoContext):
        pass


    # Enter a parse tree produced by QuimicaParser#prefijo.
    def enterPrefijo(self, ctx:QuimicaParser.PrefijoContext):
        pass

    # Exit a parse tree produced by QuimicaParser#prefijo.
    def exitPrefijo(self, ctx:QuimicaParser.PrefijoContext):
        pass



del QuimicaParser