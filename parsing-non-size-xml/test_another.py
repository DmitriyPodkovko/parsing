import pickle


class Holder:
    def __setattr__(self, name, value):
        new_name = name
        i = 1
        while hasattr(self, new_name):
            new_name = name + str(i)
            i += 1
            print('h1')
        return super().__setattr__(new_name, value)


res2 = pickle.loads(
    b'\x80\x03c__main__\nHolder\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00titleq\x03X\x0e\x00\x00\x00Demo slideshowq\x04X\x05\x00\x00\x00slideq\x05h\x00)\x81q\x06}q\x07(h\x03X\x0b\x00\x00\x00Slide titleq\x08X\x05\x00\x00\x00pointq\tX\x0e\x00\x00\x00This is a demoq\nX\x06\x00\x00\x00point1q\x0bX"\x00\x00\x00Of a program for processing slidesq\x0cubX\x06\x00\x00\x00slide1q\rh\x00)\x81q\x0e}q\x0f(h\x03X\x12\x00\x00\x00Another demo slideq\x10h\tX\x0f\x00\x00\x00It is importantq\x11X\x06\x00\x00\x00point1q\x12X\x11\x00\x00\x00To have more thanq\x13X\x06\x00\x00\x00point2q\x14X\t\x00\x00\x00one slideq\x15ubub.')
print(dir(res))