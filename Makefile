
install:
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

activate:
	. .venv/bin/activate
