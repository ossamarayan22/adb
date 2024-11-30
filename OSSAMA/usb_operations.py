import usb.core
import usb.util

def find_device(vendor_id, product_id):
    """Find a USB device by vendor and product ID."""
    device = usb.core.find(idVendor=vendor_id, idProduct=product_id)
    if device is None:
        raise ValueError("Device not found")
    return device

def read_data_from_device(device):
    """Read raw data from the USB device."""
    try:
        device.set_configuration()
        endpoint = device[0][(0, 0)][0]
        data = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
        return data
    except Exception as e:
        return f"Error: {str(e)}"
