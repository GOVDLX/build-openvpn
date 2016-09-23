import os
import MAKE_CERTS
import MAKE_CFG_SERVER
############################### OPCOES ###############################
print("1 - Instalacao e configuracao do ZERO")
print("2 - Adicionar chave e arquivo de configuracao para uma nova maquina")
print("3 - Gerar arquivo de configuracao pro Servidor OPENVPN")
print("0 - SAIR")
op = input("ESCOLHA UMA OPCAO: ")

if op == '1':
    DH = input("Tamanho da chave DiffHealm DH (default 2048): ")
    CA = input("Tempo de expiracao do root CA (default 365) em dias: ")
    KEY = input("Tempo de expiracao da chave KEY (default 365) em dias: ")
    PA = input("Pais (Exemplo: BR): ")
    EST = input("Estado (Exemplo: ES): ")
    CID = input("Cidade (Exemplo: Serra): ")
    EMP = input("Empresa (Exemplo: BNICHOST): ")
    MAIL = input("Email (Exemplo: suporte@bnichost.com.br): ")
    ST = input("Setor (Exemplo: TI): ")
    NC = input("Nome da Chave (Exemplo: BNICHOST): ")

    os.system('apt-get install openvpn openssl -y')
    os.system('mkdir -p /etc/openvpn/easy-rsa/')
    os.system('cp -rv EasyRSA-2.2.2 /etc/openvpn/easy-rsa/2.2.2/')
    os.system('ln -s /etc/openvpn/easy-rsa/2.2.2/keys /etc/openvpn/keys')
    os.system('mkdir -p /var/log/openvpn/')
    a = MAKE_CERTS
    mk = a.MAKE_CERTS(DH,CA,KEY,PA,EST,CID,EMP,MAIL,ST,NC)
    mk.build_ca()
    mk.build_dh()
    mk.build_key_server()

    exit(0)

if op == '2':
    print("W - Maquina Windows")
    print("L - Maquina Linux")
    op = input("ESCOLHA O TIPO DE SISTEMA OPERACIONAL: ")
    if op == 'W' or op == 'w':
        print("Gerando pacote para maquina Windows")

    if op == 'L' or op == 'l':
        print("Gerando pacote para maquina Linux")
    else:
        exit(1)

    exit(0)
if op == '3':
    a = MAKE_CFG_SERVER
    cfg = a.MAKE_CFG_SERVER()
    cfg.questions()
    print('Criando arquivo de configuracao do Servidor')
    cfg.make_file()


    exit(0)
if op == '0':
    exit(0)

exit(0)