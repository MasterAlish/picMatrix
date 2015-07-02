# coding=utf-8
import math


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
    almost_sqr_nums = [1, 2, 4, 6, 9, 12, 16, 20, 24, 25, 30, 35, 36, 42, 48, 49, 54, 56, 63, 64, 70, 72, 80, 81, 88, 90, 96, 99, 100, 108, 110, 117, 120, 121, 130, 132, 140, 143, 144, 150, 154, 156, 165, 168, 169, 176, 180, 182, 192, 195, 196, 204, 208, 210, 216, 221, 224, 225, 234, 238, 240, 247, 252, 255, 256, 266, 270, 272, 280, 285, 288, 289, 294, 300, 304, 306, 315, 320, 323, 324, 330, 336, 340, 342, 352, 357, 360, 361, 368, 374, 378, 380, 384, 391, 396, 399]  # Околоквдратные чияла до 400
    closest_almost_sqr_nums = {1: [1, 2], 2: [2, 4], 3: [2, 4], 4: [4, 6], 5: [4, 6], 6: [6, 9], 7: [6, 9], 8: [6, 9], 9: [9, 12], 10: [9, 12], 11: [9, 12], 12: [12, 16], 13: [12, 16], 14: [12, 16], 15: [12, 16], 16: [16, 20], 17: [16, 20], 18: [16, 20], 19: [16, 20], 20: [20, 24], 21: [20, 24], 22: [20, 24], 23: [20, 24], 24: [24, 25], 25: [25, 30], 26: [25, 30], 27: [25, 30], 28: [25, 30], 29: [25, 30], 30: [30, 35], 31: [30, 35], 32: [30, 35], 33: [30, 35], 34: [30, 35], 35: [35, 36], 36: [36, 42], 37: [36, 42], 38: [36, 42], 39: [36, 42], 40: [36, 42], 41: [36, 42], 42: [42, 48], 43: [42, 48], 44: [42, 48], 45: [42, 48], 46: [42, 48], 47: [42, 48], 48: [48, 49], 49: [49, 54], 50: [49, 54], 51: [49, 54], 52: [49, 54], 53: [49, 54], 54: [54, 56], 55: [54, 56], 56: [56, 63], 57: [56, 63], 58: [56, 63], 59: [56, 63], 60: [56, 63], 61: [56, 63], 62: [56, 63], 63: [63, 64], 64: [64, 70], 65: [64, 70], 66: [64, 70], 67: [64, 70], 68: [64, 70], 69: [64, 70], 70: [70, 72], 71: [70, 72], 72: [72, 80], 73: [72, 80], 74: [72, 80], 75: [72, 80], 76: [72, 80], 77: [72, 80], 78: [72, 80], 79: [72, 80], 80: [80, 81], 81: [81, 88], 82: [81, 88], 83: [81, 88], 84: [81, 88], 85: [81, 88], 86: [81, 88], 87: [81, 88], 88: [88, 90], 89: [88, 90], 90: [90, 96], 91: [90, 96], 92: [90, 96], 93: [90, 96], 94: [90, 96], 95: [90, 96], 96: [96, 99], 97: [96, 99], 98: [96, 99], 99: [99, 100], 100: [100, 108], 101: [100, 108], 102: [100, 108], 103: [100, 108], 104: [100, 108], 105: [100, 108], 106: [100, 108], 107: [100, 108], 108: [108, 110], 109: [108, 110], 110: [110, 117], 111: [110, 117], 112: [110, 117], 113: [110, 117], 114: [110, 117], 115: [110, 117], 116: [110, 117], 117: [117, 120], 118: [117, 120], 119: [117, 120], 120: [120, 121], 121: [121, 130], 122: [121, 130], 123: [121, 130], 124: [121, 130], 125: [121, 130], 126: [121, 130], 127: [121, 130], 128: [121, 130], 129: [121, 130], 130: [130, 132], 131: [130, 132], 132: [132, 140], 133: [132, 140], 134: [132, 140], 135: [132, 140], 136: [132, 140], 137: [132, 140], 138: [132, 140], 139: [132, 140], 140: [140, 143], 141: [140, 143], 142: [140, 143], 143: [143, 144], 144: [144, 150], 145: [144, 150], 146: [144, 150], 147: [144, 150], 148: [144, 150], 149: [144, 150], 150: [150, 154], 151: [150, 154], 152: [150, 154], 153: [150, 154], 154: [154, 156], 155: [154, 156], 156: [156, 165], 157: [156, 165], 158: [156, 165], 159: [156, 165], 160: [156, 165], 161: [156, 165], 162: [156, 165], 163: [156, 165], 164: [156, 165], 165: [165, 168], 166: [165, 168], 167: [165, 168], 168: [168, 169], 169: [169, 176], 170: [169, 176], 171: [169, 176], 172: [169, 176], 173: [169, 176], 174: [169, 176], 175: [169, 176], 176: [176, 180], 177: [176, 180], 178: [176, 180], 179: [176, 180], 180: [180, 182], 181: [180, 182], 182: [182, 192], 183: [182, 192], 184: [182, 192], 185: [182, 192], 186: [182, 192], 187: [182, 192], 188: [182, 192], 189: [182, 192], 190: [182, 192], 191: [182, 192], 192: [192, 195], 193: [192, 195], 194: [192, 195], 195: [195, 196], 196: [196, 204], 197: [196, 204], 198: [196, 204], 199: [196, 204], 200: [196, 204], 201: [196, 204], 202: [196, 204], 203: [196, 204], 204: [204, 208], 205: [204, 208], 206: [204, 208], 207: [204, 208], 208: [208, 210], 209: [208, 210], 210: [210, 216], 211: [210, 216], 212: [210, 216], 213: [210, 216], 214: [210, 216], 215: [210, 216], 216: [216, 221], 217: [216, 221], 218: [216, 221], 219: [216, 221], 220: [216, 221], 221: [221, 224], 222: [221, 224], 223: [221, 224], 224: [224, 225], 225: [225, 234], 226: [225, 234], 227: [225, 234], 228: [225, 234], 229: [225, 234], 230: [225, 234], 231: [225, 234], 232: [225, 234], 233: [225, 234], 234: [234, 238], 235: [234, 238], 236: [234, 238], 237: [234, 238], 238: [238, 240], 239: [238, 240], 240: [240, 247], 241: [240, 247], 242: [240, 247], 243: [240, 247], 244: [240, 247], 245: [240, 247], 246: [240, 247], 247: [247, 252], 248: [247, 252], 249: [247, 252], 250: [247, 252], 251: [247, 252], 252: [252, 255], 253: [252, 255], 254: [252, 255], 255: [255, 256], 256: [256, 266], 257: [256, 266], 258: [256, 266], 259: [256, 266], 260: [256, 266], 261: [256, 266], 262: [256, 266], 263: [256, 266], 264: [256, 266], 265: [256, 266], 266: [266, 270], 267: [266, 270], 268: [266, 270], 269: [266, 270], 270: [270, 272], 271: [270, 272], 272: [272, 280], 273: [272, 280], 274: [272, 280], 275: [272, 280], 276: [272, 280], 277: [272, 280], 278: [272, 280], 279: [272, 280], 280: [280, 285], 281: [280, 285], 282: [280, 285], 283: [280, 285], 284: [280, 285], 285: [285, 288], 286: [285, 288], 287: [285, 288], 288: [288, 289], 289: [289, 294], 290: [289, 294], 291: [289, 294], 292: [289, 294], 293: [289, 294], 294: [294, 300], 295: [294, 300], 296: [294, 300], 297: [294, 300], 298: [294, 300], 299: [294, 300], 300: [300, 304], 301: [300, 304], 302: [300, 304], 303: [300, 304], 304: [304, 306], 305: [304, 306], 306: [306, 315], 307: [306, 315], 308: [306, 315], 309: [306, 315], 310: [306, 315], 311: [306, 315], 312: [306, 315], 313: [306, 315], 314: [306, 315], 315: [315, 320], 316: [315, 320], 317: [315, 320], 318: [315, 320], 319: [315, 320], 320: [320, 323], 321: [320, 323], 322: [320, 323], 323: [323, 324], 324: [324, 330], 325: [324, 330], 326: [324, 330], 327: [324, 330], 328: [324, 330], 329: [324, 330], 330: [330, 336], 331: [330, 336], 332: [330, 336], 333: [330, 336], 334: [330, 336], 335: [330, 336], 336: [336, 340], 337: [336, 340], 338: [336, 340], 339: [336, 340], 340: [340, 342], 341: [340, 342], 342: [342, 352], 343: [342, 352], 344: [342, 352], 345: [342, 352], 346: [342, 352], 347: [342, 352], 348: [342, 352], 349: [342, 352], 350: [342, 352], 351: [342, 352], 352: [352, 357], 353: [352, 357], 354: [352, 357], 355: [352, 357], 356: [352, 357], 357: [357, 360], 358: [357, 360], 359: [357, 360], 360: [360, 361], 361: [361, 368], 362: [361, 368], 363: [361, 368], 364: [361, 368], 365: [361, 368], 366: [361, 368], 367: [361, 368], 368: [368, 374], 369: [368, 374], 370: [368, 374], 371: [368, 374], 372: [368, 374], 373: [368, 374], 374: [374, 378], 375: [374, 378], 376: [374, 378], 377: [374, 378], 378: [378, 380], 379: [378, 380], 380: [380, 384], 381: [380, 384], 382: [380, 384], 383: [380, 384], 384: [384, 391], 385: [384, 391], 386: [384, 391], 387: [384, 391], 388: [384, 391], 389: [384, 391], 390: [384, 391], 391: [391, 396], 392: [391, 396], 393: [391, 396], 394: [391, 396], 395: [391, 396], 396: [396, 399], 397: [396, 399], 398: [396, 399], 399: [396, 399], 400: [399, 400]}

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
        pic_weights = map(lambda pic: pic.weight, self.pics)
        extra_weight = self.round_weights(pic_weights)
        print(pic_weights)
        print(extra_weight)

    def is_almost_sqr_num(self, x):
        if x < 3:
            return True
        y = int(round(math.sqrt(x)))
        for i in range(y - 6 if y > 7 else 2, y+1):
            if x % i == 0:
                if x/i <= float(i)*1.5:
                    return True
        return False

    def round_weights(self, pic_weights):
        diff = 0
        for i in range(len(pic_weights)-1, 0, -1):
            weight = pic_weights[i]
            closests = self.closest_almost_sqr_nums[weight]
            new_weight = closests[0] if closests[0] == weight else closests[1]
            diff += new_weight - weight
            pic_weights[i] = new_weight
            while diff > 0:
                changed = False
                for j in range(0, i):
                    if pic_weights[j] > 1 and diff > 1:
                        pic_weights[j] -= 1
                        changed = True
                        diff -= 1
                if not changed:
                    break
        return diff



