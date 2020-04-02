# Anomaly detecting


### Apache access.log format  
Apache access log format can be changed from /etc/apache2/apache2.conf. Access.log format is at line 213 in apache2.conf file.
Change log format line to match --> **LogFormat "%{%d/%b/%Y/%T}t %h %>s %O %D %r" combined** . After changing Apache2 settings file restart Apache2 service.

```
%{%d/%b/%Y/%T}t	= Time stamp.
%h		= IP address.
%>s		= Status code.
%B		= Bytes sent.
%D		= Request time taken.
%r		= Method, first line of request and protocol.
```
Sample of 1 log file: 01/Apr/2020/22:47:49 10.10.10.10 200 238 460 GET / HTTP/1.1

## Follow the project blog:
[https://ailogs.design.blog/](https://ailogs.design.blog/)  


