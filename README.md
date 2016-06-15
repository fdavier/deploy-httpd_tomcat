# deploytomcat

#JDK
jdk-8u91 (manual download or create direct link and install rpm -ivh)

#HTTPD
2.4.6 (yum install httpd + devel)

#LIBXML2-DEVEL
yum install libxml2-devel

#PHP7 (packaging)
<p>--> http://doc.fedora-fr.org/wiki/RPM_:_environnement_de_construction#Cr.C3.A9ation_de_l.27utilisateur</p>
<p>add a user for build env (ex: builder)</p>
<p>install rpmdevtools</p>
<p>rpmdev-setuptree to initialize rpmbuild env</p>

util:
<p>https://fedoraproject.org/wiki/Packaging:RPMMacros</p>
<p>http://doc.fedora-fr.org/wiki/La_cr%C3%A9ation_de_RPM_pour_les_nuls_:_Cr%C3%A9ation_du_fichier_SPEC_et_du_Paquetage</p>
<p>http://adam.younglogic.com/2010/05/found-buildroot-in-installed-files-aborting/</p>
<p>http://code.haskell.org/timber/timberc.spec</p>

#TOMCAT 8.0.36
<p>-set java home:</p>
export JAVA_HOME="/usr/java/jdk1.8.0_91"
<p>-set catalina home:</p>
export CATALINA_HOME="/opt/apache-tomcat-8.0.36"
<p>wget http://apache.websitebeheerjd.nl/tomcat/tomcat-8/v8.0.36/bin/apache-tomcat-8.0.36.tar.gz</p>
mv to /opt

#MOD_JK: Tomcat Connectors JK 1.2
wget http://wwwftp.ciril.fr/pub/apache/tomcat/tomcat-connectors/jk/tomcat-connectors-1.2.41-src.tar.gz
cd native
./configure --with-apxs=/usr/bin/apxs
  make
cd apache-2.0
cp mod_jk.so /usr/lib64/httpd/modules/

-add to httpd.conf:
LoadModule jk_module          /usr/lib64/httpd/modules/mod_jk.so
JkWorkersFile /etc/httpd/conf/workers.properties
JkShmFile     /var/log/httpd/mod_jk.shm
JkLogFile /var/log/httpd/mod_jk.log
JkLogLevel info
JkLogStampFormat "[%a %b %d %H:%M:%S %Y] "

-vi /etc/httpd/conf/workers.properties
worker.list=tomcat
worker.tomcat.type=ajp13
worker.tomcat.host=localhost
worker.tomcat.port=8009
worker.tomcat.socket_keepalive=1
worker.tomcat.cachesize=20

#Dans le virtual host correspondant à l’application, il faut rajouter:
JkMount /votreappli/* tomcat
