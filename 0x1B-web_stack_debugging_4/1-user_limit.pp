# fixes increase limit
exec { 'sed -i "s/holberton hard nofile 5/holberton hard nofile 5000/" /etc/security/limits.conf':
  path => '/usr/bin:/usr/sbin:/bin',
}
exec { 'sed -i "s/holberton soft nofile 4/holberton soft nofile 4000/" /etc/security/limits.conf':
  path => '/usr/bin:/usr/sbin:/bin',
}
-> exec {'refresh conf':
  command => '/sbin/sysctl -p',
}
