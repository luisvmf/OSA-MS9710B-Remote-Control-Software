g++ -m32 -o OSA main.cpp
cd runtime
#download the runtime
wget "https://github.com/luisvmf/Electron-clone/releases/download/1.0.0/electron-l32.zip"
#-----------------------------------------------------------
unzip electron-l32.zip
rm electron-l32.zip
cd ..
echo 'build complete!'
chmod u+rwx create-shortcut.sh
chmod u+rwx OSA
./create-shortcut.sh
