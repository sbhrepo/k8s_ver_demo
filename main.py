import importlib
import os
from time import sleep
import configuration

class PROCSingleton(type):
  _instances = {}
  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super(PROCSingleton, cls).__call__(*args, **kwargs)
    return cls._instances[cls]

class process_k8s_ver_demo(metaclass = PROCSingleton):
  def __init__(self):
    self.path = configuration.local_path
    self.file = configuration.file_name

  def createPath (self, path):
    if not os.path.exists(path):
      os.makedirs(path)

  def updateVersion (self, filePath):
    f = open(filePath, 'w')
    f.write(self.version)
    f.close()

  def createFile (self, filePath):
    if os.path.isfile(filePath) == False:
      print(f'{filePath} not exist')
      self.updateVersion(filePath)

  def updateFile (self, filePath):
    with open(filePath) as f:
      try:
        major_f, minor_f, patch_f = [int(x) for x in next(f).split('.')]
      except:
        print(f'No version or wrong versiobn format in the file [{filePath}]')

    try:
      major_c, minor_c, patch_c = [int(x) for x in self.version.split('.')]
    except:
      print(f'No version or wrong versiobn format in the configuration file')

    if major_c > major_f:
      print(f'{major_c}.{minor_c}.{patch_c} > {major_f}.{minor_f}.{patch_f} - update now')
      self.updateVersion(filePath)
    elif major_c == major_f and minor_c > minor_f:
      print(f'{major_c}.{minor_c}.{patch_c} > {major_f}.{minor_f}.{patch_f} - update now')
      self.updateVersion(filePath)
    elif major_c == major_f and minor_c == minor_f and patch_c > patch_f:
      print(f'{major_c}.{minor_c}.{patch_c} > {major_f}.{minor_f}.{patch_f} - update now')
      self.updateVersion(filePath)


  def run(self):
    self.createPath(self.path)
    running = True
    while running:
      importlib.reload(configuration)
      self.version = configuration.version
      self.interval = configuration.update_interval
      self.stop = configuration.stop
      if self.stop == "yes":
        running = False
    
      self.createFile(self.path+"/"+self.file)
      #self.updateFile(self.path+"/"+self.file)
      self.updateVersion(self.path+"/"+self.file)

      sleep(self.interval)

def main():
  PAdemo_proc = process_k8s_ver_demo()
  PAdemo_proc.run()

if __name__=='__main__':
  main()