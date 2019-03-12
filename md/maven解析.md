https://www.cnblogs.com/ygj0930/p/6628201.html

Maven元素解析——pom.xml
---
一个pom.xml中包含了许多标签，各个标签是对项目生命周期、依赖管理的配置。常用的主要有：

    1：<peoject>：pom.xml的根标签，一个maven项目用一对<peoject></project>标签包裹。

    2：<modelVersion>:maven的版本

    3：当前项目的坐标以及打包方式：

        <groupId>：企业网址反写+项目名

        <artifactId>：项目名-模块名

        <version>：版本号+类型

                        版本号由三个整数表示，每个整数用“.”分隔，表示：大版本号.分支版本号.小版本号

                        类型：版本类型。主要有：snapshot快照版本(简化版本)、alpha内测版、beta公测版、release稳定版、GA正式发布版

        <packaging>：打包类型，默认是jar，可以配置成war、zip、pom类型。

    4：<name>：当前项目名

    5：<url>：项目地址

    6：<description>：项目描述信息

    7：<developers>：开发者信息

    8：<licenses>：项目许可证信息，用来发布时授予别人使用此项目的权利

    9：<organization>：组织信息，企业信息

    以上都是对这个maven项目的相关信息配置。

    10：<properties>：属性值标签，也叫变量标签。与Ant中的property一样，可以通过这个标签包含一些属性并指定属性值。那么在pom.xml的其他地方，可以通过EL表达式访问变量的方法——${属性名}  来获取具体的属性值。一般这个用来作为整个pom.xml中需要重复使用的内容或者全局变量使用。

    11：依赖标签

<dependencies>

    <!--一个依赖包-->
    <dependency>

       <!--通过坐标指定依赖包-->
        <groupId>        </groupId>
        <artifactId>      </artifactId>
        <version>        </version>

        <!--可选项：依赖范围。有六个可选值：常用compile/provided/test/runtime等-->
        <scope>一个范围</scope>
        <!--可选项：排除依赖传递：即：当前项目依赖当前配置的依赖包A时，如果这个依赖包又依赖其他包B，这里可以选择排除依赖的传递性，不下载导入B-->
         <exclusions>
            <exclusion>
              <!--被排除的依赖包坐标-->
              <groupId> </groupId>
              <artifactId> </artifactId>
              <version> </version>
            </exclusion>
         </exclusions>
    </dependency>
</dependencies>

 12：依赖管理标签：主要用于制定父pom.xml，其他项目可以继承这个pom.xml，从而避免重复定义某些depency。

 <depencyManagement>
    <depencies>
       <depency>
           依赖包的坐标...
       </depency>
    </depencies>
</depencyManagement>

 13：<build>：项目支持标签，一般用来引入插件

 <build>
    <plugins>
      <plugin>
         <!--插件坐标-->
         <groupId>         </groupId>
         <artifactId>         </artifactId>
         <version>         </version>

         其他设置...

      </plugin>
    </plugins>
</build>


14：<parent>：继承标签，用于继承父项目。

    15：<moudules>：聚合标签，用于聚合多个maven项目，这样用某指令执行这个pom就会把聚合的各项目全部执行，同时处理多个项目。

示例：一个简单的构建JavaWeb项目的pom.xml如下：

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.test</groupId>
  <artifactId>WebApp</artifactId>
  <packaging>war</packaging>
  <version>1.0</version>
  
  <name>WebApp Maven Webapp</name>
  <url>http://maven.apache.org</url>
  
  <dependencies>    
    <dependency>
      <groupId>commons-fileupload</groupId>
      <artifactId>commons-fileupload</artifactId>
      <version>1.2.1</version>
    </dependency>
    
    <!--commons-io为commons-fileupload的可选依赖包-->
    <dependency>
      <groupId>commons-io</groupId>
      <artifactId>commons-io</artifactId>
      <version>1.3.2</version>
    </dependency>
  </dependencies>
  
  <build>
    <finalName>WebApp</finalName>
  </build>
</project>



000000000000000000
https://blog.csdn.net/qq_33363618/article/details/79438044

Maven之pom.xml配置文件详解
---

https://blog.csdn.net/wangb_java/article/details/54170143

maven(四)：一个基本maven项目的pom.xml配置
---
继续之前创建的test项目，一个基本项目的pom.xml文件，通常至少有三个部分

第一部分,项目坐标，信息描述等
---


<modelVersion>4.0.0</modelVersion>
	<groupId>com.company.project</groupId>
	<artifactId>module</artifactId>
	<packaging>war</packaging>
	<version>0.0.1-SNAPSHOT</version>
	<name>test Maven Webapp</name>
	<url>http://maven.apache.org</url>

modelVersion：pom文件的模型版本

关于group id和artifact id，为了便于多人多模块协同开发管理（以后会讲），建议使用以下命名规范

group id：com.公司名.项目名

artifact id：功能模块名

packaging：项目打包的后缀，war是web项目发布用的，默认为jar

version:     artifact模块的版本

name和url：相当于项目描述，可删除

group id + artifact id +version :项目在仓库中的坐标

第二部分,引入jar包
---
<dependencies>
		<dependency>
			<groupId>junit</groupId>
			<artifactId>junit</artifactId>
			<version>3.8.1</version>
			<scope>test</scope>
		</dependency>
	</dependencies>
这是创建项目时自动生成的，将junit-3.8.1.jar引入到项目中。

dependency：引入资源jar包到本地仓库，要引入更多资源就在<dependencies>中继续增加<dependency>

group id+artifact id+version：资源jar包在仓库中的坐标

scope：作用范围，test指该jar包仅在maven测试时使用，发布时会忽略这个包。需要发布的jar包可以忽略这一配置

刚开始本地仓库是空的，maven会从远程仓库自动下载这个jar到本地仓库，下载完后，就可以在项目中使用这个jar了

第三部分,构建项目
---
<build>
		<finalName>helloworld</finalName>
		<plugins>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-compiler-plugin</artifactId>
				<version>3.5.1</version>
				<configuration>
					<source>1.7</source>
					<target>1.7</target>
				</configuration>
			</plugin>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-resources-plugin</artifactId>
				<version>3.0.1</version>
				<configuration>
					<encoding>UTF-8</encoding>
				</configuration>
			</plugin>
		</plugins>
	</build>

build：项目构建时的配置

finalName：在浏览器中的访问路径，如果将它改成helloworld，再执行maven--update，这时运行项目的访问路径是

                   http://localhost:8080/helloworld/   而不是项目名的  http://localhost:8080/test

plugins：插件，之前篇章已经说过，第一个插件是用来设置java版本为1.7，第二个插件是我刚加的，用来设置编码为utf-8

group id+artifact id+version：插件在仓库中的坐标

configuration：设置插件的参数值

https://blog.csdn.net/adeyi/article/details/17259479
pom.xml详解
---

https://www.cnblogs.com/wkrbky/p/6353285.html

pom.xml详解
---
