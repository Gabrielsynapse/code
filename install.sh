#!/bin/sh

print () {
	echo "[info] $1"
}

print "instalando code"

print "compilando shell.sh e deletando arquivos desnecessario"

shc -f "code.sh" -o "code" && rm "code.sh."*

print "movendo code para $PREFIX/bin"

mv "code" "$PREFIX/bin/code"

print "adcionando permissao para code"

chmod +xrw "$PREFIX/bin/code"

print "copiando pasta de binarios"

cp "./_code" -r "$PREFIX/bin"

print "adcionando permisao para o diretorio _code"

chmod 700 "$PREFIX/bin/_code"
chmod +xwr "$PREFIX/bin/_code"*

print "deletando arquivos .java em /bin/_code"
rm -rf $PREFIX/bin/_code/*.java

print "comando instalado com sucesso!"

code --version