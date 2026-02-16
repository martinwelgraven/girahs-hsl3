global debug_mode
global base_path_source_file

__version__ = '0.1.0'
__author__ = 'Martin Welgraven'

import argparse
import os
from parsers.json import parse_json
from parsers.module import ModuleParser

def debug(msg):
    if debug_mode:
        print(msg)

def main():
    global debug_mode
    global base_path_source_file

    parser = argparse.ArgumentParser(description=f'Generator (v{__version__}) for the generation of HSL3 logic blocks.')
    parser.add_argument('-s', '--source', default='config.xml', help='Path to the source file (default: config.xml)')
    parser.add_argument('-t', '--target', default='', help='Path to the target file (default: same directory as source file with .hsl extension)')
    parser.add_argument('-d', '--debug', action='store_true', help='Enables debug output')
    
    args = parser.parse_args()
    
    source_file = args.source
    target_file = args.target
    base_path_source_file = os.path.dirname(os.path.abspath(source_file))
    debug_mode = args.debug
    
    debug('Debug mode is enabled.')
    debug(f'Version: {__version__}')
    debug(f'Source file: {source_file}')
    debug(f'Base path: {base_path_source_file}')

    with open(source_file, 'r', encoding='utf-8') as qf:
        content = qf.read()
        _, file_extension = os.path.splitext(source_file)
        file_extension = file_extension.lower()
        if file_extension == '.xml':
            raise Exception('XML format is currently not supported. Please provide a .json file.')
            module_config = parse_xml(content)
        elif file_extension == '.json':
            module_config = parse_json(base_path_source_file, content)
        else:
            raise Exception('Unsupported file type. Please provide a .xml or .json file.')
    
    module_content = ModuleParser().get_module_file_content(base_path_source_file, module_config)
    if len(target_file) == 0:
        target_file = os.path.join(str(base_path_source_file), str(module_config.hsl_filename))
    debug(f'Target file: {target_file}')
    
    with open(target_file, 'w', encoding='iso-8859-15') as zf:
        zf.write(module_content)
        debug(f'Content written to target file \'{target_file}\'.')

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n')
    print(f'Creating HSL3 Logic Block')
    print(f'=========================')
    main()
    print(f'=========================')
    print('\n')