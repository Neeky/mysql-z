sysbench --mysql-host={{ hostIP }} --mysql-port={{ port }} --mysql-user={{ user }} \
  --mysql-password={{ password }} --mysql-db={{ db }} --tables={{ tableCount }} --table_size={{ tableSize }} \
  --events={{ events }} --threads={{ threads }} {{ item }} prepare

sysbench --mysql-host={{ hostIP }} --mysql-port={{ port }} --mysql-user={{ user }} \
  --mysql-password={{ password }} --mysql-db={{ db }} --tables={{ tableCount }} --table_size={{ tableSize }} \
  --events={{ events }} --threads={{ threads }}  {{ item }} run > /tmp/mysql-z/{{ config.name }}#{{ config.value }}/{{ item }}.log

sysbench --mysql-host={{ hostIP }} --mysql-port={{ port }} --mysql-user={{ user }} \
  --mysql-password={{ password }} --mysql-db={{ db }} --tables={{ tableCount }} --table_size={{ tableSize }} \
  {{ item }} cleanup