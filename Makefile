.PHONY: clean system-packages python-packages install tests run all

clean:
   find . -type f -name '*.pyc' -delete
   find . -type f -name '*.log' -delete

system-packages:
   sudo apt install python-pip -y

python-packages:
   pip install -r requirements-dev.txt

install: system-packages python-packages

tests:
   py.test
run:
   py.test
all: clean install tests run