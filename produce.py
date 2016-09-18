from oslo_config import cfg
import oslo_messaging as om

rabbit_host_opts = [cfg.StrOpt('rabbit_host',default='10.0.0.20',help='IP/hostname to listen on'),
                    cfg.IntOpt('rabbit_port',default=5672,help='IP/hostname to listen on'),
                     cfg.StrOpt('rabbit_userid',default='guest1',help='user'),
                     cfg.StrOpt('rabbit_password',default='cloud',help='pass'),
                    cfg.StrOpt('rabbit_login_method', default='AMQPLAIN', help='user'),
                    cfg.StrOpt('rabbit_virtual_host', default='/', help='pass'),
                    # cfg.StrOpt('rpc_backend', default='rabbit', help='user'),
 ]
conf = cfg.CONF

# conf.register_opts(rabbit_host_opts)
res = [{k:v} for k, v in cfg.CONF.iteritems()]
print res
transport = om.get_transport(cfg.CONF,url='rabbit://guest1:cloud@10.0.0.20:5672')

target = om.Target(topic='test',server='10.0.0.6')
client = om.RPCClient(transport, target)
arg = "Saju"
ctxt = {}
client.cast(ctxt, 'test_method1', arg=arg)