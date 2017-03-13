# OSA-MS9710B-Remote-Control-Software
Program to remote control Optical Spectrum Analyser MS9710B connected with RS232C port

Requires linux with g++, python, pyserial and git installed.

Instructions to install:

If you are going to use an USB to RS232C converter with OSA create a file in /etc/udev/rules.d with the name 99-usb-serial.rules with the folowing code:

        SUBSYSTEM=="tty", ATTRS{idVendor}=="????", ATTRS{idProduct}=="????", ATTRS{serial}=="????", SYMLINK+="osaUSB"

Replace the "????" with the required information. idVendor and idProduct can be found with lsusb command (the numbers after ID are idVendor:idProduct). To find the serial number run the folowing command (replace /dev/ttyUSB1 to the file that appears in /dev on your system):

        udevadm info -a -n /dev/ttyUSB1 | grep '{serial}' | head -n1;

If the serial number returned is blank remove 

        , ATTRS{serial}=="????"
        
from the code above.

Go to final install folder (for example /usr) and run:

      sudo mkdir OSA
      cd OSA
      sudo git clone https://github.com/luisvmf/OSA-MS9710B-Remote-Control-Software
      cd OSA-MS9710B-Remote-Control-Software
      sudo chmod u+rwx build-linux-32.sh
      sudo chmod u+rwx build-linux-64.sh
      sudo ./build-linux-64.sh (if your system is 32bit run sudo ./build-linux-32.sh instead).
      cd ..
      sudo chmod --recursive ugo+rx OSA-MS9710B-Remote-Control-Software/*
      sudo chmod --recursive ugo+rx OSA-MS9710B-Remote-Control-Software
      cd ..
      sudo chmod ugo+rx OSA


The desktop file (named OSA.desktop) to run the program is in OSA/OSA-MS9710B-Remote-Control-Software/.

![alt tag](https://raw.githubusercontent.com/luisvmf/OSA-MS9710B-Remote-Control-Software/master/Screenshot.png)
