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

    compliance_check = "Ensure mounting of cramfs filesystems is disabled (Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v cramfs"
    is_cramfs_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep cramfs"
    is_cramfs_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_cramfs_mp_present)
    verbose_logs("Command Output", is_cramfs_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install cramfs /bin/true\"")
    if "cramfs.ko" in is_cramfs_mp_present:
        if "EXCEPTION" in is_cramfs_lm_present:
            update_compliance_status(compliance_check, "COMPLIANT")
            compliant_count += 1
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            compliant_count -= 1
    else:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1

    compliance_check = "Ensure mounting of freevxfs filesystems is disabled (Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v freevxfs"
    is_freevxfs_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep freevxfs"
    is_freevxfs_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_freevxfs_mp_present)
    verbose_logs("Command Output", is_freevxfs_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install freevxfs /bin/true\"")
    if "freevxfs.ko" in is_freevxfs_mp_present:
        if "EXCEPTION" in is_freevxfs_lm_present:
            update_compliance_status(compliance_check, "COMPLIANT")
            compliant_count += 1
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            compliant_count -= 1
    else:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1

    compliance_check = "Ensure mounting of jffs2 filesystems is disabled (Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v jffs2"
    is_jffs2_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep jffs2"
    is_jffs2_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_jffs2_mp_present)
    verbose_logs("Command Output", is_jffs2_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install jffs2 /bin/true\"")
    if "jffs2.ko" in is_jffs2_mp_present:
        if "EXCEPTION" in is_jffs2_lm_present:
            update_compliance_status(compliance_check, "COMPLIANT")
            compliant_count += 1
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            compliant_count -= 1
    else:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1

    compliance_check = "Ensure mounting of hfs filesystems is disabled (Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v hfs"
    is_hfs_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep hfs"
    is_hfs_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_hfs_mp_present)
    verbose_logs("Command Output", is_hfs_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install hfs /bin/true\"")
    if "hfs.ko" in is_hfs_mp_present:
        if "EXCEPTION" in is_hfs_lm_present:
            update_compliance_status(compliance_check, "COMPLIANT")
            compliant_count += 1
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            compliant_count -= 1
    else:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1

    compliance_check = "Ensure mounting of hfsplus filesystems is disabled (Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v hfsplus"
    is_hfsplus_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep freevxfs"
    is_hfsplus_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_hfsplus_mp_present)
    verbose_logs("Command Output", is_hfsplus_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install hfsplus /bin/true\"")
    if "hfsplus.ko" in is_hfsplus_mp_present:
        if "EXCEPTION" in is_hfsplus_lm_present:
            update_compliance_status(compliance_check, "COMPLIANT")
            compliant_count += 1
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            compliant_count -= 1
    else:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1

    compliance_check = "Ensure mounting of squashfs filesystems is disabled (Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v squashfs"
    is_squashfs_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep squashfs"
    is_squashfs_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_squashfs_mp_present)
    verbose_logs("Command Output", is_squashfs_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install squashfs /bin/true\"")
    if "squashfs.ko" in is_squashfs_mp_present:
        if "EXCEPTION" in is_squashfs_lm_present:
            update_compliance_status(compliance_check, "COMPLIANT")
            compliant_count += 1
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            compliant_count -= 1
    else:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1

    compliance_check = "Ensure mounting of udf filesystems is disabled (Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v udf"
    is_udf_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep udf"
    is_udf_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_udf_mp_present)
    verbose_logs("Command Output", is_udf_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install udf /bin/true\"")
    if "udf.ko" in is_udf_mp_present:
        if "EXCEPTION" in is_udf_lm_present:
            update_compliance_status(compliance_check, "COMPLIANT")
            compliant_count += 1
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            compliant_count -= 1
    else:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1

    compliance_check = "Ensure mounting of FAT filesystems is disabled (Scored, Level 1 Server Level 2 Workstation)"
    cmd1 = "modprobe -n -v vfat"
    is_vfat_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep vfat"
    is_vfat_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_vfat_mp_present)
    verbose_logs("Command Output", is_vfat_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install vfat /bin/true\"")
    if "vfat.ko" in is_vfat_mp_present:
        if "EXCEPTION" in is_vfat_lm_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")

    compliance_check = "Ensure separate partition exists for /tmp (Scored, Level 2 Server and Workstation)"
    cmd = "mount | grep /tmp"
    is_tmpfs_partition_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tmpfs_partition_present)
    tmpfs_present = 0
    verbose_logs("Expected output to be compliant","similar to \"tmpfs on /tmp type tmpfs (rw,nosuid,nodev,noexec,relatime)\"")
    verbose_logs("To be compliant","For new systems create separate partition for /tmp. For previously installed systems, create a new partition and configure /etc/fstab as appropriate.")
    if "/tmp " in is_tmpfs_partition_present:
        tmpfs_present = 1
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nodev option set on /tmp partition (Scored)(Not Scored, Level 1)"
    verbose_logs("INFO", "nodev mount option specifies that the filesystem cannot contain special devices")
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tmpfs_partition_present)
    verbose_logs("Expected output to be compliant","verify that the nodev option is set on /tmp")
    verbose_logs("To be compliant, run","mount -o remount,nodev /tmp")
    if tmpfs_present:
        if "nodev" in is_tmpfs_partition_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nosuid option set on /tmp partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("INFO", "nosuid mount option specifies that the filesystem cannot contain setuid files")
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tmpfs_partition_present)
    verbose_logs("Expected output to be compliant","Verify that the nosuid option is set on /tmp")
    verbose_logs("To be compliant, run","mount -o remount,nosuid /tmp")
    if tmpfs_present:
        if "nosuid" in is_tmpfs_partition_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure noexec option set on /tmp partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("INFO", "noexec mount option specifies that the filesystem cannot contain executable binaries")
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tmpfs_partition_present)
    verbose_logs("Expected output to be compliant","Verify that the noexec option is set on /tmp")
    verbose_logs("To be compliant, run","mount -o remount,noexec /tmp")
    if tmpfs_present:
        if "noexec" in is_tmpfs_partition_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure separate partition exists for /var (Scored, Level 2 Server and Workstation)"
    cmd = "mount | grep /var"
    is_var_partition_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_var_partition_present)
    verbose_logs("Expected output to be compliant","similar to \"/dev/xvdg1 on /var type ext4 (rw,relatime,data=ordered)\"")
    verbose_logs("To be compliant","For new systems create separate partition for /var. For previously installed systems, create a new partition and configure /etc/fstab as appropriate.")
    if "/var " in is_var_partition_present:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure separate partition exists for /var/tmp (Scored, Level 2 Server and Workstation)"
    cmd = "mount | grep /var/tmp"
    is_vartmp_partition_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_vartmp_partition_present)
    vartmp_present = 0
    verbose_logs("Expected output to be compliant","similar to \"tmpfs on /var/tmp type ext4 (rw,nosuid,nodev,noexec,relatime)\"")
    verbose_logs("To be compliant","For new systems create separate partition for /var/tmp. For previously installed systems, create a new partition and configure /etc/fstab as appropriate.")
    if "/var/tmp " in is_vartmp_partition_present:
        vartmp_present = 1
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nodev option set on /var/tmp partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("INFO", "nodev mount option specifies that the filesystem cannot contain special devices")
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tmpfs_partition_present)
    verbose_logs("Expected output to be compliant","verify that the nodev option is set on /var/tmp")
    verbose_logs("To be compliant, run","mount -o remount,nodev /var/tmp")
    if vartmp_present:
        if "nodev" in is_vartmp_partition_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nosuid option set on /var/tmp partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("INFO", "nosuid mount option specifies that the filesystem cannot contain setuid files")
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_vartmp_partition_present)
    verbose_logs("Expected output to be compliant","Verify that the nosuid option is set on /var/tmp")
    verbose_logs("To be compliant, run","mount -o remount,nosuid /var/tmp")
    if vartmp_present:
        if "nosuid" in is_vartmp_partition_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure noexec option set on /var/tmp partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("INFO", "nosuid mount option specifies that the filesystem cannot contain setuid files")
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tmpfs_partition_present)
    verbose_logs("Expected output to be compliant","Verify that the nosuid option is set on /var/tmp")
    verbose_logs("To be compliant, run","mount -o remount,nosuid /var/tmp")
    if vartmp_present:
        if "nosuid" in is_vartmp_partition_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure separate partition exists for /var/log (Scored, Level 2 Server and Workstation)"
    cmd = "mount | grep /var/log"
    is_varlog_partition_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_varlog_partition_present)
    verbose_logs("Expected output to be compliant","similar to \"/dev/xvdh1 on /var/log type ext4 (rw,relatime,data=ordered)\"")
    verbose_logs("To be compliant","For new systems create separate partition for /var/log. For previously installed systems, create a new partition and configure /etc/fstab as appropriate.")
    if "/var/log " in is_varlog_partition_present:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure separate partition exists for /var/log/audit (Scored)(Not Scored, Level 2 Server and Workstation)"
    cmd = "mount | grep /var/log/audit"
    is_varlogaudit_partition_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_varlogaudit_partition_present)
    verbose_logs("Expected output to be compliant","similar to \"/dev/xvdi1 on /var/log/audit type ext4 (rw,relatime,data=ordered)\"")
    verbose_logs("To be compliant","For new systems create separate partition for /var/log/audit. For previously installed systems, create a new partition and configure /etc/fstab as appropriate.")
    if "/var/log/audit " in is_varlogaudit_partition_present:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure separate partition exists for /home (Scored, Level 2 Server and Workstation)"
    cmd = "mount | grep /home"
    is_home_partition_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_home_partition_present)
    home_present = 0
    verbose_logs("Expected output to be compliant","similar to \"/dev/xvdf1 on /home type ext4 (rw,nodev,relatime,data=ordered)\"")
    verbose_logs("To be compliant","For new systems create separate partition for /home. For previously installed systems, create a new partition and configure /etc/fstab as appropriate.")
    if "/home " in is_home_partition_present:
        home_present = 1
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nodev option set on /home partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_home_partition_present)
    verbose_logs("Expected output to be compliant","nodev option set on /home. Set this option to ensure users cannot attempt to create block or character special devices")
    verbose_logs("To be compliant, run","mount -o remount,nodev /home")
    if home_present:
        if "nodev" in is_home_partition_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nodev option set on /dev/shm partition (Scored, Level 1 Server and Workstation)"
    cmd = "mount | grep /dev/shm"
    is_devshm_partition_present = exec_command(cmd)
    verbose_logs("INFO","/dev/shm filesystem is not intended to support devices, prevent users creating special devices")
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_devshm_partition_present)
    devshm_present = 0
    verbose_logs("Expected output to be compliant","nodev option set on /home. Set this option to ensure users cannot attempt to create block or character special devices")
    verbose_logs("To be compliant, run","mount -o remount,nodev /dev/shm")
    if "/dev/shm " in is_devshm_partition_present:
        devshm_present = 1

    if devshm_present:
        if ("nodev" in is_devshm_partition_present):
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nosuid option set on /dev/shm partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_devshm_partition_present)
    verbose_logs("Expected output to be compliant","nosuid option set on /home. Set this option to ensure filesystem cannot contain setuid files, not-setting this option allows non-root users to execute privileged programs")
    verbose_logs("To be compliant, run","mount -o remount,nosuid /dev/shm")
    if devshm_present:
        if ("nosuid" in is_devshm_partition_present):
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure noexec option set on /dev/shm partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_devshm_partition_present)
    verbose_logs("Expected output to be compliant","noexec option is set on /dev/shm")
    verbose_logs("To be compliant, run","mount -o remount,noexec /dev/shm")
    if devshm_present:
        if ("noexec" in is_devshm_partition_present):
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nodev option set on removable media partitions (Scored, Level 1 Server and Workstation)"
    cmd = "mount |grep -i /dev"
    is_removablemedia_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_removablemedia_present)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure nosuid option set on removable media partitions (Scored, Level 1 Server and Workstation)"
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_removablemedia_present)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure noexec option set on removable media partitions (Scored, Level 1 Server and Workstation)"
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_removablemedia_present)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    #TODO Removable media ^^. blkid cmd might be useful

    compliance_check = "Ensure sticky bit is set on all world-writable directories (Scored, Level 1 Server and Workstation)"
    cmd = "df -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type d \\( -perm -0002 -a ! -perm -1000 \\)"
    is_sb_wwf = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sb_wwf)
    verbose_logs("Expected output to be compliant","No output should be returned")
    verbose_logs("To be compliant, run","df -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type d -perm -0002 2>/dev/null | chmod a+t")
    if "EXCEPTION" in is_sb_wwf or len(is_sb_wwf) <1:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Disable Automounting (Scored)(Not Scored, Level 1)"
    #command similar to "chkconfig --list autofs" on alpine
    cmd = "rc-status -a | grep -i autofs"
    proc_status_rlevels = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", proc_status_rlevels)
    verbose_logs("Expected output to be compliant","autofs is not available")
    verbose_logs("To be compliant, run","rc-service autofs stop")
    if "EXCEPTION" in proc_status_rlevels or len(proc_status_rlevels) <1:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def config_swUpdates():
    global compliant_count

    compliance_check = "Ensure package manager repositories are configured (Not Scored, Level 1 Server and Workstation)"
    cmd = "apk policy"
    is_apk_policy_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_apk_policy_present)
    verbose_logs("Expected output to be compliant","Verify package repositories are configured correctly")
    verbose_logs("To be compliant","Configure your package manager repositories according to site policy.")
    if "EXCEPTION" in is_apk_policy_present:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        

    compliance_check = "Ensure GPG keys are configured (Not Scored, Level 1 Server and Workstation)"
    cmd = "TODO: DID NOT FIND SPECIFIC COMMAND"
    #repo_gpgkeys_config = exec_command(cmd)
    verbose_logs("Command used", cmd)
    #verbose_logs("Command Output", repo_gpgkeys_config)
    verbose_logs("Expected output to be compliant","Verify GPG keys are configured correctly for your package manager")
    verbose_logs("To be compliant, run","")
    """
    if "EXCEPTION" in is_apk_policy_present:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    """

def fs_integrity_checking():
    global compliant_count

    compliance_check = "Ensure AIDE is installed (Scored, Level 1 Server and Workstation)"
    #AIDE not present on Alpine release 3.6.2. inotifyd is inbuild FIM
    cmd = "ps | grep -i inotifyd"
    is_inotifyd_running = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_inotifyd_running)
    verbose_logs("Expected output to be compliant","inotifyd or similar FIM tools must be running")
    verbose_logs("To be compliant, run","inotifyd on sensitive files")
    inotifyd_proc = is_inotifyd_running.split('\n')
    if len(inotifyd_proc) >=2:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure filesystem integrity is regularly checked (Scored, Level 1 Server and Workstation)"
    cmd = "crontab -u root -l | grep inotifyd"
    is_fim_cron_present = exec_command(cmd)
    #also run, "grep -r aide /etc/cron.* /etc/crontab"
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_fim_cron_present)
    verbose_logs("Expected output to be compliant","inotifyd or similar FIM tools configured as cron job")
    verbose_logs("To be compliant, run","\"crontab -u root -e\" and add \"0 5 * * * /usr/sbin/aide --check\" to crontab")
    if "inotifyd" in is_fim_cron_present:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def sec_boot_settings():
    global compliant_count
    compliance_check = "Ensure permissions on bootloader config are configured (Scored, Level 1 Server and Workstation)"
    cmd = "stat /boot/grub/menu.lst"
    bootloader_perm = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", bootloader_perm)
    # Access: (0600/-rw-------) Uid: ( 0/ root) Gid: ( 0/ root)
    verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access does not grant permissions to group or other")
    verbose_logs("To be compliant, run","\"chown root:root /boot/grub/menu.lst\",\"chmod og-rwx /boot/grub/menu.lst\"")
    check_stat_match = re.match(r'.*?Access:\s*\(\d{4}....------\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\)',bootloader_perm, re.I|re.M|re.S)
    if check_stat_match:
        print "check_stat_match.groups():", check_stat_match.groups()
        print "check_stat_match.group(1):", check_stat_match.group(1)
        print "check_stat_match.groups(2):", check_stat_match.group(2)
    #TODO

    compliance_check = "Ensure bootloader password is set (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^password\" /boot/grub/menu.lst"
    bootloader_password = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", bootloader_password)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","generate <encrypted-password> for grub/grub2 using command grub-md5-crypt/grub-mkpasswd-pbkdf2, paste it into the global section of /boot/grub/menu.lst as \"password --md5 <encrypted-password>\" and \"set superusers=\"<username>\"\" and \"password_pbkdf2 <username> <encrypted-password>\" for grub2 then run update-grub command")
    if "password" in bootloader_password:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure authentication required for single user mode (Not Scored, Level 1 Server and Workstation)"
    cmd = "grep \"/sbin/sulogin\" /etc/inittab"
    auth_sum = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", auth_sum)
    verbose_logs("Expected output to be compliant","similar to \"~~:S:respawn:/sbin/sulogin\"")
    verbose_logs("To be compliant, run","configure single user mode to require a password for login as appropriate")
    if ":S:respawn:/sbin/sulogin" in auth_sum:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure interactive boot is not enabled (Not Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^PROMPT_FOR_CONFIRM=\" /etc/sysconfig/boot"
    is_iboot_enabled = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_iboot_enabled)
    verbose_logs("Expected output to be compliant","PROMPT_FOR_CONFIRM=\"no\"")
    verbose_logs("To be compliant, check","if interactive boot is available disable it.")
    iboot_no = re.match(r'^PROMPT_FOR_CONFIRM="(.*?)".*?',is_iboot_enabled, re.I|re.M)
    if iboot_no:
        if "no" in iboot_no.group(1):
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def process_hardening():
    global compliant_count

    compliance_check = "Ensure core dumps are restricted (Scored, Level 1 Server and Workstation)"
    cmd1 = "grep -r \"hard core\" /etc/security/limits.conf /etc/security/limits.d/"
    #cmd1 = "grep \"hard core\" /etc/security/limits.conf"
    is_limits_set = exec_command(cmd1)
    verbose_logs("Command used", cmd1)
    verbose_logs("Command Output", is_limits_set)
    verbose_logs("Expected output to be compliant","* hard core 0")
    verbose_logs("To be compliant, run","Edit /etc/security/limits.conf file or a /etc/security/limits.d/* file by adding \"* hard core 0\"")
    hard_core_0 = re.match(r'.*?\*\s+hard\s+core\s+0.*?',is_limits_set,re.I|re.M)

    cmd2 = "sysctl fs.suid_dumpable"
    sysctl_suiddump = exec_command(cmd2)
    verbose_logs("Command used", cmd2)
    verbose_logs("Command Output", sysctl_suiddump)
    verbose_logs("Expected output to be compliant","fs.suid_dumpable = 0")
    verbose_logs("To be compliant, run","Set \"fs.suid_dumpable = 0\" in /etc/sysctl.conf. Run \"sysctl -w fs.suid-dumpable=1\"to set the active kernel parameter")
    is_suid_dumpable = re.match(r'fs\.suid_dumpable\s*=\s*0',sysctl_suiddump,re.I|re.M)
    if hard_core_0 and is_suid_dumpable:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure XD/NX support is enabled (Not Scored, Level 1 Server and Workstation)"
    cmd = "dmesg | grep NX"
    is_NX_active = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_NX_active)
    verbose_logs("Expected output to be compliant","NX (Execute Disable) protection: active")
    verbose_logs("To be compliant, run","enable NX or XD support in your bios")
    if ("NX " in is_NX_active) and (" active" in is_NX_active):
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure address space layout randomization (ASLR) is enabled (Scored, Level 1 Server and Workstation)"
    cmd = "sysctl kernel.randomize_va_space"
    is_aslr_set = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_aslr_set)
    verbose_logs("Expected output to be compliant","kernel.randomize_va_space = 2")
    verbose_logs("To be compliant, run","\"sysctl -w kernel.randomize_va_space=2\" or edit /etc/sysctl.conf and add kernel.randomize_va_space = 2")
    if ("kernel.randomize_va_space" in is_aslr_set) and (" 2" in is_aslr_set):
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure prelink is disabled (Scored, Level 1 Server and Workstation)"
    cmd = "apk info prelink"
    is_prelink_disabled = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_prelink_disabled)
    verbose_logs("Expected output to be compliant","Verify prelink is not installed")
    verbose_logs("To be compliant, run","apk del prelink")
    if "prelink-" in is_prelink_disabled:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")

def mandatory_access_control():
    global compliant_count

    compliance_check = "Ensure SELinux is not disabled in bootloader configuration (Scored, Level 2 Server and Workstation)"
    #check /boot/grub/menu.lst, /boot/grub/grub.cfg
    #bootloader information, file -s /dev/sda
    #SELinux may be disabled by changing 'selinux=1' to 'selinux=0'
    #'enforcing=0' (which means permissive where denied actions are logged but still executed i.e. selinux policy is not enforced, but denials are logged)
    #enforcing=1, selinux policy is enforced and denials are logged
    cmd = "grep -iE \"^\s*(kernel|linux)\" /boot/grub/menu.lst |grep -iE \"selinux|enforcing\""
    is_selinux_grub = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_selinux_grub)
    cmd = "grep -iE \"selinux|enforcing\" /boot/extlinux.conf"
    is_selinux_syslinux = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_selinux_syslinux)
    verbose_logs("Expected output to be compliant","verify that no kernel line has the selinux=0 or enforcing=0 parameters set")
    verbose_logs("To be compliant, run","Edit /boot/grub/menu.lst (grub), /etc/default/grub (grub2) and remove all instances of selinux=0 and enforcing=0 from all CMDLINE_LINUX parameters")
    if "selinux=1" in is_selinux_grub or "selinux=1" in is_selinux_syslinux:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")


    compliance_check = "Ensure the SELinux state is enforcing (Scored, Level 2 Server and Workstation)"
    cmd = "grep SELINUX=enforcing /etc/selinux/config"
    #can also be verified using sestatus command
    is_selinux_enforced = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_selinux_enforced)
    verbose_logs("Expected output to be compliant","SELINUX=enforcing")
    verbose_logs("To be compliant, run","Edit /etc/selinux/config by adding SELINUX=enforcing")
    if "SELINUX=enforcing" in is_selinux_enforced:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure SELinux policy is configured (Scored, Level 2 Server and Workstation)"
    cmd = "grep SELINUXTYPE=targeted /etc/selinux/config"
    is_selinux_policy = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_selinux_policy)
    verbose_logs("Expected output to be compliant","SELINUXTYPE=targeted or SELINUXTYPE=mls")
    verbose_logs("To be compliant, run","Edit /etc/selinux/config by adding SELINUXTYPE=targeted")
    if "SELINUXTYPE=targeted" in is_selinux_policy or "SELINUXTYPE=mls" in is_selinux_policy:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure SETroubleshoot is not installed (Scored, Level 2 Server)"
    cmd = "apk info setroubleshoot"
    is_setroubleshoot = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_setroubleshoot)
    verbose_logs("Expected output to be compliant","Verify s etroubleshoot is not installed")
    verbose_logs("To be compliant, run","Uninstall setroubleshoot using, apk del setroubleshoot")
    if "setroubleshoot" in is_setroubleshoot:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")

    compliance_check = "Ensure the MCS Translation Service (mcstrans) is not installed (Scored, Level 2 Server and Workstation)"
    cmd = "apk info mcstrans"
    is_mcstrans = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_mcstrans)
    verbose_logs("Expected output to be compliant","Verify mcstrans is not installed")
    verbose_logs("To be compliant, run","apk del mcstrans")
    if "mcstrans" in is_mcstrans:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    
    compliance_check = "Ensure no unconfined daemons exist (Scored, Level 2 Server and Workstation)"
    cmd = "ps -eZ | egrep \"initrc\" | egrep -vw \"tr|ps|egrep|bash|awk\" | tr ':' ' ' |awk '{ print $NF }'"
    no_uncofined_daemons = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", no_uncofined_daemons)
    verbose_logs("Expected output to be compliant","verify not output is produced for executed command")
    verbose_logs("To be compliant, run","Investigate any unconfined daemons found during the audit action")
    if "EXCEPTION" in no_uncofined_daemons:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure AppArmor is not disabled in bootloader configuration (Scored, Level 2 Server and Workstation)"
    cmd = "grep -iE \"^\s*(kernel|linux)\" /boot/grub/menu.lst"
    is_apparmor = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_apparmor)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","Edit /boot/grub/menu.lst and remove apparmor=0 on all kernel/linux lines. Or change apparmor=0 to apparmor=1")
    if "apparmor=0" in is_apparmor:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    
    compliance_check = "Ensure all AppArmor Profiles are enforcing (Scored, Level 2 Server and Workstation)"
    cmd = "apparmor_status"
    apparmor_status = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", apparmor_status)
    verbose_logs("Expected output to be compliant","Verify that profiles are loaded, no profiles are in complain mode, and no processes are unconfined")
    verbose_logs("To be compliant, run","enforce /etc/apparmor.d/*")

    compliance_check = "Ensure SELinux or AppArmor are installed (Not Scored, Level 2 Server and Workstation)"
    cmd = "apk info selinux && apk info apparmor"
    is_selinux_apparmor_installed = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_selinux_apparmor_installed)
    verbose_logs("Expected output to be compliant","Verify either SELinux or AppArmor is installed")
    verbose_logs("To be compliant, run","apk add selinux && apk add apparmor")
    if "selinux" in is_selinux_apparmor_installed or "apparmor" in is_selinux_apparmor_installed:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def warning_banners():
    global compliant_count

    compliance_check = "Ensure message of the day is configured properly (Scored, Level 1 Server and Workstation)"
    cmd = "cat /etc/motd"
    #\m - machine architecture (uname -a); \r - operating system release (uname -r); \s - operating system name; \v - operating system version (uname -v)
    #above options will work when there is mingetty(8) support
    #cmd = "egrep '(\\v|\\r|\\m|\\s)' /etc/motd"
    is_motd = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_motd)
    verbose_logs("Expected output to be compliant","verify that the contents match Corporate policy")
    verbose_logs("To be compliant, run","Edit /etc/motd file with the appropriate contents as per Corporate policy, remove instances of \m, \r, \s, or \v")
    update_compliance_status(compliance_check, "MANUAL VERIFICATION NEEDED")

    compliance_check = "Ensure local login warning banner is configured properly (Not Scored, Level 1 Server and Workstation)"
    cmd = "cat /etc/issue"
    is_loginbanner_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_loginbanner_present)
    verbose_logs("Expected output to be compliant","Verify that the contents match Corporate policy. Remove OS, Kernel, Release, Architecture related information.")
    verbose_logs("To be compliant, add","Authorized uses only. All activity may be monitored and reported instead of OS, Kernel, Release, Architecture related information.")
    if "Welcome to Alpine Linux" in is_loginbanner_present:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    
    compliance_check = "Ensure remote login warning banner is configured properly (Not Scored, Level 1 Server and Workstation)"
    cmd = "cat /etc/issue.net"
    is_rlogin_banner = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_rlogin_banner)
    verbose_logs("Expected output to be compliant","Verify that the contents match Corporate policy. Remove OS, Kernel, Release, Architecture related information.")
    verbose_logs("To be compliant, add","Authorized uses only. All activity may be monitored and reported instead of OS, Kernel, Release, Architecture related information.")
    if "Welcome to Alpine Linux" in is_rlogin_banner:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    

    compliance_check = "Ensure permissions on /etc/motd are configured (Not Scored, Level 1 Server and Workstation)"
    cmd = "stat /etc/motd"
    motd_permissions = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", motd_permissions)
    verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access is 644")
    verbose_logs("To be compliant, run","chown root:root /etc/motd; chmod 644 /etc/motd")
    #Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
    stat_motd = re.match(r'((.*?Access:\s*\(.644/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\)))',motd_permissions, re.I|re.M|re.S)
    if stat_motd:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure permissions on /etc/issue are configured (Scored, Level 1 Server and Workstation)"
    cmd = "stat /etc/issue"
    issue_permissions = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", issue_permissions)
    verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access is 644")
    verbose_logs("To be compliant, run","chown root:root /etc/issue; chmod 644 /etc/issue")
    stat_issue = re.match(r'((.*?Access:\s*\(.644/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\)))',issue_permissions, re.I|re.M|re.S)
    if stat_issue:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure permissions on /etc/issue.net are configured (Not Scored, Level 1 Server and Workstation)"
    cmd = "stat /etc/issue.net"
    issuenet_permissions = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", issuenet_permissions)
    verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access is 644")
    verbose_logs("To be compliant, run","chown root:root /etc/issue.net; chmod 644 /etc/issue.net")
    stat_issuenet = re.match(r'((.*?Access:\s*\(.644/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\)))',issue_permissions, re.I|re.M|re.S)
    if stat_issuenet:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")


    compliance_check = "Ensure GDM login banner is configured (Scored, Level 1 Server and Workstation)"
    #/root/xorg.conf.new; /etc/X11/xorg.conf; /etc/dconf/profile/gdm
    cmd = "grep -riE \"banner-message-enable=true|banner-message-text=\" /root/xorg.conf.new /etc/X11/xorg.conf /etc/dconf/profile/gdm"
    is_gdm_login = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_gdm_login)
    verbose_logs("Expected output to be compliant","Verify the banner-message-enable and banner-message-text options are configured")
    verbose_logs("To be compliant, run","Configure login banners as needed")
    if "banner-message-enable=true" in is_gdm_login or "banner-message-text" in is_gdm_login:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure updates, patches, and additional security software are installed (Not Scored, Level 1 Server and Workstation)"
    cmd1 = "apk update"
    n = exec_command(cmd1)
    cmd = "apk version"
    apk_version = exec_command(cmd)
    verbose_logs("Command used", cmd1 + cmd)
    verbose_logs("Command Output", apk_version)
    verbose_logs("Expected output to be compliant","Verify there are no updates or patches to install")
    verbose_logs("To be compliant, run","apk add --upgrade <package_name>")
    available_updates = apk_version.split('\n')
    #print "len(available_updates):", len(available_updates), "available_updates:", available_updates
    if len(available_updates) > 2:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def inetd_services():
    global compliant_count

    compliance_check = "Ensure chargen services are not enabled (Scored, Level 1)"
    #rc-status -a |grep -i chargen
    #rc-service chargen status
    #rc-service -l |grep chargen
    cmd = "rc-status -a |grep -i chargen; rc-service -l |grep chargen"
    is_chargen = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_chargen)
    verbose_logs("Expected output to be compliant","Verify the chargen service is not enabled")
    verbose_logs("To be compliant, run","rc-service chargen stop")
    if "chargen" in is_chargen:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure daytime services are not enabled (Scored, Level 1)"
    cmd = "rc-status -a |grep -i chargen; rc-service -l |grep chargen"
    is_daytime = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_daytime)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure discard services are not enabled (Scored)(Not Scored, Level 1)"
    cmd = "rc-status -a |grep -i chargen; rc-service -l |grep chargen"
    is_discard = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure echo services are not enabled (Scored)(Not Scored, Level 1)"
    cmd = "rc-status -a |grep -i chargen; rc-service -l |grep chargen"
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure time services are not enabled (Scored)(Not Scored, Level 1)"
    cmd = "rc-status -a |grep -i chargen; rc-service -l |grep chargen"
    is_time = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_time)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure rsh services are not enabled (Scored)(Not Scored, Level 1)"
    cmd = "rc-status -a |grep -i chargen; rc-service -l |grep chargen"
    is_rsh = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_rsh)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure talk server is not enabled (Scored)Not Scored, Level 1)"
    cmd = "rc-status -a |grep -i chargen; rc-service -l |grep chargen"
    is_talk = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_talk)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure telnet server is not enabled (Scored)(Not Scored, Level 1)"
    cmd = "rc-status -a |grep -i chargen; rc-service -l |grep chargen"
    is_telnet = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_telnet)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure tftp server is not enabled (Scored)(Not Scored, Level 1)"
    cmd = "rc-status -a |grep -i chargen; rc-service -l |grep chargen"
    is_tfpd = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tfpd)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure xinetd is not enabled (Scored)(Not Scored, Level 1)"
    cmd = "rc-status -a |grep -i chargen; rc-service -l |grep chargen"
    is_xinetd = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_xinetd)
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
    fs_integrity_checking()
    sec_boot_settings()
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
