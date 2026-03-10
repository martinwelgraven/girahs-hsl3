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
## Configuration

### Config File Format (JSON)

HSL3 modules are configured via JSON files. See [config_weatherdata_ecowitt.json](src/config_weatherdata_ecowitt.json) for a complete example.

#### Module Metadata

```json
{
  "module": {
    "id": "14649",
    "name": "Weatherdata Ecowitt",
    "category": "IOT device data",
    "context": "weatherdata_ecowitt",
    "version": "0.1.0",
    "hsl_filename": "14649_weatherdata_ecowitt.hsl"
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
      "label": "Data (x-www-form-urlencoded)"
    },
    {
      "type": "number",
      "identifier": "IN02_TEMP_UNIT",
      "init_value": 1,
      "label": "Temperature (1-Celsius, 0-Fahrenheit)"
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
      "label": "PASSKEY"
    },
    {
      "type": "number",
      "identifier": "OUT04_TEMP",
      "init_value": 0.0,
      "label": "Temperature"
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
      "label": "Last recorded temperature"
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
      "label": "Heartbeat timer",
      "default_seconds": 60
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

Use `hsl3.set_output()` to send data to connected Gira devices:

```python
hsl3.set_output("OUT04_TEMP", 22.5)           # Number output
hsl3.set_output("OUT01_KEY", b"mykey123")     # Bytes output
```

### Managing Stores (Persistent Memory)

```python
hsl3.set_store("STORE01_LAST_TEMP", 22.5)     # Save value
last_value = hsl3.stores["STORE01_LAST_TEMP"] # Retrieve value
```

### Setting Timers

```python
hsl3.set_timer("TIMER01_HEARTBEAT", 60)  # Trigger every 60 seconds
hsl3.set_timer("TIMER01_HEARTBEAT", 0)   # Stop the timer
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

## Notes

- XML input is currently not supported; use JSON.
- Make sure you incorporateS a HTML with your Logic Node information with the name `log00000.html`

## Future developments

- Develop and test other functionalities like stores and timers
- Autogenerate the HTML file for Logic Node information purposes
- Create a package to import directly in the logic node project