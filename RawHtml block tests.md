# RawHtml block tests

This page contains a couple of example uses of a Mistletoe Markdown rendering extension that supports embedding block-level HTML elements into a Markdown note.  
- Preliminary description of this extension is found [here](https://github.com/Massive-Wiki/nxcLab/blob/main/rawhtml.md)  
- TODO: test this with current non-extended Mistletoe  
- TODO: test this with a local, patched, MassiveWikiBuilder  

- Example 1:  
{< div class="example" id="test" >}
Line 1 inside a div  
Line 2 inside the div  
Line 3 inside the div  
{< /div >}

- Example 2 (test links and lists):  
{< div class="navlink" >}
- [Home](/README.html)
- [[MaryRuefle-Nettles]]  
{< /div >}

- Example 3 (an inline span test):  
 - This text, is <span style="color:red;">*special*</span>, and is rendered just fine!  
 
