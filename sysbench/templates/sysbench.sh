sysbench --mysql-host={{ hostIP }} --mysql-port={{ port }} --mysql-user={{ user }} \
  --mysql-password={{ password }} --mysql-db={{ db }} --tables={{ tableCount }} --table_size={{ tableSize }} \
  --events={{ events }} --threads={{ threads }} {{ opration }} prepare

sysbench --mysql-host={{ hostIP }} --mysql-port={{ port }} --mysql-user={{ user }} \
  --mysql-password={{ password }} --mysql-db={{ db }} --tables={{ tableCount }} --table_size={{ tableSize }} \
  --events={{ events }} --threads={{ threads }}  {{ opration }} run > /tmp/mysql-z/{{benchCase}}/{{opration}}.log

sysbench --mysql-host={{ hostIP }} --mysql-port={{ port }} --mysql-user={{ user }} \
  --mysql-password={{ password }} --mysql-db={{ db }} --tables={{ tableCount }} --table_size={{ tableSize }} \
  {{ opration }} cleanup