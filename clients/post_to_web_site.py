import requests,bs4,argparse
from utils import generate_bench_case,bench_case_list,get_csrf_token,init_session,generate_host_info

web_site_root_url  ="http://127.0.0.1:8080/"
add_host_info_url  ="{0}{1}".format(web_site_root_url,"mysqlbench/add/host/info/")
add_bench_case_url ="{0}{1}".format(web_site_root_url,"mysqlbench/add/bench/case/")
add_bench_case_instance_url ="{0}{1}".format(web_site_root_url,"mysqlbench/add/bench/case/instance/")

def post_host_info(session,name,os,cores,memorys,disks,is_log_ssd,is_data_ssd):
    """
    提交主机信息到网站后台
    """
    data=generate_host_info(name=name,os=os,cores=cores,memorys=memorys,disks=disks,is_log_ssd=is_log_ssd,is_data_ssd=is_data_ssd)
    r=session.get(add_host_info_url)
    csrf_token=get_csrf_token(r.text)
    data.update(csrf_token)
    session.post(add_host_info_url,data=data)

def post_bench_case(session,host_info,mysql_version,variable_name,bench_type,detail):
    """
    提交测试用例到网站后台
    """
    if bench_type=="all":
        benchs=['bulk_insert','oltp_delete','oltp_insert','oltp_point_select','oltp_read_only',
            'oltp_read_write','oltp_update_index','oltp_update_non_index','oltp_write_only']
        for bench_type in benchs:
            data=generate_bench_case(host_info,mysql_version,variable_name,bench_type,'sysbench标准测试用例{0}'.format(bench_type))
            print(data)
            r=session.get(add_bench_case_url)
            csrf_token=get_csrf_token(r.text)
            data.update(csrf_token)
            session.post(add_bench_case_url,data=data)  
    else:
        data=generate_bench_case(host_info,mysql_version,variable_name,bench_type,'sysbench标准测试用例{0}'.format(bench_type))
        print(data)
        r=session.get(add_bench_case_url)
        csrf_token=get_csrf_token(r.text)
        data.update(csrf_token)
        session.post(add_bench_case_url,data=data)

def post_bench_case_instance(session,host_info,mysql_version,variable_name,bench_type,
                                workers,variable_value,truncations_per_seconde,query_per_seconde,duration=0):
    """
    """
    data = {
        'host_info':host_info,
        'mysql_version':mysql_version,
        'variable_name':variable_name,
        'bench_type': bench_type,
        'workers': workers,
        'variable_value': variable_value,
        'truncations_per_seconde': truncations_per_seconde,
        'query_per_seconde': query_per_seconde,
        'duration': duration
    }
    print(data)
    r = session.get(add_bench_case_instance_url)
    csrf_token=get_csrf_token(r.text)
    data.update(csrf_token)
    r=session.post(add_bench_case_instance_url,data=data)
    print(r.text)
    




if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--name',default='2C4G128G',help='host name info')
    parser.add_argument('--os',default='centos-7.2',help='opration system version')
    parser.add_argument('--cores',default=2, type=int,help='cpu cores')
    parser.add_argument('--memorys',default=4,type=int,help='memory size')
    parser.add_argument('--disks',default=128,type=int,help='disk size')
    parser.add_argument('--host-info',default='2C4G128G',help='host name info')
    parser.add_argument('--mysql-version',default='mysql-5.7.20',help='mysql version')
    parser.add_argument('--variable-name',default='autocommit',help='mysql variable name')
    parser.add_argument('--bench-type',default='olpt_insert',help='sysbench test case name')
    parser.add_argument('--workers',default=1,type=int,help='parallel thread')
    parser.add_argument('--variable-value',default=1,help='variable value')
    parser.add_argument('--truncations-per-seconde',default=0,type=int,help='tps')
    parser.add_argument('--query_per_seconde',default=0,type=int,help='qps')
    parser.add_argument('--duration',default=0,type=float,help='duration')
    parser.add_argument('action')
    args=parser.parse_args()

    session =init_session(web_site_root_url)

    if args.action == "host_info":
        post_host_info(session=session,name=args.name,os=args.os,cores=args.cores,memorys=args.memorys,disks=args.disks,is_log_ssd=False,is_data_ssd=False)
    elif args.action == 'bench_case':
        post_bench_case(session,args.host_info,args.mysql_version,args.variable_name,args.bench_type,'')
    elif args.action == 'bench_case_instance':
        post_bench_case_instance(session,args.host_info,args.mysql_version,args.variable_name,
                                args.bench_type,args.workers,args.variable_value,args.truncations_per_seconde,
                                args.query_per_seconde,args.duration)






