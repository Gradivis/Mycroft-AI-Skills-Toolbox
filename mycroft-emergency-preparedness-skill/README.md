# Emergency Preparedness & Action Skill for Mycroft

### A selection of pre-built emergency instructions to help with disaster action & preparadness. 
This is mainly just proof-of-concept as incentive for me to properly learn Python, however as things stand it currently does work and I am actively adding things as I go. The usage section will be updated as further commands/responses are added.

For clarification, I am dividing "emergeny information" and "emergency preparedness" into two different sections. The *emergency information* command provides general information on what should be done in case of the emergencies listed. The *emergency preparedness* command will contain general information on what can be done to prepare for each emergency in advance. 

I've included a roadmap that lays out how I intend on expanding the skill (provided I can learn Python well enough), including interaction with sensors and other IoT devices. Right now this skill is purely informational.

Information was pulled from the US and CA Dept. of Public Safety websites, and should not be considered complete by any means as an effort was made to make them concise.

*Why not write a skill that queries this information from online sources?*
While this information could certainly be scraped from online sources, I didn't want to use a GET command due to the fact that inclement weather or server-side issues could interfere with retrieval of the data. For me personally at least, I would feel more comfortable knowing that vital emergency information was stored locally. 

## Usage:

**Emergency Information**
* "Mycroft, how should I respond to a [tornado/nuclear event/wildfire]?"
* "Mycroft, what should I do in case of a [tornado/nuclear event/wildfire]?"
* "Mycroft, what should I do if there is a [tornado/nuclear event/wildfire]?"

## Roadmap:
For now, this is simply proof of concept and only provides useful information for use in the future. As it stands, it could be a useful tool for disaster preparation/general knowledge, but I believe it could be significantly improved to take advantage of Mycroft's abilities, as well as integration with other devices and services. 

**PHASE I - Current**
* Add dialogue for emergency information [x]
* Test locally with Mycroft to make sure it works [x]
* Add dialogue for hurricane information [ ]
* Add dialogue for poisoning information [ ]
* Add dialogue for emergency preparedness - all events (e.g. "How do you prepare for...") [ ]
* Add dialogue for how to build an emergency kit [ ]


**PHASE II**
* The primary goal of Phase II would be to offer immediate and concise instructions in response to user prompt.
* Another goal would be to provide emergency numbers based upon the users location.
* Example Utterance 1: "*Mycroft, there is a tornado coming.*" 
* Example Dialogue 1: "*I understand. Here are some actions you should take immediately.*"
* Example Utterance 2: "*Mycroft, what is the number for poison control?*"
* Exampled Dialogue 2: "*Emergency Poison Control in the U.S. is 1-800-222-1222.*"

**PHASE III:**
* This is where things get interesting. I would like Mycroft to provide warnings and information **unprompted** by user.
* Integration with local emergency alerts - Mycroft warns of confirmed events and gives possible actions to take.
* Integration with an RPi weather station & geiger counter.
* Integration with in-home sensors (e.g. Carbon Monoxide warning, smoke detection).
* Integration with smart home/IoT; visual alerts via smart lamps for the hearing-impaired.
* Support for push notifications to mobile/smart devices.
* Support for Mycroft to ask whether he should call the emergency numbers user has requested.


### Possible Challenges:
There are a few challenges that I can see arising, other than the code itself (being new to Python). The first is to ensure that there is a broad enough range of utterances to account for the reduced thinking capacity due to adrenaline and and time-sensitivity during moments of crisis. These most be programmed without interference with other keywords/skills, because the last thing you want is for Mycroft to start pulling up Wikipedia definitions or something during an emergency. Additionally, a great amount of care will have to be taken on the content of the information/dialogue returned, as life-saving/emergency devices will always face a much higher level of scrutiny (and rightly so). Finally, I am unaware of whether an increase in the utterance/dialogue database incurrs an increase in response time, and latency must be reduced to an absolute minimum.

