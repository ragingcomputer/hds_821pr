# HDS-821PR Serial Commands - HEX Values

HDMI 2x1 Multi-Viewer Switch Seamless Switcher w/ PIP Function Support HDMI 1.3a Full HD 1080P IR Remote Control Scaler UP/Down 4 Picture Mode 2 Input 1 Output RS232 Cable Included


###RS-232 Connection Settings
```
Baudrate：115200
Data width：8bit
Parity: none
Stop: 1bit
```


## Overview

All commands are 13 bytes in length. The final byte is a checksum of the first 12 bytes.

Example for select input port:  **checksum** = ```0x100``` – ( ```0xa5``` + ```0x5b``` + ```0x02``` + ```0x03``` + **port** + ```0x00``` + ```0x01``` + ```0x00``` + 
```0x00``` + ```0x00``` + ```0x00``` + ```0x00``` )

###Available Functions
[Input](#input)  
[Resolution](#resolution)    
[Mode](#mode)  
[Pip Position](#pip-position)  
[PiP Size](#pip-size)  
[PiP Border](#pip-border)  
[Factory Reset](#factory-reset)


## Input
### Set Input
Sets the input as the primary output.

|1|2|3|4|5|6|7|8|9|10|11|12|13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ```0xa5``` | ```0x5b``` | ```0x02``` | ```0x03``` | **port** (1,2) | ```0x00``` | ```0x01``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | **checksum** |

Change only input **port** & **checksum**

For convenience, complete command and checksums are listed

| Description | Command
| --- | --- |
| Input Port 1 | A5 5B 02 03 **01** 00 01 00 00 00 00 00 F9
| Input Port 2 | A5 5B 02 03 **02** 00 01 00 00 00 00 00 F8

### Query Input

Gets the number of the input actively displayed.

##### Command
| Description | Command
| --- | --- |
| Query Input  | A5 5B 02 01 01 00 00 00 00 00 00 00 FC

##### Response

Port will be 1 or 2

|1|2|3|4|5|6|7|8|9|10|11|12|13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ```0xa5``` | ```0x5b``` | ```0x02``` | ```0x01``` | ```0x01``` | ```0x00``` | **port** | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | **checksum** |


## Resolution
### Set Output Resolution
Sets the video resolution to send on the output.

|1|2|3|4|5|6|7|8|9|10|11|12|13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ```0xA5``` | ```0x5B``` | ```0x08``` | ```0x06``` | **resolution** (0-4) | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | **checksum** |
Change only **resolution** & **checksum**

For convenience, complete command and checksums are listed

|  Value | Description | Command
| --- | --- | --- |
|00| 1080p | A5 5B 08 06 **00** 00 00 00 00 00 00 00 F2
|01| 720p | A5 5B 08 06 **01** 00 00 00 00 00 00 00 F1
|02| 1080i | A5 5B 08 06 **02** 00 00 00 00 00 00 00 F0
|03| 1024x768 | A5 5B 08 06 **03** 00 00 00 00 00 00 00 EF
|04| 1360x768 | A5 5B 08 06 **04** 00 00 00 00 00 00 00 EE

### Query Output Resolution

##### Command
| Description | Command
| --- | --- |
| Query Resolution  | A5 5B 09 06 00 00 00 00 00 00 00 00 F1

##### Response

Response will be a value 0 through 4, corresponding to the current output resolution

|1|2|3|4|5|6|7|8|9|10|11|12|13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ```0xA5``` | ```0x5B``` | ```0x09``` | ```0x06``` | **resolution** (0-4) | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | **checksum** |

| Value | Resolution |
|---|---|
|00|1080P|
|01|720P|
|02|1080I|
|03|1024X768|
|04|1360X768|


## Mode
### Set Mode
Sets the video display mode.

|1|2|3|4|5|6|7|8|9|10|11|12|13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ```0xA5``` | ```0x5B``` | ```0x19``` | ```0x01``` | **mode** (1-4) | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | **mode** (1-4) | ```0x00``` | **checksum** |
Change only display **mode** & **checksum**

For convenience, complete command and checksums are listed

| Mode | Visual | Description | Command
| --- | --- | --- | --- |
|01| ![Single Source](images/mode_single_source.png "Single Source") | Single Source | A5 5B 19 01 **01** 00 00 00 00 00 **01** 00 E4
|02| ![Picture in Picture](images/mode_pip.png "Picture In Picture") | PIP | A5 5B 19 01 **02** 00 00 00 00 00 **02** 00 E2
|03| ![Side by Side Full](images/mode_side-by-side_full.png "Side-by-Side Full") | Side-by-Side (FULL) | A5 5B 19 01 **03** 00 00 00 00 00 **03** 00 E0
|04| ![Side by Side 16:9](images/mode_side-by-side_16x9.png "Side-by-Side 16:9") | Side-by-Side (16:9) | A5 5B 19 01 **04** 00 00 00 00 00 **04** 00 DE

### Query Mode

##### Command

| Description | Command
| --- | --- |
| Query MODE  | A5 5B 19 02 00 00 00 00 00 00 00 00 E5

##### Response

Response will be a value 1 through 4, corresponding to the current output resolution

|1|2|3|4|5|6|7|8|9|10|11|12|13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ```0xA5``` | ```0x5B``` | ```0x19``` | ```0x02``` | **mode** (1-4) | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | **checksum** |

| Value | Mode |
|---|---|
|01|Single Source|
|02|PIP|
|03|Side-by-Side (FULL)|
|04|Side-by-Side (16:9)|


## Pip Position
### Set PiP Position
|1|2|3|4|5|6|7|8|9|10|11|12|13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ```0xA5``` | ```0x5B``` | ```0x19``` | ```0x03``` | **position** (1-4) | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | **position** (1-4) | ```0x00``` | **checksum** |

Change only **position** & **checksum**

For convenience, complete command and checksums are listed

| Position | Visual | Description | Command
| --- | --- | --- | --- |
| 01 | ![Top Left](images/pip_position_top_left.png "Top Left") | Top Left | A5 5B 19 03 **01** 00 00 00 00 00 **01** 00 E2
| 02 | ![Top Right](images/pip_position_top_right.png "Top Right") | Top Right | A5 5B 19 03 **02** 00 00 00 00 00 **02** 00 E0
| 03 | ![Bottom Left](images/pip_position_bottom_left.png "Bottom Left") | Bottom Left | A5 5B 19 03 **03** 00 00 00 00 00 **03** 00 DE
| 04 | ![Bottom Right](images/pip_position_bottom_right.png "Bottom Right") | Bottom Right | A5 5B 19 03 **04** 00 00 00 00 00 **04** 00 DC

### Query PiP Position

##### Command

| Description | Command
| --- | --- |
| Query Position  | A5 5B 19 04 00 00 00 00 00 00 00 00 E3

##### Response

Response will be a value 1 through 4, corresponding to the current output resolution

|1|2|3|4|5|6|7|8|9|10|11|12|13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ```0xA5``` | ```0x5B``` | ```0x19``` | ```0x04``` | **position** (1-4) | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | **checksum** |

| Value | Mode |
|---|---|
| 01 | Top Left|
| 02 | Top Right|
| 03 | Bottom Left |
| 04 | Bottom Right |


## PiP Size
### Set PiP Size

|1|2|3|4|5|6|7|8|9|10|11|12|13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ```0xA5``` | ```0x5B``` | ```0x19``` | ```0x05``` | **size** (1-3) | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | **size** (1-3) | ```0x00``` | **checksum** |

Change only **size** & **checksum**

For convenience, complete command and checksums are listed

| Description | Command
| --- | --- |
| Small  | A5 5B 19 05 **01** 00 00 00 00 00 **01** 00 E0
| Medium | A5 5B 19 05 **02** 00 00 00 00 00 **02** 00 DE
| Large  | A5 5B 19 05 **03** 00 00 00 00 00 **03** 00 DC

### Query PiP Size

##### Command

| Description | Command
| --- | --- |
| Query Size  | A5 5B 19 06 00 00 00 00 00 00 00 00 E1

##### Response

Response will be a value 1 through 3, corresponding to the current output resolution

|1|2|3|4|5|6|7|8|9|10|11|12|13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ```0xA5``` | ```0x5B``` | ```0x19``` | ```0x04``` | **size** (1-4) | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | **checksum** |

| Value | Mode |
|---|---|
| 01 | Small |
| 02 | Medium |
| 03 | Large |


## PiP Border
### Set PiP Border

|1|2|3|4|5|6|7|8|9|10|11|12|13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ```0xA5``` | ```0x5B``` | ```0x0C``` | ```0x01``` | **border** (0F/F0) | ```0x00``` | **border** (0F/F0) | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | ```0x00``` | **checksum** |

Change only **border** & **checksum**

For convenience, complete command and checksums are listed

| Description | Command
| --- | --- |
| Show Border | A5 5B 0C 01 **0F** 00 **0F** 00 00 00 00 00 D5
| Hide Border | A5 5B 0C 01 **F0** 00 **F0** 00 00 00 00 00 13




## Factory Reset
| Description | Command
| --- | --- |
| Reset | A5 5B 08 0A 00 00 00 00 00 00 00 00 EE


## Query States
| Description | Command
| --- | --- |
| Query Input  | A5 5B 02 01 01 00 00 00 00 00 00 00 FC
| Query Resolution  | A5 5B 09 06 00 00 00 00 00 00 00 00 F1
| Query MODE  | A5 5B 19 02 00 00 00 00 00 00 00 00 E5
| Query PIP Position  | A5 5B 19 04 00 00 00 00 00 00 00 00 E3
| Query Size  | A5 5B 19 06 00 00 00 00 00 00 00 00 E1
| Query Border | A5 5B 0C 03 00 00 00 00 00 00 00 00 F1