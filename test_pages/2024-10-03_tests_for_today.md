# 2024-10-03 tests for today

1. push this page and then check if this new page shows up in All-Pages.
	 - RESULT: pushing this new page triggered a build.
		 - the build yielded two `git log` errors;
		 - it seems that the latest commits are not registered in the `git` records used by the build
		 - Re-deploying and forcing the cache to be cleared does sync things up
2. push this page and this [[2024-10-03 test number 2]]  
	- RESULT: ha, ha, no notes from this test are recorded
	- so, try again on 2024-10-04  
		- RESULT: well, the index was out of sync; forcing clear cache and deploy fixed that problem.
		- next is to see what happens with this one page update
			- RESULT: updating this one page seems to build without error and All-Pages and Recent-Pages seem to be accurate
			- what test next? create a new [[adhoc test page]]  and see what happens when that is committed. RESULT:  git index out of sync
			- what happens when this single page is pushed?  

#### 2025-04-24
- makin' it modern
