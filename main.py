from model.qrcode_manager import QrCodeManager

# create simple QR Code
manager = QrCodeManager('simple_qrcode')
manager.create('https://github.com')

# create customized QR Code
manager = QrCodeManager('customized_qrcode')
manager.create('Q5V8-c44v-Lq6h-6gBS', {
    'size': 50,
    'fill_color': '#004080',
    'back_color': '#a0e0ff'
})

# read first QR Code (store data in a .txt file)
manager = QrCodeManager('output/simple_qrcode')
manager.read()

# read second QR Code (store data in a .txt file)
manager = QrCodeManager('output/customized_qrcode')
manager.read()
