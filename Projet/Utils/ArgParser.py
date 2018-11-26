import argparse


class ArgParser:
    @staticmethod
    def parse():
        parser = argparse.ArgumentParser(
            description='Relay between Oronos rocket & clients (PC/tablets).')

        parser.add_argument('-m', '--mode', help='Mode of execution', choices=['training', 'classification', 'article'], default='article')
        parser.add_argument('-i', '--input_image', help='Image to process', default='./asl_alphabet_test/A_test.jpg')
        parser.add_argument('-s', '--training_set', help='Data set', default='./asl_alphabet_test/')
        parser.add_argument('-mp', '--model_path', help='Model path', default='./TrainedModel/model.txt') 
        return parser.parse_args()