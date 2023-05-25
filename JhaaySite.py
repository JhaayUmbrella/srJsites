import socket

#jhay 

def obter_ip_por_link(link):  #funcao

    try:

        ip = socket.gethostbyname(link) #string

        return ip

    except socket.gaierror: #socket

        return None

#digitar o ip para a acao
print('''
=============================
= Coloque o site que deseja
=============================
''')
link = input("Root@Jhaay:  ")

ip = obter_ip_por_link(link)

#respostas {puxar string}

if ip:

    print(f"O endereço IP do link {link} é: {ip}")

else:

    print("Não foi possível obter o endereço IP.")
