#!/bin/bash

# Exit script on a failed command 
set -e

# Install required packages
sudo apt install \
    bluez-tools \
    git \
    libudev-dev \
    libevdev-dev \
    python3-venv \
    python3-pip \
    cmake -y

# Load required kernel modules 
sudo modprobe uinput hid_nintendo i2c-dev
# Then add them to startup
sudo sh -c "cat >>/etc/modules" <<-EOF
    i2c-dev
    uinput
    hid_nintendo
EOF

# Make a directory for 
mkdir ~/git
cd ~/git

# Add joycond support
git clone https://github.com/DanielOgorchock/joycond.git
cd joycond
cmake .
sudo make install
sudo systemctl enable --now joycond

# change back to parent directory "git"
cd ..

# Install unit_bot
git clone https://github.com/esp323277/unit_bot.git
cd unit_bot
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
deactivate

# Reboot
echo "System will reboot in 5 seconds. Press CTRL-C to cancel"
sleep 10; sudo reboot
