from sys import argv
from os import makedirs
import util

###########variaveis#############
groupId       = str()
artifactId    = str()
version       = str()
template_pom  = str()
template_java = str()
path          = str()
pwd           = str()
srcPom        = str()
srcJava       = str()
#################################
args       = argv
path       = args[1];
pwd        = args[2];
groupId    = args[3];
artifactId = args[4];
version    = args[5];

srcPom  = pwd + "/pom.xml";
srcJava = pwd + "/src/main/java/" + groupId.replace(".","/");
template_pom  = util.readFile(path+"/_code/template/javaconsole.xml");
template_java = util.readFile(path+"/_code/template/javaconsole.java");

pom = template_pom.replace("%groupId",groupId).replace("%artifactId",artifactId).replace("%version",version);

mainJava = template_java.replace("%groupId",groupId).replace("%artifactId",artifactId).replace("%version",version);
dependencies = "";

for c in range(6,len(args)):
	item = args[c]
	dependencies += util.getDependency(item)
	util.info(f"inserindo dependencia {item} ao pom.xml")

pom = pom.replace("%dependencies",dependencies);

util.info(f"Escrendo arquivo pom.xml em {pwd}/pom.xml");
util.writeFile(srcPom,pom);

util.info("Montando diretorio dos arquivos Java em "+srcJava);
makedirs(srcJava);

util.info("Escrevendo arquivo Main em "+srcJava);
util.writeFile(srcJava+"/Main.java",mainJava);