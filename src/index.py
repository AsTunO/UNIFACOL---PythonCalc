# Importando a biblioteca
from PyQt5 import uic, QtWidgets
import math

# Ligação com o arquivo .ui
app = QtWidgets.QApplication([])
style = uic.loadUi("style.ui")


factor = ""
num = ""
op = ""

# Função que faz as operações
def operation(factor, num, op):
    result = ""
    if op == "+":
        result = float(factor) + float(num)
    elif op == "-":
        result = float(factor) - float(num)
    elif op == "*":
        result = float(factor) * float(num)
    elif op == "/":
        result = float(factor) / float(num)
    elif op == "√":
        result = math.sqrt(float(num))
    elif op == "//":
        result = float(factor) // float(num)
    elif op == "%":
        result = float(num) * (float(factor) / 100)
    elif op == "**":
        result = math.pow(float(factor), float(num))
    return trunc(result, 2)


# Função para deixar os resultados com apenas duas casas decimais após a vírgula
def trunc(num, digits):
    return int(num * 10 ** digits) / 10 ** digits


# Funções para os botões
def bt0():
    print("Num 0 set from txt")
    global num
    style.label_3.setText(num + "0")
    num += "0"


def bt1():
    print("Num 1 set from txt")
    global num
    style.label_3.setText(num + "1")
    num += "1"


def bt2():
    print("Num 2 set from txt")
    global num
    style.label_3.setText(num + "2")
    num += "2"


def bt3():
    print("Num 3 set from txt")
    global num
    style.label_3.setText(num + "3")
    num += "3"


def bt4():
    print("Num 4 set from txt")
    global num
    style.label_3.setText(num + "4")
    num += "4"


def bt5():
    print("Num 5 set from txt")
    global num
    style.label_3.setText(num + "5")
    num += "5"


def bt6():
    print("Num 6 set from txt")
    global num
    style.label_3.setText(num + "6")
    num += "6"


def bt7():
    print("Num 7 set from txt")
    global num
    style.label_3.setText(num + "7")
    num += "7"


def bt8():
    print("Num 8 set from txt")
    global num
    style.label_3.setText(num + "8")
    num += "8"


def bt9():
    print("Num 9 set from txt")
    global num
    style.label_3.setText(num + "9")
    num += "9"


def btPoint():
    print("Point set from txt")
    global num
    style.label_3.setText(num + ".")
    num += "."


def btSoma():
    print("Soma set from txt")
    style.label_3.setText("+")
    global op, num, factor
    op = "+"
    factor, num = num, ""


def btSub():
    print("Sub set from txt")
    style.label_3.setText("-")
    global op, num, factor
    op = "-"
    factor, num = num, ""


def btMulti():
    print("Multi set from txt")
    style.label_3.setText("*")
    global op, num, factor
    op = "*"
    factor, num = num, ""


def btDiv():
    print("Div set from txt")
    style.label_3.setText("/")
    global op, num, factor
    op = "/"
    factor, num = num, ""


def btRaiz():
    print("Raiz set from txt")
    style.label_3.setText("√")
    global op, num, factor
    op = "√"
    result = operation(factor, num, op)
    style.label_3.setText(str(result))
    num, factor, op = "", "", ""


def btPorcent():
    print("Porcent set from txt")
    style.label_3.setText("%")
    global op, num, factor
    op = "%"
    factor, num = num, ""


def btDivInt():
    print("DivInt set from txt")
    style.label_3.setText("//")
    global op, num, factor
    op = "//"
    factor, num = num, ""


def btExpo():
    print("Expo set from txt")
    style.label_3.setText("**")
    global op, num, factor
    op = "**"
    factor, num = num, ""


def btClear():
    print("Clear set from txt")
    style.label_3.setText("")
    global op, num, factor
    num, factor, op = "", "", ""


def btRun():
    print("Run set from txt")
    global op, num, factor
    result = operation(factor, num, op)
    style.label_3.setText(str(result))
    num, factor, op = "", "", ""


# Ligação dos botões com as funções
style.pushButton.clicked.connect(bt1)
style.pushButton_3.clicked.connect(bt2)
style.pushButton_2.clicked.connect(bt3)
style.pushButton_10.clicked.connect(bt4)
style.pushButton_9.clicked.connect(bt5)
style.pushButton_5.clicked.connect(bt6)
style.pushButton_8.clicked.connect(bt7)
style.pushButton_7.clicked.connect(bt8)
style.pushButton_6.clicked.connect(bt9)
style.pushButton_4.clicked.connect(bt0)
style.pushButton_19.clicked.connect(btPoint)
style.pushButton_22.clicked.connect(btRaiz)
style.pushButton_20.clicked.connect(btSoma)
style.pushButton_21.clicked.connect(btSub)
style.pushButton_26.clicked.connect(btDiv)
style.pushButton_25.clicked.connect(btMulti)
style.pushButton_32.clicked.connect(btClear)
style.pushButton_23.clicked.connect(btPorcent)
style.pushButton_27.clicked.connect(btDivInt)
style.pushButton_28.clicked.connect(btExpo)
style.pushButton_11.clicked.connect(btRun)


style.show()
app.exec()
