from Recognizing import cube_recognizing_from_video_stream
from Processing import ImageProcessor
from Serial import SerialPortFacade

import serial

CAM_NUM = 0
PORT_ADDRESS =""

if __name__ == '__main__':
    cube_recognizing_from_video_stream(CAM_NUM, ImageProcessor(), SerialPortFacade(PORT_ADDRESS, 115200))

