import os

def get_config_items(base_path):
    """
    get_config_items('/Users/jianglexing/Desktop/logs')

    #['autocommit#off', 'autocommit#on']
    """
    configs = [config for config in os.listdir(base_path) if config.startswith('.') == False]
    return configs


def parser_sysbench_log(base_path='/Users/jianglexing/Desktop/logs/',file_path=None,file_name=None):
    """
    base_path:/Users/jianglexing/Desktop/logs/
    file_path:autocommit#off
    file_name:bulk_insert#1#346.log
    """


    #由base_path解析出已经完成的测试项
    configs = get_config_items(base_path)

    #针对每一个测试项解析一次日志
    for config in configs:
        variable_name,variable_value = config.split('#')
        #log_file_dir=os.path.join('/Users/jianglexing/Desktop/logs/','autocommit#off')
        #定位到具体测试项结果所保存的文件夹
        log_file_dir = os.path.join(base_path,config)
        log_file_names = os.listdir(log_file_dir)
        for log_file_name in log_file_names:
            if log_file_name.startswith('.'):
                continue
            
            bench_type,workers,_ = log_file_name.split('#')
            print('start open {0}'.format(os.path.join(base_path,config,log_file_name)))
            with open(os.path.join(base_path,config,log_file_name)) as f:
                try:
                    lines  = [line for line in f if 'transactions:' in line or 'queries:' in line ]
                    _,tps  = lines[0].split('(')
                    tps,*_ = tps.split(' ')
                    _,qps  = lines[1].split('(')
                    qps,*_ = qps.split(' ')
                except Exception as e:
                    continue

                yield  {'variable_name':variable_name,'variable_value':variable_value,
                        'bench_type':bench_type,'workers':workers,'tps':tps,'qps':qps}
                
# for x in parser_sysbench_log():
#     print(x)





