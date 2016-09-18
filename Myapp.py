class process(object):
    def __init__(self,num):
        self.num=num
    def show(self):
        print self.num



#
# service_opts = [
#     cfg.StrOpt('username',
#                default='default',
#                help='user name'),
#     cfg.StrOpt('password',
#                help='password')
# ]
#
#
# rabbit_group = cfg.OptGroup(
#     name='rabbit',
#     title='RabbitMQ options'
# )
#
#
# rabbit_Opts = [
#     cfg.StrOpt('host',
#                default='localhost',
#                help='IP/hostname to listen on.'),
#     cfg.IntOpt('port',
#                default=5672,
#                help='Port number to listen on.')
# ]
#
#
# CONF = cfg.CONF
#
# CONF.register_opts(service_opts)
#
# CONF.register_group(rabbit_group)
#
# CONF.register_opts(rabbit_Opts, rabbit_group)
#
# print netutils.get_my_ipv4()
# CONF(sys.argv[1:], default_config_files=['app.conf'])
#
# print ("username=%s  rabbitmq.host=%s " % (CONF.username, CONF.rabbit.host))
