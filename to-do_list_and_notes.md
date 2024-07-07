# to-do list  and notes
>[!comment] (which shows that almost [every project needs a plan](https://wiki.openglobalmind.com/ogm_stewardship/project_plans/template_for_project_(how_to_use)))

- N.B.: this may turn out to be an ad-hoc list of imagined plans  

1. primary current experiment is to use this vault to debug using a PyPI module, now named `nxc` to build a static website, and deploy using `netlify`  

2024-06-18:  
 - some other thoughts (carried over from "ghPagesLab" work):  
	 - one rationale for command-line `websiteroot` specification is that `mwb.yaml` can be used for multiple web publication sites without change  
	 - Note: this does mean that PyPI module initialization might need to query for expected deployment method (and where would that info go if not into `mwb.yaml`?)  
	 - there are questions to be resolved about how to help the user of the system set up, or modify already set up, configurations.  
   
- today's plan list :  
	- DONE - set up test vault  
	- DONE - set up Github repository  
	- DONE - modify `netlify.toml` to use test-pypi module `nxc`  
- yet TODO:  
	- bug: links returned by search do not have a correct path  
	- further local testing on my own `cleanbench`  
	- code review  
	- document  use cases and how-to use  
	- determine a name for this package and write description for PyPI  
	- public announcements?  

2024-06-28:
 - gh-pages mysteries and actions (whew!)  
 

2024-06-29 TODO:  
 - nxc: add code to incorporate websiteroot into Sidebar links  
   - testing in nxc 0.1.8
   - issue: Sidebar.html does not render local links
     solution: convert local links in all markdown_text (test in
     ghPagesLab)
     DONE: this solution included in nxc 0.1.9
	 
2024-06-30:  
 - backlinks need `{websiteroot}}` variable added on `page.html`
   - seems to be working for netlify and gh-pages
 - TODO:  
   - update PyPI code and test that  (2024-07-02 1st test DONE)  
   - test nxcTV on netlify and Github pages  

2024-07-05:  
 - used Claude-3 to refactor the html rendering for page, search, all-pages, recent-pages; the code looks good, and permits some further specialization of individual pages.
 - the next TODO is to incorporate "Edit this page" function on all pages
 - immediately followed by restricting "Edit this page" from README and Sidebar  

2024-07-06:  
 - incorporated "Edit this page" code (`nxc.py`, `page.html`, `mystyles.css`)
 - TODO: that code needs to committed to Github repo
 - `nxc.yaml` contains Github usable `edit_url` (configuration of this for other forges needs to be documented)
 - use these notes from PK on 18 April 2024:
```
edit_url: 'https://codeberg.org/{org}/{repo}/_edit/{branch}/'

edit_url: 'https://github.com/{org}/{repo}/edit/{branch}/'

edit_url: 'https://gitlab.com/{org}/{project-or subgroup}/{repo}/-/edit/{branch}/'

edit_url: 'https://gitea.com/{org}/{repo}/_edit/{branch}/'

# Bitbucket requires suffix
edit_url_prefix: 'https://bitbucket.org/{org}/{repo}/src/{branch}/'
edit_url_suffix: '?mode=edit'
```
 - TODO: CSS for the "Edit this page" button needs tweaking for Dolce theme

2024-07-06 exclude specific subdirectories from website build (feature request)  
```python
exclude_subdir = "/path/to/your/directory/exclude_subdir"
filtered_markdown_files = [file for file in markdown_files if not file.startswith(exclude_subdir)]
```
when `exclude_subdirs` is a list of directories this code is an option:  
```python
filtered_markdown_files = [file for file in markdown_files if not any(file.startswith(exclude_subdir) for exclude_subdir in exclude_subdirs)]
```

2024-07-07:
 - "Edit the page" code in the test-pypi package ToBeTested  
	 - exclude "Edit this page" button from README and Sidebar (nxc 0.1.13)
- TODO: review and organize the `nxc` templates directory  

