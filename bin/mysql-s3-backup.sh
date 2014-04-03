#!/bin/bash
# Shell script to backup MySql database

set -e

# CONFIG - Only edit the below lines to setup the script
# ===============================
 
MyUSER="backup"        # USERNAME
MyPASS="X2aVljzBeDDm"   # PASSWORD
MyHOST="localhost"      # Hostname
 
S3Bucket="mma-dexter-backups" # S3 Bucket
 
# Space-separated list of databases to backup
DBS="mma"
 
# DO NOT EDIT BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING
# ===============================
 
# Linux bin paths, change this if it can not be autodetected via which command
MYSQLDUMP="$(which mysqldump)"
GZIP="$(which gzip)"
 
# Backup Dest directory, change this if you have someother location
BACKUP_ROOT="$HOME/mysql-backups"
 
# Main directory where backup will be stored
DEST="$BACKUP_ROOT/mysql-$(date +"%Y-%m-%d")"
 
# Get hostname
HOST="$(hostname)"
 
# Get data in yyyy-mm-dd format
NOW="$(date +"%Y-%m-%d")"
 
# File to store current backup file
FILE=""
 
[ ! -d $DEST ] && mkdir -p $DEST || :
 
for db in $DBS
do
  FILE="$DEST/$db.$HOST.$NOW.gz"

  echo "Backing up $db to $FILE"

  # dump database to file and gzip
  date --rfc-3339=ns
  $MYSQLDUMP -u $MyUSER -h $MyHOST -p$MyPASS $db | $GZIP -9 > $FILE
  CODE=${PIPESTATUS[0]}
  date --rfc-3339=ns

  if [ $CODE -ne 0 ]; then
    echo "mysqldump failed"
    exit 1
  fi

  echo "Dump complete"

  ls -l $FILE
done
 
# copy mysql backup directory to S3
echo "Syncing with S3"
s3cmd sync -rv --skip-existing $DEST s3://$S3Bucket/

echo "Finished. Bye."
