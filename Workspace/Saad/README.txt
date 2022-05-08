This is your dedicated workspace. 

- Checkout your branch. Working on the main branch should be reserved for conflict resolution or special circumstances.
- Create and manage your notebooks however you please.
- Refrain from adding files to another developer's workspace
- You are responsible for managing the git aspect of your files. 
- Commit and push regularly. This is the first step in preventing major losses of work.
- Recommended push procedure (assuming cursors is in project root folder):
	- $ git add Workspace\**user** (This adds the entire user folder files)
	- $ git commit -m "meaningful message"
	- $ git push origin **user_branch**
	- Put in pull request on github

- When working in the root folder, the above steps ought to be done on a file by file basis