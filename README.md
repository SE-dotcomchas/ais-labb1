Kurs 5 Labb 1
-----------
I denna labb så har vi som uppgift fått att sätta igång en miljö för att övervaka, Vi skulle då göra det och jag gjorde labben på ubuntu med wsl, Huvud uppgiften var då att sätta upp
och configurera Wazuh för att kunna övervaka och se hur ens maskin blir attackerad och även skriva regler


Här kan man se att min agent är igång och aktiv på mitt ubuntu system
----------

<img width="2532" height="534" alt="1b688680802a95b9c028fdff0bbab38a" src="https://github.com/user-attachments/assets/d179dbf1-4f9e-4408-9850-90cf79f6a7bc" />


5 Dokumenterade regler i wazuh
---------
Enligt uppgiften så skulle vi dokumentera 5 olika regler som fanns i wazuh, jag bestämde mig för att ta en närmare titt på olika wazuh regler
  
-  rule id="5700" level="0" noalert="1"> <decoded_as>sshd</decoded_as> <description>SSHD messages grouped.</description> </rule>   

Denna SSH regeln säger bara att en SSH händelse har hänt men det betyder inte att det är skadligt eller att den skapar något larm och att den skapar grupper för regler längre ner


- rule id="5701" level="8"> <if_sid>5700</if_sid> <match>Bad protocol version identification</match> <description>sshd: Possible attack on the ssh server (or version gathering).</description> <mitre> <id>T1190</id> </mitre>  

Detta är en klassisk regel för att kunna identifiera när någon eventuellt försöker scanna portar för att få information om hur sin infrastruktur är uppbyggd. Det är inte direkt skadligt men det är något som man inte ska ignorera för att folk försöker kartlägga systemet.

- rule id="5702" level="5"> <if_sid>5700</if_sid> <match>^reverse mapping</match> <regex>failed - POSSIBLE BREAK</regex> <description>sshd: Reverse lookup error (bad ISP or attack).</description>

Detta kan betyda både en miss konfiguration efter du har satt upp ett nytt system eller så kan det vara någon som försöker spoofa sig själv. Hur som helst så är det något man borde titta in i för att se vad som skapar varningen


- rule id="5703" level="10" frequency="6" timeframe="360"> <if_matched_sid>5702</if_matched_sid> <same_source_ip /> <description>sshd: Possible breakin attempt (high number of reverse lookup errors).</description> <mitre> <id>T1110</id> </mitre>

Denna regeln varnar för en brute force attack. Man bör reagera på det genom att ha ett program som automatisk blockerar användare efter ett visst antal försök för att göra det svårare att attackera tjänsten.

- rule id="5704" level="4"> <if_sid>5700</if_sid> <match>fatal: Timeout before authentication for</match> <description>sshd: Timeout while logging in.</description> </rule>

Denna regeln visar att det är  någon som som försöker logga in men som inte gör ett försök och blir automatiskt kickad av inaktivitet. Det kan bara vara allt från en arbetare som går iväg från datorn till ett script som skannat och söker information

