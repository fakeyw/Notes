在建立SMTP服务器的过程中踩的坑

用的是mailutils

1. 首先要有一个域名，如果从域名解析到vps服务商被阻，就本地hosts改dns

   然后 /etc/postfix/main.cf 加一条 `smtp_host_lookup = dns, native`

2. myhostname 改为 主域名

3. mydomain 改为 mail.主域名

4. inet_protocols 试试 all 或 ipv4

---

当时，这种程度的配置能收到邮件 但无法正常发出邮件

可以发送到本地如 root@fakeyw.pw 

正常发送的log为

```bash
Jun 15 20:22:55 localhost postfix/pickup[4098]: 70BC720BC6: uid=0 from=<root@localhost>
Jun 15 20:22:55 localhost postfix/cleanup[4109]: 70BC720BC6: message-id=<20180615122255.70BC720BC6@fakeyw.pw>
Jun 15 20:22:55 localhost postfix/qmgr[4099]: 70BC720BC6: from=<root@localhost>, size=313, nrcpt=1 (queue active)
Jun 15 20:22:55 localhost postfix/local[4157]: 70BC720BC6: to=<root@fakeyw.pw>, relay=local, delay=0.01, delays=0/0/0/0, dsn=2.0.0, status=sent (delivered to mailbox)
Jun 15 20:22:55 localhost postfix/qmgr[4099]: 70BC720BC6: removed
```

但向外网发送时的log为

```bash
Jun 15 20:25:47 localhost postfix/pickup[4098]: 0F0BA20BC7: uid=0 from=<root@localhost>
Jun 15 20:25:47 localhost postfix/cleanup[4310]: 0F0BA20BC7: message-id=<20180615122547.0F0BA20BC7@fakeyw.pw>
Jun 15 20:25:47 localhost postfix/qmgr[4099]: 0F0BA20BC7: from=<root@localhost>, size=313, nrcpt=1 (queue active)
Jun 15 20:25:51 localhost postfix/smtp[4312]: connect to mail.fakeyw.pw[115.159.113.45]:25: Connection timed out
Jun 15 20:25:51 localhost postfix/smtp[4312]: 43FC920BC6: to=<fakeyw@163.com>, relay=none, delay=30, delays=0.02/0.01/30/0, dsn=4.4.1, status=deferred (connect to mail.fakeyw.pw[115.159.113.45]:25: Connection timed out)
```

并未发送出去

可以用postqueue -f清空发送队列

---

顺便  如果删掉了日志文件

再建一个并权限777 也不会继续记录日志

要重启下syslog

---

试了很久了还是不行

lsof命令能查端口的服务

---



