# Install Nginx web server
package { 'nginx':
	ensure => installed,
}->
file { '/var/www/html/index.nginx-debian.html':
	content => 'Holberton School',
}->
file_line { 'redirect':
	ensure => present,
	path   => '/etc/nginx/sites-enabled/default',
	line   => "listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/www.youtube.com\/;\\n\\t}",
	match  => '^listen 80 default_server;',
}
