SRC=src/
DEFAULT=$(SRC)app.py
# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY: init run clean

init:
	poetry shell

run:
	@python $(DEFAULT)

clean:
	rm -rf $(SRC)__pycache__
	rm -rf .venv
