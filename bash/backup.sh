#!/usr/bin/bash

ARCHIVE=$(date +%Y-%m-%d)_backup.tar.gz

echo "[+] Syncing OneDrive"
onedrive --synchronize
echo 
echo "Backing up files"
echo "----------------------------------------"
echo "[+] Creating backup folder"
mkdir ~/backup

echo "[+] Backing up dot files"
cp ~/.nanorc ~/backup/nanorc
cp ~/.bashrc ~/backup/bashrc

echo "[+] Backing up Templates"
cp -r ~/Templates ~/backup/Templates

echo "[+] Backing up GPG data"
cp -r ~/.gnupg ~/backup/gnupg

echo "[+] Backing up SSH data"
cp -r ~/.ssh ~/backup/ssh

cp ~/backup.sh ~/backup/backup.sh
echo 
echo "Cleaning up"
echo "----------------------------------------"
echo "[+] Creating archive" $ARCHIVE
tar czf $ARCHIVE backup

echo "[+] Removing ~/backup folder"
rm -rf ~/backup
