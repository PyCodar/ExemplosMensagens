# Importação das classes do PyQt5
from PyQt5.QtWidgets import QApplication, QMessageBox

# Cria uma aplicação Qt
app = QApplication([]) # Cria uma instância (um objeto) da classe 

# Exibe a caixa de mensagem
msg_box = QMessageBox() # Cria uma instância (um objeto) da classe 
msg_box.setWindowTitle("Olá") # Configuta um título para a janela da mensagem
msg_box.setText("Olá Usuário!") # Configura a mensagem principal do corpo da janela
msg_box.exec_() # Executa a mensagem

# Executa o loop de eventos da aplicação
app.exec()
