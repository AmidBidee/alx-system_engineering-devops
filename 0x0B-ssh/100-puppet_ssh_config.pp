# edits ssh_config file

exec {'ss config':
  command => "/bin/sed -i 's/IdentityFile.*/IdentityFile ~\/.ssh\/school/gI 2-ssh_config",
}

exec {'ssh_config':
  command => ['/bin/sed -i', 's/PasswordAuthentication.*/PasswordAuthentication no/gI', '2-ssh_config'],
}
