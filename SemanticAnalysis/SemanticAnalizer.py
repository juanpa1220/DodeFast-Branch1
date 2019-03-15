from random import choice

variables = {}
listaMovimientos = []


########################################## variables ##########################################
def variable1(var):
    variables[var] = 0


def variable2(var, val):
    variables[var] = val


########################################## condicionales ##########################################
def condicion1(cond, fromwhere):
    if fromwhere == "condicion2":
        condiciones = cond
    else:
        condiciones = separaCondiciones1([], cond[0])
        condiciones.append((cond[1], cond[2]))

    for i in condiciones:
        if i[0] == 'CUANDO':
            if verificaVariable(i[1]):  # verifica que el identificador este declarado antes
                condicion = i[2]
                identificador = variables[i[1]]
                sentencia = i[3]

                if isinstance(i[3], int):  # para cuando la sentencia es un NUMERO
                    if condicion == '=':
                        if (identificador == sentencia):
                            ejecuta(i[5])
                            break
                    elif condicion == '>':
                        if (identificador > sentencia):
                            ejecuta(i[5])
                            break
                    elif condicion == '<':
                        if (identificador < sentencia):
                            ejecuta(i[5])
                            break
                    elif condicion == '>=':
                        if (identificador >= sentencia):
                            ejecuta(i[5])
                            break
                    elif condicion == '<=':
                        if (identificador <= sentencia):
                            ejecuta(i[5])
                            break
                    elif condicion == '<>':
                        if (identificador != sentencia):
                            ejecuta(i[5])
                            break
                elif (verificaVariable(i[3])):  # para cuando la sentencia es un ID
                    if condicion == '=':
                        if (identificador == variables[sentencia]):
                            ejecuta(i[5])
                            break
                    elif condicion == '>':
                        if (identificador > variables[sentencia]):
                            ejecuta(i[5])
                            break
                    elif condicion == '<':
                        if (identificador < variables[sentencia]):
                            ejecuta(i[5])
                            break
                    elif condicion == '>=':
                        if (identificador >= variables[sentencia]):
                            ejecuta(i[5])
                            break
                    elif condicion == '<=':
                        if (identificador <= variables[sentencia]):
                            ejecuta(i[5])
                            break
                    elif condicion == '<>':
                        if (identificador != variables[sentencia]):
                            ejecuta(i[5])
                            break
                else:
                    print("error: variable de sentencia no declarada")
                    break
            else:
                print("error: identificador no declarado")
                break
        else:
            ejecuta(i[1])


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
    if len(condicion) == 6:
        resultado.append((condicion[0], condicion[1], condicion[2], condicion[3], condicion[4], condicion[5]))
        return resultado
    else:
        resultado.append((condicion[0], condicion[1], condicion[2], condicion[3], condicion[4], condicion[5]))
        return separaCondiciones1(resultado, condicion[6])


########################################## repita ##########################################
def repita(rep):
    print(rep)


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


def ejecuta(expresion):
    if (expresion[0] == 'ENCASO'):
        print('por aqui')
        pass

    elif (expresion[0] == 'INC'):
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
        print(variables[expresion[1]])

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
