#!/bin/bash

$HOME/mma-dexter/bin/mysql-s3-backup.sh >> $HOME/mma-dexter/log/backups.log 2>&1
