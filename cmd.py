
cmd_normal_format = [ 
	{'name' : 'Len',     'start_byte':3,    'start_bit':0, 'type':'B', 'byte_size':1,  'bit_mask':0xff},
	{'name' : 'Data',    'start_byte':4,    'start_bit':0, 'type':'B', 'byte_size':-1, 'bit_mask':0xff},
]

cmd_0409_format	= [ 
	{'name' : 'Len',     'start_byte':3,    'start_bit':0, 'type':'B', 'byte_size':1, 'bit_mask':0xff},
	{'name' : 'BD_ADDR', 'start_byte':4,    'start_bit':0, 'type':'B', 'byte_size':6, 'bit_mask':0xff},
	{'name' : 'Role',    'start_byte':0x0a, 'start_bit':0, 'type':'B', 'byte_size':1, 'bit_mask':0xff},
]

def cmd_analyze_fun(msg, format):
	for f in format:
		print ' %s:' % (f['name']),
		if f['byte_size'] != -1 :
			for i in msg[f['start_byte']: f['start_byte'] + f['byte_size']]:
				print '%02X' % i,
		else :
			for i in msg[f['start_byte']:]:
				print '%02X' % i,
	pass


cmd_type = [ 
	# HCI Link Control Commands
	{ 'op_code' : 0x0401, 'descript' : 'Inquiry',                               'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0402, 'descript' : 'Inquiry_Cancel',                        'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0403, 'descript' : 'Periodic_Inquiry_Mode',                 'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0404, 'descript' : 'Exit_Periodic_Inquiry_Mode',            'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0405, 'descript' : 'Create_Connection',                     'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0406, 'descript' : 'Disconnect',                            'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0407, 'descript' : 'Add_SCO_Connection',                    'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0408, 'descript' : 'Create_Connection_Cancel',              'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0409, 'descript' : 'Accept_Connection_Request',             'analyze_format' : cmd_0409_format },
	{ 'op_code' : 0x040a, 'descript' : 'Reject_Connection_Request',             'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x040b, 'descript' : 'Link_Key_Request_Reply',                'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x040c, 'descript' : 'Link_Key_Request_Negative_Reply',       'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x040d, 'descript' : 'PIN_Code_Request_Reply',                'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x040e, 'descript' : 'PIN_Code_Request_Negative_Reply',       'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x040f, 'descript' : 'Change_Connection_Packet_Type',         'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0411, 'descript' : 'Authentication_Requested',              'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0413, 'descript' : 'Set_Connection_Encryption',             'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0415, 'descript' : 'Change_Connection_Link_Key',            'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0417, 'descript' : 'Master_Link_Key',                       'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0419, 'descript' : 'Remote_Name_Request',                   'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x041a, 'descript' : 'Remote_Name_Request_Cancel',            'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x041b, 'descript' : 'Read_Remote_Supported_Features',        'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x041c, 'descript' : 'Read_Remote_Extended_Features',         'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x041d, 'descript' : 'Read_Remote_Version_Information',       'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x041f, 'descript' : 'Read_Clock_Offset',                     'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0420, 'descript' : 'Read_LMP_Handle',                       'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0428, 'descript' : 'Setup_Synchronous_Connection',          'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0429, 'descript' : 'Accept_Synchronous_Connection_Request', 'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x042a, 'descript' : 'Reject_Synchronous_Connection_Request', 'analyze_format' : cmd_normal_format },

	# HCI Link Policy Commands
	{ 'op_code' : 0x0801, 'descript' : 'Hold_Mode',                             'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0802, 'descript' : 'not used',                              'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0803, 'descript' : 'Sniff_Mode',                            'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0804, 'descript' : 'Exit_Sniff_Mode',                       'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0805, 'descript' : 'Park_Mode',                             'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0806, 'descript' : 'Exit_Park_Mode',                        'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0807, 'descript' : 'QoS_Setup',                             'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0808, 'descript' : 'not used',                              'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0809, 'descript' : 'Role_Discovery',                        'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x080a, 'descript' : 'not used',                              'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x080b, 'descript' : 'Switch_Role',                           'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x080c, 'descript' : 'Read_Link_Policy_Settings',             'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x080d, 'descript' : 'Write_Link_Policy_Settings',            'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x080e, 'descript' : 'Read_Default_Link_Policy_Settings',     'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x080f, 'descript' : 'Write_Default_Link_Policy_Settings',    'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0810, 'descript' : 'Flow_Specification',                    'analyze_format' : cmd_normal_format },

	# HCI Host Control and Baseband Commands
	{ 'op_code' : 0x0801, 'descript' : 'Hold_Mode',                             'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c01, 'descript' : 'Set_Event_Mask', 	 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c02, 'descript' : 'not used', 	 	 		 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c03, 'descript' : 'Reset', 	 	 		 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c04, 'descript' : 'not used', 	 	 		 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c05, 'descript' : 'Set_Event_Filter', 	 	 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c06, 'descript' : 'not used', 	 	 		 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c07, 'descript' : 'not used', 	 	 		 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c08, 'descript' : 'Flush', 	 	 		 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c09, 'descript' : 'Read_PIN_Type', 	 	 	 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c0a, 'descript' : 'Write_PIN_Type', 	 	 	 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c0b, 'descript' : 'Create_New_Unit_Key', 	 	 	 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c0c, 'descript' : 'not used', 		 	 	 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c0d, 'descript' : 'Read_Stored_Link_Key', 		 	 	 	'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c0e, 'descript' : 'not used', 		 	 	 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c0f, 'descript' : 'not used', 		 	 	 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c10, 'descript' : 'not used', 		 	 	 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c11, 'descript' : 'Write_Stored_Link_Key', 		 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c12, 'descript' : 'Delete_Stored_Link_Key', 	 		 	'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c13, 'descript' : 'Write_Local_Name', 		 	 		 	'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c14, 'descript' : 'Read_Local_Name', 		 		 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c15, 'descript' : 'Read_Connection_Accept_Timeout', 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c16, 'descript' : 'Write_Connection_Accept_Timeout', 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c17, 'descript' : 'Read_Page_Timeout', 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c18, 'descript' : 'Write_Page_Timeout', 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c19, 'descript' : 'Read_Scan_Enable', 		 		 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c1a, 'descript' : 'Write_Scan_Enable', 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c1b, 'descript' : 'Read_Page_Scan_Activity', 		 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c1c, 'descript' : 'Write_Page_Scan_Activity', 		 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c1d, 'descript' : 'Read_Inquiry_Scan_Activity', 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c1e, 'descript' : 'Write_Inquiry_Scan_Activity', 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c1f, 'descript' : 'Read_Authentication_Enable', 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c20, 'descript' : 'Write_Authentication_Enable', 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c21, 'descript' : 'Read_Encryption_Mode', 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c22, 'descript' : 'Write_Encryption_Mode', 	 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c23, 'descript' : 'Read_Class_of_Device', 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c24, 'descript' : 'Write_Class_of_Device', 		 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c25, 'descript' : 'Read_Voice_Setting', 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c26, 'descript' : 'Write_Voice_Setting', 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c27, 'descript' : 'Read_Automatic_Flush_Timeout', 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c28, 'descript' : 'Write_Automatic_Flush_Timeout', 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c29, 'descript' : 'Read_Num_Broadcast_Retransmissions', 	'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c2a, 'descript' : 'Write_Num_Broadcast_Retransmissions', 	'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c2b, 'descript' : 'Read_Hold_Mode_Activity', 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c2c, 'descript' : 'Write_Hold_Mode_Activity', 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c2d, 'descript' : 'Read_Transmit_Power_Level', 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c2e, 'descript' : 'Read_SCO_Flow_Control_Enable', 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c2f, 'descript' : 'Write_SCO_Flow_Control_Enable', 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c30, 'descript' : 'not used', 		 			 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c31, 'descript' : 'Set_Host_Controller_To_Host_Flow_Control', 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c32, 'descript' : 'not used', 		 			 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c33, 'descript' : 'Host_Buffer_Size', 		 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c34, 'descript' : 'not used', 		 			 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c35, 'descript' : 'Host_Number_Of_Completed_Packets', 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c36, 'descript' : 'Read_Link_Supervision_Timeout', 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c37, 'descript' : 'Write_Link_Supervision_Timeout', 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c38, 'descript' : 'Read_Number_Of_Supported_IAC', 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c39, 'descript' : 'Read_Current_IAC_LAP', 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c3a, 'descript' : 'Write_Current_IAC_LAP', 		 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c3b, 'descript' : 'Read_Page_Scan_Period_Mode', 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c3c, 'descript' : 'Write_Page_Scan_Period_Mode', 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c3d, 'descript' : 'Read_Page_Scan_Mode', 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c3e, 'descript' : 'Write_Page_Scan_Mode', 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c3f, 'descript' : 'Set_AFH_Host_Channel_ Classification', 	'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c40, 'descript' : 'not used', 		 			 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c41, 'descript' : 'not used', 		 			 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c42, 'descript' : 'Read_Inquiry_Scan_Type', 		 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c43, 'descript' : 'Write_Inquiry_Scan_Type', 		 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c44, 'descript' : 'Read_Inquiry_Mode', 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c45, 'descript' : 'Write_Inquiry_Mode', 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c46, 'descript' : 'Read_Page_Scan_Type', 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c47, 'descript' : 'Write_Page_Scan_Type', 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c48, 'descript' : 'Read_AFH_Channel_Assessment_Mode', 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x0c49, 'descript' : 'Write_AFH_Channel_Assessment_Mode', 	'analyze_format' : cmd_normal_format },

	# HCI Informational Parameter Commands
	{ 'op_code' : 0x1001, 'descript' : 'Read_Local_Version_Information', 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1002, 'descript' : 'Read_Local_Supported_Commands', 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1003, 'descript' : 'Read_Local_Supported_Features', 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1004, 'descript' : 'Read_Local_ Extended_Features', 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1005, 'descript' : 'Read_Buffer_Size', 		 		 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1006, 'descript' : 'not used', 		 		 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1007, 'descript' : 'Read_Country_Code', 					'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1008, 'descript' : 'not used', 		 		 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1009, 'descript' : 'Read_BD_ADD', 		 		 			'analyze_format' : cmd_normal_format },
	
	# HCI Status Parameter Commands
	{ 'op_code' : 0x1401, 'descript' : 'Read_Failed_Contact_Counter', 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1402, 'descript' : 'Reset_Failed_Contact_Counter', 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1403, 'descript' : 'Get_Link_Quality', 		 		 		'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1404, 'descript' : 'not used', 		 		 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1405, 'descript' : 'Read_RSSI', 		 		 			'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1406, 'descript' : 'Read_AFH _Channel_Map', 				'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1407, 'descript' : 'Read_Cloc', 		 		 			'analyze_format' : cmd_normal_format },
	
	# HCI Testing Commands
	{ 'op_code' : 0x1801, 'descript' : 'Read_Loopback_Mode', 					'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1802, 'descript' : 'Write_Loopback_Mode', 					'analyze_format' : cmd_normal_format },
	{ 'op_code' : 0x1803, 'descript' : 'Enable_Device_Under_Test_Mode', 		'analyze_format' : cmd_normal_format },
	
	
]

def cmd_analyze(msg):
	print 'Command: ',
	op = msg[2] * 256 + msg[1]
	for t in cmd_type:
		if t['op_code'] == op:
			print '%s' % (t['descript']),
			cmd_analyze_fun(msg,t['analyze_format'])
			break
