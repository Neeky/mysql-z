bench_case_list = [
    'autocommit',
    'innodb_log_files_in_group',
    'innodb_log_file_size',
    'innodb_log_buffer_size ',
    'innodb_flush_log_at_trx_commit',
    'sync_binlog',
    'binlog_cache_size',
    'binlog_format',
    'innodb_autoinc_lock_mode',
    'innodb_io_capacity',
    'innodb_io_capacity_max',
    'innodb_buffer_pool_size',
    'innodb_buffer_pool_instances'
    ]



def generate_bench_case(host_info='2C4G128G',mysql_version='mysql-5.7.20',
                        variable_name='autocommit',bench_type='oltp_insert',detail=''):
    """
    创建测试用例
    """
    return {
            'host_info': host_info,
            'mysql_version': mysql_version,
            'variable_name': variable_name,
            'bench_type':bench_type,
            'detail':detail
        }