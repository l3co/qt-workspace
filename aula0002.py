import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget

app = QApplication(sys.argv)

botao = QPushButton('Texto do Botão')
botao.setStyleSheet("font-size: 80px")

botao = QPushButton('Botão 2')
botao.setStyleSheet("font-size: 40px")

botao.show()

app.exec()