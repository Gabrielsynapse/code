#!/bin/bash

path="/sdcard/github/code"
version="v1.0"
opt="$1"
java_newjavaconsole="code/Java_newjavaconsole"

function sh_newjavaconsole(){
	print "criando um novo projeto Java Console"
	if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
		ms_error "nao pode deixar vazio!"
		ms_usage
		exit
	fi
	print "groupId    : $1"
	print "artifactId : $2"
	print "version    : $3"
	java $java_newjavaconsole "$PWD" "$path" "$1" "$2" "$3"
}
function print(){
	echo "[code] $1"
}

function ms_error(){
	echo "[code error] $1"
}
function ms_usage(){
	echo "Usage: code [-options] [args...]"
}
function ms_version(){
	echo "code version: $version"
}
function ms_helper(){
	ms_usage
	ms_version
	echo "options"
	echo "	-javaconsole"
	echo "		Cria um novo projeto Java Console"
	echo "		use: code -javaconsole package name_project version"
	echo "			package: endereco do pacote"
	echo "			name_project: nome do projeto"
	echo "			version: versao do projeto"
}

if [ "$opt" == "-javaconsole" ]; then
	sh_newjavaconsole "$2" "$3" "$4"
elif [ "$opt" == "--help" ]; then
	ms_helper
elif [ "$opt" == "--version" ]; then
	ms_version
else
	ms_usage
fi