# __init__.py Nonblocking IR blaster
# Runs on Pyboard D or Pyboard 1.x (not Pyboard Lite), ESP32 and RP2

# Released under the MIT License (MIT). See LICENSE.

# Copyright (c) 2020-2021 Peter Hinch
from .rp2_rmt import RP2_RMT
from micropython import const
from array import array
from time import ticks_us, ticks_diff
# import micropython
# micropython.alloc_emergency_exception_buf(100)

# Shared by NEC
STOP = const(0)  # End of data

# IR abstract base class. Array holds periods in μs between toggling 36/38KHz
# carrier on or off. Physical transmission occurs in an ISR context controlled
# by timer 2 and timer 5. See TRANSMITTER.md for details of operation.
class IR:
    _active_high = True  # Hardware turns IRLED on if pin goes high.
    _space = 0  # Duty ratio that causes IRLED to be off
    timeit = False  # Print timing info

    @classmethod
    def active_low(cls):
        cls._active_high = False
        cls._space = 100

    def __init__(self, pin, cfreq, asize, duty, verbose):
        self._rmt = RP2_RMT(pin_pulse=None, carrier=(pin, cfreq, duty))  # 1μs resolution
        asize += 1  # Allow for possible extra space pulse  
        self._tcb = self._cb  # Pre-allocate
        self._arr = array('H', 0 for _ in range(asize))  # on/off times (μs)
        self._mva = memoryview(self._arr)
        # Subclass interface
        self.verbose = verbose
        self.carrier = False  # Notional carrier state while encoding biphase
        self.aptr = 0  # Index into array

    def _cb(self, t):  # T5 callback, generate a carrier mark or space
        t.deinit()
        p = self.aptr
        v = self._arr[p]
        if v == STOP:
            self._ch.pulse_width_percent(self._space)  # Turn off IR LED.
            return
        self._ch.pulse_width_percent(self._space if p & 1 else self._duty)
        self._tim.init(prescaler=84, period=v, callback=self._tcb)
        self.aptr += 1

    # Public interface
    # Before populating array, zero pointer, set notional carrier state (off).
    def transmit(self, addr, data, toggle=0, validate=False):  # NEC: toggle is unused
        t = ticks_us()
        if validate:
            if addr > self.valid[0] or addr < 0:
                raise ValueError('Address out of range', addr)
            if data > self.valid[1] or data < 0:
                raise ValueError('Data out of range', data)
            if toggle > self.valid[2] or toggle < 0:
                raise ValueError('Toggle out of range', toggle)
        self.aptr = 0  # Inital conditions for tx: index into array
        self.carrier = False
        self.tx(addr, data, toggle)  # Subclass populates ._arr
        self.trigger()  # Initiate transmission
        
        if self.timeit:
            dt = ticks_diff(ticks_us(), t)
            
            print('Time = {}μs'.format(dt))

    # Subclass interface
    def trigger(self):  # Used by NEC to initiate a repeat frame
            self.append(STOP)
            self._rmt.send(self._arr)
        

    def append(self, *times):  # Append one or more time peiods to ._arr
        for t in times:
            self._arr[self.aptr] = t
            self.aptr += 1
            self.carrier = not self.carrier  # Keep track of carrier state
            self.verbose and print('append', t, 'carrier', self.carrier)

    def add(self, t):  # Increase last time value (for biphase)
        assert t > 0
        self.verbose and print('add', t)
        # .carrier unaffected
        self._arr[self.aptr - 1] += t


# Given an iterable (e.g. list or tuple) of times, emit it as an IR stream.
class Player(IR):

    def __init__(self, pin, freq=38000, verbose=False):  # NEC specifies 38KHz
        super().__init__(pin, freq, 68, 33, verbose)  # Measured duty ratio 33%

    def play(self, lst):
        for x, t in enumerate(lst):
            self._arr[x] = t
        self.aptr = x + 1
        self.trigger()

