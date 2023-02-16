FROM python:3.7-slim

ARG work_dir="/service/"
WORKDIR $work_dir
COPY . .

COPY ./crontab /etc/cron.d/crontab
RUN apt-get update      && apt-get install -y g++ cmake gcc cron     && rm -rf /var/lib/apt/lists/*     && python -m pip install --upgrade pip     && chmod 0644 /etc/cron.d/crontab     && /usr/bin/crontab /etc/cron.d/crontab     && sed -i '/^done$/a   /usr/sbin/cron' ./docker-entrypoint.sh     && chmod -v +x ./docker-entrypoint.sh

ENTRYPOINT ["/bin/bash", "./docker-entrypoint.sh"]

RUN pip install --upgrade --no-cache-dir -r requirements.txt

CMD ["/bin/bash","-c","python setup.py"]
