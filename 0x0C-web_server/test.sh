t=$(pgrep nginx | wc -l)
if [[ $t -eq 0 ]]
then
	echo 'starting'
	sudo service nginx start
else
	echo 'restarting'
	sudo service nginx restart
fi
