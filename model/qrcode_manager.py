import cv2
import qrcode
from qrcode.constants import ERROR_CORRECT_L

class QrCodeManager:

    OUTPUT_DIRECTORY = 'output/'

    def __init__(self, filename):
        self.filename = filename
        self.file_path = ''
        self.data = ''
        self.options = []

    # create QR Code
    def create(self, data, options=[]):
        self.data = data
        self.compute_output_file_path()

        if(len(options) != 0):
            self.options = options
            self.generate_customized_qrcode()
        else:
            self.generate_simple_qrcode()

    # create simple QR Code
    def generate_simple_qrcode(self):
        img = qrcode.make(self.data)
        img.save(self.file_path)

    # create customized QR Code
    def generate_customized_qrcode(self):
        qr = qrcode.QRCode(
            version=3,
            error_correction=ERROR_CORRECT_L,
            box_size=self.options['size'],
            border=2
        )
        qr.add_data(self.data)
        qr.make(fit=True)

        img = qr.make_image(
            fill_color=self.options['fill_color'],
            back_color=self.options['back_color'])
        img.save(self.file_path)

    def compute_output_file_path(self):
        self.file_path = ''.join(
            (self.OUTPUT_DIRECTORY, self.filename, '.png'))

    # get QR Code data
    def read(self):
        detector = cv2.QRCodeDetector()
        # ignoring the third returned value with '_'
        val, points, _ = detector.detectAndDecode(
            cv2.imread(self.filename + '.png'))

        # QR Code detected
        if points is not None:
            print('QR Code data :', val)
            # store QR Code data in txt file
            with open(self.filename + '_data.txt', 'w') as file:
                file.write(str(val))
        else:
            print('QR code not detected')
