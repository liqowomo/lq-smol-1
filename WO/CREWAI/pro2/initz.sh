#!/usr/bin/bash
# This bash srcript is for installing necessary pkgs
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
    echo -e "${CYAN}==================================="
    echo -e "UV Commands for insalling necessary pkgs"
    echo -e "================================================= ${NC}"
}

c1() {
    echo -e "${CYAN} Installing necessary packages${NC}"
    CO1="uv add crewai crewai-tools agentops"
    CO2="uv tree"
    echo -e "${GREEN} $CO1 ${NC}"
    $CO1
    $CO2
}

c2() {
    echo -e "${CYAN} Crew AI Setup and Commands ${NC}"
    CO1="uv run crewai create crew pu1 "
    echo -e "${GREEN} $CO1 ${NC}"
    $CO1
}

c3() {
    # Create flow ehre
    echo -e "${CYAN} Creating Flow, Executing... ${NC}"
    CO1="uv run crewai create flow mimu "
    echo -e "${GREEN}$CO1 ${NC}"
    $CO1
}

# Execution
c3
