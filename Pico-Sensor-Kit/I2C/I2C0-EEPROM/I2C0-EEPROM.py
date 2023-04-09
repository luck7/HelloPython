from machine import Pin,I2C
import time
class  AT24C(object):
    def __init__(self,i2c_num=0,i2c_scl=9,i2c_sda=8,address=0X50,pages=32, bpp=8):
        self._address = address
        self.i2c = I2C(id=i2c_num,scl=Pin(i2c_scl),sda=Pin(i2c_sda),freq=100_000)
        self.pages = pages
        self.bpp = bpp # bytes per page
    def capacity(self):
        """Storage capacity in bytes"""
        return self.pages * self.bpp

    def write(self, addr, buf):
        """Write one or more bytes to the EEPROM starting from a specific address"""
        offset = addr % self.bpp
        partial = 0
        # partial page write
        if offset > 0:     
            partial = self.bpp - offset 
            if partial > len(buf):
                partial = len(buf)
            self.i2c.writeto_mem(self._address, addr, buf[0:partial], addrsize=8)
        time.sleep_ms(2)
        # page write
        for i in range(partial, len(buf), self.bpp):
            if i+self.bpp > len(buf):
                partial = len(buf)
            else:
                partial = i+self.bpp 
            self.i2c.writeto_mem(self._address, i+addr, buf[i:partial], addrsize=8)
            time.sleep_ms(2)
    def read(self, addr, buf):
        """Read one or more bytes from the EEPROM starting from a specific address"""
        self.i2c.writeto(self._address,bytearray([addr]))
        self.i2c.readfrom_into(self._address,buf)
        #buf=self.i2c.readfrom_mem(self._address,addr,len(buf)) 


if __name__=='__main__':
    at24c02=AT24C()
    write_str=b"hello world!"
    read_str=bytearray(len(write_str))
    
    at24c02.write(0,write_str)
    print("write_str = {},len={}".format(write_str,len(write_str)))
    at24c02.read(0,read_str)
    print("read_str  = {},len={}".format(read_str,len(read_str)))



