# girahs-hsl3

A HSL3 logic toolset to design, build, test and release logic blocks from a JSON configuration file.

## Requirements

- Python 3.9.x (as installed on the HomeServer/FacilityServer itself).

## Quick start

1. Place your configuration JSON file (for example `config_00000_my_file`).
2. Run the generator:

>The configuration file must begin with the prefix `config_` and the 5-digit node-id `00000`. In this version only JSON files are supported and the file needs to have the correct structure. It generates a python file with the minimal methods required.

```
python3 generator.py -s config_14649_weatherdata_ecowitt.json
```

By default, the python is written next to the source file using the filename specified in the config JSON. You can add your code accordingly taking into account the limitations of the HSL3 framework.

## Generate Logic Node

Generating the final Logic Node is exactly like the orignal file generation.

```
python3 generator.py -s config_14649_weatherdata_ecowitt.json
```

Since the Python file is already present, it will generate a .hsl logic node file.

## CLI options

- `-s, --source`: Path to the source file (default: `config.xml`).
- `-t, --target`: Path to the target file (default: same directory as source file with `.hsl` extension).
- `-d, --debug`: Enable debug output.

## Usage 
Download this module and add it as a submodule to your logic node repositiory. Import the hsl3 Framework so you can write simple tests.
```
project
|- docs/   # documentation on the logic node
|- hsl3/   # HSL3 Framework
|- src/    # Logic Node files (.json, .py, .hsl and .html)
|- tests/  # Test files
|- README.md
|- LICENCE
```
## Notes

- XML input is currently not supported; use JSON.
- Make sure you incorporateS a HTML with your Logic Node information with the name `log00000.html`

## Future developments

- Develop and test other functionalities like stores and timers
- Autogenerate the HTML file for Logic Node information purposes
- Create a package to import directly in the logic node project