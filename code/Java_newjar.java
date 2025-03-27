package code;

public class Java_newjar{
	private static String groupId;
	private static String artifactId;
	private static String version;
	private static String template_pom;
	private static String template_java;
	private static String path;
	private static String pwd;
	private static String srcPom;
	private static String srcJava;
	private static String srcTest;
	private static String src;

	private static void print(String str){
		System.out.println("[code] " + str);
	}
	private static String getDependency(String link){
		String[] list = link.split(":");
		String groupId    = list[0];
		String artifactId = list[1];
		String version    = list[2];
		String res = "";
		res +=
		"<dependency>\n" +
		"			<groupId>"+groupId+"</groupId>\n" +
		"			<artifactId>"+artifactId+"</artifactId>\n" +
		"			<version>"+version+"</version>\n" +
		"		</dependency>\n";
		return res;
	}
	public static void main(String[] args){
		pwd        = args[0];
		path       = args[1];
		groupId    = args[2];
		artifactId = args[3];
		version    = args[4];

		src = pwd + "/" + artifactId;
		srcPom = src + "/pom.xml";
		srcJava = src + "/src/main/java/" + groupId.replaceAll("\\.","/");
		srcTest = src + "/src/test/java/" + groupId.replaceAll("\\.","/");

		template_pom  = FileUtil.readFile(path+"/template/newjar.xml");

		String pom = template_pom.
			replaceAll("%groupId",groupId).
			replaceAll("%artifactId",artifactId).
			replaceAll("%version",version);
		String dependencies = "";

		FileUtil.makeDir(src);

		for(int c=5;c < args.length;c++){
			String item = args[c];
			dependencies += getDependency(item);

			print(String.format("inserindo dependencia %s ao pom.xml",item));
		}
		pom = pom.replaceAll("%dependencies",dependencies);

		print("Escrendo arquivo pom.xml em "+pwd+"/"+artifactId+"/pom.xml");
		FileUtil.writeFile(srcPom,pom);

		print("Montando diretorio dos arquivos Java em "+srcJava);
		FileUtil.makeDir(srcJava);

		//test
		print("Motando diretorio de test em "+srcTest);
		FileUtil.makeDir(srcTest);


	}
}