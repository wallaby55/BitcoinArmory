# This script generates an html include file of all of the contributors to the Armory project

from urllib import urlopen
import json

# Grab the json array of contributors
contribJson = urlopen('https://api.github.com/repos/goatpig/BitcoinArmory/contributors',).read()
contribArr = json.loads(contribJson)

# Html template
htmlPlate1 = '  <div>\n    <div><img src="' # Link to avatar
htmlPlate2 = '"alt="icon" /></div>\n    <div><a href="https://github.com/' # Username for link to name
htmlPlate3 = '">' # Name for name
htmlPlate4 = '</a></div>\n    <div>' # Number of contributions
htmlPlate5 = '</div>\n  </div>\n'
htmlHead = '<div class="contributors">\n'
htmlTail = '</div>'
finalHtml = htmlHead

# Build html for each user
for user in contribArr:
    finalHtml += htmlPlate1 + user['avatar_url'] + htmlPlate2 + user['login'] + htmlPlate3 + user['login'] + htmlPlate4 + str(user['contributions']) + htmlPlate5

# Close html div
finalHtml += htmlTail

# Write to _includes/contributors_list.html
contribFile = open("_includes/contributors_list.html", "w+")
contribFile.write(finalHtml)
contribFile.close()