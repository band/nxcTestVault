# 2024-10-03 tests for today

1. push this page and then check if this new page shows up in All-Pages.
	 - RESULT: pushing this new page triggered a build.
		 - the build yielded two `git log` errors;
		 - it seems that the latest commits are not registered in the `git` records used by the build
		 - Re-deploying and forcing the cache to be cleared does sync things up
2. push this page and this [[2024-10-03 test number 2]]  
	- RESULT: 
