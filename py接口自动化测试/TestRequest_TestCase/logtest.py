import logging

#第一种方法，写入文件；想在console与文件中都写入log，请用第二种方法
# logging.basicConfig(level=logging.DEBUG,
#         format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#             datefmt='%a,%d %b %Y %H:%M:%S',
#             filename='testlog.log',
#             filemode='a')#a为追加，w为覆盖写入

# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')

#第二种方法
logger=logging.getLogger()
fh=logging.FileHandler('test.log')#文件输出的对象
ch=logging.StreamHandler()#console输出的对象
#定义的格式的对象
formatter=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)#从debug开始，想从info开始则写成logging.INFO

logger.debug('debug') 
logger.info('info') 
logger.warning('warning')
logger.error('error')
logger.critical('critical')