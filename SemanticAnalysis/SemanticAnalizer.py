from random import choice

variables = {}
listaMovimientos = []


########################################## variables ##########################################
def variable1(var):
    print("Se va a iniciar la variable: ")
    print(var)

    variables[var] = 0


def variable2(var, val):
    print("Se va a iniciar la variable: ")
    print(var)
    print("CON VALOR = " + str(val))
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
        print("El i[0] =")
        print(i[0])
        if i[0] == 'CUANDO':
            print("Verificando condicionales...")
            print(VerificaCondicionales(i[1], i[2], i[3]))

            print(".....")

            if(VerificaCondicionales(i[1],i[2], i[3])) == True:
                print("LO VA A EJECUTAR")
                print(i[5])

                for j in separaCondiciones1([],i[5]):

                    ejecutar((j,),0)
                break

            elif (VerificaCondicionales(i[1],i[2], i[3])) == "Error: identificador no declarado":
                print("Error: variable de sentencia no declarada")
                break
            elif (VerificaCondicionales(i[1],i[2], i[3])) == "Error: identificador no declarado":
                print("Error: identificador no declarado")
                break
        elif i[0] == "SINO":
            print("El ejectar del SiNO:")
            print(i)
            for j in separaCondiciones1([],i[1]):
                ejecutar((j,) + (),0)
            break


def VerificaCondicionales(ID, condicion,sentencia):
    if verificaVariable(ID):  # verifica que el identificador este declarado antes
        print("Esta declarado")
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
    print(len(condicion))
    while(i != len(condicion) ):

        resultado.append(condicion[i])
        i = i + 1
    print(resultado)
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

        ejecutar(arbol[1], 0)
        print(variables)


def ejecutar(expresion, ind):

    print("La expresion en la que se encuentra es:")
    print(expresion[ind][0])

    if expresion[ind][0] == None:
        ejecutar(expresion, ind + 1)

    elif (expresion[ind][0] == "ENCASO"):
        #print(" HAY UN ENCASO")


        condicion1(expresion[ind][1][0],tuple(("SINO",expresion[ind][1][2])), "")


    elif (expresion[ind][0] == "DCL"):

        if (expresion[ind][2] == "DEFAULT"):
            variable2(expresion[ind][1], expresion[ind][3])
        else:
            variable1(expresion[ind][1])

        ejecutar(expresion, ind + 1)
    elif expresion[ind][0] == "INC":
        print("HAY UN INC")
        ejecuta(expresion[ind])



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