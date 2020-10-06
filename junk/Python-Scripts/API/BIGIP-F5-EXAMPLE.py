from bigsuds import BIGIP
b = BIGIP(hostname='172.16.48.136', username='admin', password='admin')
b.LocalLB.Pool.create_v2(
        pool_names = ['Python-Pool'],
        lb_methods = ['LB_METHOD_ROUND_ROBIN'],
        members = [[
                {'address': '10.1.213.233', 'port': '80'},
                {'address': '10.1.213.234', 'port': '80'},
                {'address': '10.1.213.235', 'port': '80'}]])