#!/bin/bash

function print(){
	echo "[info] $1"
}

if [ ! -e /bin/code ]; then
	print "comando code nao esta instalado"
	exit
fi

print "desinstalando code"

print "deletando arquivo /bin/code"
rm -rf /bin/code

print "deletando diretorio /bin/_code"
rm -rf /bin/_code

print "comando code desinstalado"