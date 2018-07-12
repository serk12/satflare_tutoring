FROM ubuntu:16.04
RUN apt-get update && apt-get -y install xvfb firefox python2.7 python-pip apache2 && pip install pyvirtualdisplay selenium pillow
COPY project/lib/geckodriver /usr/bin/
COPY project /var/www/
COPY project/000-default.conf /etc/apache2/sites-available/
EXPOSE 80
WORKDIR /var/www
CMD ./run.sh
