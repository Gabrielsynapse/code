import util
from sys import argv
from os import makedirs

###########variaveis#############
args       = argv
path       = args[1];
pwd        = args[2];
groupId    = args[3];
artifactId = args[4];
version    = args[5];
deplist    = args[6:]

srcPom  = pwd + "/pom.xml";
srcJava = pwd + "/src/main/java/" + groupId.replace(".","/");
srcTest = pwd + "/src/test/java/" + groupId.replace(".","/");

template_pom  = util.readFile(path+"/_code/template/newjar.xml");
pom = template_pom.replace("%groupId",groupId).replace("%artifactId",artifactId).replace("%version",version);
dependencies = "";

#################################

for c in deplist:
	dependencies += util.getDependency(c)
	util.info("inserindo dependencia {c} ao pom.xml");

pom = pom.replace("%dependencies",dependencies);

util.info(f"Escrendo arquivo pom.xml em {pwd}/pom.xml");
util.writeFile(srcPom,pom);

util.info("Montando diretorio dos arquivos Java em "+srcJava);
makedirs(srcJava);

#test
util.info("Motando diretorio de test em "+srcTest);
makedirs(srcTest);