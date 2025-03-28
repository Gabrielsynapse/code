#!/bin/bash

function print(){
	echo "[info] $1"
}

print "instalando code"

print "compilando shell.sh e deletando arquivos desnecessario"

shc -f "code.sh" -o "code" && rm "code.sh."*

print "movendo code para /bin"

mv "code" "/bin/code"

print "adcionando permissao para code"

chmod +xrw /bin/code

print "copiando pasta de binarios"

cp "_code" -r "/bin"

print "adcionando permisao para o diretorio _code"

chmod 700 "/bin/_code"
chmod +xwr "/bin/_code"*

print "deletando arquivos .java em /bin/_code"
rm -rf /bin/_code/*.java

print "comando instalado com sucesso!"

code --version