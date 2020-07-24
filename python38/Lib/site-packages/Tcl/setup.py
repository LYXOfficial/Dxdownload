import setuptools
with open('Tcl/README.md', 'r') as fh:
	read = fh.read()


setuptools.setup(
	name = "Tcl",
	version = "0.2",


	author = "Repl.it Developer",
	author_email = "xsumagravity@gmail.com",


	description = "A coding language used for Graphical user interface",


	long_description = read,
	url = "https://github.com/SCORPIA-oss/Tcl-repo",


	packages = setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: MacOS",
	]
)