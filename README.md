# PFS-Maddash_server
Easy maddash server config, optional modules and doc for PerfSONAR

## Easy doc : 

### - install Maddash on CentOS : 

yum update

yum install epel-release

yum install http://software.internet2.edu/rpms/el7/x86_64/main/RPMS/perfSONAR-repo-0.10-4.noarch.rpm

yum clean all

yum install perfsonar-centralmanagement

### - Configure firewall (Port 80 & 443)

firewall-cmd --permanent --add-port=80/tcp

firewall-cmd --permanent --add-port=443/tcp 

firewall-cmd --reload

