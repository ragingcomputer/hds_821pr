# HDS-821PR Serial Commands - ASCII

###RS-232 Connection Settings
```
Baudrate：115200
Data width：8bit
Parity: none
Stop: 1bit
```

### Overview
All commands end with exclamation point (!).  All text is ASCII and is not case sensitive. 
?VERSION is the only command for directly querying device.
Other commands will return a status after executing the command. 
Some status is returned unrequested

| COMMAND | ACTION | RETURNS |
| --- | --- | --- |
| T1! | Change resolution to 1080p | Resolution: 1080p/60 |
| T2! | Change resolution to 720p | Resolution: 720p/60 |
| T3! | Change resolution to 1080i | Resolution: 1080i/60 |
| T4! | Change resolution to 1360x768 | Resolution: 1024x768/60 |
| T5! | Change resolution to 1024x768 | Resolution: 1360x768/60 |
| IN1! | Select input 1 | Input 1 select |
| IN2! | Select input 2 | Input 2 select |
| ONEINPUT! | Select mode QUAD | Mode: QUAD |
| PIP! | Select mode PIP | Mode: PIP |
| SIDEBYSIDE1! | Select mode POP1 | Mode: POP1 |
| SIDEBYSIDE2! | Select mode POP2 | Mode: POP2 |
| ?VERSION! | Check software version | V 1.7 |
| RESET! | Factory Reset | Factory Reset |
| POWERON! | System power on | PowerON |
| POWEROFF! | System power off | PowerOFF |

### Errata

For some reason, the input status returned by the device is opposite for RxON (port active), format (resolution). 
This does not apply to Select status.