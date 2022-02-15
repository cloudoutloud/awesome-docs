# This Dockerfile is for the building of documentation using Sphinx
# without the need to install the prerequisties directly on a
# developer laptop.

FROM ubuntu:16.04

RUN apt-get update -y \
    && apt-get install -y software-properties-common \
                          curl \
                          make \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update -y \
    && apt-get install -y python3.8 \
    && curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" \
    && python3 get-pip.py \
    && pip install sphinx \
    && pip install sphinx-autobuild \
    && pip install sphinx-rtd-theme \
    && pip install sphinxcontrib-httpdomain \
    && pip install sphinxcontrib-confluencebuilder \
    && pip install sphinx-jsonschema \
    && pip install pyquickhelper \
    && pip install sphinxcontrib.imagesvg \
    && pip install autopep8

WORKDIR /awesome-docs