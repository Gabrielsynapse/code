package code;

public class Java_newjavaconsole{
	private static String groupId;
	private static String artifactId;
	private static String version;
	private static String template;
	private static String path;
	private static String pwd;

	private static void print(String str){
		System.out.println("[code] " + str);
	}
	public static void main(String[] args){
		pwd        = args[0];
		path       = args[1];
		groupId    = args[2];
		artifactId = args[3];
		version    = args[4];

		template = FileUtil.readFile(path+"/template/javaconsole.xml");

		String pom = template.
			replaceAll("%groupId",groupId).
			replaceAll("%artifactId",artifactId).
			replaceAll("%version",version);

		print("montando diretorio "+artifactId+" em "+pwd);

		FileUtil.makeDir(pwd+"/"+artifactId);

		//System.out.println(pom);
	}
}