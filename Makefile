init: lxc-deploy provision

lxc-deploy:
	sudo cdeploy

provision:
	./scripts/provision.sh lxc -vvvv

.PHONY: init lxc-deploy provision
