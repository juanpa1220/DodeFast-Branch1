import ply.yacc as yacc
import os
import codecs
from pip._vendor.distlib.compat import raw_input
from LexicalAnalysis.LexicalAnalizer import tokens
from LexicalAnalysis.LexicalAnalizer import lexicalAnalizer
from SemanticAnalysis.SemanticAnalizer import *

from sys import stdin


def p_Start(p):
    '''
    Start : code
    '''
    iniciarEjecucion(p[1])


def p_Code(p):
    '''
    code : INICIO DOSPUNTOS cuerpo FIN PUNTOCOMA procedimiento
    '''
    p[0] = ("INICIO",p[3], p[6])

def p_cuerpo_empty(p):
    '''
    cuerpo : empty
    '''
    p[0] = None


def p_cuerpo(p):
    '''
    cuerpo : variable cuerpo
            | expresion cuerpo
    '''
    if p[2] == None:
        p[0] = (p[1],)
    else:
        p[0] = (p[1],) + p[2]


def p_Variable(p):
    '''
    variable : variable1
            | variable2

    '''

    p[0] = (p[1])


def p_Variable1(p):
    '''
    variable1 : DCL ID PUNTOCOMA
    '''
    p[0] = ("DCL", p[2], p[3])

    #variable1(p[2])


def p_Variable2(p):
    '''
    variable2 : DCL ID DEFAULT NUMERO PUNTOCOMA
    '''
    p[0] = (p[1], p[2], p[3], p[4])

    #variable2(p[2], p[4])


def p_expresion_empty(p):
    '''
    expresion : empty
        '''
    p[0] = None

def p_expresion(p):
    '''
    expresion : condicion1 expresion
            | condicion2 expresion
            | repita expresion
            | hacer expresion
            | funcion expresion
            | llamarProc expresion

    '''
    if (p[2] != None):
        p[0] = (p[1], ) + p[2]
    else:
        p[0] = p[1]


def p_condicion1(p):
    '''
    condicion1 : ENCASO cond1Aux1 FINENCASO PUNTOCOMA
    '''
    p[0] = (p[1],p[2],p[3])


def p_cond1Aux1(p):
    '''
    cond1Aux1 : cond1Aux2 SINO LLAVE_IZQ expresion LLAVE_DER
            | empty empty empty empty empty
    '''
    if (p[5] != None):
        p[0] = (p[1], p[2], p[4])
    else:
        p[0] = tuple(p[1])

    #condicion1(p[0], "")

def p_cond1Aux2_empty(p):
    '''
    cond1Aux2 : empty
        '''
    p[0] = None

def p_cond1Aux2(p):
    '''
    cond1Aux2 : CUANDO ID condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond1Aux2

    '''
    if p[9] != None:

        p[0] =  ((p[1], p[2], p[3], p[4], p[5], p[7]),) + p[9]
    elif p[9] == None:

        p[0] = ((p[1], p[2], p[3], p[4], p[5], p[7]), ) + ()



def p_condicion2(p):
    '''
    condicion2 : ENCASO ID cond2Aux1 FINENCASO PUNTOCOMA
    '''
    p[0] = (p[1], p[2], p[3], p[4])
    #condicion2(p[0])


def p_cond2Aux1(p):
    '''
    cond2Aux1 : cond2Aux2 SINO LLAVE_IZQ expresion LLAVE_DER
                | empty empty empty empty empty
    '''
    if (p[5] != None):
        p[0] = (p[1], p[2], p[4])
    else:
        p[0] = p[1]


def p_cond2Aux2(p):
    '''
        cond2Aux2 : CUANDO  condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond2Aux2
                | empty empty empty empty empty empty empty empty
        '''
    if p[8] != None:
        p[0] = (p[1], p[2], p[3], p[4], p[6], p[8])
    elif p[8] == None and p[1] != None:
        p[0] = (p[1], p[2], p[3], p[4], p[6])
    elif p[1] == None:
        p[0] = p[1]


def p_condicion(p):
    '''
    condicion : IGUAL
              | MAYOR
              | MENOR
              | DIFERENTE
              | MAYORIGUAL
              | MENORIGUAL
    '''

    p[0] = p[1]


def p_sentencia(p):
    '''
    sentencia : ID
               | NUMERO
    '''
    p[0] = p[1]


def p_repita(p):
    '''
     repita : REPITA LLAVE_IZQ expresion LLAVE_DER HASTAENCONTRAR ID condicion sentencia PUNTOCOMA
    '''
    p[0] = (p[1], p[3], p[5], p[6], p[7], p[8])

    repita(p[0])


def p_hacer(p):
    '''
    hacer : DESDE ID IGUAL sentencia HASTA sentencia HAGA LLAVE_IZQ expresion LLAVE_DER FINDESDE PUNTOCOMA
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[9])

    hacer(p[0])


def p_funcion(p):
    '''
    funcion : Aleatorio
            | Mover
            | funcionAlge
    '''
    p[0] = p[1]


def p_aleatorio(p):
    '''
    Aleatorio : ALEATORIO PARENTESIS_IZQ PARENTESIS_DER PUNTOCOMA
    '''
    p[0] = p[1]

    #funcionAleatorio()


def p_mover(p):
    '''
    Mover : MOVER PARENTESIS_IZQ paramMover PARENTESIS_DER PUNTOCOMA
    '''
    p[0] = (p[1], p[3])

    #funcionMover(p[0])


def p_ParamMover(p):
    '''
    paramMover : AF
                | F
                | DFA
                | IFA
                | DFB
                | IFB
                | A
                | DAA
                | IAA
                | DAB
                | IAB
                | AA
    '''
    p[0] = p[1]


def p_funcion_Alge(p):
    '''
    funcionAlge : INC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA expresion
             | DEC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA expresion
             | INI PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA expresion
    '''
    if p[8] == None:
        p[0] = ((p[1], p[3], p[5]),)
    elif p[8] != None:
        p[0] = ((p[1], p[3], p[5] ),)+ (p[8])






def p_procedimiento(p):
    '''
        procedimiento : PROC ID PARENTESIS_IZQ parametro PARENTESIS_DER INICIOPROC DOSPUNTOS expresion FINPROC PUNTOCOMA procedimiento
                     | empty empty empty empty empty empty empty empty empty empty empty
    '''
    if p[11] != None:
        p[0] = (p[1], p[2], p[4], p[6], p[8], p[9], p[11])
    elif p[11] == None and p[1] != None:
        p[0] = (p[1], p[2], p[4], p[6], p[8], p[9])
    else:
        p[0] = p[1]


def p_parametro(p):
    '''
    parametro : ID COMA parametro
              | ID empty empty
              | NUMERO COMA parametro
              | NUMERO empty empty
              | empty empty empty
    '''
    if p[3] != None and p[2] != None:
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]


def p_llamarProc(p):
    '''
    llamarProc : LLAMAR ID PARENTESIS_IZQ parametro PARENTESIS_DER PUNTOCOMA
    '''
    p[0] = (p[1], p[2], p[4])


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


def p_error(p):
    print("error de sintaxis " + str(p))
    print("error en la linea " + str(p.lineno))


def sintacticAnalizer(cadena):
    parser = yacc.yacc()
    parser.parse(cadena)


#################################### tester ############################################

def buscarFichero(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1
    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)
    for file in files:
        print(str(cont) + ". " + file)
        cont += 1
    while respuesta == False:
        numArchivo = raw_input('\n')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break
    return files[int(numArchivo) - 1]


def test():
    # directorio = os.path.dirname(os.getcwd()) + "/Tests/"
    # archivo = buscarFichero(directorio)
    # test = directorio + archivo

    fp = codecs.open(os.path.dirname(os.getcwd()) + "/Tests/" + "Test2", "r", "utf-8")
    cadena = fp.read()
    fp.close()

    lexicalAnalizer(cadena)
    sintacticAnalizer(cadena)


# documentar esta funcion si va a probar codigo en el GUI
test()