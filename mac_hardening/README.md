# CISBenchmarks
Hardening audit scripts validating Workstations and Servers based on CIS benchmarks

Center for Internet Security (CIS), http://benchmarks.cisecurity.org

Bechmarks are based on
-Install Updates, Patches and Additional Security Software
-System Preferences
    -Bluetooth
    -Date & Time
    -Desktop & Screen Saver
    -Sharing
    -Energy Saver
    -Security & Privacy
    -iCloud
    -Time Machine
-Logging and Auditing
    -Configure asl.conf
-Network Configurations
-System Access, Authentication and Authorization
    -File System Permissions and Access Controls
    -Password Management
-User Accounts and Environment
    -Accounts Preferences Action Items
-Additional Considerations

praveend$ ./macAudit.py -h
usage: macAudit.py [-h] [-v] [-n]

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  increase output verbosity
  -n, --nocolor  plain console output(default logging uses color)
praveend$




