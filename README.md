# girahs-hsl3

A HSL3 logic toolset to design, build, test and release logic blocks from a JSON configuration file.


> **EARLY STAGES OF DEVELOPMENT**<br/>
This software is in the early stages of development. Please use it accordingly and provide feedback if you experience issues.

> **Independent Development & Non-Affiliation Disclaimer**<br/>
This software is an independently developed SDK. It is not affiliated with, endorsed by, or supported by Gira Giersiepen GmbH & Co. KG or any of its affiliated companies. All referenced product and company names are trademarks of their respective owners and are used for identification purposes only.  

## Requirements

- Python 3.9.x (as installed on the HomeServer/FacilityServer itself).

## Logic Node Project setup 
Download the src folder from this module and add it to your logic node repository in a folder named hsl3. Import the hsl3 framework so you can write simple tests.
```
project        # foldernaam must be in the format of '00000-my-project'
├── docs/      # documentation on the logic node
├── hsl3/      # HSL3 Framework
├── src/       # Logic Node files
|    ├── config_my_logic_node.json
|    ├── hsl3_00000_my_logic_node.py
|    ├── log00000.html
|    └── 00000_my_logic_node.hsl
├── tests/     # Test files
├── README.md  # Your Logic Node readme
└── LICENSE    # Your Logic Node license
```
Please note that adhering to the file naming convention is required to make your logic node accepted by the HomeServer.

## Quick start

> Reserving your own public Logic node numbers can be requested from [DaCom Database Computing GmbH](http://www.dacom-ha.de)

1. Scaffold the project by placing a copy in the root of your new Logic Node Project and run the command:
```
python3 hsl3/hsl3_generator/generator.py -new
```
Follow the steps in the terminal to set the project basics. Options include:
 - Create a base JSON
 - Create a project Python file
 - Create and build the test folder and file.

> The provided file naming is the according to the convention of GIRA. For this package naming the folder coorrectly is most important. The hsl file should not be renamed after generation.

## Generate Logic Node

Generating the final Logic Node is similar to the initial file generation.

```
python3 hsl3/hsl3_generator/generator.py -build 
```
Again follow the steps in the terminal. You will be requested to build the HSL file and the HTML documentation file.

** WARNING ** The files will be overwritten after confirmation.

## CLI options

- `-n, --new`: Start an interactive setup to create a new project.
- `-b, --build`: Build an existing project to a `.hsl` file and generate documentation.
- `-d, --debug`: Enable debug output.

## Configuration

### Config File Format (JSON)

HSL3 modules are configured via JSON files. See [config_weatherdata_ecowitt.json](src/config_weatherdata_ecowitt.json) for an example.

#### Module Metadata

```json
{
  "module": {
    "id": "14649",
        "name": "Weatherdata Ecowitt",
        "version": "0.1.0",                           
        "version_date": "2026-03-14",                 // This is not part of the original hsl3 framework
        "description": "A Logic node for...",         // This is not part of the original hsl3 framework
        "warning": "",                                // This is not part of the original hsl3 framework
        "note": "",                                   // This is not part of the original hsl3 framework
        "category": "IOT Device Data",
        "context": "weatherdata_ecowitt",
        "hsl_filename": "14649_weatherdata_ecowitt.hsl",
  }
}
```

#### Inputs

Inputs are data points received by the logic module (e.g., sensor readings, configuration parameters).

```json
{
  "inputs": [
    {
      "type": "string",
      "identifier": "IN01_DATA",
      "init_value": "",
      "label": "Data (x-www-form-urlencoded)",
      "description": "This is a description for the Help file" // This is not part of the original hsl3 framework  
    },
    {
      "type": "number",
      "identifier": "IN02_TEMP_UNIT",
      "init_value": 1,
      "label": "Temperature (1-Celsius, 0-Fahrenheit)",
      "description": "This is a description for the Help file" // This is not part of the original hsl3 framework
    }
  ]
}
```

Supported input types: `string`, `number`, `bytes`

#### Outputs

Outputs are values calculated by the logic and sent to other Gira devices.

```json
{
  "outputs": [
    {
      "type": "string",
      "identifier": "OUT01_KEY",
      "init_value": "",
      "label": "PASSKEY",
      "description": "This is a description for the Help file" // This is not part of the original hsl3 framework
    },
    {
      "type": "number",
      "identifier": "OUT04_TEMP",
      "init_value": 0.0,
      "label": "Temperature",
      "description": "This is a description for the Help file" // This is not part of the original hsl3 framework
    }
  ]
}
```

#### Stores (Persistent Memory)

Stores retain values between logic executions.

```json
{
  "stores": [
    {
      "type": "number",
      "identifier": "STORE01_LAST_TEMP",
      "init_value": 0.0,
      "label": "Last recorded temperature",
      "description": "This is a description for the Help file" // This is not part of the original hsl3 framework
    }
  ]
}
```

#### Timers

Timers trigger logic at specified intervals.

```json
{
  "timers": [
    {
      "identifier": "TIMER01_HEARTBEAT",
      "description": "This is a description for the Help file" // This is not part of the original hsl3 framework
    }
  ]
}
```

### Creating a Custom HSL3 Module

1. **Create a JSON configuration** defining your module's inputs, outputs, stores, and timers
2. **Use the generator** to create Python code from the configuration
3. **Implement your logic** in the generated module's process methods
4. **Test** with the provided test framework

### Example: Processing Weather Data

The `LogicModule` in generated code processes incoming data:

```python
def process_data(headers, post_data):
    """Process incoming weather data from HTTP POST"""
    # Parse x-www-form-urlencoded data
    # Extract PASSKEY, temperature, humidity, wind speed, etc.
    # Set HSL3 outputs with calculated values
    # Optionally update stores and set timers
```

### Setting Outputs

Use `self.fw.set_output()` to send data to connected Gira devices:

```python
self.fw.set_output("OUT04_TEMP", 22.5)           # Number output
self.fw.set_output("OUT01_KEY", b"mykey123")     # Bytes output
```

### Managing Stores (Persistent Memory)

```python
self.fw.set_store("STORE01_LAST_TEMP", 22.5)     # Save value
last_value = self.fw.stores["STORE01_LAST_TEMP"] # Retrieve value
```

### Setting Timers

```python
self.fw.set_timer("TIMER01_HEARTBEAT", 60)  # Trigger every 60 seconds
self.fw.set_timer("TIMER01_HEARTBEAT", 0)   # Stop the timer
```

### Logging

```python
logger = hsl3.get_logger("127.0.0.1", 65002, console=True, level="INFO")
logger.info("Weather data received successfully")
```

## HSL3 Concepts

### Context

The HSL3 context represents the execution environment within the Gira HomeServer. Code must be run within this context to interact with outputs, stores, and timers. Use `hsl3.run_in_context(callback, params)` for multi-threaded code.

### Inputs

External data provided to the logic module (e.g., sensor readings, user configuration). Inputs trigger logic execution when updated.

### Outputs

Values calculated by the logic that are made available to other Gira devices and systems. Outputs communicate results back to the HomeServer.

### Stores

Persistent memory that retains values between logic executions. Useful for tracking state, historical averages, or configuration.

### Timers

Periodic events that trigger logic execution at specified intervals. Used for polling, heartbeats, and scheduled tasks.

## Data Formats

Input and output definitions in this project are JSON-based. XML input is currently not supported.

## Notes

- XML input is currently not supported; use JSON.
- Make sure you include an HTML file with your Logic Node information named `log00000.html`.

## Standard Libraries

In Python 3.9 the following libraries are available

**Built-in Functions & Exceptions**
print, len, sum, map, zip, range, int, float, str, list, dict, set, tuple, type, ValueError, TypeError, KeyError, IndexError

**Numeric & Mathematical Modules**
math, cmath, decimal, fractions, random, statistics, numbers

**Data Types & Collections**
collections, collections.abc, array, heapq, bisect, weakref, types, copy, pprint, reprlib, enum

**Text Processing**
string, re, textwrap, difflib, unicodedata, stringprep, readline

**File & Directory Access**
os, os.path, pathlib, io, fileinput, stat, filecmp, tempfile, glob, fnmatch, linecache, shutil

**Data Persistence**
pickle, copyreg, shelve, marshal, dbm, sqlite3

**Data Compression & Archiving**
zlib, gzip, bz2, lzma, zipfile, tarfile

**File Formats**
csv, configparser, json, plistlib, netrc, xdrlib

**Cryptographic Services**
hashlib, hmac, secrets

**Generic OS Services**
time, argparse, getopt, logging, getpass, curses, platform, errno, ctypes, signal, resource

**Networking & Internet Protocols**
socket, ssl, select, asyncio, asyncore, asynchat

**Internet Data Handling**
email, base64, binascii, quopri, uu

**Structured Data & Parsing**
html, html.parser, xml.etree.ElementTree, xml.dom, xml.sax

**Development & Testing Tools**
unittest, doctest, pdb, trace, timeit, profile, cProfile

**Runtime Services**
sys, traceback, warnings, gc, inspect, atexit, faulthandler

**Concurrency & Parallelism**
threading, multiprocessing, concurrent.futures, queue, _thread

**Importing & Packaging**
importlib, pkgutil, modulefinder, runpy, zipimport

**GUI (Tk)**
tkinter, tkinter.ttk, tkinter.scrolledtext

**Multimedia**
audioop, wave, chunk, colorsys, imghdr, sndhdr

**Other Utilities**
abc, contextlib, dataclasses, functools, itertools, operator, typing, uuid, zoneinfo

## External Libraries

requests, websockets, beautifulsoup4, pytz, python-dateutil, pymodbus


## Future developments

- Develop and test other functionalities like stores and timers
- Autogenerate the HTML file for Logic Node information purposes
- Create a package to import directly in the logic node project