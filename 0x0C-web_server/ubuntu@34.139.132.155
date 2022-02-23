t=$(pgrep nginx | wc -l)
if [[ $t -le 0 ]]
then
	echo 'starting'
	sudo service nginx start
else
	echo 'restarting'
	sudo service nginx restart
fi
