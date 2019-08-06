#make changes to our configuration file
file { '/etc/ssh/ssh_config':
  ensure => present
}->
file_line { 'BatchMode yes':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'BatchMode yes',
  match  => '^BatchMode',
}->
file_line { 'IdentityFile':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
  match  => '^IdentityFile',
}
