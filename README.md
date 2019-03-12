# A simple Python log parser

## About this tool

This parser uses https://github.com/rory/apache-log-parser as base to parse your log files. All the supported values (Log Formatting) are supported via the `config.ini`. 

The core feature is to provide an easy and simple overview of your logfiles with ways to customize this to your own liking. 

## Installation

 - Make a checkout
 - run `python setup.py`
 - customize the config in `~/config/logparse/config.ini`

## Using it

Simply use `logparse` followed by the location of your logfile. For instance:

- `logparse apache.log`
- `logparse /var/log/apache.log`
- etc

## Features

It will return an overview with the top 10 most requests. 

```
+status-----+
| 500 | 172 |
| 200 | 44  |
| 302 | 36  |
| 304 | 3   |
+-----+-----+
+request_url_path---------+----+
| /                       | 43 |
| /robots.txt             | 43 |
| /wp-login.php           | 15 |
| /ads.txt                | 14 |
| /feed/                  | 10 |
| /feed                   | 6  |
| /wp-404.php             | 6  |
| /category/scripts/feed/ | 6  |
| /category/guide/feed/   | 5  |
| /category/slack/feed/   | 5  |
+-------------------------+----+
+request_header_user_agent-----------------------------------------------------------------------------------------------------------------------------------------------+----+
| Mozilla/5.0 (compatible; SeznamBot/3.2; +http://napoveda.seznam.cz/en/seznambot-intro/)                                                                                | 40 |
| Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)                                                                                                | 28 |
| Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)                                                                                               | 19 |
| Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Applebot/0.1; +http://www.apple.com/go/applebot) | 18 |
| Apache-HttpClient/4.5.2 (Java/1.8.0_151)                                                                                                                               | 16 |
| Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)                                                                                    | 11 |
| Mozilla/5.0 (compatible; AhrefsBot/6.1; +http://ahrefs.com/robot/)                                                                                                     | 10 |
| Jersey/2.25.1 (HttpUrlConnection 1.8.0_141)                                                                                                                            | 8  |
| Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0                                        | 8  |
| Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36                                                      | 6  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----+
+------+-----+
| GET  | 249 |
| POST | 6   |
+------+-----+
+remote_host-----+----+
| x.x.x.x        | 18 |
| x.x.x.x        | 16 |
| x.x.x.x        | 8  |
| x.x.x.x        | 8  |
| x.x.x.x        | 8  |
| x.x.x.x        | 8  |
| x.x.x.x        | 8  |
| x.x.x.x        | 8  |
| x.x.x.x        | 8  |
| x.x.x.x        | 8  |
+----------------+----+

```

## ToDo

Just for myself

*Provide an overview for:*

- most HTTP codes (by IP)
- most used paths
- most used agents
- specific url's and/or IP's

*Provide configuration options for:*

- amount of resulsts
- multiple logfiles
- ???