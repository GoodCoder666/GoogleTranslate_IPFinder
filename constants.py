# -*- coding: utf-8 -*-
from PySide6.QtCore import QLocale

__all__ = ['DefaultConfig', 'GTDB_IPS', 'ONLINE_SERVICES']

class DefaultConfig:
    language = 'zh_CN' if 'zh' in QLocale.system().name() else 'en_US'
    test_host = 'translate.googleapis.com'
    save_hosts = ['translate.googleapis.com', 'translate-pa.googleapis.com']
    template = 'https://{}/translate_a/single?client=gtx&sl=en&tl=fr&q=a'
    num_threads = 64
    timeout = 1.5
    repeat = 3

ONLINE_SERVICES = (
    (
        'https://ghp.ci/https://raw.githubusercontent.com/GoodCoder666/gtdb/main/src/ip.txt',
        'https://raw.githubusercontent.com/GoodCoder666/gtdb/main/src/ip.txt'
    ),
    (
        'https://ghp.ci/https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/ip.txt',
        'https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/ip.txt'
    ),
    (
        'https://ghp.ci/https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/IPv6.txt',
        'https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/IPv6.txt'
    )
)

# IPs from gtdb
# updated 2024-10-17
GTDB_IPS = '''108.177.111.90
108.177.122.90
108.177.123.90
108.177.125.186
108.177.126.90
108.177.127.107
108.177.127.144
108.177.127.197
108.177.127.90
108.177.97.100
142.250.0.90
142.250.1.90
142.250.10.124
142.250.10.133
142.250.10.193
142.250.10.90
142.250.100.90
142.250.101.105
142.250.101.165
142.250.101.181
142.250.101.90
142.250.102.90
142.250.103.90
142.250.105.90
142.250.107.156
142.250.107.90
142.250.11.102
142.250.11.104
142.250.11.110
142.250.11.112
142.250.11.116
142.250.11.117
142.250.11.137
142.250.11.142
142.250.11.144
142.250.11.146
142.250.11.149
142.250.11.152
142.250.11.154
142.250.11.155
142.250.11.164
142.250.11.193
142.250.11.194
142.250.11.196
142.250.11.197
142.250.11.198
142.250.11.200
142.250.11.201
142.250.11.31
142.250.11.84
142.250.11.90
142.250.11.99
142.250.110.90
142.250.111.90
142.250.112.136
142.250.112.190
142.250.112.90
142.250.113.90
142.250.114.90
142.250.115.90
142.250.12.90
142.250.123.90
142.250.125.185
142.250.125.90
142.250.126.90
142.250.128.90
142.250.13.90
142.250.136.90
142.250.138.90
142.250.141.90
142.250.142.90
142.250.145.90
142.250.147.90
142.250.148.202
142.250.149.90
142.250.152.90
142.250.153.90
142.250.157.118
142.250.157.18
142.250.157.183
142.250.157.184
142.250.157.186
142.250.157.194
142.250.157.90
142.250.158.122
142.250.158.90
142.250.159.90
142.250.176.213
142.250.177.11
142.250.177.14
142.250.179.131
142.250.179.141
142.250.179.169
142.250.180.40
142.250.181.121
142.250.181.40
142.250.182.34
142.250.182.77
142.250.185.40
142.250.186.141
142.250.187.210
142.250.188.207
142.250.188.41
142.250.188.5
142.250.189.183
142.250.190.134
142.250.190.36
142.250.190.70
142.250.191.141
142.250.191.69
142.250.192.130
142.250.192.226
142.250.194.102
142.250.194.166
142.250.195.164
142.250.195.226
142.250.196.192
142.250.196.193
142.250.196.194
142.250.196.195
142.250.196.196
142.250.196.197
142.250.196.198
142.250.196.199
142.250.196.200
142.250.196.201
142.250.196.202
142.250.196.203
142.250.196.205
142.250.196.206
142.250.196.207
142.250.196.209
142.250.196.210
142.250.196.215
142.250.196.217
142.250.196.222
142.250.196.223
142.250.197.100
142.250.197.104
142.250.197.113
142.250.197.114
142.250.197.120
142.250.197.141
142.250.197.142
142.250.197.149
142.250.197.151
142.250.197.152
142.250.197.153
142.250.197.193
142.250.197.195
142.250.197.197
142.250.197.199
142.250.197.200
142.250.197.201
142.250.197.203
142.250.197.205
142.250.197.206
142.250.197.210
142.250.197.213
142.250.197.215
142.250.197.216
142.250.197.222
142.250.197.223
142.250.199.133
142.250.199.135
142.250.199.139
142.250.199.151
142.250.199.165
142.250.199.181
142.250.199.183
142.250.199.184
142.250.199.185
142.250.200.65
142.250.200.68
142.250.203.102
142.250.203.200
142.250.203.78
142.250.204.126
142.250.205.163
142.250.205.168
142.250.205.193
142.250.205.226
142.250.206.97
142.250.207.109
142.250.207.85
142.250.217.102
142.250.217.70
142.250.218.226
142.250.219.104
142.250.219.106
142.250.219.130
142.250.219.4
142.250.219.82
142.250.219.88
142.250.27.114
142.250.27.118
142.250.27.122
142.250.27.124
142.250.27.143
142.250.27.144
142.250.27.145
142.250.27.146
142.250.27.152
142.250.27.165
142.250.27.181
142.250.27.194
142.250.27.196
142.250.27.199
142.250.27.202
142.250.27.31
142.250.27.90
142.250.27.98
142.250.28.90
142.250.30.90
142.250.31.117
142.250.31.122
142.250.31.123
142.250.31.124
142.250.31.144
142.250.31.164
142.250.31.194
142.250.31.195
142.250.31.196
142.250.31.197
142.250.31.198
142.250.31.199
142.250.31.202
142.250.31.90
142.250.4.185
142.250.4.90
142.250.64.102
142.250.64.107
142.250.64.109
142.250.64.119
142.250.64.120
142.250.64.139
142.250.64.151
142.250.64.169
142.250.64.171
142.250.64.181
142.250.64.183
142.250.64.203
142.250.64.207
142.250.64.217
142.250.64.224
142.250.64.242
142.250.64.248
142.250.64.249
142.250.64.87
142.250.64.88
142.250.64.96
142.250.66.164
142.250.66.171
142.250.66.178
142.250.66.183
142.250.66.184
142.250.66.191
142.250.66.201
142.250.66.205
142.250.66.210
142.250.66.215
142.250.66.216
142.250.66.223
142.250.66.237
142.250.66.239
142.250.66.248
142.250.66.249
142.250.66.94
142.250.67.11
142.250.67.21
142.250.67.41
142.250.67.50
142.250.67.53
142.250.67.55
142.250.67.56
142.250.67.63
142.250.67.65
142.250.67.73
142.250.67.75
142.250.67.82
142.250.67.95
142.250.68.113
142.250.68.139
142.250.68.37
142.250.68.69
142.250.70.136
142.250.71.34
142.250.72.6
142.250.74.38
142.250.77.193
142.250.77.194
142.250.78.206
142.250.8.90
142.250.80.38
142.250.80.43
142.250.81.110
142.250.81.225
142.250.9.90
142.250.96.104
142.250.96.110
142.250.96.116
142.250.96.133
142.250.96.143
142.250.96.145
142.250.96.146
142.250.96.147
142.250.96.148
142.250.96.164
142.250.96.167
142.250.96.181
142.250.96.191
142.250.96.195
142.250.96.196
142.250.96.199
142.250.96.200
142.250.96.201
142.250.96.202
142.250.96.84
142.250.96.90
142.250.96.96
142.250.96.98
142.250.97.90
142.250.98.105
142.250.98.116
142.250.98.117
142.250.98.124
142.250.98.142
142.250.98.148
142.250.98.149
142.250.98.152
142.250.98.155
142.250.98.194
142.250.98.196
142.250.98.90
142.250.99.100
142.250.99.90
142.251.0.90
142.251.0.92
142.251.1.110
142.251.1.112
142.251.1.124
142.251.1.133
142.251.1.143
142.251.1.144
142.251.1.146
142.251.1.165
142.251.1.166
142.251.1.167
142.251.1.176
142.251.1.195
142.251.1.199
142.251.1.200
142.251.1.202
142.251.1.31
142.251.1.83
142.251.1.90
142.251.1.96
142.251.10.110
142.251.10.138
142.251.10.141
142.251.10.152
142.251.10.19
142.251.10.196
142.251.10.200
142.251.10.31
142.251.10.90
142.251.107.90
142.251.111.90
142.251.112.90
142.251.116.101
142.251.116.90
142.251.117.90
142.251.12.118
142.251.12.137
142.251.12.141
142.251.12.185
142.251.12.81
142.251.12.90
142.251.120.90
142.251.129.113
142.251.129.121
142.251.129.129
142.251.129.178
142.251.129.194
142.251.129.224
142.251.129.255
142.251.129.79
142.251.13.90
142.251.130.30
142.251.132.17
142.251.132.226
142.251.132.53
142.251.133.70
142.251.134.77
142.251.143.73
142.251.143.75
142.251.143.77
142.251.143.79
142.251.15.103
142.251.15.104
142.251.15.105
142.251.15.106
142.251.15.90
142.251.15.99
142.251.16.185
142.251.16.90
142.251.160.90
142.251.161.90
142.251.162.90
142.251.163.90
142.251.165.90
142.251.166.90
142.251.168.100
142.251.168.103
142.251.168.104
142.251.168.105
142.251.168.107
142.251.168.110
142.251.168.112
142.251.168.113
142.251.168.116
142.251.168.117
142.251.168.118
142.251.168.123
142.251.168.126
142.251.168.132
142.251.168.136
142.251.168.137
142.251.168.138
142.251.168.142
142.251.168.144
142.251.168.146
142.251.168.147
142.251.168.148
142.251.168.152
142.251.168.154
142.251.168.155
142.251.168.156
142.251.168.164
142.251.168.165
142.251.168.166
142.251.168.167
142.251.168.189
142.251.168.190
142.251.168.191
142.251.168.194
142.251.168.196
142.251.168.199
142.251.168.31
142.251.168.81
142.251.168.82
142.251.168.84
142.251.168.88
142.251.168.92
142.251.168.94
142.251.168.96
142.251.168.99
142.251.170.104
142.251.170.90
142.251.171.90
142.251.172.103
142.251.172.114
142.251.172.122
142.251.172.148
142.251.172.17
142.251.172.176
142.251.172.194
142.251.172.195
142.251.172.201
142.251.172.90
142.251.172.96
142.251.172.97
142.251.173.90
142.251.174.104
142.251.174.110
142.251.174.143
142.251.174.200
142.251.174.202
142.251.175.90
142.251.176.112
142.251.176.148
142.251.177.90
142.251.178.90
142.251.179.90
142.251.18.155
142.251.18.90
142.251.182.90
142.251.183.90
142.251.184.90
142.251.185.101
142.251.185.102
142.251.185.103
142.251.185.104
142.251.185.106
142.251.185.107
142.251.185.110
142.251.185.112
142.251.185.116
142.251.185.118
142.251.185.122
142.251.185.123
142.251.185.124
142.251.185.133
142.251.185.136
142.251.185.137
142.251.185.138
142.251.185.139
142.251.185.141
142.251.185.142
142.251.185.143
142.251.185.144
142.251.185.145
142.251.185.147
142.251.185.148
142.251.185.149
142.251.185.154
142.251.185.156
142.251.185.157
142.251.185.164
142.251.185.165
142.251.185.166
142.251.185.167
142.251.185.176
142.251.185.181
142.251.185.189
142.251.185.19
142.251.185.191
142.251.185.193
142.251.185.194
142.251.185.195
142.251.185.196
142.251.185.197
142.251.185.198
142.251.185.199
142.251.185.200
142.251.185.201
142.251.185.202
142.251.185.214
142.251.185.31
142.251.185.81
142.251.185.82
142.251.185.83
142.251.185.84
142.251.185.85
142.251.185.88
142.251.185.90
142.251.185.91
142.251.185.94
142.251.185.95
142.251.185.97
142.251.185.98
142.251.185.99
142.251.2.214
142.251.2.90
142.251.208.102
142.251.208.103
142.251.208.117
142.251.208.128
142.251.208.135
142.251.208.137
142.251.208.139
142.251.208.143
142.251.208.152
142.251.208.166
142.251.208.167
142.251.208.184
142.251.208.191
142.251.220.0
142.251.220.21
142.251.220.24
142.251.220.31
142.251.220.7
142.251.32.64
142.251.32.68
142.251.32.82
142.251.32.87
142.251.32.89
142.251.33.11
142.251.33.4
142.251.35.228
142.251.36.11
142.251.36.111
142.251.36.134
142.251.36.139
142.251.36.141
142.251.36.15
142.251.36.17
142.251.36.198
142.251.36.205
142.251.36.21
142.251.36.228
142.251.36.32
142.251.36.47
142.251.37.105
142.251.4.112
142.251.4.201
142.251.4.90
142.251.4.92
142.251.4.96
142.251.40.107
142.251.40.129
142.251.40.143
142.251.40.145
142.251.40.161
142.251.40.174
142.251.40.177
142.251.40.197
142.251.40.230
142.251.40.237
142.251.40.75
142.251.40.87
142.251.41.17
142.251.42.65
142.251.42.71
142.251.43.114
142.251.43.119
142.251.43.137
142.251.43.152
142.251.43.203
142.251.43.205
142.251.43.226
142.251.43.36
142.251.43.75
142.251.43.98
142.251.45.11
142.251.45.13
142.251.45.68
142.251.46.132
142.251.47.117
142.251.47.196
142.251.47.71
142.251.5.90
142.251.6.90
142.251.8.90
142.251.9.90
172.217.0.46
172.217.12.145
172.217.13.142
172.217.14.102
172.217.14.73
172.217.16.247
172.217.16.46
172.217.163.201
172.217.164.119
172.217.164.127
172.217.165.0
172.217.165.55
172.217.167.0
172.217.168.0
172.217.168.247
172.217.169.192
172.217.170.196
172.217.173.247
172.217.173.55
172.217.192.90
172.217.193.90
172.217.194.137
172.217.195.90
172.217.203.90
172.217.204.90
172.217.212.90
172.217.214.90
172.217.215.90
172.217.218.90
172.217.222.90
172.217.27.209
172.217.31.142
172.253.112.90
172.253.113.90
172.253.114.90
172.253.115.116
172.253.115.90
172.253.116.90
172.253.117.90
172.253.118.194
172.253.118.90
172.253.119.133
172.253.119.143
172.253.119.181
172.253.119.194
172.253.119.198
172.253.119.199
172.253.119.200
172.253.119.201
172.253.119.202
172.253.119.82
172.253.119.90
172.253.122.90
172.253.123.90
172.253.124.107
172.253.124.110
172.253.124.112
172.253.124.114
172.253.124.118
172.253.124.122
172.253.124.123
172.253.124.124
172.253.124.133
172.253.124.149
172.253.124.164
172.253.124.166
172.253.124.194
172.253.124.196
172.253.124.200
172.253.124.90
172.253.124.96
172.253.125.110
172.253.125.90
172.253.126.90
172.253.127.90
172.253.58.90
172.253.62.90
172.253.63.90
173.194.175.194
173.194.175.199
173.194.175.200
173.194.192.195
173.194.205.196
173.194.207.199
173.194.210.199
173.194.212.147
173.194.212.194
173.194.215.100
173.194.215.194
173.194.217.194
173.194.217.94
173.194.220.196
173.194.222.195
173.194.76.194
173.194.76.198
173.194.76.199
173.194.77.200
173.194.79.94
209.85.144.196
209.85.145.200
209.85.200.107
209.85.235.104
209.85.235.198
209.85.235.99
216.239.32.40
216.58.207.200
216.58.207.215
216.58.207.242
216.58.209.174
216.58.214.14
216.58.215.226
216.58.215.43
216.58.215.70
216.58.220.142
216.58.223.207
216.58.223.216
216.58.227.65
216.58.227.66
216.58.227.67
34.1.15.24
64.233.176.98
64.233.181.99
64.233.189.191
64.233.189.92
74.125.133.198
74.125.134.97
74.125.136.196
74.125.137.105
74.125.137.106
74.125.137.107
74.125.137.110
74.125.137.116
74.125.137.117
74.125.137.123
74.125.137.133
74.125.137.141
74.125.137.143
74.125.137.146
74.125.137.165
74.125.137.167
74.125.137.176
74.125.137.19
74.125.137.191
74.125.137.194
74.125.137.195
74.125.137.198
74.125.137.200
74.125.137.201
74.125.137.202
74.125.137.90
74.125.137.96
74.125.137.98
74.125.138.93
74.125.139.136
74.125.140.136
74.125.141.196
74.125.142.94
74.125.143.98
74.125.193.196
74.125.196.113
74.125.196.94
74.125.199.194
74.125.204.139
74.125.206.105
74.125.206.194
74.125.26.196
74.125.71.194'''.split()
