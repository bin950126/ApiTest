import os
import logging
import time


root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(root_path, 'log')


class Loggers:
    def __init__(self):
        # 定义日志位置和名称
        self.logname = os.path.join(log_path, '{}.log'.format(time.strftime('%Y-%m-%d')))
        # 定义日志容器
        self.logger = logging.getLogger('log')
        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)
        # 创建日志输入的格式
        self.formatter = logging.Formatter('%(asctime)s - %(filename)s -%(name)s - %(levelname)s - %(message)s')
        # 创建日志处理器，用来存放日志文件
        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding='utf-8')
        # 创建日志处理器，在控制台输出日志
        self.console = logging.StreamHandler()
        # 设置控制台打印日志的界别
        self.console.setLevel(logging.DEBUG)
        # 文件存放日志的级别
        self.filelogger.setLevel(logging.DEBUG)
        # 文件存放日志的格式
        self.filelogger.setFormatter(self.formatter)
        # 控制台打印日志的格式
        self.console.setFormatter(self.formatter)
        # 将日志处理器添加到日志容器中
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


logger = Loggers().logger

if __name__ == '__main__':
    logger.debug('debug message')
