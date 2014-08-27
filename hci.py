import sys
from msg import msg_analyze

msg_db = []

def storeMsg(msg_time, msg_direction, msg_msg):
	global msg_db
	
	this_msg = {'time'      : msg_time,
	            'direction' : msg_direction,
				'msg'       : msg_msg
	}
	msg_db += [this_msg]


def loadSrcFile(file_name, direction):
	f_in = open(file_name)
	lines = f_in.readlines()

	# 消息分段时间  50 us
	time_split = 5e-5
	# 上次单个数据发生的时间，处理完一个数据后更新
	t = -100.0
	# 消息数据
	msg_data = []
	# 消息发生时间
	msg_time = -100

	# 排除第一行
	for line in lines[1:]:
		q = line.split(',')
		o_time = float(q[0])
		o_date = int(q[1], 16)
		# 消息分段
		if (o_time - t) > time_split:
			if msg_time >= 0:
				storeMsg(msg_time, direction, msg_data)
			msg_time = o_time
			msg_data = [o_date]
		else:
			msg_data += [o_date]
		t = o_time

	# 最后一条消息
	if msg_time >= 0:
		storeMsg(msg_time, direction, msg_data)
		
	f_in.close()

# 读取文件
loadSrcFile('tx.txt', 'TX')
loadSrcFile('rx.txt', 'RX')

# 按时间排序
stored_msg_db = sorted(msg_db, cmp=lambda x,y:cmp(x['time'],y['time']))

for msg in stored_msg_db:
	# 输出消息数据
	print "[%5.6f %s] " % (msg['time'] , msg['direction']) ,
	for i in msg['msg']:
		print "%02X" % i ,
	print
	
	# 如果命令行参数为 '-d' 或 '-D'  解析消息内容
	if (len(sys.argv) == 2):
		if (sys.argv[1] == '-D') or (sys.argv[1] == '-d'):
			msg_analyze(msg['msg'])