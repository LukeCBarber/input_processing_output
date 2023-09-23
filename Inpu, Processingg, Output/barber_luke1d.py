#File Input
file_kb = float(input('Enter a file size in kilobytes (KB): '))
print('')
print(file_kb, 'KB ...')
print('')


#File Conversion
#the following would cause a runtime error
#the variable file_byte is not defined
#file_bit = file_byte*8
#file_byte = file_kb*1024
#the following would cause a syntax error
#cannot assign string to a literal
#'file_byte' = file-kb*1024
file_byte = file_kb*1024
file_bit = file_byte*8
#the following would cause a logic error
#the value file_mb would be incorret
#file_mb = file_byte/1024
file_mb = file_kb/1024
file_gb = file_mb/1024



#Output
#the following would cause a syntax error
#undetermined string literal 'bits'
#print(format('... in bits','20s'),format(str(('{:.1f}'.format(file_bit))),'>20s'),' bits)
print(format('... in bits','20s'),format(str(('{:.1f}'.format(file_bit))),'>20s'),' bits')
print(format('... in bytes','20s'),format(str(('{:.1f}'.format(file_byte))),'>20s'),' bytes')
print(format('... in megabytes','20s'),format(str(('{:.1f}'.format(file_mb))),'>20s'),' MB')
print(format('... in gigabytes','20s'),format(str(('{:.1f}'.format(file_gb))),'>20s'),' GB')
#the following would cause a logic error
#the file in mb would be diplayed in place of the file in gb
#print(format('... in gigabytes','20s'),format(str(('{:.1f}'.format(file_mb))),'>20s'),' GB')
