#!/usr/bin/env bash
###
####
ALLPROCESS=4
UWSGIBIN=/usr/bin/uwsgi
PROCESSINI=/var/www/Ant/Ant/ant.ini

# start function
start(){
  psid=`ps aux | egrep "uwsgi" | egrep -v "grep" | wc -l`
  if [ $psid -gt ${ALLPROCESS} ];then
    echo "uwsgi is running..."
    exit 0
  else
    ${UWSGIBIN} --ini ${PROCESSINI}
    echo "Start uwsgi service [OK]"
  fi
}

# stop function
stop(){
  pkill -9 uwsgi
  echo "Stop uwsgi is [OK]"
}

# reload function
reload(){
  ${UWSGIBIN} -s reload ${PROCESSINI}
  echo "Reload configure is [OK]"
}

case "$1" in
  start)
    start && exit 0
  ;;
  stop)
    stop && exit 0
  ;;
  restart)
    stop
    start && exit 0
  ;;
  reload)
    reload && exit 0
  ;;
  *)
    echo "Usages: bash $0 [start|stop|restart|reload]"
  ;;
esac
