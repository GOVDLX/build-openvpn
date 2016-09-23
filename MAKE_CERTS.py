
class MAKE_CERTS:
    def __init__(self,K_SIZE,CA_EXP,K_EXP,K_PAIS,K_ESTADO,K_CIDADE,K_EMPRESA,K_EMAIL,K_SETOR,K_NAME):
        self.E_RSA = '`pwd`'
        self.OPENSSL = 'openssl'
        self.PK11TOOL = 'pkcs11-tool'
        self.GREP = 'grep'
        self.K_CONFIG = '`$EASY_RSA/whichopensslcnf $EASY_RSA`'
        self.K_DIR = '$EASY_RSA/keys'
        self.PKCS_MOD_PATH = 'dummy'
        self.PKCS_PIN = 'dummy'
        self.K_SIZE = K_SIZE
        self.CA_EXP = CA_EXP
        self.K_EXP = K_EXP
        self.K_PAIS = K_PAIS
        self.K_ESTADO = K_PAIS
        self.K_CIDADE = K_CIDADE
        self.K_EMPRESA = K_EMPRESA
        self.K_EMAIL = K_EMAIL
        self.K_SETOR = K_SETOR
        self.K_NAME = K_NAME
        self.dir = '/etc/openvpn/'
        self.dircert = 'easy-rsa/2.2.2/'

    def build_dh(self):
        import os
        os.system(self.dir + self.dircert + 'vars')
        command = self.dir+self.dircert+'build-dh'
        os.system(command)
        return 0

    def build_ca(self):
        import os
        os.system(self.dir + self.dircert + 'vars')
        command = self.dir+self.dircert+'build-ca'
        os.system(command)
        return 0

    def build_key(self):
        import os
        os.system(self.dir+self.dircert+'vars')
        print("Informe o IP da maquina")
        command = self.dir+self.dircert+'build-key'
        os.system(command)
        return 0
    def build_key_server(self):
        import os
        os.system(self.dir + self.dircert + 'vars')
        command = self.dir+self.dircert+'build-key-server server'
        os.system(command)
        return 0

    def vars(self):


       FILE_VARS=[
           ['export EASY_RSA=' + self.E_RSA],
           ['export OPENSSL=' + self.OPENSSL],
           ['export PKCS11TOOL=' + self.PK11TOOL],
           ['export GREP=' + self.GREP],
           ['export KEY_CONFIG=' + self.K_CONFIG],
           ['export KEY_DIR=' + self.K_DIR],
           ['export PKCS11_MODULES_PATH=' + self.PKCS_MOD_PATH],
           ['export PKCS11_PIN='+self.PKCS_PIN],
           ['export KEY_SIZE=' + self.K_SIZE],
           ['export CA_EXPIRE='+self.CA_EXP],
           ['export KEY_EXPIRE='+self.K_EXP],
           ['export KEY_COUNTRY='+self.K_PAIS],
           ['export KEY_PROVINCE='+self.K_ESTADO],
           ['export KEY_CITY='+self.K_CIDADE],
           ['export KEY_ORG='+self.K_EMPRESA],
           ['export KEY_EMAIL='+self.K_EMAIL],
           ['export KEY_OU='+self.K_SETOR],
           ['export KEY_NAME='+self.K_NAME]]

       file = open("bnichost-vars", "w")


       for line in FILE_VARS:
           file.write(line[0]+'\n')
       file.close()
       return 0




