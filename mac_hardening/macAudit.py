#!/usr/bin/python
import os, sys, time, re
import argparse
import subprocess

#Scored - Failure to comply will decrease the final benchmark score
#Not Scored - Failure to comply will not decrease the final benchmark score 
#Level 1 - general requirement
#Level 2 - required where security is paramount. Extends Level 1 profile

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

def check_patches():
    global total_compliances
    global compliant_count

    compliance_check = "Verify all Apple provided software is current (Scored, Level 1)"
    cmd = "softwareupdate -l" 
    is_sw_uptodate = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sw_uptodate)
    verbose_logs("Expected output to be compliant","All the software must be uptodate")
    if "No new software available" in is_sw_uptodate:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Enable Auto Update (Scored, Level 1)"
    cmd = "defaults read /Library/Preferences/com.apple.SoftwareUpdate AutomaticCheckEnabled" 
    au = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", au)
    verbose_logs("Expected output to be compliant","AutomaticCheckEnabled should be 1")
    verbose_logs("To be compliant, run","sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate AutomaticCheckEnabled -int 1")
    if "1" in au:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Enable app update installs (Scored, Level 1)"
    cmd = "defaults read /Library/Preferences/com.apple.commerce AutoUpdate" 
    apui = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", apui)
    verbose_logs("Expected output to be compliant","Returned value should be 1")
    verbose_logs("To be compliant, run(needs logout/login)","sudo defaults write /Library/Preferences/com.apple.commerce AutoUpdate -bool TRUE")
    if "1" in apui:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Enable system data files and security update installs (Scored, Level 1)"
    #split the command into two
    cmd = "defaults read /Library/Preferences/com.apple.SoftwareUpdate | egrep '(ConfigDataInstall|CriticalUpdateInstall)'" 
    sui = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sui)
    verbose_logs("Expected output to be compliant","Returned value should be 1 for both ConfigDataInstall,CriticalUpdateInstall")
    verbose_logs("To be compliant, run","sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate ConfigDataInstall -bool true && sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate CriticalUpdateInstall -bool true")
    if "1" in sui:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Enable OS X update installs (Scored, Level 1)"
    cmd = "defaults read /Library/Preferences/com.apple.commerce AutoUpdateRestartRequired" 
    osxui = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", osxui)
    verbose_logs("Expected output to be compliant","Returned value should be 1")
    verbose_logs("To be compliant, run","sudo defaults write /Library/Preferences/com.apple.commerce AutoUpdateRestartRequired -bool TRUE")
    if "1" in osxui:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def system_preferences():
    global total_compliances
    global compliant_count

    #BLUETOOTH
    compliance_check = "Turn off Bluetooth, if no paired devices exist (Scored, Level 1)"
    cmd = "defaults read /Library/Preferences/com.apple.Bluetooth ControllerPowerState" 
    bt_pde = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", bt_pde)
    verbose_logs("Expected output to be compliant","Returned value should be 0")
    if "0" in bt_pde:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1
    elif "1" in bt_pde:
        cmd = "system_profiler SPBluetoothDataType | grep \"Bluetooth:\" -A 20 | grep Connectable"
        bt_enabled = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", bt_enabled)
        verbose_logs("Expected output to be compliant","Paired Bluetooth devices should exist")
        verbose_logs("To be compliant, run","sudo defaults write /Library/Preferences/com.apple.Bluetooth ControllerPowerState -int 0 && sudo killall -HUP blued")
        if "EXCEPTION" in bt_enabled:
                compliant_count -= 1
                update_compliance_status(compliance_check, "NON-COMPLIANT")
        else:
                update_compliance_status(compliance_check, "COMPLIANT")
                compliant_count += 1
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Turn off Bluetooth \"Discoverable\" mode when not pairing devices (Scored, Level 1)"
    cmd = "/usr/sbin/system_profiler SPBluetoothDataType | grep -i discoverable" 
    bt_discoverable = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", bt_discoverable)      
    verbose_logs("Expected output to be compliant","Discoverable: Off")
    if "off" in bt_discoverable.lower():
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Show Bluetooth status in menu bar (Scored, Level 1)"
    cmd = "defaults read com.apple.systemuiserver menuExtras | grep Bluetooth.menu"
    bt_status_menubar = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", bt_status_menubar)      
    verbose_logs("Expected output to be compliant","/System/Library/CoreServices/Menu Extras/Bluetooth.menu")
    verbose_logs("To be compliant, run","defaults write com.apple.systemuiserver menuExtras -array-add \"/System/Library/CoreServices/Menu Extras/Bluetooth.menu\"")
    verbose_logs("Use case", "Enabling Bluetooth menu will help the user know Bluetooth on/off status easily")
    if "bluetooth.menu" in bt_status_menubar.lower():
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    #DATE AND TIME
    #NEED sudo ACCESS FOR BELOW COMMANDS
    compliance_check = "Enable \"Set time and date automatically\" (Not Scored, Level 2)"
    cmd = "sudo systemsetup -getusingnetworktime" 
    dt_auto = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", dt_auto)      
    verbose_logs("Expected output to be compliant","Network Time: On")
    verbose_logs("To be compliant, run","sudo systemsetup -setnetworktimeserver <timeserver> && sudo systemsetup -setusingnetworktime on")
    if "network time: on" in dt_auto.lower():
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure time set is within appropriate limits (Scored, Level 1)"
    cmd = "sudo systemsetup -getnetworktimeserver" 
    dt_ntp_server = exec_command(cmd)
    verbose_logs("Command used", cmd)
    if "EXCEPTION" in dt_ntp_server:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        ntp_domain = dt_ntp_server.split(':')[1].strip()
        cmd = "sudo ntpdate -svd " + ntp_domain + " | egrep offset |egrep ntpdate"
        #command output: 10 Oct 19:06:24 ntpdate[26544]: adjust time server 17.253.82.253 offset -0.037603 sec
        dt_ntp_offset = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", dt_ntp_offset)      
        verbose_logs("Expected output to be compliant","Offset result(s) are smaller than 270.x or -270.x seconds")
        ntpdate_output = dt_ntp_offset.split('\n')
        for eachline in ntpdate_output:
            match_offset = re.match(r'.*?ntpdate.*?time\s+server.*?offset\s+([-.\d]+)\s+sec.*?',eachline, re.I|re.M)
            if match_offset:
                offset_val = float(match_offset.group(1))
                verbose_logs("Current ntpdate offset value", offset_val)
                if (offset_val > -270.0) or (offset_val < 270.0):
                    compliant_count += 1
                    update_compliance_status(compliance_check, "COMPLIANT")
                else:
                    compliant_count -= 1
                    update_compliance_status(compliance_check, "NON-COMPLIANT")
                    verbose_logs("To be compliant, run","sudo systemsetup -setnetworktimeserver <timeserver> && sudo systemsetup -setusingnetworktime on")
                    verbose_logs("Current ntpdate offset value", offset_val)
            else:
                compliant_count -= 1
                update_compliance_status(compliance_check, "NON-COMPLIANT")
                verbose_logs("To be compliant, run","sudo systemsetup -setnetworktimeserver <timeserver> && sudo systemsetup -setusingnetworktime on")

    compliance_check = "Restrict NTP server to loopback interface (Scored, Level 1)"
    cmd = "cat /etc/ntp-restrict.conf | grep \"restrict lo\"" 
    dt_ntp_lo = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", dt_ntp_lo)      
    verbose_logs("Expected output to be compliant","restrict lo")
    verbose_logs("To be compliant, add","restrict lo interface ignore wildcard interface listen lo to /etc/ntp-restrict.conf")
    if "restrict lo" in dt_ntp_lo.lower():
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    #DESKTOP & SCREEN SAVER
    compliance_check = "Set an inactivity interval of 20 minutes or less for the screen saver (Scored, Level 1)"
    cmd = "ioreg -rd1 -c IOPlatformExpertDevice | grep \"IOPlatformUUID\"" 
    dss_uuid = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", dss_uuid)      
    uuid = dss_uuid.split('=')[1].replace('\"','').strip()
    verbose_logs("UUID", uuid)      
    cmd = "find /Users -type d -maxdepth 1"
    get_all_users = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", get_all_users)      
    all_users =  get_all_users.split('\n')
    for euser in all_users:
        pref = euser + "/Library/Preferences/ByHost/com.apple.screensaver." + uuid
        fplist = pref + ".plist"
        if os.path.isfile(fplist) and euser:
            cmd = "sudo defaults read " + fplist.strip() + " idleTime"
            read_plist = exec_command(cmd)
            verbose_logs("Command used", cmd)
            verbose_logs("Command Output", read_plist)      
            verbose_logs("Expected output to be compliant","Verify the setting is not 0 but is adequately low (< 1200)")
            if "EXCEPTION" in read_plist:
                compliant_count -= 1
                update_compliance_status(compliance_check, "NON-COMPLIANT")
            else:
                idle_time = int (read_plist)
                if idle_time >0 and idle_time <=1200:
                    update_compliance_status(compliance_check + "(for user " +euser+ ")", "COMPLIANT")
                else:
                    update_compliance_status(compliance_check + "(for user" +euser+ ")", "NON-COMPLIANT")
                    verbose_logs("To be compliant, run","defaults -currentHost write com.apple.screensaver idleTime -int 600")
        else:
            #file not present
            continue
    verbose_logs("INFO","Check system is configured as prescribed for the current logged in user")
    cmd = "defaults -currentHost read com.apple.screensaver idleTime"
    idletime = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", idletime)      
    verbose_logs("Expected output to be compliant","Verify the setting is not 0 but is adequately low (< 1200)")
    if "EXCEPTION" in read_plist:
        compliant_count -= 1
        update_compliance_status(compliance_check +"(current logged in user)", "NON-COMPLIANT")
    else:
        idle_time = int(read_plist)
        if idle_time >0 and idle_time <=1200:
            compliant_count += 1
            update_compliance_status(compliance_check +"(current logged in user)", "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check +"(current logged in user)", "NON-COMPLIANT")
            verbose_logs("To be compliant, run","defaults -currentHost write com.apple.screensaver idleTime -int 600")

    compliance_check = "Secure screen saver corners (Scored, Level 2)"
    cmd = "defaults read ~/Library/Preferences/com.apple.dock | grep -i corner"
    dss_ssc = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", dss_ssc)      
    verbose_logs("Expected output to be compliant","Verify that 6 is not returned for any key value for any user")
    if " 6" in dss_ssc:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, check","System Preferences->Mission Control->Hot Corners->Remove corners which are set to Disable Screen Saver. Make it -")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    
    compliance_check = "Verify Display Sleep is set to a value larger than the Screen Saver (Not Scored, Level 1)"
    cmd = "pmset -g | grep displaysleep" 
    dss_ds = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", dss_ds)      
    verbose_logs("Expected output to be compliant","verify displaysleep value returned is longer than the Screen Saver, if the Screen Saver is used to lock the screen")
    match_offset = re.match(r'.*?displaysleep\s+(\d+).*?',dss_ds)
    if match_offset:
        offset_val = int(match_offset.group(1))
        disp_sleep = int(dss_ds.split(' ')[-1].strip())
    if disp_sleep > idle_time:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo pmset -c displaysleep 0")

    compliance_check = "Set a screen corner to Start Screen Saver (Scored, Level 1)"
    cmd = "defaults read ~/Library/Preferences/com.apple.dock | grep -i corner" 
    dss_sc_sss = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", dss_sc_sss)      
    verbose_logs("Expected output to be compliant","Atleast one of the 4 corners should be \"wvous-*-corner\" = 5")
    if " 5" in dss_sc_sss:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, check","System Preferences->Mission Control->Hot Corners, make sure at least one Active Screen Corner is set to Start Screen Saver.")

    #SHARING
    compliance_check = "Disable Remote Apple Events (Scored, Level 1)"
    cmd = "sudo systemsetup -getremoteappleevents" 
    sh_rae = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sh_rae)      
    verbose_logs("Expected output to be compliant","Verify the value returned is Remote Apple Events: Off")
    if " off" in sh_rae.lower():
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo systemsetup -setremoteappleevents off")

    compliance_check = "Disable Internet Sharing (Scored, Level 1)"
    verbose_logs("Expected output to be compliant","NAT Config file should not exist or Enabled = 0 for all network interfaces")
    if os.path.isfile("/Library/Preferences/SystemConfiguration/com.apple.nat"):
        cmd = "sudo defaults read /Library/Preferences/SystemConfiguration/com.apple.nat | grep -i Enabled"
        sh_dis = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", sh_dis)
        verbose_logs("To be compliant, check","Open System Preferences->Select Sharing->uncheck Internet Sharing")
        match_enable0 = re.match(r'.*?Enable:\s+0.*?',sh_dis,re.I|re.M|re.S)
        if match_enable0:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            verbose_logs("To be compliant, check","Open System Preferences->Select Sharing->uncheck Internet Sharing")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
        

    compliance_check = "Disable Screen Sharing (Scored, Level 1)"
    cmd = "sudo launchctl load /System/Library/LaunchDaemons/com.apple.screensharing.plist" 
    sh_dss = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sh_dss)
    verbose_logs("Expected output to be compliant","Verify the value returned is Service is disabled")
    if "service is disabled" in sh_dss.lower():
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, check","Open System Preferences->Sharing->uncheck Screen Sharing")

    compliance_check = "Disable Printer Sharing (Scored, Level 1)"
    cmd = "system_profiler SPPrintersDataType | egrep \"Shared: Yes\"" 
    sh_dps = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sh_dps)      
    verbose_logs("Expected output to be compliant","output should be empty")
    if "EXCEPTION" in sh_dps:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:    
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, check","Open System Preferences->Sharing->uncheck Printer Sharing")

    compliance_check = "Disable Remote Login (Scored, Level 1)"
    cmd = "sudo systemsetup -getremotelogin" 
    sh_drl = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sh_drl)      
    verbose_logs("Expected output to be compliant","Verify the value returned is Remote Login: Off")
    if "remote login: off" in sh_drl.lower():
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:    
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo systemsetup -setremotelogin off")

    compliance_check = "Disable DVD or CD Sharing (Scored, Level 1)"
    cmd = "sudo launchctl list | egrep ODSAgent" 
    sh_cdrom = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sh_cdrom)      
    verbose_logs("Expected output to be compliant","com.apple.ODSAgent should not be in the output")
    if "com.apple.ODSAgent" in sh_cdrom:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, check","Open System Preferences->Sharing->uncheck DVD or CD Sharing")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")

    compliance_check = "Disable Bluetooth Sharing (Scored, Level 1)"
    cmd = "system_profiler SPBluetoothDataType | grep State" 
    sh_bt = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sh_bt)      
    verbose_logs("Expected output to be compliant","State: Disabled")
    if "enabled" in sh_bt.lower():
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, check","Open System Preferences->Sharing->uncheck Bluetooth Sharing")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")

    compliance_check = "Disable File Sharing (Scored, Level 1)"
    cmd = "sudo launchctl list | egrep AppleFileServer" 
    sh_afs = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sh_afs)      
    verbose_logs("Expected output to be compliant","No output should be present")
    cmd = "grep -i array /Library/Preferences/SystemConfiguration/com.apple.smb.server.plist" 
    sh_winfs = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sh_winfs)      
    verbose_logs("Expected output to be compliant","No output should be present")
    if ("EXCEPTION" in sh_afs) and ("EXCEPTION" in sh_winfs):
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:    
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.AppleFileServer.plist")
        verbose_logs("To be compliant, run","sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.smbd.plist")

    compliance_check = "Disable Remote Management (Scored, Level 1)"
    cmd = "ps -ef | egrep ARDAgent" 
    sh_drm = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sh_drm)      
    verbose_logs("Expected output to be compliant","Ensure /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/MacOS/ARDAgent is not present as a running process")
    if "/System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/MacOS/ARDAgent" not in sh_drm:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:    
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, check","in System Preferences->Sharing->turn off Remote Management")
    
    #ENERGY SAVER
    compliance_check = "Disable \"Wake for network access\" (Scored, Level 2)"
    cmd = "pmset -g | grep -i 'AC Power'" 
    ac_power_status = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", ac_power_status)      
    verbose_logs("Expected output to be compliant","Verify that both values returned are 0")
    if "ac power" in ac_power_status.lower():
        verbose_logs("INFO","We are using AC Power source")
        #-c for charger (wall power), -b for battery
        cmd = "pmset -c -g | grep womp; pmset -b -g | grep womp"
        womp_values = exec_command(cmd) 
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", womp_values)      
        verbose_logs("Expected output to be compliant","Verify that both values returned are 0")
        match_womp = re.match(r'.*?womp\s+[1-9].*?',womp_values, re.I|re.M|re.S)
        if match_womp:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            verbose_logs("To be compliant, run","sudo pmset -a womp 0")
        else:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
    else:
        update_compliance_status(compliance_check, "COULD NOT VERIFY COMPLIANCE")

    compliance_check = "Disable sleeping the computer when connected to power (Scored, Level 2)"
    if "AC Power" in ac_power_status:
        cmd = "pmset -g | egrep \"^\s*sleep\""
        pwr_is_sleep = exec_command(cmd) 
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", womp_values)      
        verbose_logs("Expected output to be compliant","Verify returned value is 0")
        #sleep_val = re.match(r'', pwr_is_sleep, re.I|re.M|re.S) 
        if " 0" in pwr_is_sleep:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            verbose_logs("To be compliant, run","sudo pmset -c sleep 0 or System Preferences->Energy Saver->slider for Put the computer to sleep/Turn display off after to never")

    #SECURITY AND PRIVACY
    compliance_check = "Enable FileVault (Scored, Level 1)"
    cmd = "diskutil cs list | grep -i encryption"
    sp_enc_status = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sp_enc_status)      
    verbose_logs("Expected output to be compliant","Logical Volume should show as both Encrypted and unlocked")
    enc_status = re.match(r'Encryption\s+Type:(.*?)', sp_enc_status, re.I|re.M)
    if enc_status:
        print "enc_status groups:", enc_status.groups()
        print "enc_status group1:", enc_status.group(1)
    if ("AES-XTS" in sp_enc_status) and ("Unlocked" in sp_enc_status):
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, Check","System Preferences->Security and Privacy->FileVault->Turn on FileVault")

    compliance_check = "Enable Gatekeeper (Scored, Level 1)"
    cmd = "sudo spctl --status" 
    sp_gatekeeper = exec_command(cmd)
    if "assessments enabled" in sp_gatekeeper:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, Check","System Preferences->Security and Privacy->General->select Allow applications downloaded from: Mac App Store and identified developers")
        verbose_logs("or execute command", "sudo spctl --master-enable")

    compliance_check = "Enable Firewall (Scored, Level 1)"
    cmd = "defaults read /Library/Preferences/com.apple.alf globalstate"
    sp_fw_status = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sp_fw_status)      
    verbose_logs("Expected output to be compliant","Returned value must be 1 or 2")
    if "1" in sp_fw_status or "2" in sp_fw_status:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","defaults write /Library/Preferences/com.apple.alf globalstate - int <value>")
        verbose_logs("or to be compliant check", "System Preferences->Security and Privacy->Firewall->select Turn On Firewall")

    compliance_check = "Enable Firewall Stealth Mode (Scored, Level 1)"
    cmd = "/usr/libexec/ApplicationFirewall/socketfilterfw --getstealthmode"
    sp_fw_stealthmode = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sp_fw_stealthmode)      
    verbose_logs("Expected output to be compliant","Verify the value returned is Stealth mode enabled")
    if "enabled" in sp_fw_stealthmode:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode on")
        verbose_logs("or To be compliant, check","System Preferences->Security and Privacy->Firewall Options->select Enable stealth mode")
        verbose_logs("INFO","ping might not work")

    compliance_check = "Review Application Firewall Rules (Scored, Level 1)"
    cmd = "/usr/libexec/ApplicationFirewall/socketfilterfw --listapps |grep \" : \" |wc -l"
    sp_fw_rulecount = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sp_fw_rulecount)      
    verbose_logs("Expected output to be compliant","Verify that the number of rules returned is lower than 10")
    verbose_logs("To be compliant, run(to remove ACL's)","/usr/libexec/ApplicationFirewall/socketfilterfw --remove </Applications/app_name_toremove.app>")
    fw_rule_count = int(sp_fw_rulecount.strip())
    if fw_rule_count <= 10:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run(to remove ACL's)","/usr/libexec/ApplicationFirewall/socketfilterfw --remove </Applications/app_name_toremove.app>")
        verbose_logs("To be compliant, Check","System Preferences->Security and Privacy->Firewall Options->select unneeded rules->select the minus sign below to delete them")

    compliance_check = "Enable Location Services (Not Scored, Level 2)"
    cmd = "sudo launchctl load /System/Library/LaunchDaemons/com.apple.locationd.plist"
    ps_location_services = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", ps_location_services)      
    verbose_logs("Expected output to be compliant","Operation already in progress or service already loaded in output")
    if ("operation already in progress" in ps_location_services) or ("service already loaded" in ps_location_services):
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo launchctl load /System/Library/LaunchDaemons/com.apple.locationd.plist")

    compliance_check = "Monitor Location Services Access (Not Scored, Level 2)"
    cmd = "defaults read ~/Library/Preferences/com.apple.safari.plist SafariGeolocationPermissionPolicy globalstate"
    sp_lsa = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sp_lsa)      
    verbose_logs("Expected output to be compliant","Recommend using 0 or 1")
    if "2" in sp_lsa:
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo launchctl load /System/Library/LaunchDaemons/com.apple.locationd.plist")
    else:    
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
        verbose_logs("To be compliant, check","open Safari->Select Safari from the menu bar->Preferences->Privacy->Check Deny without prompting(0) or Prompt for each website once each day(1)")
        verbose_logs("Review Applications using Location Services","System Preferences->Security and Privacy->Privacy->Location Services->Uncheck applications that are not approved for access to location service information")
    cmd = "sudo defaults read /var/db/locationd/clients.plist | grep -i com.*"
    sp_els = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output(Applications using Location Services)", sp_els)      

    #iCloud
    compliance_check = "iCloud configuration (Not Scored, Level 2)"
    verbose_logs("Command used", "COMMAND NOT FOUND FOR THIS CHECK")
    verbose_logs("Expected output to be compliant","Disable iCloud or configure the access to best enable data protection")
    update_compliance_status(compliance_check, "MANUAL VERIFICATION NEEDED")
    verbose_logs("INFO","Data Leakage is possible")

    compliance_check = "iCloud keychain (Not Scored, Level 2)"
    verbose_logs("Command used", "COMMAND NOT FOUND FOR THIS CHECK")
    verbose_logs("Expected output to be compliant","open System Preferences->iCloud->deselect Keychain if it is not approved in your organization")
    update_compliance_status(compliance_check, "MANUAL VERIFICATION NEEDED")
    verbose_logs("INFO","Ensure that the iCloud keychain is used consistently with organizational requirements")
    compliance_check = "iCloud Drive (Not Scored, Level 2)"
    
    compliance_check = "iCloud Drive(Not Scored, Level 2)"
    verbose_logs("Command used", "COMMAND NOT FOUND FOR THIS CHECK")
    verbose_logs("Expected output to be compliant","open System Preferences->iCloud->uncheck iCloud Drive")
    update_compliance_status(compliance_check, "MANUAL VERIFICATION NEEDED")

    compliance_check = "iCloud Drive Document sync (Scored, Level 2)"
    cmd = "ls -l ~/Library/Mobile?\ Documents/com~apple~CloudDocs/Documents/ | grep total"
    ps_ddsync = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", ps_ddsync)      
    verbose_logs("Expected output to be compliant","There should be no result")
    verbose_logs("To be compliant, check","open System Preferences->iCloud->iCloud Drive->select Options next to iCloud Drive->uncheck Desktop & Documents Folders")
    if "EXCEPTION" in ps_ddsync:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "iCloud Drive Desktop sync (Scored, Level 2)"
    cmd = "ls -l ~/Library/Mobile?\ Documents/com~apple~CloudDocs/Desktop/ | grep total"
    icloud_dds = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", icloud_dds)      
    verbose_logs("Expected output to be compliant","There should be no result")
    verbose_logs("To be compliant, check","open System Preferences->iCloud->iCloud Drive->select Options next to iCloud Drive->uncheck Desktop & Documents Folders")
    if "EXCEPTION" in icloud_dds:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    #TIME MACHINE
    compliance_check = "Time Machine Auto-Backup (Scored, Level 2)"
    cmd = "defaults read /Library/Preferences/com.apple.TimeMachine.plist AutoBackup"
    tm_bkup = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", tm_bkup)      
    verbose_logs("Expected output to be compliant","output should not be zero")
    if int(tm_bkup) != 0:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","defaults write /Library/Preferences/com.apple.TimeMachine.plist AutoBackup 1")

    compliance_check = "Time Machine Volumes Are Encrypted (Not Scored, Level 1)"
    cmd = "tmutil destinationinfo"
    tm_vol = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", tm_vol)      
    verbose_logs("Expected output to be compliant","")
    if "no destinations configured" in tm_vol.lower():
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    elif "local" in tm_vol.lower():
        cmd = "diskutil list"
        tm_drive_list = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", tm_drive_list)      
        verbose_logs("Expected output to be compliant","All Time Machine targets identified using tmutil should show an encrypted status")
        #TODO - did not get encrypted drives on test machine 
        verbose_logs("To be compliant, run","defaults write /Library/Preferences/com.apple.TimeMachine.plist AutoBackup 1")
        update_compliance_status(compliance_check, "MANUAL VERIFICATION NEEDED")

    compliance_check = "Pair the remote control infrared receiver if enabled (Scored, Level 1)"
    cmd = "system_profiler 2>/dev/null | egrep \"IR Receiver\""
    tm_sp = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", tm_sp)      
    verbose_logs("Expected output to be compliant","If DeviceEnabled = 1, then verify the value returned for the UIDFilter does not equal none")
    if "EXCEPTION" in tm_sp:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        cmd = "defaults read /Library/Preferences/com.apple.driver.AppleIRController"
        ir_details = exec_command(cmd)
        ir_dev_enabled = re.match(r'.*?DeviceEnabled\s+=\s+(\d);.*?',ir_details, re.I|re.M|re.S)
        ir_udifilter = re.match(r'.*?UIDFilter\s+=\s+(\w+);.*?',ir_details, re.I|re.M|re.S)
        print "ir_dev_enabled.groups:", ir_dev_enabled.groups(), "1:", ir_dev_enabled.group(1)
        print "ir_udifilter.groups:", ir_udifilter.groups(), "1:",ir_udifilter.group(1)
        print "Verify the value returned for DeviceEnabled = 0"
        verbose_logs("To be compliant, check","System Preferences->Security & Privacy->General->Advanced->check Disable remote control infrared receiver")

    compliance_check = "Enable Secure Keyboard Entry in terminal.app (Scored, Level 1)"
    cmd = "defaults read -app Terminal SecureKeyboardEntry"
    skbe = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", skbe)      
    verbose_logs("Expected output to be compliant","Verify the value returned is 1")
    verbose_logs("To be compliant, check","open Terminal->select Terminal menu->select Secure Keyboard Entry")
    if "1" in skbe:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, check","open Terminal->select Terminal menu->select Secure Keyboard Entry")
        verbose_logs("INFO","Secure Keyboard Entry prevents other applications on system/network from detecting and recording what is typed into Terminal")

    compliance_check = "Java 6 is not the default Java runtime (Scored, Level 2)"
    cmd = "java -version"
    java_ver = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", java_ver)      
    verbose_logs("Expected output to be compliant","Java version greater than 1.6")
    verbose_logs("To be compliant, run","Update Java to latest version")
    #correct comparison is check for versions less than 1.7
    if "1.6" in java_ver:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")

    compliance_check = "Securely delete files as needed (Not Scored, Level 2)"
    cmd = "diskutil secureErase"
    update_compliance_status(compliance_check + "(using command \"" + cmd +"\")", "MANUAL VERIFICATION NEEDED")

def check_logging_and_auditing():
    global compliant_count

    #LOGGING AND AUDITING
    #Configure asl.conf
    verbose_logs("INFO","maximum file size limitation string should be removed \"all_max=\"")
    verbose_logs("INFO","An organization appropriate retention should be added \"ttl=\"")
    verbose_logs("INFO","The rotation should be set with time stamps \"rotate=utc\" or \"rotate=local\"")

    compliance_check = "Retain system.log for 90 or more days (Scored, Level 1)"
    #> system.log mode=0640 format=bsd rotate=seq compress file_max=5M all_max=50M
    cmd = "grep -i ttl /etc/asl.conf |grep -i system\.log"
    systemlog_ttl = exec_command(cmd) 
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", systemlog_ttl)      
    verbose_logs("Expected output to be compliant","Verify that the ttl for system.log is greater than 90 days")
    verbose_logs("To be compliant, edit","/etc/asl.conf by adding ttl=90 or greater to system.log line")
    system_log_line = re.match(r'\s*[>?]\s*system.log.*?ttl=(\d+)',systemlog_ttl, re.I|re.M)
    if system_log_line:
        print "system_log_line groups:", system_log_line.groups()
        print "system_log_line group 1:", system_log_line.group(1)
        system_log_ttl = int(system_log_line.group(1))
        if system_log_ttl >= 90:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Retain appfirewall.log for 90 or more days (Scored, Level 1)"
    cmd = "grep -i ttl /etc/asl.conf |grep -i appfirewall\.log"
    appfirewalllog_ttl = exec_command(cmd) 
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", appfirewalllog_ttl)      
    verbose_logs("Expected output to be compliant","Verify that the ttl for appfirewall.log is greater than 90 days")
    verbose_logs("To be compliant, edit","/etc/asl.conf by adding ttl=90 or greater to appfirewall.log line")
    appfirewall_log_line = re.match(r'\s*[>?]\s*appfirewall.log.*?ttl=(\d+)',appfirewalllog_ttl, re.I|re.M)
    if appfirewall_log_line:
        appfirewall_log_ttl = int(appfirewall_log_line.group(1))
        if appfirewall_log_ttl >= 90:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Retain authd.log for 90 or more days (Scored, Level 1)"
    cmd = "grep -i ttl /etc/asl/com.apple.authd"
    authd_log_ttl = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", authd_log_ttl)      
    verbose_logs("Expected output to be compliant","Verify that ttl is 90 or higher for authd.log")
    verbose_logs("To be compliant, run","")
    verbose_logs("To be compliant, edit","/etc/asl.conf by adding ttl=90 or greater to system.log line")
    authd_log_line = re.match(r'\s*[>|?|*]\s*authd.log.*?ttl=(\d+)',authd_log_ttl, re.I|re.M)
    if authd_log_line:
        print "authd_log_line groups:", authd_log_line.groups()
        print "authd_log_line group 1:", authd_log_line.group(1)
        authd_log_ttl = int(authd_log_line.group(1))
        if authd_log_ttl >= 90:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Enable security auditing (Scored, Level 1)"
    cmd = "sudo launchctl list | grep -i auditd"
    sec_audit = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sec_audit)      
    verbose_logs("Expected output to be compliant","Verify \"com.apple.auditd\" appears.")
    if "com.apple.auditd" in sec_audit:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.auditd.plist")

    compliance_check = "Configure Security Auditing Flags (Scored, Level 2)"
    cmd = "sudo egrep \"^flags:\" /etc/security/audit_control"
    sec_audit_flags = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sec_audit_flags)      
    verbose_logs("Expected output to be compliant","Atleast one of the flags lo, ad, fd, fm, -all must be set")
    verbose_logs("To be compliant, edit","/etc/security/audit_control by adding required flag(s) lo, ad, fd, fm, -all")
    if "lo" in sec_audit_flags or "ad" in sec_audit_flags or "fd" in sec_audit_flags or "fm" in sec_audit_flags or "-all" in sec_audit_flags:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, edit","/etc/security/audit_control by adding required flag(s) lo, ad, fd, fm, -all")
        verbose_logs("INFO", "lo - audit successful/failed login/logout events")
        verbose_logs("INFO", "ad - audit successful/failed administrative events") 
        verbose_logs("INFO", "fd - audit successful/failed file deletion events")
        verbose_logs("INFO", "fm - audit successful/failed file attribute modification events")
        verbose_logs("INFO", "-all - audit all failed events across all audit classes")

    compliance_check = "Enable remote logging for Desktops on trusted networks (Not Scored, Level 2)"
    cmd = "grep -v \"127\.0\.0\" /etc/syslog.conf"
    #flat file logs are now configured in /etc/asl.conf
    syslog_ipaddr = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", syslog_ipaddr)      
    verbose_logs("Expected output to be compliant","Remote loggind enabled. Must find entry \"*.*   @syslog_ip_addr\"")
    syslog_server_config = re.match(r'@\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',syslog_ipaddr, re.I|re.M)
    #check valip Syslog Server IP Address is configured
    if syslog_server_config:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, edit","/etc/syslog.conf by adding \"*.*   @syslog_ip_addr\" on the top of the file")

    compliance_check = "Retain install.log for 365 or more days (Scored, Level 1)"
    cmd = "grep -i ttl /etc/asl/com.apple.install"
    install_log_ttl = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", install_log_ttl)      
    verbose_logs("Expected output to be compliant","Verify that ttl is 365 or higher for install.log")
    verbose_logs("To be compliant, run","")
    verbose_logs("To be compliant, edit","/etc/asl/com.apple.install by adding ttl=90 or greater to install.log line")
    install_log_line = re.match(r'\s*[>|?|*]\s*install.log.*?ttl=(\d+)',install_log_ttl, re.I|re.M)
    if install_log_line:
        print "install_log_line groups:", install_log_line.groups()
        print "install_log_line group 1:", install_log_line.group(1)
        install_log_ttl = int(install_log_line.group(1))
        if install_log_ttl >= 365:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def network_configurations():
    global compliant_count

    compliance_check = "Disable Bonjour advertising service (Scored, Level 2)"
    #file was not present on my test machine
    cmd = "defaults read /Library/Preferences/com.apple.mDNSResponder.plist NoMulticastAdvertisements"
    is_bonjour_running = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_bonjour_running)      
    verbose_logs("Expected output to be compliant","Verify the value returned is 1")
    if "1" in is_bonjour_running:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","defaults write /Library/Preferences/com.apple.mDNSResponder.plist NoMulticastAdvertisements")
        verbose_logs("INFO","Final Cut Studio and AirPort Base Station management might not work if mDNSResponder is turned off")

    compliance_check = "Enable \"Show Wi-Fi status in menu bar\" (Scored, Level 1)"
    cmd = "defaults read com.apple.systemuiserver menuExtras | grep AirPort.menu"
    wifi_menubar = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", wifi_menubar)      
    verbose_logs("Expected output to be compliant","output should have /System/Library/CoreServices/Menu Extras/AirPort.menu")
    if "/System/Library/CoreServices/Menu Extras/AirPort.menu" in wifi_menubar:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, check","System Preferences->Network->check Check Show Wi-Fi status in menu bar")

    compliance_check = "Create network specific locations (Not Scored, Level 2)"
    verbose_logs("INFO","Ready Network configs for Mobility")
    verbose_logs("INFO","Remove unnecessary Network services like FireWire, VPN, AirPort or Ethernet")
    verbose_logs("Command used", "COMMAND NOT FOUND FOR THIS CHECK")
    update_compliance_status(compliance_check, "MANUAL VERIFICATION NEEDED")
    print "MANUAL. Open System Preferences: Network. Verify each network location is set up properly"
    verbose_logs("To be compliant, check","open System Preferences->Network->Verify each network location is set up properly. Remove unnecessary Network services")

    compliance_check = "Ensure http server is not running (Scored, Level 1)"
    cmd = "ps -ef | grep -i httpd"
    is_httpd_running = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_httpd_running)      
    verbose_logs("Expected output to be compliant","No results for /usr/sbin/httpd")
    if "/httpd" in is_httpd_running.lower():
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo apachectl stop; sudo defaults write /System/Library/LaunchDaemons/org.apache.httpd Disabled -bool true")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")

    compliance_check = "Ensure ftp server is not running (Scored, Level 1)"
    cmd = "sudo launchctl list | egrep ftp"
    is_ftpd_running = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_ftpd_running)      
    verbose_logs("Expected output to be compliant","No results for com.apple.ftpd")
    if "com.apple.ftpd" in is_ftpd_running:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo -s launchctl unload -w /System/Library/LaunchDaemons/ftp.plist")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
        
    compliance_check = "Ensure nfs server is not running (Scored, Level 1)"
    cmd = "ps -ef | grep -i nfsd"
    is_nfsd_running = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_nfsd_running)      
    verbose_logs("Expected output to be compliant","no results for /sbin/nfsd and /etc/export file should not be present")
    if "/nfsd" in is_nfsd_running or os.path.isfile("/etc/exports"):
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo nfsd disable; rm /etc/export")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")

def sysAccess_Authen_Authoriz():
    global compliant_count

    #SYSTEM ACCESS, AUTHENTICATION AND AUTHORIZATION
    #File System Permissions and Access Controls
    compliance_check = "Secure Home Folders (Scored, Level 1)"
    cmd = "ls -l /Users/"
    usr_dirlist = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", usr_dirlist)      
    verbose_logs("Expected output to be compliant","User directory permissions should be either \"drwx------\" or \"drwx--x--x\"")
    udl = usr_dirlist.split('\n')
    for each_udl in udl:
        print "each_udl:", each_udl
        if "drwx------" not in each_udl or "drwx--x--x" not in each_udl:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            verbose_logs("To be compliant, run","")
            break
        else:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")

    compliance_check = "Check System Wide Applications for appropriate permissions (Scored, Level 1)"
    cmd = "sudo find /Applications -iname \"*\.app\" -type d -perm -2 -ls"
    app_permissions = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", app_permissions)      
    verbose_logs("Expected output to be compliant","There should not be any Apps with world writable permissions")
    if "/Applications/" in app_permissions or "EXCEPTION" not in app_permissions:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant","Applications identified should be removed or changed permissions to drwxr-xr-x")
        verbose_logs("To be compliant,run ","sudo chmod -R o-w /Applications/BadPermissions.app/")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")

    compliance_check = "Check System folder for world writable files (Scored, Level 1)"
    cmd = "sudo find /System -type d -perm -2 -ls | grep -v \"Public/Drop Box\""
    sys_permissions = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sys_permissions)      
    verbose_logs("Expected output to be compliant","There should not be any System folder with world writable permissions")
    if "/System/" in sys_permissions or "EXCEPTION" not in sys_permissions:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant,run","sudo chmod -R o-w /Bad/Directory")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    
    compliance_check = "Check Library folder for world writable files (Scored, Level 2)"
    cmd = "sudo find /Library -type d -perm -2 -ls | grep -v Caches"
    world_writable_libs = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", world_writable_libs)      
    verbose_logs("Expected output to be compliant","There should not be any Library folder with world writable permissions")
    if "/Library" in world_writable_libs or "EXCEPTION" not in world_writable_libs:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant,run","sudo chmod -R o-w /Bad/Directory")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")

    #Password Management
    compliance_check = "Configure account lockout threshold (Scored)"
    #pwpolicy -getaccountpolicies did not return any value on my test setup
    #sudo pwpolicy -n /Local/Default -a <admin_user> -setglobalpolicy minChars=8
    #sudo pwpolicy -n /Local/Default -setglobalpolicy "minChars=14 requiresAlpha=1 requiresNumeric=1 requiresMixedCase=1 requiresSymbol=1 passwordCannotBeName=1 maxFailedLoginAttempts=5"
    #sudo pwpolicy -n /Local/Default -getglobalpolicy
    cmd = "pwpolicy -getaccountpolicies | grep -A 1 '<key>policyAttributeMaximumFailedAuthentications</key>' | tail -1 | cut -d'>' -f2 | cut -d '<' -f1"
    lockout_threshold = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", lockout_threshold)      
    verbose_logs("Expected output to be compliant","Verify the value returned is 5 or lower")
    if int(lockout_threshold) <=5:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run(sample password policy configuration)","sudo pwpolicy -n /Local/Default -setglobalpolicy \"minChars=15 requiresAlpha=1 requiresNumeric=1 requiresMixedCase=1 requiresSymbol=1 passwordCannotBeName=1 maxFailedLoginAttempts=5\"")

    compliance_check = "Set a minimum password length (Scored, Level 1)"
    cmd = "pwpolicy -getaccountpolicies | egrep \"\d+ characters\""
    passwd_len_str = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", passwd_len_str)      
    verbose_logs("Expected output to be compliant","<string>Password must be a minimum of 15 characters in length</string>")
    passwd_len_stmt = re.match(r'.*?be\s+a\s+minimum\s+of\s+(\d+)\s+characters\s+in\s+length.*?',passwd_len_str, re.I|re.M|re.S)
    if passwd_len_stmt:
        passwd_len = int(passwd_len_stmt.group(1))
        if passwd_len >= 15:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            verbose_logs("To be compliant, run","sudo pwpolicy -n /Local/Default -setglobalpolicy \"minChars=15 requiresAlpha=1 requiresNumeric=1 requiresMixedCase=1 requiresSymbol=1 passwordCannotBeName=1 maxFailedLoginAttempts=5\"")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo pwpolicy -n /Local/Default -setglobalpolicy \"minChars=15 requiresAlpha=1 requiresNumeric=1 requiresMixedCase=1 requiresSymbol=1 passwordCannotBeName=1 maxFailedLoginAttempts=5\"")
    
    compliance_check = "Complex passwords must contain an Alphabetic Character (Scored, Level 1)"
    cmd = "pwpolicy -getaccountpolicies | egrep Alpha"
    requiresAlpha = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", requiresAlpha)      
    verbose_logs("Expected output to be compliant","should have \"<string>com.apple.policy.legacy.requiresAlpha</string>\" or \"<string>RequiresAlpha</string>\"")
    if "requiresalpha" in requiresAlpha.lower():
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo pwpolicy -n /Local/Default -setglobalpolicy \"minChars=15 requiresAlpha=1\"")

    compliance_check = "Complex passwords must contain a Numeric Character (Scored, Level 1)"
    cmd = "pwpolicy -getaccountpolicies | egrep Numeric"
    requiresNumeric = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", requiresNumeric)      
    verbose_logs("Expected output to be compliant","should have \"<string>com.apple.policy.legacy.requiresNumeric</string>\" or \"<string>RequiresNumeric</string>\"")
    if "requiresnumeric" in requiresNumeric.lower():
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo pwpolicy -n /Local/Default -setglobalpolicy \"minChars=15 requiresNumeric=1\"")

    compliance_check = "Complex passwords must contain a Special Character (Scored, Level 1)"
    cmd = "pwpolicy -getaccountpolicies | egrep -i symbol"
    requiresSymbol = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", requiresSymbol)      
    verbose_logs("Expected output to be compliant","should have \"<string>com.apple.policy.legacy.requiresSymbol</string>\" or \"<string>RequiresSymbol</string>\"")
    verbose_logs("To be compliant, run","sudo pwpolicy -n /Local/Default -setglobalpolicy \"minChars=15 requiresSymbol=1\"")
    if "requiressymbol" in requiresSymbol.lower():
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo pwpolicy -n /Local/Default -setglobalpolicy \"minChars=15 requiresSymbol=1\"")

    compliance_check = "Complex passwords must uppercase and lowercase letters (Scored, Level 1)"
    cmd = "pwpolicy -getaccountpolicies |grep -i requiresMixedCase"
    requiresMixedCase = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", requiresMixedCase)      
    verbose_logs("Expected output to be compliant","should have \"<string>com.apple.policy.legacy.requiresMixedCase</string>\" or \"<string>RequiresMixedCase</string>\"")
    verbose_logs("To be compliant, run","sudo pwpolicy -n /Local/Default -setglobalpolicy \"minChars=15 requiresMixedCase=1\"")
    if "requiresmixedcase" in requiresMixedCase.lower():
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo pwpolicy -n /Local/Default -setglobalpolicy \"minChars=15 requiresMixedCase=1\"")

    compliance_check = "Password Age (Scored, Level 1)"
    cmd = "pwpolicy -getaccountpolicies | grep -B8 -A8 -i maxMinutesUntilChangePassword |grep -i integer | grep -oE \"\d+\""
    passwordExp_noDays = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", passwordExp_noDays)      
    verbose_logs("Expected output to be compliant","should have \"<string>com.apple.policy.legacy.maxMinutesUntilChangePassword</string>\" or \"<string>maxMinutesUntilChangePassword</string>\"")
    #30 days = 30d*24h*60 = 43200
    verbose_logs("To be compliant, run","sudo pwpolicy -n /Local/Default -setglobalpolicy \"minChars=15 maxMinutesUntilChangePassword=43200\"")
    if int(passwordExp_noDays) <= 90:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("To be compliant, run","sudo pwpolicy -n /Local/Default -setglobalpolicy \"minChars=15 requiresMixedCase=1\"")

    compliance_check = "Password History (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Reduce the sudo timeout period (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Automatically lock the login keychain for inactivity (Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Ensure login keychain is locked when the computer sleeps (Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Enable OCSP and CRL certificate checking (Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Do not enable the "root" account (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Disable automatic login (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Require a password to wake the computer from sleep or screen saver (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Require an administrator password to access system-wide preferences (Scored, Level 1))"
    cmd = ""
    n = exec_command(cmd)
    
    compliance_check = "Disable ability to login to another user's active and locked session (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Create a custom message for the Login Screen (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Create a Login window banner (Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Do not enter a password-related hint (Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Disable Fast User Switching (Not Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Secure individual keychains and items (Not Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Create specialized keychains for different purposes (Not Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "System Integrity Protection status (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Install an approved tokend for smartcard authentication (Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

def user_AccountsEnvironment():
    global compliant_count

    compliance_check = "Display login window as name and password (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Disable \"Show password hints\" (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Disable guest account login (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Disable \"Allow guests to connect to shared folders\" (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Remove Guest home folder (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Turn on filename extensions (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Disable the automatic run of safe files in Safari (Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Safari disable Internet Plugins for global use (Not Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Use parental controls for systems that are not centrally managed (Not Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

def additional_considerations():
    global compliant_count
    compliance_check = "Wireless technology on OS X (Not Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("INFO", "Check Corporate Policies on Disabling/Enabling wireless technologies like Wi-Fi or Bluetooth")
    update_compliance_status(compliance_check, "MANUAL VERIFICATION NEEDED")

    compliance_check = "iSight Camera Privacy and Confidentiality Concerns (Not Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Computer Name Considerations (Not Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Software Inventory Considerations (Not Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Firewall Consideration (Not Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Automatic Actions for Optical Media (Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "App Store Automatically download apps purchased on other Macs Considerations (Not Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Extensible Firmware Interface (EFI) password (Not Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "FileVault and Local Account Password Reset using AppleID (Not Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Repairing permissions is no longer needed (Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "App Store Password Settings (Not Scored, Level 2)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Siri on MacOS (Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Apple Watch features with MacOS (Not Scored, Level 1)"
    cmd = ""
    n = exec_command(cmd)

    compliance_check = "Apple File System (APFS) (Not Scored, Level 1))"
    cmd = ""
    n = exec_command(cmd)

if __name__ == "__main__":
    global total_compliances
    global compliant_count

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",action="store_true")
    parser.add_argument("-n", "--nocolor", help="plain console output(default logging uses color)",action="store_true")
    args = parser.parse_args()

    print "Hardening Checks for Apple MAC based on Centre for Internet Security Benchmarks"
    print "Benchmark Reference","CIS Apple OSX 10.12 Benchmark v1.0.0 - 11-04-2016"
    print "Author: Praveen Darshanam"

    verbose_logs("RECOMMENDATION SECTION","Install Updates, Patches and Additional Security Software")
    check_patches()

    verbose_logs("RECOMMENDATION SECTION","System Preferences")
    system_preferences()

    verbose_logs("RECOMMENDATION SECTION","Logging and Auditing")
    check_logging_and_auditing()

    verbose_logs("RECOMMENDATION SECTION","Network Configurations")
    network_configurations()

    verbose_logs("RECOMMENDATION SECTION","System Access, Authentication and Authorization")
    sysAccess_Authen_Authoriz()
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
