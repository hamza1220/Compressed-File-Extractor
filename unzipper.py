from pyunpack import Archive
import os, imp
import zipfile

print "------------SETUP INSTRUCTIONS---------------"
print "pip install patool"
print "pip install pyunpack"
print "install 7-zip from 7-zip.org (for Rar files)"
print "set env var for 7-zip (in Program Files)"
print "---------------------------------------------"
print "\n"

def findLatestSubmission(options):
	ext =""
	for each in options:
		if len(each)>len(ext):
			ext = each
		elif len(each)==len(ext):
			if int(each[-5])> int(ext[-5]):
				# print "new ext", each
				ext= each
	return ext


def writeToFile(filename,toWrite):
	f = open(filename, "a+")
	for item in toWrite:
		f.write(item)
		print item
	f.close()


def unzip(src, dest):
	dual_subs = []
	i = 0
	ss = 0
	for file in os.listdir(src):
		for file2 in os.listdir(src+'\\'+file):
			if file2.endswith(".txt"):
				continue
			options =[]
			for file3 in os.listdir(src+'\\'+file+"\\"+file2):
				if file3.endswith(".zip") or file3.endswith(".rar"):
					options.append(file3)
			
			# ext = findLatestSubmission(options)
			print i, file
			if len(options)<1:
				print "NO SUBMISSIONS\n"
			else:
				ext = options[0]
				if len(options)==1:
					print options
					ss+=1
					try:
						print "Extracting", ext

						if file3.endswith(".zip"):
							print "Contents", zipfile.ZipFile(src+'\\'+file+"\\"+file2+"\\"+ext).namelist()[0]

						Archive(os.path.join(os.path.abspath(__file__)[:-12] ,src , file, file2, ext)).extractall(dest)
						print "Successful!\n"
					except:
						print "Error\n"
				else:
					print "DUAL submissions\n"
					dual_subs.append(file)

			i+=1

	print "people with single submissions", ss
	print "people with multiple submissions:",len(dual_subs)
	return dual_subs


multiple_subs = unzip('src','dest')
writeToFile("Multiple_Submissions.txt",multiple_subs)