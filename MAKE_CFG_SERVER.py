class MAKE_CFG_SERVER:


#    def __init__(self,ip,port,prot,type,net,server_mode,push1,push2):
#        self.ip = ip
#        self.port = port
#        self.prot = prot
#        self.type = type
#        self.ca = 'keys/ca.crt'
#        self.cert = 'keys/server.crt'
#        self.keys = 'keys/server.key'
#        self.dh = 'keys/dh2048.pem'
#        self.net = net
#        #self.server_mode = server_mode
##        self.push1 = push1
#       self.push2 = push2
#        self.ccd = 'client-config-dir ccd'
#        self.acc_client = 'client-to-client'
#        self.cn = ';duplicate-cn'
#        self.keepalive = 'keepalive 10 120'
#        self.tls = ';tls-auth ta.key 0'
#        self.cipherBF = ';cipher BF-CBC'
#        self.cipherAES = ';cipher AES-128-CBC'
#        self.cipherDES = ';DES-EDE3-CBC'
#        self.compression = 'comp-lzo'
#        self.maxclients = ';max-clients 100'
#        self.user = ';nobody'
#        self.group = ';nogroup'
#        self.perskey = 'persist-key'
#        self.perstun = 'persist-tun'
#        self.statuslog = '/var/log/openvpn/openvpn-status.log'
#        self.appendlog = '/var/log/openvpn/openvpn-server.log'
#        self.serverlog = '/var/log/openvpn/openvpn-server.log'
#        self.verbose = 'verb 3'
#        self.mute = ';mute

    def __init__(self):
        self.ip = ''
        self.port = ''
        self.prot = ''
        self.type = ''
        self.ca = 'keys/ca.crt'
        self.cert = 'keys/server.crt'
        self.keys = 'keys/server.key'
        self.dh = 'keys/dh2048.pem'
        self.net = ''
        #self.server_mode = server_mode
        self.push1 = ''
        self.push2 = ''
        self.ccd = 'client-config-dir ccd'
        self.acc_client = 'client-to-client'
        self.cn = ';duplicate-cn'
        self.keepalive = 'keepalive 10 120'
        self.tls = ';tls-auth ta.key 0'
        self.cipherBF = ';cipher BF-CBC'
        self.cipherAES = ';cipher AES-128-CBC'
        self.cipherDES = ';DES-EDE3-CBC'
        self.compression = 'comp-lzo'
        self.maxclients = ';max-clients 100'
        self.user = ';nobody'
        self.group = ';nogroup'
        self.perskey = 'persist-key'
        self.perstun = 'persist-tun'
        self.statuslog = '/var/log/openvpn/openvpn-status.log'
        self.appendlog = '/var/log/openvpn/openvpn-server.log'
        self.serverlog = '/var/log/openvpn/openvpn-server.log'
        self.verbose = 'verb 3'
        self.mute = ';mute 10'

    def make_cfg(self):
            FILE_CFG=[
                ['#CONFIGURACAO DO SERVIDOR'],
                ['local '+self.ip,'IP QUE O SERVICO VAI ESCUTAR'],
                ['port '+self.port,'PORTA QUE O SERVICO VAI ESCUTAR'],
                ['proto '+self.prot,'PROTOCOLO QUE O SERVICO VAI FUNCIONAR'],
                ['dev '+self.type,'TIPO DE VPN '],
                ['ca '+self.ca,'CA - CERTIFICATE AUTHORITY'],
                ['cert '+self.cert,'CERT - CERTIFICADO DO SERVIDOR'],
                ['key '+self.keys,'KEYS - CHAVE DO SERVIDOR'],
                ['dh '+self.dh,'DH - DiffieHellman'],
                [self.net,'REDE QUE A VPN VAI FUNCIONAR'],
                [self.push1,'REDE ROTEADA PELO SERVIDOR VPN'],
                [self.push2,'REDE ROTEADA PELO SERVIDOR VPN'],
                [self.ccd,'DIRETORIO COM OS IPS DE CADA MAQUINA QUE FARA PARTE DA VPN'],
                [self.acc_client,'PERMITE COMUNICACAO DIRETA ENTRE AS MAQUINAS DA VPN'],
                [self.cn,'MULTIUSUARIOS COM O MESMO CERTIFICADO'],
                [self.keepalive,' SINAL DE PING PARA O HOST'],
                [self.tls,'SEGURANCA EXTRA CONTRA ATAQUES DoS E UDP POR FLOODING'],
                [self.cipherBF,'CRYPTOGRAFIA BF-CBC BLOWFISH (default)'],
                [self.cipherAES,'CRYPTOGRAFIA AES-128-CBC'],
                [self.cipherDES,'CRYPTOGRAFIA DES-EDE3-CBC'],
                [self.compression,'COMPRESSAO '],
                [self.maxclients,'NUMERO MAXIMO DE CLIENTES CONECTADOS'],
                [self.user,'USUARIO PADRAO, OPCAO PARA WINDOWS'],
                [self.group,'GRUPO PADRAO,OPCAO PARA WINDOWS'],
                [self.perskey,'FORCA A RECONEXAO SER FEITA ATRAVES DE CHAVE'],
                [self.perstun,'FORCA A RECONEXAO SER FEITA UTILIZANDO TUNNEL'],
                ['status '+self.statuslog,'LOG DE STATUS'],
                ['log-append '+self.appendlog,'LOGS ADICIONAIS'],
                ['log '+self.serverlog,'LOGS DO SERVIDOR'],
                [self.verbose,'NIVEL DE VERBOSE DO SERVICO'],
                [self.mute,'ANULA REPETICAO APARTIR DE X OCORRENCIAS']
            ]
            return FILE_CFG

    def questions(self):
            self.ip = input("IP EXTERNO DO SERVIDOR: ")
            self.port = input("PORTA DO SERVICO. Default 1194: ")
            self.prot = input("PROTOCOLO UDP ou TCP: ")
            self.net = input("REDE DA VPN. Exemplo(10.1.1.0 255.255.255.0): ")
            self.type = input("TIPO DE VPN. TAP -> VPN LAYER 2, TUN -> VPN TUNNEL: ")
            if self.type == 'TAP':
                self.net = 'server-bridge'
            else:
                self.net = 'server '+self.net
            self.push1 = input("PRIMEIRA REDE QUE O SERVIDOR VPN VAI ROTEAR PELA VPN (OPCIONAL) ")
            if self.push1 == '':
                self.push1 = ';push'
            self.push2 = input("SEGUNDA REDE QUE O SERVIDOR VPN VAI ROTEAR PELA VPN (OPCIONAL) ")
            if self.push2 == '':
                self.push2 = ';push'

            return 0

    def make_file(self):
            file = open('server.conf','w')
            for line in self.make_cfg():
                file.write(line[0]+'\n')
            file.close()
            return 0
