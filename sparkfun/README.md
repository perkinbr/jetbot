Files for sparkfun jetbot

The shutdown script is modified from the raasberry pi one.
It's experimental, and it may or may not cause random shutdowns due to problems with the pull up.

TO use it, but pHat.service in /etc/systemd/system/ and shutdownd.py in /usr/local/bin
You can use 

$ systemctl start pHat

to start it and

$ systemctl enable pHat

to enable it on reboot
