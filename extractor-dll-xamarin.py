from elftools.elf.elffile import ELFFile
from zipfile import ZipFile
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO 
import gzip, string
import sys



if __name__ == "__main__":
    file_to_unpack = sys.argv[1]
    data = open(file_to_unpack).read()
    f = StringIO(data)
    elffile = ELFFile(f)
    section = elffile.get_section_by_name('.dynsym')

    for symbol in section.iter_symbols():
        if symbol['st_shndx'] != 'SHN_UNDEF' and symbol.name.startswith('assembly_data_'):
            print(symbol.name)
            dll_data = data[symbol['st_value']:symbol['st_value']+symbol['st_size']]
            dll_data = gzip.GzipFile(fileobj=StringIO(dll_data)).read()
            outfile = open(symbol.name[14:].replace('_dll', '.dll'), 'w')
            outfile.write(dll_data)
            outfile.close()