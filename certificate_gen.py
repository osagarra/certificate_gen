#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       certitficate_gen.py
#       
#       Copyright 2012 Oleguer Sagarra <oleguer.sagarra@gmail.com>
#       
#       
#       

import os
import copy

def main():
	tex_file=open('./text.tex','r')
	names=open('./names.txt','r')
	posters=open('./posters.txt','r')
	name_list=names.readlines()
	poster_list=posters.readlines()
	text=tex_file.readlines()
	names.close()
	posters.close()
	tex_file.close()
	try:
		os.mkdir('./output_tex')
	except OSError:
		pass
	if len(name_list)!=len(poster_list):
		print "Different number of names and posters! Aborting "
		return
	i=0
	print "## Generating tex files ##"
	for name in name_list:
		dummy_text=copy.deepcopy(text)
		j=0
		for ele in dummy_text:
			if 'NNAMEE' in ele:
				dummy_text[j]=dummy_text[j].replace('NNAMEE',name_list[i])
				print 'Name replaced!'
			if ' PPOSTERR ' in ele:
				dummy_text[j]=dummy_text[j].replace(' PPOSTERR ',poster_list[i])
				print 'COntribution replaced!'
			j+=1
		a=open('./output_tex/'+name_list[i].split()[1],'w')
		a.writelines(dummy_text)
		a.close()
		i+=1
	print "## Generating pdf files ##"
	file_list=os.listdir('./output_tex')
	try:
		os.mkdir('./output_pdf')
	except OSError:
		pass
	for tex in file_list:
		os.system('pdflatex '+'./output_tex/'+tex+' '+tex.split('.')[0]+'.pdf') # substitue "pdflatex" y your favorite latex compiler
		os.system('mv '+tex.split('.')[0]+'.pdf'+' ./output_pdf/'+tex.split('.')[0]+'.pdf') # for win users change "mv by move"
		os.system('rm *.log') # for win users comment this line
		os.system('rm *.aux') # for win users comment this line
	return 0

if __name__ == '__main__':
	main()

