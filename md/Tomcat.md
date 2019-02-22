启动并配置Tomcat服务器
---


1）Tomcat服务器的配置文件位于F:\xampp\tomcat\conf\server.xml 
<Connector port="8080" protocol="HTTP/1.1" 
               connectionTimeout="20000" 
               redirectPort="8443" /> 

默认的端口为8080，只要修改端口就可以了。



2）在XAMPP控制面板中启动Tomcat服务器，直到服务器启动完成，在浏览器中输入：http://localhost:8080
--------------------- 
作者：头像是我爱豆 
来源：CSDN 
原文：https://blog.csdn.net/u014800380/article/details/52382518 
