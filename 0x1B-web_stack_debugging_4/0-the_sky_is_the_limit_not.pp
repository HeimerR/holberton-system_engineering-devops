# fixes increase limit
exec { 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 5000\"/g" /etc/default/nginx':
  path => '/usr/bin:/usr/sbin:/bin',
}
-> exec {'restart service':
  command => '/usr/sbin/service nginx restart',
}
