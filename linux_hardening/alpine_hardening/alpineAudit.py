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

    compliance_check = "Ensure mounting of cramfs filesystems is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "iEnsure mounting of freevxfs filesystems is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure mounting of jffs2 filesystems is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure mounting of hfs filesystems is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure mounting of hfsplus filesystems is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure mounting of squashfs filesystems is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure mounting of udf filesystems is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure mounting of FAT filesystems is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure separate partition exists for /tmp (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure nodev option set on /tmp partition (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure nosuid option set on /tmp partition (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure noexec option set on /tmp partition (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure separate partition exists for /var (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure separate partition exists for /var/tmp (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure nodev option set on /var/tmp partition (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure nosuid option set on /var/tmp partition (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure noexec option set on /var/tmp partition (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure separate partition exists for /var/log (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure separate partition exists for /var/log/audit (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure separate partition exists for /home (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure nodev option set on /home partition (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure nodev option set on /dev/shm partition (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure nosuid option set on /dev/shm partition (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure noexec option set on /dev/shm partition (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure nodev option set on removable media partitions (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure nosuid option set on removable media partitions (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure noexec option set on removable media partitions (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure sticky bit is set on all world-writable directories (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Disable Automounting (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def config_swUpdates():
    global compliant_count

    compliance_check = "Ensure package manager repositories are configured (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure GPG keys are configured (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def fs_integrity_checking():
    global compliant_count

    compliance_check = "Ensure AIDE is installed (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure filesystem integrity is regularly checked (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def secBoot_settings():
    global compliant_count
    compliance_check = "Ensure permissions on bootloader config are configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure bootloader password is set (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure authentication required for single user mode (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure interactive boot is not enabled (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def process_hardening():
    global compliant_count

    compliance_check = "Ensure core dumps are restricted (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure XD/NX support is enabled (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure address space layout randomization (ASLR) is enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure prelink is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def mandatory_access_control():
    global compliant_count

    compliance_check = "Ensure SELinux is not disabled in bootloader configuration (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure the SELinux state is enforcing (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SELinux policy is configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SETroubleshoot is not installed (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure the MCS Translation Service (mcstrans) is not installed (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure no unconfined daemons exist (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure AppArmor is not disabled in bootloader configuration (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure all AppArmor Profiles are enforcing (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SELinux or AppArmor are installed (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def warning_banners():
    global compliant_count

    compliance_check = "Ensure message of the day is configured properly (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure local login warning banner is configured properly (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure remote login warning banner is configured properly (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure permissions on /etc/motd are configured (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure permissions on /etc/issue are configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure permissions on /etc/issue.net are configured (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure GDM login banner is configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure updates, patches, and additional security software are installed (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def inetd_services():
    global compliant_count

    compliance_check = "Ensure chargen services are not enabled (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure daytime services are not enabled (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure discard services are not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure echo services are not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure time services are not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure rsh services are not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Ensure talk server is not enabled (Scored)Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure telnet server is not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure tftp server is not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure xinetd is not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def special_purpose_services():
    global compliant_count

    compliance_check = "Ensure time synchronization is in use (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure ntp is configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure chrony is configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure X Window System is not installed (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure Avahi Server is not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure CUPS is not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure DHCP Server is not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure LDAP server is not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure NFS and RPC are not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure DNS Server is not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure FTP Server is not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure HTTP server is not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure IMAP and POP3 server is not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure Samba is not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure HTTP Proxy Server is not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SNMP Server is not enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Ensure mail transfer agent is configured for local-only mode (Scored)Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Ensure rsync service is not enabled (Scored)Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Ensure NIS Server is not enabled (Scored)Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def service_clients():
    global compliant_count

    compliance_check = "Ensure NIS Client is not installed (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure rsh client is not installed (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure talk client is not installed (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure telnet client is not installed (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure LDAP client is not installed (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def networkParam_hostRouter():
    global compliant_count

    compliance_check = "Ensure IP forwarding is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure packet redirect sending is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure source routed packets are not accepted (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure ICMP redirects are not accepted (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure secure ICMP redirects are not accepted (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure suspicious packets are logged (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure broadcast ICMP requests are ignored (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure bogus ICMP responses are ignored (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure Reverse Path Filtering is enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure TCP SYN Cookies is enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def ipv6():
    global compliant_count

    compliance_check = "Ensure IPv6 router advertisements are not accepted (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure IPv6 redirects are not accepted (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure IPv6 is disabled (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def tcp_wrappers():
    global compliant_count

    compliance_check = "Ensure TCP Wrappers is installed (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure /etc/hosts.allow is configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure /etc/hosts.deny is configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure permissions on /etc/hosts.allow are configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure permissions on /etc/hosts.deny are 644 (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def uncommon_nwProtocols():
    global compliant_count
    compliance_check = "Ensure DCCP is disabled (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SCTP is disabled (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure RDS is disabled (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure TIPC is disabled (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def firewall_configuration():
    global compliant_count

    compliance_check = "Ensure iptables is installed (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure default deny firewall policy (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure loopback traffic is configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure outbound and established connections are configured (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure firewall rules exist for all open ports (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure wireless interfaces are disabled (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def config_sysAccounting():
    global compliant_count

    compliance_check = "Configure System Accounting (auditd)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure audit log storage size is configured (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure system is disabled when audit logs are full (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure audit logs are not automatically deleted (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure auditd service is enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure auditing for processes that start prior to auditd is enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure events that modify date and time information are collected (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure events that modify user/group information are collected (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure events that modify the system's network environment are collected (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure events that modify the system's Mandatory Access Controls are collected (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure login and logout events are collected (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure session initiation information is collected (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure discretionary access control permission modification events are collected (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure unsuccessful unauthorized file access attempts are collected (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure use of privileged commands is collected (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure successful file system mounts are collected (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure file deletion events by users are collected (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure changes to system administration scope (sudoers) is collected(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure system administrator actions (sudolog) are collected (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure kernel module loading and unloading is collected (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure the audit configuration is immutable (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def config_logging():
    global compliant_count

    compliance_check = "Ensure rsyslog Service is enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure logging is configured (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure rsyslog default file permissions configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure rsyslog is configured to send logs to a remote log host (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure remote rsyslog messages are only accepted on designated log hosts. (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure syslog-ng service is enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure logging is configured (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure syslog-ng default file permissions configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure syslog-ng is configured to send logs to a remote log host (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure remote syslog-ng messages are only accepted on designated log hosts (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure rsyslog or syslog-ng is installed (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure permissions on all logfiles are configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure logrotate is configured (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
def config_cron():
    global compliant_count

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def config_SSH():
    global compliant_count

    compliance_check = "Ensure permissions on /etc/ssh/sshd_config are configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SSH Protocol is set to 2 (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SSH LogLevel is set to INFO (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SSH X11 forwarding is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SSH MaxAuthTries is set to 4 or less (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SSH IgnoreRhosts is enabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SSH HostbasedAuthentication is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SSH root login is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SSH PermitEmptyPasswords is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SSH PermitUserEnvironment is disabled (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure only approved ciphers are used (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure only approved MAC algorithms are used (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SSH Idle Timeout Interval is configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SSH LoginGraceTime is set to one minute or less (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SSH access is limited (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure SSH warning banner is configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def config_PAM():
    global compliant_count

    compliance_check = "Ensure password creation requirements are configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure lockout for failed password attempts is configured (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure password reuse is limited (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure password hashing algorithm is SHA-512 (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

def userAccounts_andEnvironment():
    global compliant_count

    compliance_check = "Ensure password expiration is 90 days or less (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure minimum days between password changes is 7 or more (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure password expiration warning days is 7 or more (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure inactive password lock is 30 days or less (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure system accounts are non-login (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure default group for the root account is GID 0 (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure default user umask is 027 or more restrictive (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure root login is restricted to system console (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure access to the su command is restricted (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
def sysFilePermissions():
    global compliant_count

    compliance_check = "Audit system file permissions (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure permissions on /etc/passwd are configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure permissions on /etc/shadow are configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure permissions on /etc/group are configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure permissions on /etc/gshadow are configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure permissions on /etc/passwd- are configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure permissions on /etc/shadow- are configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure permissions on /etc/group- are configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure permissions on /etc/gshadow- are configured (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no world writable files exist (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no unowned files or directories exist (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no ungrouped files or directories exist (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Audit SUID executables (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Audit SGID executables (Not Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
def userGroupSettings():
    global compliant_count

    compliance_check = "Ensure password fields are not empty (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure no legacy \"+\" entries exist in /etc/passwd (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure no legacy \"+\" entries exist in /etc/shadow (Scored)(Scored, Level 1))"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure no legacy \"+\" entries exist in /etc/group (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "(Ensure root is the only UID 0 account (Scored)Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure root PATH Integrity (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure all users' home directories exist (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure users' home directories permissions are 750 or more restrictive (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure users own their home directories (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure users' dot files are not group or world writable (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no users have .forward files (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no users have .netrc files (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure users' .netrc Files are not group or world accessible (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no users have .rhosts files (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure all groups in /etc/passwd exist in /etc/group (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no duplicate UIDs exist (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no duplicate GIDs exist (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no duplicate user names exist (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no duplicate group names exist (Scored)(Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure shadow group is empty (Scored)(Not Scored, Level 1)"
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
