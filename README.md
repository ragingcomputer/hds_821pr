# hds_821pr
Sometimes you get lucky. Sometimes you find a generic (cheap) device that does what you need. Sometimes it even has a manual... and sometimes you have to run a sketchy control program and sniff communications.

The unit I purchased has the following title on Amazon: 
TNP HDMI 2x1 Multi-Viewer Switch Seamless Switcher w/ PIP Function Support HDMI 1.3a Full HD 1080P IR Remote Control Scaler UP/Down 4 Picture Mode 2 Input 1 Output RS232 Cable Included

It's hard to tell you where exactly to get your own. [youting-hd](http://www.youting-hd.com/en/productshow.asp?id=253&sid=311&tid=311) seems to have the most pictures referenced. The control programs I've found all reference [HDS-821PR](http://www.hdcvt.com/index.php/product/des?id=142) so this package continues that trend.

Import the package

```python
import hds_821pr
```

There are 2 ways to control this device, so I wrote both ways into this package. See the documentation for HDS-821PR Serial Commands - [HEX Values](docs/hex_commands.md) - [ASCII](docs/ascii_commands.md).  To instantiate, pass in a string containing the name of the serial device.

```python
pip = hds_821pr.Hex('COM4')
```

```python
pip = hds_821pr.Ascii('/dev/ttyS0')
```

### Functions and valid inputs:

To make things easier, I added some constants, or you can use the values directly.

```set_port()```  
hds-821pr.ports.port_1 = '1'  
hds-821pr.ports.port_2 = '2'  

```set_mode()```  
hds-821pr.modes.single = 'single'  
hds-821pr.modes.pip = 'pip'  
hds-821pr.modes.side_full = 'side_full'  
hds-821pr.modes.side_scale = 'side_scale'  

```set_pip_size()```  
hds-821pr.pip_sizes.small = 'small'  
hds-821pr.pip_sizes.medium = 'medium'  
hds-821pr.pip_sizes.large = 'large'  

```set_pip_position()```  
hds-821pr.pip_positions.top_left = 'top_left'  
hds-821pr.pip_positions.top_right = 'top_right'  
hds-821pr.pip_positions.bottom_left = 'bottom_left'  
hds-821pr.pip_positions.bottom_right = 'bottom_right'  

```set_pip_border()```  
hds-821pr.pip_borders.show = 'show'  
hds-821pr.pip_borders.hide = 'hide'  

```set_resolution()```  
hds-821pr.resolutions.res_1080p = '1080p'  
hds-821pr.resolutions.res_720p = '720p'  
hds-821pr.resolutions.res_1080i = '1080i'  
hds-821pr.resolutions.res_1024x768 = '1024x768'  
hds-821pr.resolutions.res_1360x768 = '1360x768'  

### Example

```python
import hds_821pr
import logging

logging.basicConfig(level=logging.DEBUG)

pip = hds_821pr.Hex('COM4')

pip.reset()
pip.set_port(hds_821pr.ports.port_1)
pip.set_pip_size(hds_821pr.pip_sizes.large)
pip.set_pip_position(hds_821pr.pip_positions.top_right)
pip.set_pip_border(hds_821pr.pip_borders.hide)
pip.set_mode(hds_821pr.modes.pip)

print(pip.get_resolution())
print(pip.get_port())
print(pip.get_mode())
print(pip.get_pip_position())
print(pip.get_pip_size())
print(pip.get_pip_border())
```

asdf