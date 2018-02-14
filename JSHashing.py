#!/usr/bin/python
#_*_coding: latin-1 _*_
import StringIO
import getopt
import hashlib
import sys
import os
import time
print "  "
print "JSHashing Cracking"
print "Versão 1.0"
print "Criado por Joas Antonio\n"

def info():
  print " "
  print "Informações:"
  print "[+] Opções:"
  print "[+](-h) Hash"
  print "[+](-t) Tipo [Quais hashs são suportadas]"
  print "[+](-w) Wordlist"
  print "[+](-n) Numeros de bruteforce"
  print "[+](-v) Verbose\n"
  print "[+] Exemplos:"
  print "[!] ./JSHashing.py -h <hash> -t md5 -w wordlist.txt"
  print "[!] ./JSHashing.py -h <hash> -t sha384 -n -v"
  print "[+] Hashs Suportadas:"
  print "[!] md5, sha1, sha224, sha256, sha384, sha512"
  print "[+] Por enquanto só isso\n"
  

def checkOS():
    if os.name == "nt":
        operatingSystem = "Windows"
    elif os.name == "unix":
        operatingSystem = "Linux"
    else:
        operatingSystem = "Nenhum"
    return operatingSystem


class hashCracking:
  
  def hashCrackWordlist(self, userHash, hashType, wordlist, verbose):
    start = time.time()
    self.lineCount = 0
    if (hashType == "md5"):
       h = hashlib.md5
    elif (hashType == "sha1"):
       h = hashlib.sha1
    elif (hashType == "sha224"):
       h = hashlib.sha224
    elif (hashType == "sha256"):
       h = hashlib.sha256
    elif (hashType == "sha384"):
       h = hashlib.sha384
    elif (hashType == "sha512"):
       h = hashlib.sha512
    else:
       print "[-]É %s um tipo de hash suportada?" % hashType
       exit()
    with open(wordlist, "rU") as infile:
      for line in infile:
        line = line.strip()
        lineHash = h(line).hexdigest()
        if (verbose == True):
            sys.stdout.write('\r' + str(line) + ' ' * 20)
            sys.stdout.flush()
        if (lineHash == userHash.lower()):
            end = time.time()
            print "\n[+]Hash é: %s" % line
            print "[!]Palavras tentadas: %s" % self.lineCount
            print "[!]Tempo: %s segundos" % round((end-start), 2)
            exit()
        else:
            self.lineCount = self.lineCount + 1
    end = time.time()
    print "\n[-]Quebra Falhou!"
    print "[*]Chegou ao fim da wordlist"
    print "[*]Palavras tentadas: %s" % self.lineCount
    print "[*]Tempo: %s segundos" % round((end-start), 2)
    exit()

  def hashCrackNumberBruteforce(self, userHash, hashType, verbose):
    start = time.time()
    self.lineCount = 0
    if (hashType == "md5"):
       h = hashlib.md5
    elif (hashType == "sha1"):
       h = hashlib.sha1
    elif (hashType == "sha224"):
       h = hashlib.sha224
    elif (hashType == "sha256"):
       h = hashlib.sha256
    elif (hashType == "sha384"):
       h = hashlib.sha384
    elif (hashType == "sha512"):
       h = hashlib.sha512
    else:
       print "[-]É %s um tipo de hash suportada?" % hashType
       exit()
    while True:
       line = "%s" % self.lineCount
       line.strip()
       numberHash = h(line).hexdigest().strip()
       if (verbose == True):
           sys.stdout.write('\r' + str(line) + ' ' * 20)
           sys.stdout.flush()
       if (numberHash.strip() == userHash.strip().lower()):
           end = time.time()
           print "\n[+]Hash é: %s" % lineCount
           print "[*]Tempo: %s segundos" % round((end-start), 2)
           break
       else:
         self.lineCount = self.lineCount + 1

def main(argv):
  hashType = userHash = wordlist = verbose = numbersBruteforce = None
  print "[Corrida em %s]\n" % checkOS()
  try:
      opts, args = getopt.getopt(argv,"ih:t:w:nv",["ifile=","ofile="])
  except getopt.GetoptError:
      print '[*]./JSHashing.py -t <tipo> -h <hash> -w <wordlist>'
      print '[*]Para mais detalhes digite: ./JSHashing.py -i mostrar informações'
      sys.exit(1)
  for opt, arg in opts:
      if opt == '-i':
          info()
          sys.exit()
      elif opt in ("-t", "--tipe"):
          hashType = arg
      elif opt in ("-h", "--hash"):
          userHash = arg
      elif opt in ("-w", "--wordlist"):
          wordlist = arg
      elif opt in ("-v", "--verbose"):
          verbose = True
      elif opt in ("-n", "--numeros"):
          numbersBruteforce = True
  if not (hashType and userHash):
      print '[*]./JSHashing.py -t <tipo> -h <hash> -w <wordlist>'
      print '[*]./JSHashing.py -i <mais informações>'
      sys.exit()
  print "[*]Hash: %s" % userHash
  print "[*]Tipo de Hash: %s" % hashType
  print "[*]Wordlist: %s" % wordlist
  print "[+]Quebrando..."
  try:
      h = hashCracking()
      if (numbersBruteforce == True):
         h.hashCrackNumberBruteforce(userHash, hashType, verbose)
      else:
         h.hashCrackWordlist(userHash, hashType, wordlist, verbose)

  except IndexError:
        print "\n[-]Hash não quebrada:"
        print "[*]Chegou ao fim da wordlist"
        print "[*]Experimente outra wordlist"
        print "[*]Palavras tentadas: %s" % h.lineCount
        
  except KeyboardInterrupt:
        print "\n[Saindo...]"
        print "Palavras tentadas: %s" % h.lineCount
        
  except IOError:
        print "\n[-]Não conseguiu encontrar a wordlist"
        print "[*]Isto está certo?"
        print "[>]%s" % wordlist
        
if __name__ == "__main__":
    main(sys.argv[1:])
