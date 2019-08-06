#make changes to our configuration file
file { '/etc/ssh/ssh_config':
  ensure => present
}->
file_line { 'pass no':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication yes',
}->
file_line { 'IdentityFile':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
  match  => '^IdentityFile',
}
