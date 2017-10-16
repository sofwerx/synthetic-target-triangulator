TMPDIR := $(shell mktemp -d)

requirements.txt: */*.py */*/*.py */*/*/*.py
	pip install virtualenv pipreqs
	pipreqs . --force
	virtualenv $(TMPDIR)/cybertick
	[ -n "$(TMPDIR)" -a -d $(TMPDIR) ]
	. $(TMPDIR)/cybertick/bin/activate \
		&& pip install -r $@ \
		&& pip freeze > $@ \
		&& deactivate \
		&& rm -fr $(TMPDIR)/cybertick \
		&& rmdir $(TMPDIR)

