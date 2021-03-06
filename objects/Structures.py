class UnetParam(object):
    def __init__(self, unet_model_path, unet_model_scale, unet_model_thrh, unet_img_size):
        self.unet_model_path = unet_model_path
        self.unet_model_scale = unet_model_scale
        self.unet_model_thrh = unet_model_thrh
        self.unet_img_size = unet_img_size


class ImgResolution(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class ImgChannelTime(object):
    def __init__(self, channel_name, img, time):
        self.name = channel_name
        self.img = img
        self.time_point = time


class Signal(object):
    def __init__(self, channel_name, intensity):
        self.name = channel_name
        self.intensity = intensity


class NucAreaData(object):
    def __init__(self, center, area):
        self.area = area
        self.center = center
        self.signals = None

    def update_signals(self, signals):
        self.signals = signals
