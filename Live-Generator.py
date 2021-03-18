#!/usr/bin/env python
#-*- coding: iso-8859-1 -*-
import getopt
import time
import os
import sys
import datetime
from random import randint

version = "1.0.0"
#Mensaje
os.system ("clear")
print("\033[1;32m+\033[1;36m LIVE-GENERATOR")
time.sleep(1.2)
#Informacion de ayuda
def dexter1999():
    print("\033[1;32m             ______________")
    print("\033[1;32m       ,===:'.,            `-._")
    print("\033[1;32m           `:.`---.__         `-._")
    print("\033[1;32m             `:.     `--.         `.")
    print("\033[1;32m               \.        `.         `.")
    print("\033[1;32m       (,,(,    \.         `.   ____,-`.,")
    print("\033[1;32m     (,'     `/   \.   ,--.___`.'")
    print("\033[1;32m ,  ,'  ,--.  `,   \.;'         `")
    print("\033[1;32m `{D, {    \  :    \;")
    print("\033[1;32m   V,,'    /  /    //")
    print("\033[1;32m   j;;    /  ,' ,-//.    ,---.      ,")
    print("\033[1;32m   \;'   /  ,' /  _  \  /  _  \   ,'/")
    print("\033[1;32m         \   `'  / \  `'  / \  `.' /")
    print("\033[1;32m          `.___,'   `.__,'   `.__,'")
dexter1999()
time.sleep(1.2)
print("")
print("\033[1;32m Informatic in Termux")
print("")
time.sleep(1.6)
print(" https://t.me/Informatic_in_Termux_1")
print("")
time.sleep(2.2)


#Informacion de ayuda
def usage():
    print("+\033[1;37m Metodo de uso\033[1;31m +")
    print("")
    print("\033[1;33m  python2 Live-Generator.py -b \033[1;31m >>>\033[1;33m Opciones de uso")
    print("\033[1;33m  python2 Live-Generator.py -h \033[1;31m >>>\033[1;33m Mensaje de ayuda")
    print("")
    print("+\033[;32m Opciones de uso\033[1;31m +")
    print("")
    print("\033[1;32m -b, \033[1;31m >>>\033[1;32m -bin\033[1;31m >>>\033[1;32m Formato de bin")
    print("\033[1;32m -u, \033[1;31m >>>\033[1;32m -cantidad\033[1;31m >>>\033[1;32m tarjetas a generar")
    print("\033[1;32m -c, \033[1;31m >>>\033[1;32m -ccv\033[1;31m >>>\033[1;32m Genera ccv al azar")
    print("\033[1;32m -d, \033[1;31m >>>\033[1;32m -date\033[1;31m >>>\033[1;32m Genera fechas al azar")
    print("")
    print("+\033[;33m Ejemplo de uso\033[1;31m +")
    print("")
    print("\033[1;37m EL USO DE ESTA HERRAMIENTA\033[0m")
    print("\033[1;37m ES RESPONSABILIDAD DE QUIEN LA UTILICE")
    print("")
    print("\033[1;36mpython2 Live-Generator.py -b 123456xxxxxxxxxx -u 30 -d -c ")
    print("")
#Arg parser
def parseOptions(argv):
    bin_format = ""
    saveopt = False
    limit = 30
    ccv = False
    date = False
    check = False

    try:
        opts, args = getopt.getopt(argv, "h:b:u:gcd",["help", "bin", "guardar", "cantidad", "ccv", "date"])
        for opt, arg in opts:
            if opt in ("-h"):
                usage()
                sys.exit()
            elif opt in ("-b", "-bin"):
                bin_format = arg
            elif opt in ("-g", "-guardar"):
                saveopt = True
            elif opt in ("u", "-cantidad"):
                limit = arg
            elif opt in ("-c", "-ccv"):
                ccv = True
            elif opt in ("-d", "-date"):
                date = True

        return(bin_format, saveopt, limit, ccv, date)

    except getopt.GetoptError:
        usage()
        sys.exit(2)

#CHECKER BASADO EN ALGORITMO LUHN
def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """

    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )

#GENERA UNA BASE DE BIN XXXXXXXXXXXXXXXX
def ccgen(bin_format):
    out_cc = ""
    if len(bin_format) == 16:
        #Iteration over the bin
        for i in range(15):
            if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                out_cc = out_cc + bin_format[i]
                continue
            elif bin_format[i] in ("x"):
                out_cc = out_cc + str(randint(0,9))
            else:
                print("\nCaracter no valido en el formato: {}\n".format(bin_format))
                print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
                print("Ayuda: python2 Live-Generator.py -h \n")
                sys.exit()

        #Generate checksum (last digit) -- IMPLICIT CHECK
        for i in range(10):
            checksum_check = out_cc
            checksum_check = checksum_check + str(i)

            if cardLuhnChecksumIsValid(checksum_check):
                out_cc = checksum_check
                break
            else:
                checksum_check = out_cc

    else:
        print("\033[1;32m")
        print("\nERROR: Inserta un bin valido\n")
        print("SOLUCION: El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        print("AYUDA: python2 Live-Generator.py -h\n")
        sys.exit()

    return(out_cc)

#Write on a file that takes a list for the argument
def save(generated):
    now = datetime.datetime.now()
    file_name = "cc-gen_output_{0}.txt".format(str(now.day) + str(now.hour) + str(now.minute) + str(now.second))
    f = open(file_name, 'w')
    for line in generated:
        f.write(line + "\n")
    f.close

#Random ccv gen
def ccvgen():
    ccv = ""
    num = randint(10,999)

    if num < 100:
        ccv = "0" + str(num)
    else:
        ccv = str(num)

    return(ccv)

#Random exp date
def dategen():
    now = datetime.datetime.now()
    date = ""
    month = str(randint(1, 12))
    current_year = str(now.year)
    year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
    date = month + "|" + year

    return date

#The main function
def main(argv):
    bin_list = []
    #get arg data
    (bin_format, saveopt, limit, ccv, date) = parseOptions(argv)
    if bin_format is not "":
        for i in range(int(limit)):
            if ccv and date:
                bin_list.append(ccgen(bin_format) + "|" + ccvgen() + "|" + dategen())
                print(bin_list[i])
            elif ccv and not date:
                bin_list.append(ccgen(bin_format) + "|" + ccvgen())
                print(bin_list[i])
            elif date and not ccv:
                bin_list.append(ccgen(bin_format) + "|" + dategen())
                print(bin_list[i])
            elif not date and not ccv:
                bin_list.append(ccgen(bin_format))
                print(bin_list[i])

        if not bin_list:
            print("\nERROR: el bin que insertaste no es valido\n")
        else:
            print("\n Todas las tarjetas fueron validadas con exito ")
            print("\n Pueden ser usadas satisfactoriamente")

        if saveopt:
            save(bin_list)
    else:
        usage()
        sys.exit()

if __name__ == '__main__':
    main(sys.argv[1:])
