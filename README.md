# domain

ps aux 显示当前所有运行的进程

ps -ef | grep xxx 查看进程xx相关信息

pgrep xxx 查看xxx PID

kill -s 9 pid号 杀死pid程序

后台运行
nohup python3 alisdk_domain.py > run.log 2>&1 &