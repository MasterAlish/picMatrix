# coding=utf-8


class Pic:
    def __init__(self, pic_index, pic_weight):
        self.index = pic_index
        self.weight = pic_weight

    @staticmethod
    def convert(weights_array):
        result = []
        for pic_index in range(0, len(weights_array)):
            pic_weight = weights_array[pic_index]
            weight_object = Pic(pic_index, pic_weight)
            result.append(weight_object)
        return result

    def __unicode__(self):
        return "Pic %i: %i w" % (self.index, self.weight)

    def __repr__(self):
        return self.__unicode__()


class PicMatrix(object):
    pics = []
    volume = 400  # Емкость конечного изображения. количество ячеек в нем
    count = 0

    def __init__(self, pic_weights):
        self.pics = Pic.convert(pic_weights)
        self.count = len(pic_weights)

    def run(self):
        self.set_volume()
        self.sort_pics_by_weight()
        self.scale_weights()
        self.fix_weights()

    def set_volume(self):
        # Просто на глаз сделал
        if self.count > 50:
            self.volume = 400
        elif self.count > 35:
            self.volume = 324
        elif self.count > 25:
            self.volume = 256
        elif self.count > 20:
            self.volume = 225
        elif self.count > 15:
            self.volume = 196
        elif self.count > 12:
            self.volume = 144
        elif self.count > 10:
            self.volume = 121
        else:
            self.volume = 100

    def sort_pics_by_weight(self):
        self.pics = sorted(self.pics, key=lambda pic: pic.weight)

    def scale_weights(self):
        weights_sum = sum(map(lambda pic: pic.weight, self.pics))
        diff = float(weights_sum)/float(self.volume)
        for pic in self.pics:
            pic.weight = int(round(float(pic.weight)/diff))
            if pic.weight == 0:
                pic.weight = 1
        weights_sum = sum(map(lambda pic: pic.weight, self.pics))
        diff = self.volume - weights_sum

        while diff > 0:
            for i in range(0, len(self.pics)):
                self.pics[-(i+1)].weight += 1
                diff -= 1

        while diff < 0:
            for i in range(0, len(self.pics)):
                w = self.pics[i].weight
                if w > 1:
                    self.pics[i].weight -= 1
                    diff += 1

    def fix_weights(self):
        pass