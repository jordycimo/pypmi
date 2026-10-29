import subprocess

class iLOClient:
  def __init__(self, ip: str, username: str, password: str, port: int = 623):
    # create an ipmitool instance with information provided, open shell for repeated use.
    self.ipmitool = subprocess.Popen(
      ["ipmitool", "-I lanplus", f"-H {ip}", f"-P {port}", f"-U {username}", f"-P {password}", "shell"],
      stdout = subprocess.PIPE,
      text = True
    )

    # test
    output, _ = subprocess.communicate("chassis power")
