import datetime
import random
import string


class FakeSMI:
    def __init__(self, padding: int = 1):
        self.padding = padding
        self.gpu_configs = {
            'h100': {
                'name': 'NVIDIA H100 80GB HBM3',
                'mem': '81559MiB',
                'power_cap': 700,
                'temp_range': (28, 34),
                'watt_range': (105, 120),
                'mig_mode': 'Disabled'
            },
            'a100': {
                'name': 'NVIDIA A100-SXM4-40GB',
                'mem': '40536MiB',
                'power_cap': 400,
                'temp_range': (30, 40),
                'watt_range': (40, 60),
                'mig_mode': 'N/A'
            },
            'v100': {
                'name': 'V100-SXM4-16GB',
                'mem': '16160MiB',
                'power_cap': 300,
                'temp_range': (40, 45),
                'watt_range': (80, 90),
                'mig_mode': 'N/A'
            },
            'p100': {
                'name': 'Tesla P100-PCIE-16GB',
                'mem': '16280MiB',
                'power_cap': 250,
                'temp_range': (35, 40),
                'watt_range': (60, 70),
                'mig_mode': 'N/A'
            },
            'k80': {
                'name': 'Tesla K80',
                'mem': '12288MiB',
                'power_cap': 300,
                'temp_range': (40, 50),
                'watt_range': (80, 99),
                'mig_mode': 'N/A'
            },
            't4': {
                'name': 'Tesla T4',
                'mem': '15109MiB',
                'power_cap': 70,
                'temp_range': (30, 35),
                'watt_range': (50, 60),
                'mig_mode': 'N/A'
            }
        }

    @staticmethod
    def __generate_serial():
        while True:
            serial = "".join(random.choices(string.ascii_uppercase + string.digits, k=2))
            if not serial.isalpha():
                return serial

    @staticmethod
    def __print_date():
        now = datetime.datetime.now()
        date_str = now.strftime("%a %b %d %H:%M:%S %Y")
        # Pad to exactly match original format
        print(f"{date_str}       ")

    @staticmethod
    def __print_header():
        # Each line exactly 91 characters
        print("+-----------------------------------------------------------------------------------------+")
        print("| NVIDIA-SMI 575.57.08              Driver Version: 575.57.08      CUDA Version: 12.9     |")
        print("|-----------------------------------------+------------------------+----------------------+")
        print("| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |")
        print("| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |")
        print("|                                         |                        |               MIG M. |")
        print("|=========================================+========================+======================|")

    @staticmethod
    def __print_footer():
        print("+-----------------------------------------------------------------------------------------+")
        print("| Processes:                                                                              |")
        print("|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |")
        print("|        ID   ID                                                               Usage      |")
        print("|=========================================================================================|")
        print("|  No running processes found                                                             |")
        print("+-----------------------------------------------------------------------------------------+")

    def __print_gpu_block(self, gpu_id: int, config: dict):
        temp = random.randint(*config['temp_range'])
        watt = random.randint(*config['watt_range'])
        power_cap = config['power_cap']
        mem_total = config['mem']
        name = config['name']
        mig_mode = config['mig_mode']

        # Generate memory usage (some used memory for realism)
        mem_used = random.randint(15000, 30000)
        
        # Generate bus ID with proper format
        bus_id = f"00000000:0{random.randint(1, 9)}:{random.randint(10, 99)}.0"

        # Build each line to be exactly 91 characters
        # Original: |   0  NVIDIA H100 80GB HBM3          On  |   00000000:06:10.0 Off |                    0 |
        line1_base = f"|   {gpu_id}  {name}"
        line1_middle = " On  |   "
        line1_end = f"{bus_id} Off |                    0 |"
        spaces_needed = 91 - len(line1_base) - len(line1_middle) - len(line1_end)
        line1 = line1_base + " " * spaces_needed + line1_middle + line1_end
        
        # Original: | N/A   30C    P0            113W /  700W |   26626MiB /  81559MiB |      0%      Default |
        temp_str = f"{temp}C" if temp >= 10 else f" {temp}C"
        watt_str = f"{watt}W" if watt >= 100 else f" {watt}W" if watt >= 10 else f"  {watt}W"
        line2_start = f"| N/A   {temp_str}    P0            {watt_str} /  {power_cap}W |   "
        line2_end = f"{mem_used}MiB /  {mem_total} |      0%      Default |"
        spaces_needed = 91 - len(line2_start) - len(line2_end)
        line2 = line2_start + " " * spaces_needed + line2_end
        
        # Original: |                                         |                        |             Disabled |
        line3_start = "|                                         |                        |"
        line3_end = f"{mig_mode} |"
        spaces_needed = 91 - len(line3_start) - len(line3_end)
        line3 = line3_start + " " * spaces_needed + line3_end
        
        # Separator line - exactly 91 characters
        line4 = "+-----------------------------------------+------------------------+----------------------+"

        # Ensure all lines are exactly 91 characters
        lines = [line1, line2, line3, line4]
        for line in lines:
            if len(line) != 91:
                # Force to 91 characters
                if len(line) < 91:
                    line = line + " " * (91 - len(line))
                else:
                    line = line[:91]
            print(line)

    def flex(self, gpu_type: str, gpu_num: int = 1):
        gpu_type = gpu_type.lower()
        if gpu_type not in self.gpu_configs:
            print(f"Invalid gpu_type: {gpu_type}")
            return

        self.__print_date()
        self.__print_header()

        for gpu_id in range(gpu_num):
            self.__print_gpu_block(gpu_id, self.gpu_configs[gpu_type])

        # Only print empty line after all GPUs, before footer
        print(" " * 91)
        self.__print_footer()
