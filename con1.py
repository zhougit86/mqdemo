#
# from oslo_config import cfg
# from oslo_utils import netutils
# from oslo_utils import importutils
# from oslo_messaging import serializer as om_serializer
# from osprofiler import profiler
# import oslo_messaging
#
#
# rabbit_group = cfg.OptGroup(name='oslo_messaging_rabbit',title='messaging_rabbit')
#
# rabbit_host_opts = [cfg.StrOpt('rabbit_host',default='localhost',help='IP/hostname to listen on'),
#                     cfg.StrOpt('rabbit_userid',default='aaa',help='user'),
#                     cfg.StrOpt('rabbit_password',default='bbb',help='pass'),
# ]
# conf = cfg.CONF
# conf.register_group(rabbit_group)
# conf.register_opts(rabbit_host_opts, rabbit_group)
# conf(default_config_files=['app.conf'])
#
# ALLOWED_EXMODS = []
# EXTRA_EXMODS = []
# print conf.oslo_messaging_rabbit.rabbit_host
#
# def get_allowed_exmods():
#     return ALLOWED_EXMODS + EXTRA_EXMODS
#
# TRANSPORT_ALIASES = {
#     'neutron.openstack.common.rpc.impl_fake': 'fake',
#     'neutron.openstack.common.rpc.impl_qpid': 'qpid',
#     'neutron.openstack.common.rpc.impl_kombu': 'rabbit',
#     'neutron.openstack.common.rpc.impl_zmq': 'zmq',
#     'neutron.rpc.impl_fake': 'fake',
#     'neutron.rpc.impl_qpid': 'qpid',
#     'neutron.rpc.impl_kombu': 'rabbit',
#     'neutron.rpc.impl_zmq': 'zmq',
# }
# exmods = get_allowed_exmods()
# TRANSPORT = oslo_messaging.get_transport(conf,allowed_remote_exmods=exmods)
#
# class RequestContextSerializer(om_serializer.Serializer):
#     """This serializer is used to convert RPC common context into
#     Neutron Context.
#     """
#     def __init__(self, base=None):
#         super(RequestContextSerializer, self).__init__()
#         self._base = base
#
#     def serialize_entity(self, ctxt, entity):
#         if not self._base:
#             return entity
#         return self._base.serialize_entity(ctxt, entity)
#
#     def deserialize_entity(self, ctxt, entity):
#         if not self._base:
#             return entity
#         return self._base.deserialize_entity(ctxt, entity)
#
#     def serialize_context(self, ctxt):
#         _context = ctxt.to_dict()
#         prof = profiler.get()
#         if prof:
#             trace_info = {
#                 "hmac_key": prof.hmac_key,
#                 "base_id": prof.get_base_id(),
#                 "parent_id": prof.get_id()
#             }
#             _context['trace_info'] = trace_info
#         return _context
#
#     def deserialize_context(self, ctxt):
#         rpc_ctxt_dict = ctxt.copy()
#         trace_info = rpc_ctxt_dict.pop("trace_info", None)
#         if trace_info:
#             profiler.init(**trace_info)
#         user_id = rpc_ctxt_dict.pop('user_id', None)
#         if not user_id:
#             user_id = rpc_ctxt_dict.pop('user', None)
#         tenant_id = rpc_ctxt_dict.pop('tenant_id', None)
#         if not tenant_id:
#             tenant_id = rpc_ctxt_dict.pop('project_id', None)
#         return context.Context(user_id, tenant_id, **rpc_ctxt_dict)
#
# def get_server(target, endpoints, serializer=None):
#     assert TRANSPORT is not None
#     serializer = RequestContextSerializer(serializer)
#     return oslo_messaging.get_rpc_server(TRANSPORT, target, endpoints,
#                                          'eventlet', serializer)
#
# target=oslo_messaging.Target(topic='test',server=netutils.get_my_ipv4(),fanout=False)
# end=importutils.import_class('Myapp.process')
# manager = end(num=1)


from oslo_config import cfg
import oslo_messaging as om
from oslo_utils import netutils

# cfg.CONF.set_override('rabbit_host', '10.0.0.20')
# cfg.CONF.set_override('rabbit_port', 5672)
# cfg.CONF.set_override('rabbit_userid', 'guest')
# cfg.CONF.set_override('rabbit_password', 'cloud')
# cfg.CONF.set_override('rabbit_login_method', 'AMQPLAIN')
# cfg.CONF.set_override('rabbit_virtual_host', '/')
# cfg.CONF.set_override('rpc_backend', 'rabbit')
rabbit_host_opts = [cfg.StrOpt('rabbit_host',default='10.0.0.20',help='IP/hostname to listen on'),
                    cfg.IntOpt('rabbit_port',default=5672,help='IP/hostname to listen on'),
                     cfg.StrOpt('rabbit_userid',default='guest1',help='user'),
                     cfg.StrOpt('rabbit_password',default='cloud',help='pass'),
                    cfg.StrOpt('rabbit_login_method', default='AMQPLAIN', help='user'),
                    cfg.StrOpt('rabbit_virtual_host', default='/', help='passdddd'),
                    # cfg.StrOpt('rpc_backend', default='rabbit', help='userssss'),
 ]
conf = cfg.CONF

# conf.register_opts(rabbit_host_opts)
res = [{k:v} for k, v in cfg.CONF.iteritems()]
# cfg.CONF.set_override('rpc_backend', 'rabbit')
print res
transport = om.get_transport(cfg.CONF,url='rabbit://guest1:cloud@10.0.0.20:5672')
target=om.Target(topic='test',server=netutils.get_my_ipv4())
class TestEndpoint(object):
    def test_method1(self, ctx, arg):
        res = "Result from test_method1 " + str(arg)
        print res
        return res
    def test_method2(self, ctx, arg):
        res = "Result from test_method2 " + str(arg)
        print res
        return res

endpoints = [TestEndpoint(),]
server = om.get_rpc_server(transport, target, endpoints, executor='blocking')
print 'ready'
server.start()
server.wait()