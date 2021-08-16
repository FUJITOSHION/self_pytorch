import argparse
import os
import urllib.request
import zipfile


class MakeData():
    def __init__(self, conf):
        self.data_dir = './data_' + conf.part
        if not os.path.exists(self.data_dir):
            os.mkdir(self.data_dir)

    def generate(self):
        print('No generate')


class FirstMakeData(MakeData):
    def __init__(self, conf):
        super().__init__(conf)
        self.json_url = "https://s3.amazonaws.com/deep-learning-models/image-models/imagenet_class_index.json"
        self.json_save_path = os.path.join(
            self.data_dir, "imagenet_class_index.json")
        self.url = "https://download.pytorch.org/tutorial/hymenoptera_data.zip"
        self.save_path = os.path.join(self.data_dir, "hymenoptera_data.zip")

    def generate(self):
        if not os.path.exists(self.json_save_path):
            urllib.request.urlretrieve(self.json_url, self.json_save_path)

        if not os.path.exists(self.save_path):
            urllib.request.urlretrieve(self.url, self.save_path)

            # ZIPファイルを読み込み
            zip = zipfile.ZipFile(self.save_path)
            zip.extractall(self.data_dir)  # ZIPを解凍
            zip.close()  # ZIPファイルをクローズ

            # ZIPファイルを消去
            os.remove(self.save_path)


if __name__ == "__main__":
    ch_dict = {'ch01': FirstMakeData}
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--part', default='ch01')
    conf = parser.parse_args()

    make_data_class = ch_dict[conf.part](conf)
    make_data_class.generate()
