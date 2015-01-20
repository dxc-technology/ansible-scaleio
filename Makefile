YML := $(wildcard **/*.yml)

all:
	ansible-playbook -i hosts site.yml

debug:
	ansible-playbook -vvvv -i hosts site.yml

check:
	ansible-playbook -i hosts --syntax-check site.yml	

.PHONY: test

test: $(YML)

$(YML): %.yml
	ansible-playbook -i hosts --syntax-check $<
