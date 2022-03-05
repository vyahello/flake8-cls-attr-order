#!/usr/bin/env bash

# specifies a set of variables to declare files to be used for code assessment
PACKAGE="flake8_cls_attr_order"

# specifies a set of variables to declare CLI output color
FAILED_OUT="\033[0;31m"
PASSED_OUT="\033[0;32m"
NONE_OUT="\033[0m"


pretty-printer-box() {
:<<DOC
    Provides pretty-printer check box
DOC
    echo "Start ${1} analysis ..."
}


check-black() {
:<<DOC
    Runs "black" code analyser
DOC
    pretty-printer-box "black" && ( black --check ${PACKAGE} )
}


check-flake() {
:<<DOC
    Runs "flake8" code analysers
DOC
    pretty-printer-box "flake" && ( flake8 ${PACKAGE} )
}

check-isort() {
:<<DOC
    Runs "isort" code analysers
DOC
    pretty-printer-box "isort" && ( isort ${PACKAGE} --check-only --verbose)
}


check-tests() {
:<<DOC
    Runs "unit tests"
DOC
    pretty-printer-box "unit tests" && pytest
}


main() {
:<<DOC
    Runs "main" code analyser
DOC
    check-black && check-flake && check-isort && check-tests
}

main