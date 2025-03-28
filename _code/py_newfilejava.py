import util
from os import makedirs
from sys import argv

###########variaveis#############
args       = argv
path       = args[1];
pwd        = args[2];
filename_l = args[3:];
srcPom  = pwd + "/pom.xml";
groupId    = util.getTagPom(srcPom,"groupId")
artifactId = util.getTagPom(srcPom,"artifactId")

src_template_java = path + "/_code/template/newfilejava.java"
src_template_test = path + "/_code/template/newfilejavateste.java"
template_java = util.readFile(src_template_java)
template_test = util.readFile(src_template_test)

#################################

srcJava = pwd + "/src/main/java/" + (groupId).replace(".","/")
srcTest = pwd + "/src/test/java/" + (groupId).replace(".","/")

d1 = util.existDependency(srcPom,"org.junit.jupiter","junit-jupiter-api","5.10.2")
d2 = util.existDependency(srcPom,"org.junit.jupiter","junit-jupiter-engine","5.10.2")

for filename in filename_l:
	newsrc_java = f"{srcJava}/{filename}.java"
	newsrc_test = f"{srcTest}/{filename}Test.java"

	util.info(f"criando arquivo {filename}.java em {srcJava}")
	makedirs(srcJava,exist_ok=True)
	util.writeFile(newsrc_java,template_java.replace("%groupId",groupId).replace("%artifactId",filename))

	if d1 and d2:
		util.info(f"criando arquivo {filename}Test.java em {srcTest}")
		makedirs(srcTest,exist_ok=True)
		util.writeFile(newsrc_test,template_test.replace("%groupId",groupId).replace("%artifactId",filename))
