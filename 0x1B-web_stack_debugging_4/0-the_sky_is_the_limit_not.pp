# Increasing the limit of concurrent requests to our server
exec { 'ulimit-increase' :
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/bin', '/usr/local/bin','/bin/',],
  onlyif  => 'grep -q "15" /etc/default/nginx',
}

exec { 'restart-nginx' :
  command     => 'service nginx restart',
  path        => ['/usr/bin', '/usr/local/bin','/bin/', '/usr/sbin/'],
  subscribe   => Exec['ulimit-increase'],
  refreshonly => true,
}
