#Esse e o install.sh caceta
#!/bin/bash

set -e

clear

# Cores
VERMELHO='\e[1;31m'
VERDE='\e[1;32m'
AMARELO='\e[1;33m'
AZUL='\e[1;34m'
CYA='\e[1;36m'
BRANCO='\e[1;37m'
LARANJA='\e[1;93m'
NC='\e[0m'

# Verifica se o script está sendo executado como root
if [[ $EUID -ne 0 ]]; then
   echo -e "${VERMELHO}Este script deve ser executado como root${NC}"
   exit 1
fi

# Seleciona uma cor aleatória para a saída
NUM_COR=$((RANDOM % 7))
case $NUM_COR in
    0) COR=$VERMELHO;;
    1) COR=$VERDE;;
    2) COR=$AMARELO;;
    3) COR=$AZUL;;
    4) COR=$CYA;;
    5) COR=$LARANJA;;
    *) COR=$BRANCO;;
esac

# Exibe o cabeçalho
echo -e "${COR}"
echo ""
echo "   ███████╗██████╗  █████████╗██╗  ██╗███████╗██╗  ██╗██╗   ██╗██████╗ ██████╗ ███████╗"
echo "   ██╔════╝██╔══██╗██╔════╝██║  ██║██╔════╝██║  ██║██║   ██║██╔══██╗██╔══██╗██╔══██╗██╔════╝"
echo "   ███████╗██████╔╝█████╗  ███████║█████╗  ███████║██║   ██║██████╔╝██████╔╝██████╔╝█████╗  "
echo "   ╚════██║██╔═══╝ ██╔══╝  ██╔══██║██╔══╝  ██╔══██║██║   ██║██╔══██╗██╔══██╗██╔═══╝ ██╔══╝  "
echo "   ███████║██║     ███████╗██║  ██║███████╗██║  ██║╚██████╔╝██║  ██║██║  ██║██║     ███████╗"
echo "   ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝"
echo ""

echo -e "${AZUL}                                     ${NC}"
echo -e "${VERMELHO}                                     [!] Esta ferramenta deve ser executada como ROOT [!]${NC}\n"
echo -e "${CYA}              Selecione a Melhor Opção : \n"
echo -e "${BRANCO}              [1] Kali Linux / Parrot-OS (apt)"
echo -e "${BRANCO}              [2] Arch Linux (pacman)" # Suporte ao Arch Linux adicionado por solicitação de recurso #231
echo -e "${BRANCO}              [0] Sair "

echo -e "${COR}┌──($USER㉿$HOST)-[$(pwd)]"
escolha=$1
if [[ ! $escolha =~ ^[1-2]+$ ]]; then
    read -p "└─$>>" escolha
fi

# Define diretórios de instalação
dir_instalacao="/usr/share/hackingtool"
dir_bin="/usr/bin"

# Verifica se o usuário escolheu uma opção válida e executa os passos de instalação
if [[ $escolha =~ ^[1-2]+$ ]]; then
    echo -e "${AMARELO}[*] Verificando conexão com a Internet ...${NC}"
    echo ""
    if curl -s -m 10 https://www.google.com > /dev/null || curl -s -m 10 https://www.github.com > /dev/null; then
        echo -e "${VERDE}[✔] Conexão com a Internet está OK [✔]${NC}"
        echo ""
        echo -e "${AMARELO}[*] Atualizando lista de pacotes ..."
        # Executa os passos de instalação com base na escolha do usuário
        if [[ $escolha == 1 ]]; then
            sudo apt update -y && sudo apt upgrade -y
            sudo apt-get install -y git python3-pip figlet boxes php curl xdotool wget -y
        elif [[ $escolha == 2 ]]; then
            sudo pacman -Suy -y
            sudo pacman -S python-pip -y
        else
            exit
        fi
        echo ""
        echo -e "${AMARELO}[*] Verificando diretórios...${NC}"
        if [[ -d "$dir_instalacao" ]]; then
            echo -e -n "${VERMELHO}[!] O diretório $dir_instalacao já existe. Deseja substituí-lo? [y/n]: ${NC}"
            read entrada
            if [[ $entrada == "y" ]] || [[ $entrada == "Y" ]]; then
                echo -e "${AMARELO}[*] Removendo módulo existente... ${NC}"
                sudo rm -rf "$dir_instalacao"
            else
                echo -e "${VERMELHO}[✘] Instalação não necessária [✘] ${NC}"
                exit
            fi
        fi
        echo ""
        echo -e "${AMARELO}[✔] https://github.com/PitchuxKali/KaliXPitchu${NC}"
        if sudo git clone https://github.com/PitchuxKali/KaliXPitchu $dir_instalacao; then
            # Instala o ambiente virtual
            echo -e "${AMARELO}[*] Instalando Ambiente Virtual...${NC}"
            if [[ $escolha == 1 ]]; then
                sudo apt install python3-venv -y
            elif [[ $escolha == 2 ]]; then
                echo "Python 3.3+ já vem com um módulo chamado venv."
            fi
            echo ""
            # Cria um ambiente virtual para a ferramenta
            echo -e "${AMARELO}[*] Criando ambiente virtual..."
            sudo python3 -m venv $dir_instalacao/venv
            source $dir_instalacao/venv/bin/activate
            # Instala as dependências
            echo -e "${VERDE}[✔] Ambiente Virtual criado com sucesso [✔]${NC}"
            echo ""
            echo -e "${AMARELO}[*] Instalando dependências...${NC}"
            if [[ $escolha == 1 ]]; then
                pip3 install -r $dir_instalacao/requirements.txt
                sudo apt install figlet -y
            elif [[ $escolha == 2 ]]; then
                pip3 install -r $dir_instalacao/requirements.txt
                sudo -u $SUDO_USER git clone https://aur.archlinux.org/boxes.git && cd boxes
                sudo -u $SUDO_USER makepkg -si
                sudo pacman -S figlet -y
            fi
            # Cria um script para lançar a ferramenta
            echo -e "${AMARELO}[*] Criando um script para iniciar a ferramenta..."
            echo '#!/bin/bash' > $dir_instalacao/hackingtool.sh
            echo "source $dir_instalacao/venv/bin/activate" >> $dir_instalacao/hackingtool.sh
            echo "python3 $dir_instalacao/hackingtool.py \$@" >> $dir_instalacao/hackingtool.sh
            chmod +x $dir_instalacao/hackingtool.sh
            sudo mv $dir_instalacao/hackingtool.sh $dir_bin/hackingtool
            echo -e "${VERDE}[✔] Script criado com sucesso [✔]"
        else
            echo -e "${VERMELHO}[✘] Falha ao baixar Hackingtool [✘]"
            exit 1
        fi

    else
        echo -e "${VERMELHO}[✘] Conexão com a Internet não disponível [✘]${NC}"
        exit 1
    fi

    if [ -d $dir