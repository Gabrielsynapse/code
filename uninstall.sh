#!/bin/sh

print () {
	echo "[info] $1"
}

if [ ! -e $PREFIX/bin/code ]; then
	print "comando code nao esta instalado"
	exit
fi

print "desinstalando code"

print "deletando arquivo /bin/code"
rm -rf $PREFIX/bin/code

print "deletando diretorio /bin/_code"
rm -rf $PREFIX/bin/_code

print "comando code desinstalado"