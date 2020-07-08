from crontab import CronTab
from croniter import croniter

# cron設定
cron = CronTab()
job = cron.new(command="python3 ./tweet.py")
job.setall("00 12 * * *")

cron.write("output.tab")

for res in cron.run_scheduler():
    print("実行しました")