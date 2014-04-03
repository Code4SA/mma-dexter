#!/bin/bash

. $HOME/.bashrc
export PATH=$PATH:/opt/mysql/server-5.6/bin

$HOME/mma-dexter/bin/mysql-s3-backup.sh >> $HOME/mma-dexter/log/backups.log 2>&1
