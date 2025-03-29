import os
import util
from shutil import rmtree
from sys import argv

###########variaveis#############
args       = argv
path       = args[1];
pwd        = args[2];
groups     = args[3:];
srcPom  = pwd + "/pom.xml";
srcJava = pwd + "/src/main/java"
srcTest = pwd + "/src/test/java"
#################################

d1 = util.existDependency(srcPom,"org.junit.jupiter","junit-jupiter-api","5.10.2")
d2 = util.existDependency(srcPom,"org.junit.jupiter","junit-jupiter-engine","5.10.2")

for group in groups:
	java = srcJava + "/" + (group.replace(".","/"))
	test = srcTest + "/" + (group.replace(".","/"))
	# se for diretorio:
	if os.path.isdir(java):
		#deve deletar o diretorio
		util.info(f"deletando pasta {java}")
		rmtree(java)
		#se tiver teste:
		if d1 and d2:
			#deletar a pasta teste
			util.info(f"deletando pasta teste {test}.java")
			rmtree(test)
	#ou se for arquivo:
	elif os.path.isfile(java+".java"):
		#deletar o arquivo
		util.info(f"deletando arquivo {java}")
		os.remove(java+".java")
		#se tiver teste:
		if d1 and d2:
			#deletar o arquivo teste
			util.info(f"deletando arquivo teste {test}Test.java")
			os.remove(test+"Test.java")
	else:
		util.info(f"o diretorio ou arquivo {java} nao existe")
