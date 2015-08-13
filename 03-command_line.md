# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

>> PIPING AND REDIRECTION
cmd1|cmd2    Take the output from cmd1, pipe it as input to cmd2.

cmd<file     Take the contents of file as input for cmd.

cmd>file     Take the output from cmd and write to file.

cmd>>file    Take the output from cmd and append to file.    


BASH TERMINAL COMMANDS
pwd		print working directory

hostname 	my computer's network name
		   -s	 omit domain information

mkdir 		make directory
		   -p	 create intermediate directories as necessary
  
cd 		change directory

ls 		list directory
		   -l	 long output
		   -A	 list all entries but . and ..
		   -lh	 display sizes in unit prefixes (B, KB, MB, ...)
		   -m	 stream output (comma separated)
		   -p	 distinguish directories by appending '/'
		   -R	 show full tree beneath pwd

rmdir 		remove directory
		   -p    delete intermediate directories (so be careful!)
		   	   this is confusing, so here's an example:
			   to remove the entire tree from the root bob3:
			   (pwd)
			   |____bob3
				|____bob4
				     |_____bob5
			   type: rmdir -p bob3/bob4/bob5

pushd 		push directory
		   +N	 rotate stack to Nth directory on top
		   -N	 rotate stack to Nth (from right) directory on top
		   -n	 add dir to stack in 2nd position (don't change pwd)

popd 		pop directory
		   +N	 pop Nth directory starting from 0
		   -N	 pop Nth (from right) directory starting from 0
		   -n	 same as popd +1

touch	 	create new empty file (actually designed to change times)
cp 		copy a file or directory
		   Syntax is 'cp (source) (target)'
		   -i    prompt before overwriting
		   -n 	 do not overwrite
		   -R	 allows copying of directories (and their contents)

mv 		move or rename a file or directory
		   Syntax for renaming is 'mv (old name) (new name)'
		   Syntax for moving is 'mv (name) (target directory)'
		   -i	 prompt before overwriting
		   -n 	 do not overwrite

less		page through a file

cat 		print some files
		   -n 	 print line numbers
		   -b	 print line numbers only for non-blank lines
		   -s	 squeeze adjacent whitespace into one line

rm		remove file (or directory)
		   -d    remove (empty) directory
		   -r	 recursive delete (BE VERY CAREFUL/USE -i)
		   -i 	 prompt before deletion

xargs		feed list of arguments from standard input into utility
		   Syntax is 'xargs (utility)', then arguments, then C-d
		   (Note: alternatively, use piping ...) 
		   -E (eof)    use (eof) as a logical end of file marker
		   -p 	       echo each command before execution (y/n)

find		find files
		   (One) syntax is 'find STARTDIR -name WILDCARD -print'
		   (General) syntax is 'find [options] PATH (expr)'
		   	     where expr is made up of primaries/operands 
		   Options:
		   -d	 depth-first traversal
		   -s	 alphabetical order traversal
		   Primaries:
		   -delete	      delete found files and directories
		   		      (depth first)
		   -empty     	      return true if file or directory is empty
		   -exec and -execdir (these seem v. useful and return true 
		   	     	      contingent on a separate utility command,
				      run from pwd or from directory of the
				      current file, resp.)
		   -iname (str)	      case insensitive name search
		   -maxdepth (num)    descend at most (num) levels from PATH
		   -mindepth (num)    only test once (num) levels from PATH
		   -name (str)	      name search (use wildcards!)
		   -newer (file)      true if current file has more recent
		   	  	      modification time than (file)
		   -path (str)	      path search (use wildcards!)
		   -print	      (default) prints pathname of current file
		   -size (n)	      true if file's size (in 512-byte blocks)
		   	 	      is (n) and also can take other units
				      [ckMGTP]
		   Operators:
		   ! or -not		not
		   -false		false
		   -true		true
		   (exp) -and (exp)	logical AND (alternatively (exp)(exp))
		   (exp) -or (exp)	logical OR

grep		find things inside files
		   Syntax is 'grep (options) (pattern) (file)'
		   -c	     print a count of number of lines
		   	     containing (pattern)
		   -i 	     case insensitive matching
		   -m (num)  stop reading file after (num) matches
		   -n 	     include line numbers with matched output
		   -o	     prints only matching part of lines
		   -r 	     recursive search through subdirectories
		   -v	     inverted search (think !grep)

man		read a manual page
		   -a  	     display all pages matching search
		   
apropos		find what man page is appropriate

env		look at your environment

echo 		print some arguments

export		set a new environment variable
		   Syntax for changing PATH: 'PATH=$PATH:/your/path/here'

unset		get rid of an environment variable

sudo		DANGER! become super user root DANGER!

chmod		change permission modifiers

chown		change ownership

exit		exit the shell


---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

>> 'ls' prints a list of the contents of the present working directory. 
When combined with the option '-a', the command prints items in the directory that begin with '.'; for example, in my cloned local copy of the dsp repository, 'ls -a' prints the normally-visible contents of dsp/ as well as '.', '..', '.DS_Store', '.git', and '.gitignore'.
When combined with the option '-l', the command prints a detailed, formatted list of the contents of the present working directory. This display shows the permissions ("file mode"), the number of links to each item, owner name, group name, number of bytes, exact time of last modification, and path name.
When we add on the option '-lh', the only change from '-l' is that appropriate units are used in displaying file size. For example, a 1M file would be displayed as such rather than as 1024K or as 1048576B.
Note that the '-h' option only does anything when used in conjunction with the '-l' option. Using 'ls -h' or 'ls -ah' will not give an error, but the h's will essentially be ignored since file size is not printed at all. We can, of course, combine all three of these options: 'ls -alh' will print the long form contents of the current working directory, including those items starting with '.', and using appropriate unit suffixes to display file sizes. 

---


---

What does `xargs` do? Give an example of how to use it.

>> 'xargs' reads in a list of arguments and supplies them as input for a utility. xargs can do this from standard input (default) or you can pipe in your argument list to xargs. The example below shows how you can delete all of the .txt files in the present working directory (and all its subdirectories):

find . -name "*.txt" -print | xargs rm

While this seems like it would certainly be useful in certain (probably more complicated) cases, it does certainly seem easier in this case to simply run the command 'rm *.txt', which does the same thing. I will be on the lookout for ways that xargs gets around more complicated constructions.
---

