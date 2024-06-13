# Changing the OS configuration so that it is possible to login with
# the holberton user and open a file without any error message
exec { 'hard_limit_change' :
  command => "sed -i '/^holberton hard/s/5/10000/' /etc/security/limits.conf",
  path    => ['/usr/local/bin', '/bin/',],
}

exec { 'soft_limit_change' :
  command => "sed -i '/^holberton soft/s/4/10000/' /etc/security/limits.conf",
  path    => ['/usr/local/bin', '/bin/',],
}
