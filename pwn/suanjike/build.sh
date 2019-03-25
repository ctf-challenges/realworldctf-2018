#!/bin/bash -e

# cloud-init is too hard, we poor man curl | sudo bash -

# Our time machine is not perfect :p
systemctl stop systemd-timesyncd
systemctl disable systemd-timesyncd

apt update
apt --yes install docker.io openssh-server
docker pull debian

useradd -G docker -m -s /home/container/run.sh container

cat > /home/container/run.sh <<EOT
#!/bin/bash
docker run -it -m 128m debian # You are here!
EOT
chmod +x /home/container/run.sh

mkdir -p /home/container/.ssh
cat > /home/container/.ssh/authorized_keys <<EOT
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDl0HKNu/NgGHee+tEL0EU+3suDB2rMIstuhIB9IRJzo
EOT
chmod 0600 /home/container/.ssh/*
chmod 0700 /home/container/.ssh
chown -R container:container /home/container/.ssh

echo 'FLAG_SHOULD_BE_HERE' > /root/flag
chmod 000 /root/flag # lol yes
