
if [ -z "$pkg" ] || [ -z "$name" ] || [ -z "$v" ]; then
	ms_error "nao pode deixar vazio!"
	ms_usage
	exit
fi
