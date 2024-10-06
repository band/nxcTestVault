# adhoc test page

**Netlify build test page**
ASSERT: once committed and pushed to the repo this page will be at the top of the Recent-Pages and All-Pages pages.  
RESULT: git log for page is empty  
WhatIsHappening (WIH): git index in the cache does not have this file  

Test: push a page that does exist; does the log return the latest commit info?  
RESULT: no, it returns the previous commit info  

Test: push this adhoc page, which is not in the index  
ASSERT: the git log try for this file will yield an error message  
RESULT: the ASSERT is correct  

Test: add remove cache directory after build:  
	DONE: this page still returns an empty git log message  
Next test: add new text to this page and then commit and push it  
ASSERT: cache will be clear and this page will show up as the latest
Recent-Pages and All-Pages entry  
RESULT: cache is not cleared, so, now what?  

2024-10-06:  
Test: make sure log error repeats  






