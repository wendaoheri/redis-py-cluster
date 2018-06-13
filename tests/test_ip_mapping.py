# -*- coding: utf-8 -*-

from rediscluster import StrictRedisCluster


def test_host_port_startup_node():
    """
    Test that it is possible to use host & port arguments as startup node args
    """
    startup_nodes = '10.25.161.126:7000,10.25.161.126:7001,10.25.161.126:7002,10.25.161.127:7000,10.25.161.127:7001,10.25.161.127:7002'
    startup_nodes = map(lambda x: {'host': x.split(':')[0], 'port': x.split(':')[1]}, startup_nodes.split(','))
    c = StrictRedisCluster(startup_nodes=startup_nodes)
    with c.pipeline() as pipe:
        pipe.set('hello', 'world')
        pipe.execute()


test_host_port_startup_node()
