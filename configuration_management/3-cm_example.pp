define resolve($nameserver1, $nameserver2, $domain, $search) {
	$str = "search ${search}
		domain ${domain}
		nameserver ${nameserver1}
		nameserver ${nameserver2}
		"
	file {'/etc/resolv.conf':
		content => $str,
	}
}
