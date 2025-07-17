# Fake NVIDIA SMI

Just flex with your friends that you have an NVIDIA A100! 🚀

A Python library that generates fake `nvidia-smi` output for various GPU types, perfect for demonstrations, testing, or just showing off to your friends.

## Features

- **Multiple GPU Support**: Simulate H100, A100, V100, P100, K80, and T4 GPUs
- **Realistic Output**: Mimics the actual `nvidia-smi` command output format
- **Dynamic Values**: Generates random but realistic temperature, power consumption, and serial numbers
- **Multiple GPUs**: Support for simulating multiple GPUs of the same type
- **Easy to Use**: Simple API with just one main method

## Installation

### From Source
```bash
git clone https://github.com/[username]/fake-nvidia-smi.git
cd fake-nvidia-smi
pip install -e .
```

### Using Poetry
```bash
poetry install
```

## Quick Start

```python
from fake_nvidia_smi import FakeSMI

# Create an instance
fake_smi = FakeSMI()

# Show a single A100 GPU
fake_smi.flex('a100')

# Show multiple H100 GPUs
fake_smi.flex('h100', gpu_num=4)
```

## Supported GPU Types

| GPU Type | Model Name | Memory | Power Cap |
|----------|------------|--------|-----------|
| `h100` | NVIDIA H100 80GB HBM3 | 81,559 MiB | 700W |
| `a100` | NVIDIA A100-SXM4-40GB | 40,536 MiB | 400W |
| `v100` | V100-SXM4-16GB | 16,160 MiB | 300W |
| `p100` | Tesla P100-PCIE-16GB | 16,280 MiB | 250W |
| `k80` | Tesla K80 | 12,288 MiB | 300W |
| `t4` | Tesla T4 | 15,109 MiB | 70W |

## Usage Examples

### Single GPU
```python
from fake_nvidia_smi import FakeSMI

fake_smi = FakeSMI()
fake_smi.flex('a100')
```

Output:
```
Thu Jul 17 14:30:25 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 575.57.08              Driver Version: 575.57.08      CUDA Version: 12.9     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A100-SXM4-40GB          On  |   00000000:06:10.0 Off |                    0 |
| N/A   35C    P0             45W /  400W |   28156MiB /  40536MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                           
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

### Multiple GPUs
```python
fake_smi.flex('h100', gpu_num=2)
```

### All Supported Types
```python
# Try different GPU types
gpu_types = ['h100', 'a100', 'v100', 'p100', 'k80', 't4']

for gpu_type in gpu_types:
    print(f"\n=== {gpu_type.upper()} ===")
    fake_smi.flex(gpu_type)
```

## API Reference

### `FakeSMI` Class

#### `flex(gpu_type: str, gpu_num: int = 1)`

Generates and prints fake nvidia-smi output.

**Parameters:**
- `gpu_type` (str): Type of GPU to simulate. Supported values: 'h100', 'a100', 'v100', 'p100', 'k80', 't4'
- `gpu_num` (int, optional): Number of GPUs to simulate. Default is 1.

**Returns:**
- None (prints output directly to console)

## Development

The project includes Jupyter notebooks showing the development process:

- `Fake_Nvidia_SMI_V0.1.ipynb` - Initial development version
- `Fake_Nvidia_SMI_V0.2.ipynb` - Improved version with better structure

### Project Structure
```
fake-nvidia-smi/
├── fake_nvidia_smi/
│   ├── __init__.py
│   └── main.py
├── pyproject.toml
├── setup.py
└── README.md
```

## Technical Details

- **Random Values**: Temperature, power consumption, and bus IDs are randomly generated within realistic ranges for each GPU type
- **Realistic Formatting**: Output matches the exact format and spacing of real `nvidia-smi` command
- **No Dependencies**: Uses only Python standard library (datetime, random, string)

## Use Cases

- **Demonstrations**: Show GPU capabilities without actual hardware
- **Testing**: Test applications that parse nvidia-smi output
- **Education**: Learn about different GPU specifications
- **Fun**: Impress friends with your "powerful" GPU setup 😄

## Contributing

Feel free to contribute by:
- Adding support for more GPU types
- Improving the realism of generated values
- Adding new features like process simulation
- Fixing bugs or improving documentation

## License

MIT License - see the project files for details.

## Disclaimer

This tool is for educational and entertainment purposes only. It generates fake output and should not be used to misrepresent actual hardware capabilities.