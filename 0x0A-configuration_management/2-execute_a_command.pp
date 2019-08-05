# kills a process named killmenow
exec { 'pkill':
  command => '/usr/bin/pkill -f killmenow',
}
