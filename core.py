import os
import sys
import webbrowser
from platform import system
from traceback import print_exc
from typing import Callable, List, Tuple


def clear_screen():
    """Limpa a tela do terminal com base no sistema operacional."""
    os.system("cls" if system() == "Windows" else "clear")


def validate_input(ip, val_range):
    """Valida a entrada do usuário, garantindo que seja um número inteiro dentro de um intervalo."""
    val_range = val_range or []
    try:
        ip = int(ip)
        if ip in val_range:
            return ip
    except ValueError:
        return None
    return None


class HackingTool:
    """Classe base para uma ferramenta de hacking."""

    TITLE: str = ""  # Usado para mostrar informações no menu
    DESCRIPTION: str = ""

    INSTALL_COMMANDS: List[str] = []
    INSTALLATION_DIR: str = ""

    UNINSTALL_COMMANDS: List[str] = []

    RUN_COMMANDS: List[str] = []

    OPTIONS: List[Tuple[str, Callable]] = []

    PROJECT_URL: str = ""

    def __init__(self, options=None, installable: bool = True, runnable: bool = True):
        """Inicializa a ferramenta com opções de instalação e execução."""
        options = options or []
        if isinstance(options, list):
            self.OPTIONS = []
            if installable:
                self.OPTIONS.append(('Install', self.install))
            if runnable:
                self.OPTIONS.append(('Run', self.run))
            self.OPTIONS.extend(options)
        else:
            raise Exception("options must be a list of (option_name, option_fn) tuples")

    def show_info(self):
        """Exibe informações sobre a ferramenta, incluindo a descrição e URL do projeto."""
        desc = self.DESCRIPTION
        if self.PROJECT_URL:
            desc += f'\n\t[*] {self.PROJECT_URL}'
        os.system(f'echo "{desc}" | boxes -d boy | lolcat')

    def show_options(self, parent=None):
        """Mostra as opções disponíveis e processa a entrada do usuário."""
        clear_screen()
        self.show_info()
        for index, option in enumerate(self.OPTIONS):
            print(f"[{index + 1}] {option[0]}")
        if self.PROJECT_URL:
            print(f"[{98}] Open project page")
        print(f"[{99}] Back to {parent.TITLE if parent is not None else 'Exit'}")
        option_index = input("Select an option: ").strip()
        try:
            option_index = int(option_index)
            if option_index - 1 in range(len(self.OPTIONS)):
                ret_code = self.OPTIONS[option_index - 1][1]()
                if ret_code != 99:
                    input("\n\nPress ENTER to continue:").strip()
            elif option_index == 98:
                self.show_project_page()
            elif option_index == 99:
                if parent is None:
                    sys.exit()
                return 99
        except (TypeError, ValueError):
            print("Please enter a valid option")
            input("\n\nPress ENTER to continue:").strip()
        except Exception:
            print_exc()
            input("\n\nPress ENTER to continue:").strip()
        return self.show_options(parent=parent)

    def before_install(self):
        """Método para ser sobrescrito antes da instalação."""
        pass

    def install(self):
        """Instala a ferramenta executando comandos de instalação."""
        self.before_install()
        if isinstance(self.INSTALL_COMMANDS, (list, tuple)):
            for install_command in self.INSTALL_COMMANDS:
                os.system(install_command)
            self.after_install()

    def after_install(self):
        """Método para ser sobrescrito após a instalação."""
        print("Successfully installed!")

    def before_uninstall(self) -> bool:
        """Pede confirmação ao usuário e retorna se a desinstalação deve prosseguir."""
        return True

    def uninstall(self):
        """Desinstala a ferramenta executando comandos de desinstalação."""
        if self.before_uninstall():
            if isinstance(self.UNINSTALL_COMMANDS, (list, tuple)):
                for uninstall_command in self.UNINSTALL_COMMANDS:
                    os.system(uninstall_command)
            self.after_uninstall()

    def after_uninstall(self):
        """Método para ser sobrescrito após a desinstalação."""
        pass

    def before_run(self):
        """Método para ser sobrescrito antes da execução."""
        pass

    def run(self):
        """Executa a ferramenta executando comandos definidos."""
        self.before_run()
        if isinstance(self.RUN_COMMANDS, (list, tuple)):
            for run_command in self.RUN_COMMANDS:
                os.system(run_command)
            self.after_run()

    def after_run(self):
        """Método para ser sobrescrito após a execução."""
        pass

    def is_installed(self, dir_to_check=None):
        """Método não implementado para verificar se a ferramenta está instalada."""
        print("Unimplemented: DO NOT USE")
        return "?"

    def show_project_page(self):
        """Abre a página do projeto no navegador web."""
        webbrowser.open_new_tab(self.PROJECT_URL)


class HackingToolsCollection:
    """Classe que gerencia uma coleção de ferramentas de hacking."""

    TITLE: str = ""  # Usado para mostrar informações no menu
    DESCRIPTION: str = ""
    TOOLS: List[HackingTool] = []

    def __init__(self):
        """Inicializa a coleção de ferramentas."""
        pass

    def show_info(self):
        """Exibe informações sobre a coleção de ferramentas."""
        os.system(f"figlet -f standard -c {self.TITLE} | lolcat")
        # os.system(f'echo "{self.DESCRIPTION}" | boxes -d boy | lolcat')
        # print(self.DESCRIPTION)

    def show_options(self, parent=None):
        """Mostra as opções disponíveis na coleção e processa a entrada do usuário."""
        clear_screen()
        self.show_info()
        for index, tool in enumerate(self.TOOLS):
            print(f"[{index}] {tool.TITLE}")
        print(f"[{99}] Back to {parent.TITLE if parent is not None else 'Exit'}")
        tool_index = input("Choose a tool to proceed: ").strip()
        try:
            tool_index = int(tool_index)
            if tool_index in range(len(self.TOOLS)):
                ret_code = self.TOOLS[tool_index].show_options(parent=self)
                if ret_code != 99:
                    input("\n\nPress ENTER to continue:").strip()
            elif tool_index == 99:
                if parent is None:
                    sys.exit()
                return 99
        except (TypeError, ValueError):
            print("Please enter a valid option")
            input("\n\nPress ENTER to continue:").strip()
        except Exception:
            print_exc()
            input("\n\nPress ENTER to continue:").strip()
        return self.show_options(parent=parent)