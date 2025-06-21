#!/bin/bash

SPARK_WORKLOAD=$1

echo "SPARK_WORKLOAD: $SPARK_WORKLOAD"

if [ "$SPARK_WORKLOAD" == "master" ];
then
  $SPARK_HOME/sbin/start-master.sh -p 7077
elif [ "$SPARK_WORKLOAD" == "worker" ];
then
  $SPARK_HOME/sbin/start-worker.sh spark://spark-master:7077
elif [ "$SPARK_WORKLOAD" == "history" ]
then
  $SPARK_HOME/sbin/start-history-server.sh
fi


ZIP_FILE="/opt/spark/work-dir/gfg_technical_challenge/data/zip_data/test_data.zip"
EXTRACT_DIR="/opt/spark/work-dir/gfg_technical_challenge/data/unzip_data/"
TARGET_FILE="data.json"
PASS_PHRASE="welcometotheiconic"

if [ ! -f "$EXTRACT_DIR/$TARGET_FILE" ]; then
  echo "Extracting $ZIP_FILE to $EXTRACT_DIR..."
  python3 - <<EOF
import pyzipper
import hashlib
import os

zip_path = "$ZIP_FILE"
extract_dir = "$EXTRACT_DIR"
passphrase = "$PASS_PHRASE"
target_file = "$TARGET_FILE"

os.makedirs(extract_dir, exist_ok=True)
m = hashlib.sha256()
m.update(passphrase.encode('utf-8'))
hashed = m.hexdigest()

with pyzipper.AESZipFile(zip_path, 'r') as zf:
    zf.pwd = hashed.encode('utf-8')
    zf.extract(target_file, path=extract_dir)

print(f"Extraction complete: {target_file}")
EOF
else
  echo "Already extracted: $EXTRACT_DIR/$TARGET_FILE"
fi