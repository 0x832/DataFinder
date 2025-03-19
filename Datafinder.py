import argparse 
import time 
import os
import sys
from googlesearch import search 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from urllib.error import HTTPError


PURPLE = '\033[1;35m'
BLUE = '\033[94m'
CYAN = '\033[96m'
LIGHT_CYAN = '\033[1;36m'
GREEN = '\033[92m'
LIGHT_GREEN = '\033[1;32m' 
YELLOW_DARCK = '\033[93m'

LIGHT_RED = '\033[1;31m' 
RED = '\033[91m'
RESET = '\033[0m'
WHITE = '\033[1m'
UNDERLINE = '\033[4m'


def clear():
    if os.name == "nt":
        os.system("cls")
    elif os.name == 'posix': 
        os.system('clear')

def ocultar_cursor():
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()

def mostrar_cursor():
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()


def inicio_script():
    ocultar_cursor()
    
    clear()
    
    print("\n          ╭━━━╮╱╱╭╮╱╱╱╭━━━╮╱╱╱╱╱╭╮")
    print("          ╰╮╭╮┃╱╭╯╰╮╱╱┃╭━━╯╱╱╱╱╱┃┃")
    time.sleep(0.4)
    print("          ╱┃┃┃┣━┻╮╭╋━━┫╰━━┳┳━╮╭━╯┣━━┳━╮")
    print("          ╱┃┃┃┃╭╮┃┃┃╭╮┃╭━━╋┫╭╮┫╭╮┃┃━┫╭╯")
    time.sleep(0.4)

    print("          ╭╯╰╯┃╭╮┃╰┫╭╮┃┃╱╱┃┃┃┃┃╰╯┃┃━┫┃")
    print("          ╰━━━┻╯╰┻━┻╯╰┻╯╱╱╰┻╯╰┻━━┻━━┻╯")
    time.sleep(0.4)
    mostrar_cursor()
    print(f"         Para más información {RED}-h, --help {RESET} \n")
    print(f'         Ejemplo de uso: {RED} -si "edu " -in "vulnerability" -t "pdf redes" -be "2023-01-01" -na "documento" --nu "10"{RESET}\n\n')
    exit()

def inicio_script2():
        print("\n")
        time.sleep(0.3)

        print("    █▀▄ ▄▀█ ▀█▀ ▄▀█   █▀▀ █ █▄░█ █▀▄ █▀▀ █▀█")
        time.sleep(0.3)

        print("    █▄▀ █▀█ ░█░ █▀█   █▀░ █ █░▀█ █▄▀ ██▄ █▀▄")
        print("\n")

def estructura():
    clear()

    parser = argparse.ArgumentParser(description='Descripción de tu script\n'
        'Ejemplo de uso: {RED} -si "edu " -in "vulnerability" -t "pdf redes" -be "2023-01-01" -na "documento" --nu "10"{RESET}\n\n', add_help=False)

    print("\n")
    parser.add_argument('-h', '--help', action='help', help='Para más información')
    parser.add_argument('-S', '--search', metavar='', help='Parámetro básico de búsqueda')
    parser.add_argument('-si', '--site', metavar='', help='Limita los resultados a un dominio específico(ejemplo: -si ".edu")')
    parser.add_argument('-all', '--allinurl', metavar='', help='Muestra páginas que contienen todos los términos especificados en la URL (ejemplo: -all "informática")')
    parser.add_argument('-if', '--info', metavar='', help='Proporciona información sobre un dominio o página web específica (ejemplo: -if "ejemplo.com")')
    parser.add_argument('-in', '--intext', metavar='', help='Busca una palabra o frase específica en el contenido del texto de las páginas web (ejemplo:  -in "vulnerability")')
    parser.add_argument('-inu', '--inurl', metavar='', help='Busca páginas con términos específicos en la URL.(ejemplo: -inu "log4j")')
    parser.add_argument('-it', '--intitle', metavar='', help='Busca páginas con términos específicos en el título(ejemplo: -it "passwords" )')
    parser.add_argument('-al', '--allintitle', metavar='', help='Muestra páginas que contienen todos los términos especificados en el título (ejemplo: -al "login page")')
    parser.add_argument('-t', '--filetype', metavar='', help='Busca archivos de un tipo de extensión específica (ejemplo: -t "pdf networking")')
    parser.add_argument('-df', '--define', metavar='', help='Muestra definiciones de una palabra o frase (ejemplo: -df "linux")')
    parser.add_argument('-m', '--movie', metavar='', help='Proporciona información sobre una película específica (ejemplo: -m "whoami")')
    parser.add_argument('-ac', '--actions', metavar='', help='Muestra información financiera sobre una acción en particular (ejemplo: -ac "meta")')
    parser.add_argument('-be', '--before', metavar='', help='Limita los resultados a páginas publicadas antes de una fecha específica (ejemplo: -be"2005-01-01" -it "hackers")')
    parser.add_argument('-af', '--after', metavar='', help='Limita los resultados a páginas publicadas después de una fecha específica (ejemplo: -af"2005-01-01" -it "hackers")')
    parser.add_argument('-mp', '--map', metavar='', help='Muestra un mapa de la ubicación especificada (ejemplo: -mp "portugala")')
    parser.add_argument('-na', '--name', metavar='', help='Crea un archivo TXT con el nombre desado')
    parser.add_argument('--nu', '--num', metavar='', help='Cantitdad de respuestas')

    args = parser.parse_args()

    query = ""

    no_search = any([   
        args.site,args.allinurl,args.info,args.intext,args.inurl,args.intitle,args.allintitle,args.filetype,args.define,args.movie,args.actions,args.before,args.after,args.map])

    if args.name:
        nombre_file = f'{args.name}' 
    else:
        nombre_file = "resultados" 

    def busqueda():
        filename = f"{nombre_file}.txt"
        lista=[]

        num = int(args.nu) if args.nu else 10
        resultados_encontrados = False 

        inicio_script2()
        print(f"Buscando en información: {RED}{query}{RESET}")

        google = enumerate(search(query, start=0, pause=1, stop=num), 1)
     
        try:  
            for i, resultado in google:
                if resultado: 
                    datos = f"\n    Resultado {i}: {resultado}"
                    print(datos)
                    lista.append(datos)
                    resultados_encontrados = True 

            if resultados_encontrados:
                with open(filename, 'a') as archivo:
                    archivo.writelines(lista)  
                    print(f"\n    {PURPLE}Se ha creado el archivo con los enlaces: {RED}{filename}{RESET}\n")    
            else:
                print("    \nNo se encontraron resultados.")
                exit()

        except HTTPError as e:
            if e.code == 429:
                print("Demasiadas solicitudes")

    if args.search and not no_search:  
        busqueda()

    elif args.search:
    
        inicio_script2()
        time.sleep(0.3)
        print(f"    {RED}Error: El parámetro -S/--search no puede combinarse con otros argumentos de búsqueda específicos.{RESET}")
        time.sleep(0.3)

        print("    Este parámetro está diseñado para búsquedas generales y debe usarse solo o con -na/--name\n")
        time.sleep(0.3)

        print(f"    Para más información {RED}-h/--help{RESET}\n")    
      
    search_args = {         
        "site": "site",
        "allinurl": "allinurl",
        "info": "info",
        "intext": "intext",
        "inurl": "inurl",
        "intitle": "intitle",
        "allintitle": "allintitle",
        "filetype": "filetype",
        "define": "define",
        "movie": "movie",
        "actions": "stock",
        "before": "before",
        "after": "after",
        "map": "map",
        "num": "num"
    }

    for arg, query_param in search_args.items(): 
                                              
        value = getattr(args, arg, None)

        if value and not args.search:
            query += f"{query_param}:{value} "

    if query: 
        busqueda()

def main():
    if len(sys.argv) > 1:  
        estructura()
    else:
        inicio_script()

if __name__ == '__main__':
    main()



