# test replace

file {'./test.txt':
  ensure => present,
}
exec {'change something':
  path  => '.',
  match => "^there. *$",
}
