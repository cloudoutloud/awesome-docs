# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make html".
html:
	rm -fr "$(BUILDDIR)/html"
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -w "$(BUILDDIR)/html.log"

# rm -rf "build/html"
# sphinx-build -M html "source" "build" -w "build/html.log"

# Build documentation and push to confluence (see conf.py for configuration details).
conf:
	@$(SPHINXBUILD) -b confluence "$(SOURCEDIR)" "$(BUILDDIR)/confluence" -E -a -v

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
