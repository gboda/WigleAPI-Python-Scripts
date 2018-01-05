# WigleAPI-Python-Scripts
* Dependencies:
  * CPython 3.6
  * requests library

* Prereqs:
  * Replace <secret key> in the Authorization Header with the Base64 encoded Wigle API token.
  
 * wigle-userinfo.py - connects to the Wigle API and prints:
	 * user data (profile, API auth)
	 * rank (overall and monthly)
	 * number of discovered Wifi and GSM/EDGE/UMTS/4G cells
	 
* wigle-net_count_per_cc.py connects to the Wigle API, requests two digit country code ('IE' for Ireland etc..) and prints:
	* total number of discovered Wifi networks and GSM/EDGE/UMTS/4G cells
