from PyQt6.QtWidgets import QLabel, QApplication
from PyQt6.QtGui import QPixmap, QImage
import numpy as np

class GrainImageWidget(QLabel):
    def showImage(self, image):
        np.ma.set_fill_value(image, 0)
        image = np.logical_not(image.filled())
        image = image.astype(np.uint8) * 255
        height, width = image.shape

        # Invert colors in dark mode
        if QApplication.instance() and QApplication.instance().isDarkMode():
            image[image == 255] = 30
            image[image == 0] = 192

        qImg = QImage(image.data, width, height, QImage.Format.Format_Grayscale8)
        pixmap = QPixmap(qImg)
        self.setPixmap(pixmap)
