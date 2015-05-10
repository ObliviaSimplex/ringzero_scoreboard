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

def get_challenge_dict(uid):
    response = requests.get("http://ringzer0team.com/profile/" + str(uid))
    doc = response.text
    found = False
    challenge_points = {}
    splitdoc = doc.split('\n')
    for l in range(len(splitdoc)):
        line = splitdoc[l]
        # '\<a href=\"\/challenges\/.*'
        m = re.match(r'.*challenges.*', line)
        if m is not None:
            
            points = ("".join([c for c in splitdoc[l+3] if c in "0123456789"]))
            
            challenge_points[m.group(0)]=points
    return challenge_points
    
        
def main():
    print """<html>
  <body>
    <h3>Scoreboard</h3>
    <table>
      <tr><th>User</th><th>Points</th></tr>
    """
    challenge_points = {}
    challenge_pwners = {}
    for line in fileinput.input("userids.txt"):
        user = line.strip('\n').split(',')
        cpoints = get_challenge_dict(user[1])
        for c in cpoints:
            if c in challenge_pwners:
                challenge_pwners[c].append(user[0])
            else:
                challenge_pwners[c] = [user[0]]
        if len(cpoints) > 0:
            challenge_points.update(cpoints)
	anchor = "<a href=\"http://ringzer0team.com/profile/" + user[1] \
		+ "\">" + user[0] + "</a>"
        if user[1] != '':
            print "<tr><td>" + anchor + '</td><td>' + getscore(user[1]) + '</td></tr>'
        else:
            print "<tr><td>" + user[0] + '</td><td>unavailable</td></tr>'
    print "</table>"
    print "<h3>ALL CHALLENGES COMPLETED</h3>"
    print "<table>"
    print "<tr><td></td><td></td><td></td></tr>"
    grand_total=0
    for c in challenge_points:
        try:
            grand_total += int(challenge_points[c])
            pwnedby = ""
            for name in challenge_pwners[c]:
                pwnedby += name+" "
            print "<tr><td>"+c+"</td><td>"+challenge_points[c]+"</td><td>"+pwnedby+"</td></tr>"
        except:
            pass
        
    print "<tr><td>GRAND TOTAL</td><td>"+str(grand_total)+"</td></tr>"
    
    print """</table></body></html>"""

main()


    
