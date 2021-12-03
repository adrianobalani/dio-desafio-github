from PyQt5 import QtCore, QtGui, QtWidgets
import json


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(339, 329)
        Dialog.setSizeGripEnabled(False)
        self.lista_de_itens = QtWidgets.QTreeWidget(Dialog)
        self.lista_de_itens.setGeometry(QtCore.QRect(10, 10, 321, 191))
        self.lista_de_itens.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lista_de_itens.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lista_de_itens.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.lista_de_itens.setAutoScroll(True)
        self.lista_de_itens.setIndentation(1)
        self.lista_de_itens.setRootIsDecorated(False)
        self.lista_de_itens.setUniformRowHeights(True)
        self.lista_de_itens.setItemsExpandable(False)
        self.lista_de_itens.setAnimated(False)
        self.lista_de_itens.setWordWrap(True)
        self.lista_de_itens.setExpandsOnDoubleClick(False)
        self.lista_de_itens.setObjectName("lista_de_itens")

        self.lista_de_itens.header().setVisible(True)
        self.lista_de_itens.header().setCascadingSectionResizes(False)
        self.lista_de_itens.header().setDefaultSectionSize(94)
        self.lista_de_itens.header().setHighlightSections(False)
        self.lista_de_itens.header().setMinimumSectionSize(35)
        self.lista_de_itens.header().setSortIndicatorShown(False)
        self.lista_de_itens.header().setStretchLastSection(False)

        self.box_item = QtWidgets.QLineEdit(Dialog)
        self.box_item.setGeometry(QtCore.QRect(10, 210, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.box_item.setFont(font)
        self.box_item.setPlaceholderText("Item")
        self.box_item.setObjectName("box_item")

        self.box_unidades = QtWidgets.QLineEdit(Dialog)
        self.box_unidades.setGeometry(QtCore.QRect(10, 250, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.box_unidades.setFont(font)
        self.box_unidades.setPlaceholderText("Unidades")
        self.box_unidades.setObjectName("box_unidades")

        self.box_valor = QtWidgets.QLineEdit(Dialog)
        self.box_valor.setGeometry(QtCore.QRect(180, 250, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.box_valor.setFont(font)
        self.box_valor.setPlaceholderText("Valor")
        self.box_valor.setObjectName("box_valor")

        self.botao_carregar = QtWidgets.QPushButton(Dialog)
        self.botao_carregar.setGeometry(QtCore.QRect(121, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.botao_carregar.setFont(font)
        self.botao_carregar.setObjectName("botao_carregar")

        self.botao_adicionar = QtWidgets.QPushButton(Dialog)
        self.botao_adicionar.setGeometry(QtCore.QRect(11, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.botao_adicionar.setFont(font)
        self.botao_adicionar.setObjectName("botao_adicionar")

        self.botao_remover = QtWidgets.QPushButton(Dialog)
        self.botao_remover.setGeometry(QtCore.QRect(240, 290, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.botao_remover.setFont(font)
        self.botao_remover.setObjectName("botao_remover")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lista_de_itens.setSortingEnabled(False)
        self.lista_de_itens.headerItem().setText(0, _translate("Dialog", "Item"))
        self.lista_de_itens.headerItem().setText(1, _translate("Dialog", "Unidades"))
        self.lista_de_itens.headerItem().setText(2, _translate("Dialog", "Valor"))
        __sortingEnabled = self.lista_de_itens.isSortingEnabled()
        self.lista_de_itens.setSortingEnabled(False)
        self.lista_de_itens.setSortingEnabled(__sortingEnabled)
        self.botao_carregar.setText(_translate("Dialog", "Carregar"))
        self.botao_adicionar.setText(_translate("Dialog", "Adicionar"))
        self.botao_remover.setText(_translate("Dialog", "Remover"))


class TreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, num, item, unidades, valor):
        super(TreeWidgetItem, self).__init__([item, unidades, valor])
        self._num = num


class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.botao_carregar.clicked.connect(self.botao_carregar_clicked)
        self.botao_adicionar.clicked.connect(self.botao_adicionar_clicked)
        self.botao_remover.clicked.connect(self.botao_remover_clicked)

    @QtCore.pyqtSlot()
    def botao_carregar_clicked(self):
        # remove all items
        self.lista_de_itens.clear()
        # load new items from file
        self.carregar_itens_do_arquivo()

    @QtCore.pyqtSlot()
    def botao_adicionar_clicked(self):
        item_input = self.box_item.text()
        valor_input = self.box_valor.text()
        unidades_input = self.box_unidades.text()
        if not item_input or not valor_input or not unidades_input:
            print("empty fields")
            return
        num_input = max([self.lista_de_itens.topLevelItem(i)._num for i in range(self.lista_de_itens.topLevelItemCount())] + [-1])+1
        it = TreeWidgetItem(num_input, item_input, valor_input, unidades_input)
        self.lista_de_itens.addTopLevelItem(it)
        self.salvar_itens_em_um_arquivo()
        self.box_item.clear()
        self.box_valor.clear()
        self.box_unidades.clear()

    @QtCore.pyqtSlot()
    def botao_remover_clicked(self):
        for it in reversed(self.lista_de_itens.selectedItems()):
            i = self.lista_de_itens.indexOfTopLevelItem(it)
            it_ = self.lista_de_itens.takeTopLevelItem(i)
            del it_
        self.salvar_itens_em_um_arquivo()

    def carregar_itens_do_arquivo(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
            for e in data['database']:
                it = TreeWidgetItem(int(e["num"]), e["item"], e["unidades"], e["valor"])
                self.lista_de_itens.addTopLevelItem(it)

    def salvar_itens_em_um_arquivo(self):
        data = { "database": [] }
        for i in range(self.lista_de_itens.topLevelItemCount()):
            it = self.lista_de_itens.topLevelItem(i)
            row = {"num": str(it._num), "item" : it.text(0), "unidades": it.text(1), "valor": it.text(2)}
            data["database"].append(row)

        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Dialog()
    w.show()
    sys.exit(app.exec_())