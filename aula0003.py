import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout

app = QApplication(sys.argv)

botao = QPushButton('Texto do Botão')
botao.setStyleSheet("font-size: 80px")

botao_2 = QPushButton('Botão 2')
botao.setStyleSheet("font-size: 40px")

central_widget = QWidget()
layout = QHBoxLayout()
central_widget.setLayout(layout)

layout.addWidget(botao)
layout.addWidget(botao_2)


central_widget.show()

app.exec()