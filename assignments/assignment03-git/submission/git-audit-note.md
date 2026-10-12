# Git Audit Note

## Diff summary
File changed: assignments/README.md
Changes: added a note about how to copy starter files into own folder to complete assignments (Line 5-12). ```git diff``` only showed README.md  and confirmed the exact changes by looking in Source Control window.

## .gitignore check
Automatically added: ```**/*.quarto_ipynb``` to .gitignore, so I commited it. Already contained comment about how required HTML/PDF submission are purposely not ignored. I ran ``` git-ls files``` and found no temporary files being tracked. I found two rendered .html files being tracked ('practice_report.html' and 'assignments/assignment02-r-with-ai/submission/analysis-note.html'), but both were required submission files so I left them.

## AI use
I used AI to explain how to inspect results from ```git diff``` and how to use ```git ls-files``` to confirm what files were tracked. I also used AI to explain the Git worflow in this assignment. I asked AI about how to structure my README.md note and it suggested a sentence and a 'cp' command with placeholders. I added this near the instructions about not editing the starter file directly and checked how it rendered.

## M0 readiness
Members: [Kyle Fernandez, Miriam Nguyen, Keerit Gill, Megan Kadzirange]
Access: repo is accesible to all group members; all can open and push to it
Communication Plan: Whatsapp groupchat; 24hr reply window (48hr on weekends), weely 30 min online meeting during weekend
Overall: ready for future assignments
