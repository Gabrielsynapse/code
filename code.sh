#!/bin/bash

path="/bin"
version="v1.0"
opt="$1"
py_newjavaconsole=$path"/_code/py_newjavaconsole.py"
py_newjar=$path"/_code/py_newjar.py"
py_newfilejava=$path"/_code/py_newfilejava.py"
py_deletefilejava=$path"/_code/py_deletefilejava.py"

function sh_newjavaconsole(){
	shift
	print "criando um novo projeto Java Console"
	if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
		ms_error "nao pode deixar vazio!"
		ms_usage
		exit
	fi
	print "groupId    : $1"
	print "artifactId : $2"
	print "version    : $3"

	python3 $py_newjavaconsole "$path" "$PWD" "$@"
}
function sh_newjar(){
	shift
	print "criando um novo projeto Jar"
	if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
		ms_error "nao pode deixar vazio!"
		ms_usage
		exit
	fi
	print "groupId    : $1"
	print "artifactId : $2"
	print "version    : $3"
	python3 $py_newjar "$path" "$PWD" "$@"
}
function sh_newfilejava(){
	shift
	if [ -e ./pom.xml ]; then
		python3 $py_newfilejava "$path" "$PWD" "$@"
	else
		ms_error "navegue até a pasta que contem o arquivo pom.xml"
	fi
}
function sh_deletefilejava(){
	shift
	if [ -e ./pom.xml ]; then
		python3 $py_deletefilejava "$path" "$PWD" "$@"
	else
		ms_error "navegue até a pasta que contem o arquivo pom.xml"
	fi
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
	echo "		use: code -javaconsole [package] [name_project] [version] [dependency...]"
	echo "			package: endereco do pacote"
	echo "			name_project: nome do projeto"
	echo "			version: versao do projeto"
	echo "			dependency: dependencia do projeto"
	echo "				groupId:artifactId:version"
}

if [ "$opt" == "-javaconsole" ]; then
	sh_newjavaconsole $@;
elif [ "$opt" == "-jar" ]; then
	sh_newjar $@;
elif [ "$opt" == "-newfilejava" ]; then
	sh_newfilejava "$@"
elif [ "$opt" == "-deletefilejava" ]; then
	sh_deletefilejava "$@"
elif [ "$opt" == "--help" ]; then
	ms_helper
elif [ "$opt" == "--version" ]; then
	ms_version
else
	ms_usage
fi