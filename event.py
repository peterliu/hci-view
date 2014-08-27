
event_type = [ 
	{ 'event_code' : 0x01, 'descript' : 'Inquiry Complete',                         },
	{ 'event_code' : 0x02, 'descript' : 'Inquiry Result',                           },
	{ 'event_code' : 0x03, 'descript' : 'Connection Complete',                      },
	{ 'event_code' : 0x04, 'descript' : 'Connection Request',                       },
	{ 'event_code' : 0x05, 'descript' : 'Disconnection Complete',                   },
	{ 'event_code' : 0x06, 'descript' : 'Authentication Complete',                  },
	{ 'event_code' : 0x07, 'descript' : 'Remote Name Request Complete',             },
	{ 'event_code' : 0x08, 'descript' : 'Encryption Change',                        },
	{ 'event_code' : 0x09, 'descript' : 'Change Connection Link Key Complete',      },
	{ 'event_code' : 0x0a, 'descript' : 'Master Link Key Complete',                 },
	{ 'event_code' : 0x0b, 'descript' : 'Read Remote Supported Features Complete',  },
	{ 'event_code' : 0x0c, 'descript' : 'Read Remote Version Information Complete', },
	{ 'event_code' : 0x0d, 'descript' : 'QoS Setup Complete',                       },
	{ 'event_code' : 0x0e, 'descript' : 'Command Complete',                         },
	{ 'event_code' : 0x0f, 'descript' : 'Command Status',                           },
	{ 'event_code' : 0x10, 'descript' : 'Hardware Error',                           },
	{ 'event_code' : 0x11, 'descript' : 'Flush Occurred',                           },
	{ 'event_code' : 0x12, 'descript' : 'Role Change',                              },
	{ 'event_code' : 0x13, 'descript' : 'Number Of Completed Packets',              },
	{ 'event_code' : 0x14, 'descript' : 'Mode Change',                              },
	{ 'event_code' : 0x15, 'descript' : 'Return Link Keys',                         },
	{ 'event_code' : 0x16, 'descript' : 'PIN Code Request',                         },
	{ 'event_code' : 0x17, 'descript' : 'Link Key Request',                         },
	{ 'event_code' : 0x18, 'descript' : 'Link Key Notification',                    },
	{ 'event_code' : 0x19, 'descript' : 'Loopback Command',                         },
	{ 'event_code' : 0x1a, 'descript' : 'Data Buffer Overflow',                     },
	{ 'event_code' : 0x1b, 'descript' : 'Max Slots Change',                         },
	{ 'event_code' : 0x1c, 'descript' : 'Read Clock Offset Complete',               },
	{ 'event_code' : 0x1d, 'descript' : 'Connection Packet Type Changed',           },
	{ 'event_code' : 0x1e, 'descript' : 'QoS Violation',                            },
	{ 'event_code' : 0x1f, 'descript' : 'Page Scan Mode Change',                    },
	{ 'event_code' : 0x20, 'descript' : 'Page Scan Repetition Mode Change',         },
	{ 'event_code' : 0x21, 'descript' : 'HCI Flow Specification Complete',          },
	{ 'event_code' : 0x22, 'descript' : 'Inquiry Result with RSSI',                 },
	{ 'event_code' : 0x23, 'descript' : 'Read Remote Extended Features Complete',   },
	{ 'event_code' : 0x2c, 'descript' : 'Synchronous Connection Complete',          },
	{ 'event_code' : 0x2d, 'descript' : 'Synchronous Connection Changed',           },
	{ 'event_code' : 0xfe, 'descript' : 'reserved for Bluetooth Logo testing',      },
	{ 'event_code' : 0xff, 'descript' : 'reserved for vendor specific events',      },
]

	
def event_analyze(msg):
	print 'Event: ',
	code = msg[1]
	for t in event_type:
		if t['event_code'] == code:
			print '%s' % (t['descript']),
			#cmd_analyze_fun(msg,t['analyze_format'])
			break
	pass
