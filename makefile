# Define the command to install packages from requirements.txt
install:
	@echo "Installing packages from requirements.txt..."
	@pip install -r requirements.txt

# Define the command to uninstall installed packages
clean:
	@echo "Uninstalling installed packages..."
	@pip freeze | xargs pip uninstall -y

# Define the command to update installed packages
update:
	@echo "Updating installed packages..."
	@pip install -r requirements.txt --upgrade

# Define the command to check the list of installed packages
list:
	@echo "List of installed packages:"
	@pip list --format=columns