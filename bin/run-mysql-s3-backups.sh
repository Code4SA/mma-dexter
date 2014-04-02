#!/bin/bash

$HOME/mma-dexter/bin/mysql-s3-backups.sh 2>&1 >> $HOME/mma-dexter/log/backups.log
