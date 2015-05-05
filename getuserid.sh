#/bin/bash
cat users.txt | while read x; do printf "$x",; grep ">$x<" index.html | perl -n -e'/.*value..(\d+).*/ && print $1'; echo; done > userids.txt
