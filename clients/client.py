import requests,bs4,argparse
from utils import log_parser

web_site_root_url  ="http://127.0.0.1:8080/"
add_host_info_url  ="{0}{1}".format(web_site_root_url,"mysqlbench/add/host/info/")
add_bench_case_url ="{0}{1}".format(web_site_root_url,"mysqlbench/add/bench/case/")
add_bench_case_instance_url ="{0}{1}".format(web_site_root_url,"mysqlbench/add/bench/case/instance/")

if __name__ == "__main__":
    #1连接到网站
    session = requests.Session()
    session.get(web_site_root_url)

    #2.0增加主机信息
    response=session.get(add_host_info_url)
    #2.1解析出页面的csrf值
    html           = response.text
    soup           = bs4.BeautifulSoup(html,'html.parser')
    csrf_token     = soup.find(attrs={'name':'csrfmiddlewaretoken'})
    host_data_form = {'csrfmiddlewaretoken':csrf_token['value']}

    #2.2 增加主机相关数据
    host_data_form.update({
            'name':'24C128G4000G',
            'os':'centos-7.2',
            'cores':24,
            'memorys':128,
            'disks':4000,
            'is_log_ssd':False,
            'is_data_ssd': False
                })
    #2.3 发送信息到服务器
    session.post(add_host_info_url,data=host_data_form)

    #3.0 提交测试用例数据到服务器
    bench_case_instances = log_parser.parser_sysbench_log()
    for x in bench_case_instances:
        bench_case_data_form = {
            'host_info': '24C128G4000G',
            'mysql_version': 'mysql-5.7.21',
            'variable_name': x['variable_name'],
            'bench_type':x['bench_type'],
            'detail':'无'
        }
        #3.1 
        response=session.get(add_bench_case_url)
        html           = response.text
        soup           = bs4.BeautifulSoup(html,'html.parser')
        csrf_token     = soup.find(attrs={'name':'csrfmiddlewaretoken'})
        bench_case_data_form.update({'csrfmiddlewaretoken':csrf_token['value']})
        response=session.post(add_bench_case_url,data=bench_case_data_form)
        #print(bench_case_data_form)

    #4.0 提交测试用例实例数据到服务器
    bench_case_instances = log_parser.parser_sysbench_log()
    for x in bench_case_instances:
        print(x)
        bench_case_instance_data_form={
        'host_info':'24C128G4000G',
        'mysql_version':'mysql-5.7.21',
        'variable_name':x['variable_name'],
        'bench_type': x['bench_type'],
        'workers': x['workers'],
        'variable_value': x['variable_value'],
        'truncations_per_seconde': x['tps'],
        'query_per_seconde': x['qps'],
        'duration': 0
        }
        response=session.get(add_bench_case_instance_url)
        html           = response.text
        soup           = bs4.BeautifulSoup(html,'html.parser')
        csrf_token     = soup.find(attrs={'name':'csrfmiddlewaretoken'})
        bench_case_instance_data_form.update({'csrfmiddlewaretoken':csrf_token['value']})
        response=session.post(add_bench_case_instance_url,data=bench_case_instance_data_form)
        print(bench_case_instance_data_form)
        
