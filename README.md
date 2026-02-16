# girahs-hsl3

A HSL3 logic toolset ot design, build, test and release logic blocks from a JSON configuration file.

## Requirements

- Python 3.9.x (as installed on the HomeServer/FacilityServer itself.)

## Quick start

1. Place your configuration JSON file (for example `hsl3_00000_my_file`).
2. Run the generator:

>Each file must begin with the prefix hsl3_ and the node ID and end with the suffix .py. Only files with this structure ? can be converted by the HSL3 Generator.

```
python generator.py -s config.json
```

By default, the output is written next to the source file using the filename specified in the config.

## CLI options

- `-s, --source`: Path to the source file (default: `config.xml`).
- `-t, --target`: Path to the target file (default: same directory as source file with `.hsl` extension).
- `-d, --debug`: Enable debug output.

## Development

Install dependencies (none external by default) and run tests:

```
python -m unittest discover -s tests
```

## Notes

XML input is currently not supported; use JSON.
