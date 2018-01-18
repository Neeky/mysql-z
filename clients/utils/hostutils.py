def generate_host_info(name='2C4G128G',os='centos-7.2',cores=2,memorys=4,
                        disks=128,is_log_ssd=False,is_data_ssd=False):
    """
    用于创建主机信息
    """
    return {
            'name':name,
            'os':os,
            'cores':cores,
            'memorys':memorys,
            'disks':disks,
            'is_log_ssd':is_log_ssd,
            'is_data_ssd': is_data_ssd
                }

