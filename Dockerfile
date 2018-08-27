FROM python:2-alpine

COPY requirements.txt /tmp/requirements.txt
RUN mkdir /tmp/results/
RUN pip install -r /tmp/requirements.txt
COPY . /usr/src/app/project-automation/
RUN chmod -R 664 /usr/src/app/project-automation/
WORKDIR /usr/src/app/project-automation/
CMD ["nosetests", "-v", "--with-xunit", "--xunit-file=/tmp/results/results.xml"]