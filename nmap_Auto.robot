*** Settings ***
Library           Process
Library           SeleniumLibrary
Library           BMScan.py
Library           VIScan.py
Library           CSDnmap.py
Library           Mcfxnmap.py
Library           datafile.py

*** Test Cases ***
Download nmap
    [Tags]    Download_nmap
    Open Browser    https://nmap.org/download.html    edge
    Maximize Browser Window
    Click Element    xpath://html/body/table[2]/tbody/tr[1]/td[2]/table/tbody/tr/td/p[16]//a[2]
    Sleep    20
    Close Browser

BMScan
    [Tags]    BMScan
    ${bm}=    Run Process    Python    BMScan.py
    log    ${bm}

VIScan
    [Tags]    VIScan
    ${vi}=    Run Process    Python    VIScan.py
    log    ${vi}

CSDScan
    [Tags]    CSDScan
    ${csd}=    Run Process    Python    CSDnmap.py
    log    ${csd}

MCFXScan
    [Tags]    MCFXScan
    ${mcfx}=    Run Process    Python    Mcfxnmap.py
    log    ${mcfx}
