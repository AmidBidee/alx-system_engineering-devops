# this manifest creats a file in /tmp/school
file {'create tmp':
  'path'    => '/tmp/school',
  'mode'    => '0744',
  'owner'   => 'www-data',
  'group'   => 'www-data',
  'content' => 'I love puppet'
}
