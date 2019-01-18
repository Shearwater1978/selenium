#!/bin/bash

file_name="./dodo_arch/dodo_"$(date +%d-%m-%y_%H%M)".zip"
echo $file_name
find ./dodo_body/ -mmin +30 -name '*.html' -exec zip -q -9 ./dodo_arch/dodo_"$(date +%d-%m-%y_%H%M)".zip {} \;

archive_state=$(unzip -q -t "$file_name" | awk '{print $1,$2,$3}')
echo $archive_state
if [ "$archive_state" = "No errors detected" ]
   then
       echo 'Zip archive ok'
       echo 'Source file(-s) must be remove'
       find ./dodo_body/ -mmin +30 -name '*.html' -delete
   else
       echo 'Zip archive not`ok'
       echo 'Source file(-s) not removed'
fi
