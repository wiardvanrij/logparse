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

Currently it will only return the top 10 most used IP adressess with it's amount of requests.

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