#!/usr/bin/env bats


setup() {
:<<DOC
  Installs emoji package
DOC
  python setup.py install
}


teardown() {
:<<DOC
  Removes emoji package
DOC
  rm -rf ${PACKAGE_NAME}.egg-info dist build
}


@test "package name" {
:<<DOC
  Test package name
DOC
  pip list | grep ${PACKAGE_NAME}
  [ "$?" -eq 0 ]
}


@test "package version" {
:<<DOC
  Test package version
DOC
  pip list | grep ${PACKAGE_VERSION}
  [ "$?" -eq 0 ]
}


@test "package help message" {
:<<DOC
  Test package help message
DOC
  flake8 --help | grep "${PACKAGE_NAME}: ${PACKAGE_VERSION}"
  [ "$?" -eq 0 ]
}
