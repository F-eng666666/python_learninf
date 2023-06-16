import logging

#编程的方式来写一下高级的写法

#记录器
logger =  logging.getLogger('applog')
#logger.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)

#处理器handler
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

#没有给fileHandler指定日志级别，将使用logger的级别
fileHandler = logging.FileHandler(filename = 'addDemo.log')
fileHandler.setLevel (logging.DEBUG)

#formater格式
formatter = logging.Formatter("%(asctime)s|%(levelname)-8s|%(filename)20s:%(lineno)s | %(message)s")

#给处理器创建格式
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

#给记录器设置处理器
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

#定义一个过滤器
flt = logging.Filter( "cn.cccb")

#关联过滤器
#logger.addFilter(flt)
fileHandler.addFilter(flt)


#打印日志
logger.debug('This is Debug log')
logger.info('This is info log')
logger.warning('This is warning log')
logger.error('This is error log')
logger.critical('This is critical log')