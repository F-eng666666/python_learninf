import os

cmd_list= [ "getprop | grep ro.build.display.id",
			"getprop | grep ro.vendor.liauto.mdb.serialno",
			"getprop | grep ro.boot.board.type",
			"getprop | grep ro.boot.board.SSVersion",
			"getprop | grep ro.boot.hardware.secure",
			"getprop | grep ro.boot.secure.develop.mode",
			"getprop | grep ro.boot.secure.recycled.dev",
			"getprop | grep ro.boot.vbmeta.device_state",
			"getprop | grep vendor.liauto.mdb.vin",
			"getprop | grep vendor.liauto.mdb.sn",
			"getprop | grep ro.boot.hu.boot.mode",
			"laconfig get-string ECUSWID",
			"laconfig get-string ECUHWID",
			"flash_mcu",
			"/vendor/bin/flash_mcu",
			"getprop | grep ro.vendor.mcu.version",
			"get_mcu_version",
			"getprop | grep vendor.liauto.mdb.version5g",
			"getprop | grep vendor.liauto.mdb.5g",
			"setprop vendor.liauto.mdb.5g download_start",
			"setprop vendor.liauto.mdb.5g download_start_fastboot",
			"ls /ota_package/5g_image",
			"mcurpc_tool UART 0 0x0705 000310"
            ]
for str in cmd_list:
    cmd = "mdb.exe -socf -S 172.31.2.1 \""+str+"\""
    os.system(cmd)

print("ending")