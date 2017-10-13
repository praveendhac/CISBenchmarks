#!/usr/bin/python

import os, sys, time, re
import argparse
import subprocess

#Scored - Success/Failure to comply will incerease/decrease the final benchmark score
#Not Scored - Failure to comply will not decrease the final benchmark score. Compliance will not increase the score.
#Level 1 Server - general requirement
#Level 1 Workstation - general requirement
#Level 2 Server - required where security is paramount. Extends Level 1 profile
#Level 2 Workstation - required where security is paramount. Extends Level 1 profile

total_compliances = 0
compliant_count = 0

def update_compliance_status(compliance_check, compliance_status):
    global total_compliances
    total_compliances +=1
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CEND    = '\33[0m'

    if args.nocolor:
        print compliance_check + ": " + compliance_status
    else:
        if "NON-" in compliance_status:
            print compliance_check + ": " + CRED + compliance_status + CEND
        else:
            print compliance_check + ": " + CGREEN + compliance_status + CEND
    return

def exec_command(cmd):
    global total_compliances
    global compliant_count
    try:
        out = subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
    except:
        out = "EXCEPTION. Command execution failed or no output"
    return out

def verbose_logs(info_str, op):
    if args.verbose:
        print info_str +": "+ op
    return

def filesystem_config():
    global compliant_count

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def config_swUpdates():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def fs_integrity_checking():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def secBoot_settings():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def process_hardening():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def mandatory_access_control():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def warning_banners():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def inetd_services():
    global compliant_count

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def special_purpose_services():
    global compliant_count

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def service_clients():
    global compliant_count

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def networkParam_hostRouter():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def ipv6():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def tcp_wrappers():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def uncommon_nwProtocols():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def firewall_configuration():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def config_sysAccounting():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def config_logging():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
def config_cron():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def config_SSH():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def config_PAM():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def userAccounts_andEnvironment():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
def sysFilePermissions():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def userGroupSettings():
    global compliant_count
    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Scored, Level 1))"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

if __name__ == "__main__":
    global total_compliances
    global compliant_count

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",action="store_true")
    parser.add_argument("-n", "--nocolor", help="plain console output(default logging uses color)",action="store_true")
    args = parser.parse_args()

    print "Hardening Checks for Alpine Linux based on Centre for Internet Security Benchmarks"
    print "Benchmark Reference","CIS Distribution Independent Linux v1.0.1 - 01-31-2017"
    print "Author: Praveen Darshanam"

    verbose_logs("RECOMMENDATION SECTION","Initial Setup")
    filesystem_config()
    config_swUpdates()
    fsIntegrity_checking()
    secBoot_settings()
    process_hardening()
    mandatory_access_control()
    warning_banners()

    verbose_logs("RECOMMENDATION SECTION","Services")
    inetd_services()
    special_purpose_services()
    service_clients()
    
    verbose_logs("RECOMMENDATION SECTION","Network Configuration")
    networkParam_hostRouter()
    ipv6()
    tcp_wrappers()
    uncommon_nwProtocols()
    firewall_configuration()

    verbose_logs("RECOMMENDATION SECTION","Logging and Auditing")
    config_sysAccounting()
    config_logging()

    verbose_logs("RECOMMENDATION SECTION","Access, Authentication and Authorization")
    config_cron()
    config_SSH()
    config_PAM()
    userAccounts_andEnvironment()

    verbose_logs("RECOMMENDATION SECTION","System Maintenance")
    sysFilePermissions()
    userGroupSettings()


    """
    print "Checking File System Permissions and Access Controls"
    print "Checking Password Management"
    """
    verbose_logs("RECOMMENDATION SECTION","User Accounts and Environment")
    user_AccountsEnvironment()

    verbose_logs("RECOMMENDATION SECTION","Additional Considerations")
    additional_considerations()

    print "Total Compliances Checklist:", total_compliances
    print "Total Compliances Passed:", compliant_count
