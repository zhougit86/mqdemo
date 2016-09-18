# print 'hello word'
#
# list=xrange(5)
# square= [x**2 for x in list]
# a,b,c=square[0:3]
# print a

# import copy
# person=['name',['saving',100]]
# a=person
# b=copy.deepcopy(person)
# a[1][1]=200
# print [id(x) for x in a,person,b]
# print person[1][1],b[1][1]


import logging
#adding the name of the file appear in the log
LOG = logging.getLogger(__name__)

# the lowest level of log to appear
logging.basicConfig(level=40)

LOG.info("Python Standard Logging")
LOG.warning("Python Standard Logging")
LOG.error("Python Standard Logging")
