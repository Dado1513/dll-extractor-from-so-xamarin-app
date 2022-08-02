from elftools.elf.elffile import ELFFile
from zipfile import ZipFile
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO 
import gzip, string
import sys
import os
import subprocess


if __name__ == "__main__":
    if len(sys.argv) == 3:
        file_to_unpack = sys.argv[1]
        output_dir = sys.argv[2]
        try:
            os.mkdir(output_dir)
        except: 
            pass    
        data = open(file_to_unpack).read()
        f = StringIO(data)
        elffile = ELFFile(f)
        section = elffile.get_section_by_name('.dynsym')

        for symbol in section.iter_symbols():
            if symbol['st_shndx'] != 'SHN_UNDEF' and symbol.name.startswith('assembly_data_'):
                print(symbol.name)
                dll_data = data[symbol['st_value']:symbol['st_value']+symbol['st_size']]
                dll_data = gzip.GzipFile(fileobj=StringIO(dll_data)).read()
                output_file_name = os.path.join(output_dir, symbol.name[14:].replace('_dll', '.dll'))
                outfile = open(output_file_name, 'w')
                outfile.write(dll_data)
                outfile.close()

                # convert dll into cs
                try:
                    cmd = ["ilspycmd", output_file, "-o", os.path.dirname(output_file)]
                    ilspycmd_ouput = subprocess.check_output(cmd)
                except Exception as e:
                    print(f"[*] Error {output_file}")

                

    else:
        print("[*] Usage python extractor-dll-xamarin.py file.so output-dir")