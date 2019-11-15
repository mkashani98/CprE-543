import serial,time,numpy

class Connect:
    #global variables
    Port = '/dev/ttyUSB0'
    Baudrate = 115200
    Serial = None

    Error = {'port': "Port can't be found.\n\
        Change the port using toSerial(port = \'/dev/ttyUSB0\',baudrate = 115200)"}

    def __init__(self,port = None, baudrate =None):
        if port is not None:
            self.Port = port
            if Baudrate is not None:
                self.Baudrate = baudrate
        try:    
            self.Serial = serial.Serial(port,baudrate)
        except:
            print(self.Error['port'])

    def __del__(self):
        if self.Serial is not None:
            self.Serial.close()


    def toSerial(self,port = None,baudrate = None):
        if port is not None:
            self.Port = port
        if Baudrate is not None:
            self.Baudrate = baudrate
        try:    
            self.Serial = serial.Serial(port,baudrate)
        except:
            print(self.Error['port'])
        return self.Serial


class Sync:
    ACK = "A\n"
    Serial = None
    serErr = False
    

    Error = {'serial': "The serial does not responding!\n\
            You should give a proper serial like\n\
            getdata(serial.Serial(port = \'/dev/ttyUSB0\',baudrate = 115200))",
            'connectionLost': "The Connection to the device suddenly lost\n\
            You should try again with a proper serial like\n\
            getdata(serial.Serial(port = \'/dev/ttyUSB0\',baudrate = 115200))",
            'dataType': "data type should be either String or Char!",
            'NoACK': "No ACK has been recieved!\n\
                Now may be they are not shynchronous!"}
    def __init__(self,serial):
        try:
            self.Serial = serial.Serial
        except:
            self.Serial = serial
        try:
            self.Serial.close()
            self.Serial.open()
        except:
            print(self.Error['serial'])
            self.serErr = True
            
        
        self.Serial.write(b'Connection started\n')
        if self.Serial.readline().decode('utf-8') != self.ACK:
            print(self.Error['noACK'])
            return

    
    #def __del__(self):

    def getData(self,serial = None):
        if serial is not None:
            self.Serial = serial
        elif self.serErr:
            print(self.Error['serial'])
            return
        try:
            data = self.Serial.readline()
            self.Serial.write(self.ACK)
            self.serErr = False
        except:
            print(self.Error['connectionLost'])
            self.serErr = True
            return
        return data.decode('utf-8')


    def sendData(self, data, serial = None):
        if serial is not None:
            self.Serial = serial
        elif self.serErr:
            print(self.Error['serial'])
            return

        try:
            data = data.encode()
        except:
            print(self.Error['dataType'])
            return
        
        try:
            
            self.Serial.write(data)
            self.serErr = False
            if self.Serial.readline().decode('utf-8') != self.ACK:
                print(self.Error['noACK'])
            
        except:
            print(self.Error['connectionLost'])
            self.serErr = True
            return
        return True
        
        
class MACAdrress:
    
    
    Warning = {'MACFormat': "Mac should be a 12 digit number base 16 !\n\
                             to Turn the warnings off try to"}
    
    
    def __init__(self,warning = None):
        
        
    
    def __del__(self):
    
    def MACToArray(self,x,warning = None):
        print(self.Warning['MACFormat'])
    

        

