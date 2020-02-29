#!/usr/bin/python3

# Power management for VR lightouses
# Usage:
#   ./lighthouse.py [on|off]

from bluepy import btle
import sys

class DiscoLH(btle.DefaultDelegate):

    def __init__(self):
        self.devices = []
        btle.DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if not isNewDev:
            return

        isLH = False
        name = dev.getValueText(0x09)

        if not name is None and name.startswith("HTC BS"):
            print('Found LightHouse %s: address = %s' %
                  (dev.getValueText(0x09), dev.addr))
            self.devices.append(dev)

if __name__ == '__main__':
    scanner = btle.Scanner()
    delegate = DiscoLH()
    scanner.withDelegate(delegate)
    scanner.scan(2)
    for device in delegate.devices:
        lh = btle.Peripheral()
        print("Connecting to %s" % (device.addr))
        lh.connect(device)

        id = b"\x00\x00\x00\x00"
        if len(sys.argv) > 1 and sys.argv[1] == 'on':
            id = b"\xff\xff\xff\xff"
        elif device.addr.endswith(":c6"):
            id = b"\x8c\x28\xd1\xf1"
        elif device.addr.endswith(":a8"):
            id = b"\x95\x27\x36\x0b"

        print("  > ID = {}".format(id))

        print("  > Services:")
        for service in lh.getServices():
            print("    > UUID: {}".format(service.uuid.getCommonName()))
            print("      > Characteristics:")
            for characteristic in service.getCharacteristics():
                print("        > UUID: {}".format(characteristic.uuid.getCommonName()))
                print("          > Handle: {:04x}".format(characteristic.getHandle()))
                if characteristic.supportsRead():
                    value = characteristic.read()
                    print("          > Value: {}".format(value))
                    print("          > Value (raw): {}".format(" ".join("{:02x}".format(c) for c in value)))
                else:
                    print("          > Cannot read value")
                print("          > Properties: {}".format(characteristic.propertiesToString()))

        read = lh.readCharacteristic(0x0035)
        print("  > Read 0x0035:  {}".format(" ".join("{:02x}".format(c) for c in read)))

        write = b"\x12\x02" + b"\x01\x2c" + id + (b"\x00" * 12)
        lh.writeCharacteristic(0x0035, write)
        print("  > Write 0x0035: {}".format(" ".join("{:02x}".format(c) for c in write)))

        read = lh.readCharacteristic(0x0035)
        print("  > Read 0x0035:  {}".format(" ".join("{:02x}".format(c) for c in read)))
        
        lh.disconnect()
