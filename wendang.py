text='This is my first test.\n This is next line.\n This is last line'
append_text='\n This is appended file'

my_file=open('my file.txt','a')
my_file.write(text)
my_file.write(append_text)
my_file.close()
