+++++ note: this will obsolete when CONTENTdm upgrades to new version in summer/fall 2024

GITHUB: https://github.com/grahaa/batch-edit-metadata-in-CDM
Yes, this works for individual items as well as compound objects

Instructions:
1. export a collection or portion of a collection. Nice because you can export a portion (search results) of the entire collection.
	https://server16786.contentdm.oclc.org/cgi-bin/admin/start.exe
2. bring data into excel (Anne can do this so quickly and easily so she usually do it)
3. Anne sends spreadsheet to user
4. User changes any fields and colors EVERY CHANGED CELL to indicate there has been a change
5. User sends spreadsheet to Anne

6. Eliminate any fields and columns that are not colored
7. MUST retain the contentdm number (far right edge of spreadsheet)
8. Get field nicknames from admin interface, field properties (hover over "edit" button and watch lower left edge of screen, there is a pause)
9. Create a csv with this structure: record number,fieldnickname,value          [be sure to choose a good delimiter, often use "~"]
10. Bring csv into Notepad++ and do searches for difficult characters such as:
	"&"  use &amp; or change to "and" or take a note of record and go back in and edit it back to an &.
	Scene’s
	“this is the end” 
	MS has a proprietary hyphen  "–" just typed two dashes 
	me‘am
	... microsoft has a proprietary elipsis character

11. Open proj client in collection of interest 
12. Search for specific records (or download all) and add to the project
13. Sort by title - can take a couple minutes
14. Go to directory of project
	C:\Users\yourprofilename\AppData\Roaming\OCLC\CONTENTdm Project Client\collectioname\Project #
15. Make a backup of the desc files, place in some safe subdirectory. Can roll back if there is a problem or mistake!
16. Copy the .py file (python 3 script) and the csv file into this directory
17. Close the project client!
18. Open a windows terminal (CMD) and change directory to the directory of the project (where the .desc files are)
19. Run the script: 
	python editmetadata.py
	script asks for: 
		name of csv file (give full file name)
		delimiter you want to use, usually ~
20. Assuming it ends gracefully, open project client and see if the edits are visible - they should be 
21. Upload, approve, and index the collection. 

Note: you may need to turn off a field's controlled vocabulary setting before approving, and turn it back on after indexing.

Note: Anne is planning to write a followup script to check every record to be sure it changed exactly as specified (up till now been doing this by hand with a fresh export)
