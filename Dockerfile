FROM python:3.11.0a1-alpine3.14
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY /scripts/garbmgr.py /bin/garbmgr.py
COPY /scripts/my_secrets.py /bin/my_secrets.py
COPY /scripts/garbcal.py /bin/garbcal.py
COPY /scripts/cal_data.py /bin/cal_data.py
COPY /scripts/mqtt_ctrl.py /bin/mqtt_ctrl.py
COPY root /var/spool/cron/crontabs/root
RUN chmod +x /bin/garbmgr.py
CMD crond -l 2 -f
