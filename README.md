# OSA MS9710B Remote Control Software
![alt tag](https://img.shields.io/badge/build-passing-brightgreen.svg)

# ***This is no longer mantained, suport for OSA MS9710 will be eventualy added to spectraread***
***This software depends on many old system libraries and will not run on newer systems***

Program to remotely control Optical Spectrum Analyser MS9710B connected with RS232C port

Requires Linux with g++, python, pyserial (included by default on most Linux distributions), pygtk (included by default on most Linux distributions), wget , unzip and git installed.

****Instructions to install:****

***************
IMPORTANT:

****DON'T CONNECT OR DISCONNECT THE USB TO SERIAL CONVERTER WITH THE OSA TURNED ON.****
***************

We are going to use an USB to RS232C converter with OSA, so create a file in /etc/udev/rules.d with the name 99-usb-serial.rules with the folowing code:

        SUBSYSTEM=="tty", ATTRS{idVendor}=="????", ATTRS{idProduct}=="????", ATTRS{serial}=="????", SYMLINK+="osaUSB"

Replace the "????" with the required information. idVendor and idProduct can be found with lsusb command (the numbers after ID are idVendor:idProduct). To find the serial number run the folowing command (replace /dev/ttyUSB1 to the file that appears in /dev on your system):

        udevadm info -a -n /dev/ttyUSB1 | grep '{serial}' | head -n1;

If the serial number returned is blank remove 

        , ATTRS{serial}=="????"
        
from the above code.


Go to final install folder (for example /usr) and run:

      sudo mkdir OSA
      cd OSA
      sudo git clone https://github.com/luisvmf/OSA-MS9710B-Remote-Control-Software
      cd OSA-MS9710B-Remote-Control-Software
      sudo chmod u+rwx build-linux-32.sh
      sudo chmod u+rwx build-linux-64.sh
      sudo ./build-linux-64.sh ****(if your system is 32bit run sudo ./build-linux-32.sh instead)****.
      cd ..
      sudo chmod --recursive ugo+rx OSA-MS9710B-Remote-Control-Software/*
      sudo chmod --recursive ugo+rx OSA-MS9710B-Remote-Control-Software
      cd ..
      sudo chmod ugo+rx OSA




The desktop file (named OSA.desktop) to run the program is in OSA/OSA-MS9710B-Remote-Control-Software/.

------
KNOWN PROBLEMS:

1)SWEEP AVERAGE MUST BE DISABLED ON OSA.

2)SCALE FOR GRAPH IN OSA SCREEN IS ALWAYS SET AT 1.

------

Program main screen:
![alt tag](https://raw.githubusercontent.com/luisvmf/OSA-MS9710B-Remote-Control-Software/master/screenshots/screenshot.png)

Program main screen running on system with dark theme:
![alt tag](https://raw.githubusercontent.com/luisvmf/OSA-MS9710B-Remote-Control-Software/master/screenshots/system_with_dark_theme.png)

Program main screen with linear scale option selected:
![alt tag](https://raw.githubusercontent.com/luisvmf/OSA-MS9710B-Remote-Control-Software/master/screenshots/lin_scale.png)

Program main screen with LOG scale option selected:
![alt tag](https://raw.githubusercontent.com/luisvmf/OSA-MS9710B-Remote-Control-Software/master/screenshots/LOG_scale.png)

Program main screen during data acquisition:
![alt tag](https://raw.githubusercontent.com/luisvmf/OSA-MS9710B-Remote-Control-Software/master/screenshots/Data_download_progress_bar.png)

