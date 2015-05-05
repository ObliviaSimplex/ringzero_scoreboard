# Generate an HTML page for the scoreboard by querying
# user profiles.

import requests
import re
import fileinput

def getscore(uid):
    response = requests.get("http://ringzer0team.com/profile/" + str(uid))
    doc = response.text
    found = False
    for line in doc.split('\n'):
        m = re.match(r'.*Points.*<span class="points">(\d+)</span></td>.*', line)
        if m is not None:
            return m.group(1)

def main():
    print """<html>
  <body>
    <h3>Scoreboard</h3>
    <table>
      <tr><th>User</th><th>Points</th></tr>
"""
    for line in fileinput.input("userids.txt"):
        user = line.strip('\n').split(',')
        if user[1] != '':
            print "<tr><td>" + user[0] + '</td><td>' + getscore(user[1]) + '</td></tr>'
        else:
            print "<tr><td>" + user[0] + '</td><td>unavailable</td></tr>'
    print """</table></body></html>"""

main()


    
