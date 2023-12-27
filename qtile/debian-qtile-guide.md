# Qtile

To install qtile:
https://github.com/qtile/qtile/discussions/4542

- create base folders: xdg-user-dirs-update
- install qtile with pipx
  - sudo apt install pipx xserver-xorg-core xserver-xorg-input-libinput xinit mate-terminal light
  #### Note to self: mate-terminal pulls in the necessary cairo and pango packages)
  - to probe qtile create .xinitrc on ./ and write: exec qtile start
  - later use startx on terminal after reboot system
- copy qtile bin file of ~/.config/qtile/config.py on /bin/
- config qtile.desktop file on /usr/share/xsessions/ follow qtile documentation
_______________

### Audio config with PulseAudio
- sudo apt install pulseaudio*
- sudo apt install pavucontrol
pavucontrol is to have a GUI of pulseaudio

### WIFI Connection configure
To manage wifi it's necessary install debian with Ethernet adapter:
- sudo apt install network-manager
- sudo systemctl start NetworkManager.service
- sudo systemctl status N.....

### Bluetooth connection configure
To review bluetooth config use:
- sudo systemctl status bluetooth.service
Now with bluetoothctl use that

### System try utils
- bluetooth: blueman-applet, requires blueman
- pasystry(allow manage  pulseaudio): requires pulseaudio
- nm-tray(manage NetworkManager): requires nmcli

### Rest of utilities
- Thunar: file explorer
To install Thunar we need to install and configure lxappearance qt5ct and qt5-style-plugins, dont modifi anything wuth qt5ct only do changes with lxappearance, or maybe could be bugs or problems
  - sudo apt install lxappearance
  - sudo apt install qt5ct
  - sudo apt install qt5-style-plugin

  We need to configure path variable to use qt5ct:
  - https://unix.stackexchange.com/questions/680483/how-to-add-qt-qpa-platformtheme-qt5ct-environment-variable-in-arch-linux
  Now we can download gkt themes from gnom-lock and we can install icons and themes on: ~/.icons ~/.themes:
  - https://youtu.be/qU6iDx4xB5o?si=G2sdLgcu1UwdAQMs

### Disable keyboard
How to disable latop keyboard:
- install xinput: sudo apt install xinput
- xinput: list devices
- xinput float id
- xinput reattach id master

### Config brightness with terminal
- sudo apt install brightnessctl
- brightnessctl
- brightnessctl -d "intel_backlight" set 50%
https://www.baeldung.com/linux/monitor-brightness-change#:~:text=Using%20brightnessctl,smooth%20transitions%20between%20brightness%20levels
