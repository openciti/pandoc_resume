import pypandoc, os, subprocess
os.system('./t.sh')
inF = 'resume.md'
outF = 'demo.pdf'
texTemplateF = 'withcolors.tex'
tempTexF = 'resume.tex'

latexEngine = 'xelatex'
latexArg = '--latex-engine=' + latexEngine

paper = 'A4'
paperSize = 'papersize=' + paper

eargs = []
eargs.extend([latexArg, '--standalone'])
eargs.extend(['--template', texTemplateF])
eargs.extend(['--from', 'markdown', '--to', 'context'])
eargs.extend(['-V', paperSize])
eargs.extend(['-o', tempTexF, inF])

print (eargs)
pypandoc.convert_file(inF, 'pdf', outputfile=outF, extra_args=eargs)

os.system('context ' + tempTexF)

