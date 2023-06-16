import logging

logging.basicConfig(
                    format = "%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s | %(message)s",
                    datefmt="%Y-%M-%d %H:%M:%S",
                    level = logging.DEBUG,
                    )
#可以设置进程号和线程号

print('learn logging')
logging.debug('This is Debug log')
logging.info('This is info log')
logging.warning('This is warning log')
logging.error('This is error log')
logging.critical('This is critical log')

name = 'zhang'
age = 18
logging.debug('姓名： %s ,年龄：%d',name,age)
logging.debug('姓名： %s ,年龄：%d' %(name,age))
logging.debug('姓名： {} ,年龄：{}'.format(name,age))
logging.debug(f'姓名：{name},年龄{age}')