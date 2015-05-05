#/bin/bash

# Queries the messages page to get the user ids from the user names.
# input: users.txt a list of user names to query
# output: userids.txt a csv file with user names and uids

cat users.txt | while read x; do printf "$x",; grep ">$x<" ringer.txt | perl -n -e'/.*value..(\d+).*/ && print $1'; echo; done > userids.txt
