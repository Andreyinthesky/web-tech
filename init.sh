sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/nginx.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/etc/ask.py   /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
