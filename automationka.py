#!/usr/bin/env python3
# Version 1.1.0
import os
import sys
import webbrowser
from platform import system
from time import sleep
from core import HackingToolsCollection
from tools.anonsurf import AnonSurfTools
from tools.ddos import DDOSTools
from tools.exploit_frameworks import ExploitFrameworkTools
from tools.forensic_tools import ForensicTools
from tools.information_gathering_tools import InformationGatheringTools
from tools.other_tools import OtherTools
from tools.payload_creator import PayloadCreatorTools
from tools.phishing_attack import PhishingAttackTools
from tools.post_exploitation import PostExploitationTools
from tools.remote_administration import RemoteAdministrationTools
from tools.reverse_engineering import ReverseEngineeringTools
from tools.sql_tools import SqlInjectionTools
from tools.steganography import SteganographyTools
from tools.tool_manager import ToolManager
from tools.webattack import WebAttackTools
from tools.wireless_attack_tools import WirelessAttackTools
from tools.wordlist_generator import WordlistGeneratorTools
from tools.xss_attack import XSSAttackTools

logo = """
  _____ _       _     _    _ _    
 |  __ (_)     | |   | |  | (_)   
 | |__) | _ __ | | __| |  | |_ ___
 |  ___/ | '_ \| |/ _` |  | | / __|
 | |   | | | | | | (_| |  | | \__ \
 |_|   |_|_| |_|_|\__,_|  |_|_|___/
                                   
"""

print(logo)

# Lista de todas as ferramentas
all_tools = [
    AnonSurfTools(),
    InformationGatheringTools(),
    WordlistGeneratorTools(),
    WirelessAttackTools(),
    SqlInjectionTools(),
    PhishingAttackTools(),
    WebAttackTools(),
    PostExploitationTools(),
    ForensicTools(),
    PayloadCreatorTools(),
    ExploitFrameworkTools(),
    ReverseEngineeringTools(),
    DDOSTools(),
    RemoteAdministrationTools(),
    XSSAttackTools(),
    SteganographyTools(),
    OtherTools(),
    ToolManager()
]

class AllTools(HackingToolsCollection):
    TITLE = "Pitchu Tools"
    TOOLS = all_tools

    def show_info(self):
        """Exibe o logotipo e outras informações da coleção."""
        print(logo + '\033[0m \033[97m')

if __name__ == "__main__":
    try:
        if system() == 'Linux':
            fpath = os.path.expanduser("~/hackingtoolpath.txt")
            if not os.path.exists(fpath):
                os.system('clear')
                print("""
                        [@] Definir Pasta (Todas suas ferramentas serão adicionadas para este diretório!!)
                        [1] Manual 
                        [2] Padrão
                """)
                choice = input("Pitchu =>> ").strip()

                if choice == "1":
                    inpath = input("Insira pasta (Com nome de diretório) >> ").strip()
                    with open(fpath, "w") as f:
                        f.write(inpath)
                    print(f"Sucesso ao definir pasta para: {inpath}")
                elif choice == "2":
                    autopath = "/home/KaliXPitchuu/"
                    with open(fpath, "w") as f:
                        f.write(autopath)
                    print(f"Sua pasta padrão é: {autopath}")
                    sleep(3)
                else:
                    print("Escolha inválida, tente novamente.")
                    sys.exit(0)

            with open(fpath) as f:
                archive = f.readline().strip()
                os.makedirs(archive, exist_ok=True)
                os.chdir(archive)
                AllTools().show_options()

        elif system() == "Windows":
            print(r"\033[91m Execute este script em Debian ou derivados \e[00m")
            sleep(2)
            webbrowser.open_new_tab("https://tinyurl.com/y522modc")

        else:
            print("Sistema não suportado. Verifique o sistema ou ocorrem erros!")

    except KeyboardInterrupt:
        print("\nSaindo...")
        sleep(2)