import time

#Funçao para logs do sistema
def log(mensagem, log):
    arquivo = open(log, 'a')
    data = str(time.strftime("%Y-%m-%d %H:%M:%S"))
    arquivo.write('['+data+'] '+mensagem+'\n\n')
    arquivo.close()