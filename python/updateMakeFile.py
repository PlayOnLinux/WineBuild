#!/usr/bin/python

# This file update winegcc make file, so that winegcc can build in a linux system for osx system
# Written by Tinou, August 07 2011
import sys, os

try:
	fichier = open(sys.argv[1],"r").readlines()
except:
	sys.exit()

final = []
for line in fichier:
	append = True
	if("-DLDDLLFLAGS" in line):
		final.append('\t-DLDDLLFLAGS="\\"-bundle -multiply_defined suppress -F/usr/lib/apple/SDKs/MacOSX'+os.environ["FRAMEWORK"]+'.sdk/System/Library/Frameworks\\"" \\\n')
		append = False
	if("-DCPP" in line):
		final.append('\t-DCPP="\\"i686-apple-darwin10-cpp\\"" \\\n')
		append = False
	if("-DCXX" in line):
		final.append('\t-DCXX="\\"i686-apple-darwin10-g++ -m32\\"" \\\n')
		append = False

	if(append == True):
		final.append(line)	

fichier = open(sys.argv[1],"w")
for line in final:
	fichier.write(line)
