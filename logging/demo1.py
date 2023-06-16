import logging

logging.basicConfig(#filename = 'demo.log',
                    level = logging.DEBUG,
                    #filemode = 'w'
                    )

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