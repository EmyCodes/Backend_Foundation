# Equivqlent resources

file { '/etc/inetd.conf':
	ensure => '/etc/inetd.conf',
}

file { '/etc/inetd/conf':
	ensure => link,
	target => '/etc/inetd.conf'
}
