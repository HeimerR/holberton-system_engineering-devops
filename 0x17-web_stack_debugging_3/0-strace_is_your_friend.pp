# fixes corrupted file with extension phpp
exec {'restart service':
  command => '/usr/bin/apt-get update',
}
-> file_line { 'replace line':
  path  => '/var/www/html/wp-settings.php',
  match => 'require_once\( ABSPATH \. WPINC \. \'/class-wp-locale\.phpp\' \);',
  line  => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );',
}
-> exec {'restart service':
  command => '/usr/sbin/service apache2 restart',
}
