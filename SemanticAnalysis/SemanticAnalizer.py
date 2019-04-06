import threading
from random import choice
from LexicalAnalysis.LexicalAnalizer import reservadas
from ArduinoServer.ArduinoSever import ArduinoServer

variables = {}
listaMovimientos = []
procedimientos_dic = {}

procedimientos_param = {}


########################################## variables ##########################################
def variable1(var):
    variables[var] = 0


def variable2(var, val):
    variables[var] = val


########################################## condicionales ##########################################
def condicion1(cond, sino, fromwhere):
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

            if (VerificaCondicionales(i[1], i[2], i[3])) == True:
                print("LO VA A EJECUTAR")
                print(i[5])

                ejecutar(i[5])
                break

            elif (VerificaCondicionales(i[1], i[2], i[3])) == "Error: identificador no declarado":
                print("Error: variable de sentencia no declarada")
                IDE.OutputArea.setPlainText("\n" + ">>> ERROR: variable de sentencia no declarada ")
                break
            elif (VerificaCondicionales(i[1], i[2], i[3])) == "Error: identificador no declarado":
                print("Error: identificador no declarado")
                IDE.OutputArea.setPlainText("\n" + ">>> ERROR: identificador no declarado")
                break
        elif i[0] == "SINO":

            print("El ejectar del SiNo:")
            print(i)
            ejecutar(i[1])
            break


def VerificaCondicionales(ID, condicion, sentencia):
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
            IDE.OutputArea.setPlainText("\n" + ">>> ERROR: variable no declarada: " + ID)
            return "Error: variable de sentencia no declarada"
    else:
        IDE.OutputArea.setPlainText("\n" + ">>> ERROR: identificador no declarado: " + ID)
        return "Error: identificador no declarado"


def condicion2(cond):
    print("CONDICION 2:")
    print(cond[2][0])  # Cuandos
    print(cond[1])  # ID
    print(cond[2][1])  # SINO
    print(cond[2][2])  # EXPRESION DEL SINO

    cond1 = condicion2to1([], cond[2][0], cond[1])

    cond1.append((cond[2][1], cond[2][2]))

    print(cond1)
    condicion1(cond1, "sino", "condicion2")


def condicion2to1(result, cond, id):
    for i in cond:
        result.append((i[0], id, i[1], i[2], i[3], i[4]))

    return result


def separaCondiciones1(resultado, condicion):
    i = 0

    while (i != len(condicion)):
        resultado.append(condicion[i])

        i = i + 1

    return resultado


########################################## repita ##########################################


def repita(rep):
    print(rep)
    sentencia1 = rep[1]
    ID = rep[3]
    condicion = rep[4]
    sentencia2 = rep[5]

    print(sentencia1)

    print(ID)
    print(condicion)
    print(sentencia2)
    print(variables.get(ID))

    if condicion == '=':

        print("es =")

        while (variables.get(ID) != sentencia2):
            print("Va a ejecutar la sentencia:")
            print(sentencia1)
            ejecutar(sentencia1)
        print(variables.get(ID))
    elif condicion == '>':
        print("es >")
        while (variables.get(ID) < sentencia2):
            ejecutar(sentencia1)
    elif condicion == '<':
        print("es <")
        while (variables.get(ID) > sentencia2):
            ejecutar(sentencia1)
    elif condicion == '>=':
        print("es >=")
        while (variables.get(ID) <= sentencia2):
            ejecutar(sentencia1)
    elif condicion == '<=':
        print("es <=")
        while (variables.get(ID) >= sentencia2):
            ejecutar(sentencia1)
    elif condicion == '<>':
        print("es <>")
        while (variables.get(ID) == sentencia2):
            ejecutar(sentencia1)


########################################## procedimientos ##########################################

def set_Values_to_Params(nombreProc, params):
    parametros_de_procedimiento = procedimientos_param.get(nombreProc)

    i = 0

    while (i != len(params)):
        variables.update({parametros_de_procedimiento[i]: params[i]})
        i = i + 1


def getValuesOfParams(params):
    result = []
    for param in params:
        if (isinstance(param, str)):
            if param in variables:
                result.append(variables.get(param))
        elif isinstance(param, int):
            result.append(param)
        else:
            print(">>> ERROR:Objeto invalido de parametro")
            IDE.OutputArea.setPlainText("\n" + ">>> ERROR: parametro  invalido: " + param)
            return

    return result


def restablecerVariables(variablesAntes, variablesDesp):
    shared_items = {k: variablesAntes[k] for k in variablesAntes if
                    k in variablesDesp and variablesAntes[k] == variablesDesp[k]}
    dif_items = {k: variablesDesp[k] for k in variablesDesp if
                 k in variablesAntes and variablesDesp[k] != variablesAntes[k]}

    print("******************************************************************************************************")
    print(shared_items)
    print(dif_items)
    print(dict(shared_items, **dif_items))
    print("******************************************************************************************************")

    return dict(shared_items, **dif_items)


def eliminarParamsUsados(params):
    for param in params:
        print(param)


def llamarProc(nombreProc, parametros):
    if nombreProc in procedimientos_dic:

        if len(parametros) == len(procedimientos_dic.get(nombreProc)[1]):

            variables1 = variables.copy()

            set_Values_to_Params(nombreProc, getValuesOfParams(parametros))

            ejecutar(procedimientos_dic.get(nombreProc)[3])

            restablecerVariables(variables1, variables)

            newVars = restablecerVariables(variables1, variables)
            variables.clear()
            variables.update(newVars)

            print("===================================================================================================")
            print(variables)
            print("===================================================================================================")

        else:
            print("El procedimiento no tiene los parametros establecidos")
            print("El procedimiento tiene:" + str(len(procedimientos_dic.get(nombreProc)[1])) +
                  ", pero fueron dados: " + str(len(parametros)))

    else:
        print(">>> ERROR: EL procedimiento no ha sido declarado")
        IDE.OutputArea.setPlainText("\n" + ">>> ERROR: el procedimiento: " + nombreProc + "  no ha sido declarado")


def set_parametros_procedimientos(nombreProc, parametros):
    params = []
    for parametro in parametros:
        params.append(parametro)

    procedimientos_param.update({nombreProc: params})
    print(procedimientos_param)


def set_procedimientos(procedimientos):
    for procedimiento in procedimientos:
        if procedimiento[0] == "PROC":

            if (procedimiento[1] in procedimientos_dic):
                print(">>> ERROR: PROCEDIMIENTO YA ESTA DECLARADO")
                IDE.OutputArea.setPlainText(
                    "\n" + ">>> ERROR: el procedimiento: " + procedimiento[1] + "  ya ha sido declarado")
                return
            else:
                procedimientos_dic.update({procedimiento[1]: procedimiento[2]})
                set_parametros_procedimientos(procedimiento[1], procedimiento[2][1])

    print(procedimientos_dic)
    print("------------------------------------------------------------------------------------")


########################################## hacer ##########################################
def hacer(hacer):
    print(hacer)

    sentencia1 = hacer[3]
    sentencia2 = hacer[5]

    print(sentencia1)
    print(sentencia2)
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

            for i in range(sentencia1, sentencia2):
                ejecutar(hacer[7])
        else:
            print(">>> ERROR: la sentencia 1 debe ser menor a la sentencia 2")
            IDE.OutputArea.setPlainText(
                "\n" + ">>> ERROR: la sentencia: " + sentencia1 + " debe ser menor a la sentencia:" + sentencia2)
    else:
        print(">>> ERROR: sentencia no declarada")
        IDE.OutputArea.setPlainText(
            "\n" + ">>> ERROR: alguna de las sentencias: " + sentencia1 + "," + sentencia2 + " no ha sido declarada")


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


def iniciarEjecucion(arbol, window):
    global IDE
    IDE = window
    print("El arbol es:")
    print(arbol[0])

    global variables
    global listaMovimientos
    global procedimientos_dic
    global procedimientos_param

    variables = {}
    listaMovimientos = []
    procedimientos_dic = {}
    procedimientos_param = {}

    if (arbol[0] == "INICIO"):
        set_procedimientos(arbol[3])
        ejecutar(arbol[1])
        print(variables)
        print(listaMovimientos)

        error = IDE.OutputArea.toPlainText()
        if error == "":
            if len(listaMovimientos) == 0:
                IDE.OutputArea.setPlainText(
                    ">>> Se ha compilado correctamente. No hay movimientos definidos para el dode.")
            else:
                IDE.OutputArea.setPlainText(
                    ">>> Se ha compilado correctamente.\n>>> La lista de movimientos que hará el dode será: " +
                    str(listaMovimientos) + ".")

                t = threading.Thread(target=instanciaArduinoServer)
                t.start()


def instanciaArduinoServer():
    arduinoServer = ArduinoServer(listaMovimientos)


def ejecutar(expresionCompleta):
    if (len(expresionCompleta) == 1 and len(expresionCompleta[0]) == 1):
        ejecutar(expresionCompleta[0])
        return
    print("El 0 de expresion completa es:")
    print(expresionCompleta)
    if (expresionCompleta[0] in reservadas.values()):
        expresiones = [expresionCompleta]
    else:
        expresiones = separaCondiciones1([], expresionCompleta)

    print(expresiones)
    for expresion in expresiones:
        # print("La expresion es:")
        # print(expresion)
        if expresion[0] == "DCL":
            if expresion[2] == "DEFAULT":
                variable2(expresion[1], expresion[3])
            else:
                variable1(expresion[1])
        elif expresion[0] == "ENCASO" and isinstance(expresion[1], tuple):
            print(expresion[1][0])
            print(expresion[1][1])
            print(expresion[1][2])
            condicion1(expresion[1][0], (expresion[1][1],) + (expresion[1][2],), "")
        elif expresion[0] == "ENCASO":
            print("ENCASO 2 -------------------------------------------------------------------------------")
            # print(expresion[1]) # esto contiene la variable
            # print(expresion[2]) #esto contiene los cuando
            condicion2(expresion)

        elif expresion[0] == "INC" or expresion[0] == "DEC" or expresion[0] == "INI" or expresion[0] == "MOVER":
            ejecuta(expresion)
        elif expresion[0] == "DESDE":
            hacer(expresion)
        elif expresion[0] == "REPITA":
            repita(expresion)
        elif expresion[0] == "LLAMAR":
            llamarProc(expresion[1], expresion[2])


def ejecuta(expresion):
    if (expresion[0] == 'INC'):
        if (verificaVariable(expresion[1])):
            print("lo va a incrementar")
            print("antes")
            print(variables[expresion[1]])

            if isinstance(expresion[2], int):
                variables[expresion[1]] += int(expresion[2])
            elif verificaVariable(expresion[2]):
                variables[expresion[1]] += int(variables[expresion[2]])
            else:
                print(">>> ERROR: sentencia no declarada")
                IDE.OutputArea.setPlainText("\n" + ">>> ERROR: sentencia no declarada")
                return
        else:
            print(">>> ERROR:variable a operar no declarada")
            IDE.OutputArea.setPlainText(
                "\n" + ">>> ERROR: variable a operar: " + expresion[1] + " no ha sido declarada")
            return

        print('despues')
        print(variables[expresion[1]])

    elif (expresion[0] == 'DEC'):
        if (verificaVariable(expresion[1])):
            print("lo va a decrementar")
            print("antes")
            print(variables[expresion[1]])
            if isinstance(expresion[2], int):
                variables[expresion[1]] -= int(expresion[2])
            elif verificaVariable(expresion[2]):
                variables[expresion[1]] -= int(variables[expresion[2]])
            else:
                print(">>> ERROR: sentencia no declarada")
                IDE.OutputArea.setPlainText("\n" + ">>> ERROR: sentencia no declarada")
                return
        else:
            print(">>> ERROR: variable a operar no declarada")
            IDE.OutputArea.setPlainText(
                "\n" + ">>> ERROR: variable a operar: " + expresion[1] + " no ha sido declarada")
            return
        print('despues')
        print(variables[expresion[1]])

    elif (expresion[0] == 'INI'):
        if (verificaVariable(expresion[1])):
            print("la va a inicializar")
            print("antes")
            print(variables[expresion[1]])

            if isinstance(expresion[2], int):
                variables[expresion[1]] = int(expresion[2])
            elif verificaVariable(expresion[2]):
                variables[expresion[1]] = int(variables[expresion[2]])
            else:
                print(">>> ERROR: sentencia no declarada")
                IDE.OutputArea.setPlainText(">>> ERROR: sentencia no declarada")
                return
        else:
            print(">>> ERROR: variable a operar no declarada")
            IDE.OutputArea.setPlainText(
                "\n" + ">>> ERROR: variable a operar: " + expresion[1] + " no ha sido declarada")
            return

        print('despues')
        print(variables[expresion[1]])

    elif (expresion[0] == 'MOVER'):
        movimiento = expresion[1]
        listaMovimientos.append(movimiento)
        print(listaMovimientos)
