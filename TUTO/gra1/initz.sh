#!/usr/bin/bash
# This bash srcript is for installing the KL docker image here
clear

# Colors
export RED='\033[0;31m'
export GREEN='\033[0;32m'
export YELLOW='\033[0;33m'
export BLUE='\033[0;34m'
export PURPLE='\033[0;35m'
export CYAN='\033[0;36m'
export WHITE='\033[0;37m'
export NC='\033[0m' # No Color

# Commands
b1() {
    echo -e "${CYAN}======================="
    echo -e " Gradio Testing Installs Here"
    echo -e "=======================${NC}"
}

c1() {
    # PKG Installs
    CO1="uv add rich asyncio gradio"
    CO2="uv tree"
    echo -e "${GREEN} PKG Install with uv Executing..."
    echo -e " $CO1 ${NC}"
    $CO1 && $CO2

}

# Execution
b1
c1
