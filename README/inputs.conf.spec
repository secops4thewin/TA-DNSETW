* This stub spec file is here to quell warnings from btool in earlier releases.

[perfmon://*]
useEnglishOnly = [true|false]
* Controls which Windows perfmon API is used.
* If true, PdhAddEnglishCounter() is used to add the counter string.
* If false, PdhAddCounter() is used to add the counter string.
* Note: if set to true, object regular expression is disabled on
  non-English language hosts.
* Defaults to false.

[WinEventLog://*]
renderXml= [true|false]
* Controls if the Event data is returned as XML or plain text
* Defaults to false.