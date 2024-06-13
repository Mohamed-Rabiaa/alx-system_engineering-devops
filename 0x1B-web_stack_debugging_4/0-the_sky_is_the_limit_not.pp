# Increasing the limit of concurrent requests to our server
exec { 'ulimit-increase' :
     command     => 'sed -i "s/15/4096/" /etc/default/nginx',
     path    	 => ['/usr/bin', '/usr/sbin',],
     }

exec { 'restart-nginx' "
     command     => 'sudo service nginx restart',
     path        => ['/usr/bin', '/usr/sbin',],
}