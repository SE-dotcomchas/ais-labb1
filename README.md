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

FIM, File integrity monitoring system configurerat för att övervaka vissa känsliga filer
-----------
<img width="949" height="394" alt="2edc2b3db71c5b66bf48ffa771bd9380" src="https://github.com/user-attachments/assets/5ee3944c-861c-4468-9165-2bc4d885f330" />



3 Egna skrivna regler som är tillagda i local_rules.xml
------------
Rule 100001 Existerar för att detectera brute force attackar genom att den ränkar inloggs försök, Om det skulle uppstå med än 5 försök under 120 sekunder så triggas larmet då att det sker

Rule 100002 Varnar för ett lyckat login vid en brute force attack så om man ser den triggad måste man snabbt agera för att hålla sin information hemlig

Rule 100003 Denna regeln triggar oavsett var vid en SSH inloggning och att man måste manuellt kolla vart personen kommer ifrån


Anomalidetekteringsrapport + Dashboard
--------------------------


<img width="2538" height="836" alt="ddcec10f1e17e32ebae21c6147043ab6" src="https://github.com/user-attachments/assets/a29893d7-4196-4740-8341-d1aab64804b1" />

<img width="996" height="746" alt="600f51c06fc98e4c5ff191694a9ee718" src="https://github.com/user-attachments/assets/51cfa4e4-0e17-4bc2-ac70-47b65363a148" />

Här kan man attacken jag gjorde den 2 Maj, ovanför med hundratals detektioner tidigare dagar var när jag manuellt laddade test data på Wazuh för att kolla att själva dashboarden funkade. Man kan se totalt 200 händelser då den andra maj från en enda ip så då vet jag att det
var jag som endast skapade attacken. Bilden ovan visar hur dashboarden ser ut med testdata för att visa att den funkar helt

Wazuh Karta
---------------

<img width="829" height="830" alt="bc9cf3307179166aec1294124f037ab4" src="https://github.com/user-attachments/assets/15851c6c-da34-4344-9294-beab43635720" />

Reflektion
-------------
Efter jag har användigt Wazuh så har jag nu insett att det är en extremt kraftfult verktyg för att se och upptäcka hot, Innan i kurs 2 så använde vi suricata för att samla in loggar och ser alerts, Wazuh lyckas visa allting på ett mycket bättre och klarare sätt
så att man för en bättre bild över det hela, När man använde Suricata så var det bara en gigantisk text fil med larm medans i wazuh kan man filtrera datan för att visa tillexempel hur många misslyckade ssh försök händer dagligen, Dock programmet är stort och det krävs väldigt tid att configurera från nytt
och att sen ha kunskapen att kunna skapa alla nya regler och att sätta upp FIM på alla viktiga mappar med känslig information. 

Men när allt väl  är upsatt så är det ett extremt stark verkyg att ha tillgång till med tanke på att den kan se allt från filändringar, samlar in loggar från vad användare gör, massa med andra funktioner så är det ett av dom bästa verktygen att ha för att hitta hot i systemet eller att upptäcka när attacker händer
