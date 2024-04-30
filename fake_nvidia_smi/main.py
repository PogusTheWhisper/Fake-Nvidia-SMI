import datetime
import random
import string

class Fake_Nvidia_SMI:
    def __init__(self):
      pass

    @staticmethod
    def __date():
      now = datetime.datetime.now()
      current_time = now.strftime("%a %b %d %H:%M:%S %Y")
      print(current_time)

    @staticmethod
    def __header():
      header = ["+---------------------------------------------------------------------------------------+",
                "| NVIDIA-SMI 535.104.05             Driver Version: 535.104.05   CUDA Version: 12.2     |",
                "|-----------------------------------------+----------------------+----------------------+",
                "| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |",
                "| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |",
                "|                                         |                      |               MIG M. |",
                "|=========================================+======================+======================|"]
      for line in header:
        print(line)

    @staticmethod
    def __footer():
      footer = ["+---------------------------------------------------------------------------------------+",
                "| Processes:                                                                            |",
                "|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |",
                "|        ID   ID                                                             Usage      |",
                "|=======================================================================================|",
                "|  No running processes found                                                           |",
                "+---------------------------------------------------------------------------------------+"]
      for line in footer:
        print(line)

    @staticmethod
    def __generate_serial():
      while True:
        serial = "".join(random.choices(string.ascii_uppercase + string.digits, k=2))
        if not serial.isalpha():
          return serial

    def __h100(self, gpu_num):
      for gpu_num in range(gpu_num):
        serial = self.__generate_serial()
        now_watt = random.randint(120, 130)
        temp = random.randint(50, 55)
        h100_status = [f"|   {gpu_num}  NVIDIA H100 PCI...            Off  | 00000000:{serial}:00.0 Off |                    0 |",
                       f"| N/A   {temp}C    P0             {now_watt}W / 500W |      0MiB / 40536MiB |      0%      Default |",
                        "|                                         |                      |                  N/A |",
                        "+-----------------------------------------+----------------------+----------------------+"]
        for line in h100_status:
          print(line)

    def __a100(self, gpu_num):
      for gpu_num in range(gpu_num):
        serial = self.__generate_serial()
        now_watt = random.randint(40, 60)
        temp = random.randint(30, 40)
        a100_status = [f"|   {gpu_num}  NVIDIA A100-SXM...            Off  | 00000000:{serial}:00.0 Off |                    0 |",
                       f"| N/A   {temp}C    P0              {now_watt}W / 400W |      0MiB / 40536MiB |      0%      Default |",
                        "|                                         |                      |                  N/A |",
                        "+-----------------------------------------+----------------------+----------------------+"]
        for line in a100_status:
          print(line)

    def __v100(self, gpu_num):
      for gpu_num in range(gpu_num):
        serial = self.__generate_serial()
        now_watt = random.randint(80, 90)
        temp = random.randint(40, 45)
        v100_status = [f"|   {gpu_num}  Tesla V100-SXM4...            Off  | 00000000:{serial}:00.0 Off |                    0 |",
                       f"| N/A   {temp}C    P0              {now_watt}W / 300W |      0MiB / 16160MiB |      0%      Default |",
                        "|                                         |                      |                  N/A |",
                        "+-----------------------------------------+----------------------+----------------------+"]
        for line in v100_status:
          print(line)

    def __p100(self, gpu_num):
      for gpu_num in range(gpu_num):
        serial = self.__generate_serial()
        now_watt = random.randint(60, 70)
        temp = random.randint(35, 40)
        p100_status = [f"|   {gpu_num}  Tesla P100-PCIE...            Off  | 00000000:{serial}:00.0 Off |                    0 |",
                       f"| N/A   {temp}C    P0              {now_watt}W / 250W |      0MiB / 16280MiB |      0%      Default |",
                        "|                                         |                      |                  N/A |",
                        "+-----------------------------------------+----------------------+----------------------+"]
        for line in p100_status:
          print(line)

    def __k80(self, gpu_num):
      for gpu_num in range(gpu_num):
        serial = self.__generate_serial()
        now_watt = random.randint(80, 99)
        temp = random.randint(40, 50)
        k80_status = [f"|   {gpu_num}  Tesla K80                      Off | 00000000:{serial}:00.0 Off |                    0 |",
                      f"| N/A   {temp}C    P0              {now_watt}W / 300W |      0MiB / 12288MiB |      0%      Default |",
                       "|                                         |                      |                  N/A |",
                       "+-----------------------------------------+----------------------+----------------------+"]
        for line in k80_status:
          print(line)

    def __t4(self, gpu_num):
      for gpu_num in range(gpu_num):
        serial = self.__generate_serial()
        now_watt = random.randint(50, 60)
        temp = random.randint(30, 35)
        t4_status = [f"|   {gpu_num}  Tesla T4                       Off | 00000000:{serial}:00.0 Off |                    0 |",
                     f"| N/A   {temp}C    P0              {now_watt}W /  70W |      0MiB / 15109MiB |      0%      Default |",
                      "|                                         |                      |                  N/A |",
                      "+-----------------------------------------+----------------------+----------------------+"]
        for line in t4_status:
          print(line)

    def flex(self, gpu_type, gpu_num=1):
      self.__date()
      self.__header()

      if gpu_type == 'h100':
          self.__h100(gpu_num)

      elif gpu_type == 'a100':
          self.__a100(gpu_num)

      elif gpu_type == 'v100':
          self.__v100(gpu_num)

      elif gpu_type == 'p100':
        self.__p100(gpu_num)

      elif gpu_type == 'k80':
        self.__k80(gpu_num)

      elif gpu_type == 't4':
        self.__t4(gpu_num)
      else:
          print(f"Invalid gpu_type: {gpu_type}")

      print("                                                                               ")
      self.__footer()