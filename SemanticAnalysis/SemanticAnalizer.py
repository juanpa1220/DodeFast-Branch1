from random import choice
from LexicalAnalysis.LexicalAnalizer import reservadas
variables = {}
listaMovimientos = []


########################################## variables ##########################################
def variable1(var):


    variables[var] = 0


def variable2(var, val):

    variables[var] = val


########################################## condicionales ##########################################
def condicion1(cond,sino, fromwhere):

    if fromwhere == "condicion2":
        condiciones = cond
    else:
        condiciones = separaCondiciones1([], cond)
        condiciones += [sino]

        print("LAS CONDICIONES SON: ")
        print(condiciones)


    for i in condiciones:

        print(i)

        if i[0] == 'CUANDO':

            if(VerificaCondicionales(i[1],i[2], i[3])) == True:
                print("LO VA A EJECUTAR")
                print(i[5])

                ejecutar(i[5])
                break

            elif (VerificaCondicionales(i[1],i[2], i[3])) == "Error: identificador no declarado":
                print("Error: variable de sentencia no declarada")
                break
            elif (VerificaCondicionales(i[1],i[2], i[3])) == "Error: identificador no declarado":
                print("Error: identificador no declarado")
                break
        elif i[0] == "SINO":

            print("El ejectar del SiNo:")
            print(i)
            ejecutar(i[1])
            break


def VerificaCondicionales(ID, condicion,sentencia):
    if verificaVariable(ID):  # verifica que el identificador este declarado antes

        identificador = variables[ID]

        if isinstance(sentencia, int):  # para cuando la sentencia es un NUMERO
            if condicion == '=':
                if (identificador == sentencia):
                                      # Si cumple esta condicion se ejecuta el Entons
                    return True
            elif condicion == '>':
                if (identificador > sentencia):

                    return True
            elif condicion == '<':
                if (identificador < sentencia):
                    return True
            elif condicion == '>=':
                if (identificador >= sentencia):
                    return True
            elif condicion == '<=':
                if (identificador <= sentencia):
                    return True
            elif condicion == '<>':
                if (identificador != sentencia):
                    return True
        elif (verificaVariable(ID)):  # para cuando la sentencia es un ID
            if condicion == '=':
                if (identificador == variables[sentencia]):
                    return True
            elif condicion == '>':
                if (identificador > variables[sentencia]):
                    return True
            elif condicion == '<':
                if (identificador < variables[sentencia]):
                    return True
            elif condicion == '>=':
                if (identificador >= variables[sentencia]):
                    return True
            elif condicion == '<=':
                if (identificador <= variables[sentencia]):
                    return True
            elif condicion == '<>':
                if (identificador != variables[sentencia]):
                    return True
        else:
            print("error: variable de sentencia no declarada")
            return "Error: variable de sentencia no declarada"
    else:

        return "Error: identificador no declarado"

def condicion2(cond):
    cond1 = condicion2to1([], cond[2][0], cond[1])
    cond1.append((cond[2][1], cond[2][2]))
    condicion1(cond1, "condicion2")


def condicion2to1(result, cond, id):
    if len(cond) == 5:
        result.append((cond[0], id, cond[1], cond[2], cond[3], cond[4]))
        return result
    else:
        result.append((cond[0], id, cond[1], cond[2], cond[3], cond[4]))
        return condicion2to1(result, cond[5], id)


def separaCondiciones1(resultado, condicion):

    i = 0

    while(i != len(condicion) ):

        resultado.append(condicion[i])
        i = i + 1

    return resultado

########################################## repita ##########################################


def repita(rep):
    print(rep)
    sentencia1 = rep[2]
    Id = rep[4]
    condicion = rep[5]
    sentencia = rep[6]






########################################## hacer ##########################################
def hacer(hacer):
    print(hacer)
    sentencia1 = hacer[3]
    sentencia2 = hacer[5]
    if (isinstance(sentencia1, int) or verificaVariable(sentencia1)) and (
            isinstance(sentencia2, int) or verificaVariable(sentencia2)):
        if isinstance(sentencia1, int):
            sentencia1 = sentencia1
        elif verificaVariable(sentencia1):
            sentencia1 = variables[sentencia1]
        if isinstance(sentencia2, int):
            sentencia2 = sentencia2
        elif verificaVariable(sentencia2):
            sentencia2 = variables[sentencia2]

        if sentencia1 < sentencia2:

            for i in range(sentencia1, sentencia2 + 1):
                expresion = hacer[7]
                cont = hacer[1]
                expresion = sustituye(expresion, cont, i)
                ejecuta(expresion)

        else:
            print("error: la sentencia 1 debe ser menor a la sentencia 2")
    else:
        print("error: sentencia no declarada")


def sustituye(expresion, cont, i):
    result = []
    for j in expresion:
        if j == cont:
            result.append(i)
        else:
            result.append(j)
    return tuple(result)


########################################## funciones ##########################################
def funcionAleatorio():
    moviminetos = ['AF', 'F', 'DFA', 'IFA', 'DFB', 'IFB', 'A', 'DAA', 'IAA', 'DAB', 'IAB', 'AA']
    random = choice(moviminetos)
    expresion = ('MOVER', random)
    ejecuta(expresion)


def funcionMover(funcion):
    ejecuta(funcion)


def funcionesOperadoras(funcion):
    ejecuta(funcion)


########################################## ejecutables ##########################################


def verificaVariable(var):
    for i in variables.keys():
        if i == var:
            return True
    return False



def iniciarEjecucion(arbol):
    print("El arbol es:")
    print(arbol[1])
    if(arbol[0] == "INICIO"):

        ejecutar(arbol[1])
        print(variables)



def ejecutar(expresionCompleta):
    print("El 0 de expresion completa es:")
    print(expresionCompleta)
    if (expresionCompleta[0] in reservadas.values()):
        expresiones = [expresionCompleta]
    else:
        expresiones = separaCondiciones1([],expresionCompleta)

    print(expresiones)

    for expresion in expresiones:
        #print("La expresion es:")
        #print(expresion)
        if expresion[0] == "DCL":
            if expresion[2] == "DEFAULT":
                variable2(expresion[1],expresion[3])
            else:
                variable1(expresion[1])
        elif expresion[0] == "ENCASO":
            print(expresion[1][0])
            print(expresion[1][1])
            print(expresion[1][2])
            condicion1(expresion[1][0],(expresion[1][1],) + (expresion[1][2],),"")
        elif expresion[0] ==  "INC" or expresion[0] == "DEC" or expresion[0] == "INI" or expresion[0] == "MOVER":
            ejecuta(expresion)




def ejecuta(expresion):


    if (expresion[0] == 'INC'):
        print("antes")

        print(variables[expresion[1]])

        if (verificaVariable(expresion[1])):

            if isinstance(expresion[2], int):
                variables[expresion[1]] += int(expresion[2])
            elif verificaVariable(expresion[2]):
                variables[expresion[1]] += int(variables[expresion[2]])
            else:
                print("error: sentencia no declarada")
        else:
            print("error: variable a operar no declarada")

        print('despues')
        print(variables[expresion[1]])

    elif (expresion[0] == 'DEC'):
        print("lo va a decrementar")
        print("antes")
        print(variables[expresion[1]])

        if (verificaVariable(expresion[1])):
            if isinstance(expresion[2], int):
                variables[expresion[1]] -= int(expresion[2])
            elif verificaVariable(expresion[2]):
                variables[expresion[1]] -= int(variables[expresion[2]])
            else:
                print("error: sentencia no declarada")
        else:
            print("error: variable a operar no declarada")

        print('despues')
        print(variables[expresion[1]])

    elif (expresion[0] == 'INI'):
        print("antes")

        if (verificaVariable(expresion[1])):
            if isinstance(expresion[2], int):
                variables[expresion[1]] = int(expresion[2])
            elif verificaVariable(expresion[2]):
                variables[expresion[1]] = int(variables[expresion[2]])
            else:
                print("error: sentencia no declarada")
        else:
            print("error: variable a operar no declarada")

        print('despues')
        print(variables[expresion[1]])

    elif (expresion[0] == 'MOVER'):
        movimiento = expresion[1]
        listaMovimientos.append(movimiento)
        print(listaMovimientos)