# custom http header response NGiNX
exec {'run':
  command => '/usr/sbin/service nginx stop',
}
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
-> exec {'run2':
  command => '/usr/sbin/service nginx start',
  returns => [0,1,2]
}
