### Generic Variables
SHELL := /bin/zsh

.PHONY: help
help: ## Display help message (*: main entry points / []: part of an entry point)
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


################################################################################
# ATD-fabric
################################################################################

.PHONY: prepare
prepare: ## Build container topology in CVP to simulate a ZTP environment
	ansible-playbook playbooks/atd-prepare-lab.yml

.PHONY: fabric-build
fabric-build: ## Build DC fabric artifacts
	ansible-playbook playbooks/dc-fabric-build.yml -i dc-fabrics/inventory.yml

.PHONY: fabric-deploy
fabric-deploy: ## Push DC configurations to CVP and create tasks (user must execute)
	ansible-playbook playbooks/dc-fabric-deploy.yml -i dc-fabrics/inventory.yml

.PHONY: fabric-validate
fabric-validate: ## Validate the fabric from the EOS nodes using eAPI
	ansible-playbook playbooks/dc-fabric-validate.yml -i dc-fabrics/inventory.yml

.PHONY: core-build
core-build: ## Build core artifacts
	ansible-playbook playbooks/core-build.yml -i core-fabric/inventory.yml

.PHONY: core-deploy
core-deploy: ## Push core configurations to CVP and create tasks (user must execute)
	ansible-playbook playbooks/core-deploy.yml -i core-fabric/inventory.yml

.PHONY: core-validate
core-validate: ## Validate the core from the EOS nodes using eAPI
	ansible-playbook playbooks/core-validate.yml -i core-fabric/inventory.yml