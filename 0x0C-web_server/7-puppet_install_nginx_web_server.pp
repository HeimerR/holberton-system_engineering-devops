# Install Nginx web server
package { 'nginx':
  ensure => 'present',
}->
file { 'index.html':
  ensure  => 'present',
  content => 'Holberton School',
  path    => '/var/www/html/index.html',
}->
file_line { 'redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  line   => "listen 80 default_server;\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/;\n\t}",
  match  => '^listen 80 default_server;',
}
