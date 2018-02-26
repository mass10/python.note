#!/usr/bin/env python3
# coding: utf-8




import os
import sys
import io
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot
import pandas
import optparse
import glob






def _as_tsv(s):

	fields = s.split()
	return "\t".join(fields)

def _push_line(name, line):

	file = open(name, "a+")
	file.write(line)
	file.write("\n")
	file.close()

def _remove(name):

	names = glob.glob(name)
	for e in names:
		if not os.path.exists(e):
			continue
		os.remove(e)

def _split_main(path):

	_remove("tmp/cpu.tsv")
	_remove("tmp/cpu-*.tsv")
	_remove("tmp/DEV.tsv")
	_remove("tmp/disk.tsv")
	_remove("tmp/IFACE error.tsv")
	_remove("tmp/IFACE.tsv")
	_remove("tmp/load average.tsv")
	_remove("tmp/mem.tsv")
	_remove("tmp/nfs.tsv")
	_remove("tmp/nfsd.tsv")
	_remove("tmp/nodes.tsv")
	_remove("tmp/page cache.tsv")
	_remove("tmp/pages.tsv")
	_remove("tmp/SOCK.tsv")
	_remove("tmp/swap size.tsv")
	_remove("tmp/swap.tsv")
	_remove("tmp/tasks.tsv")
	_remove("tmp/TTY.tsv")

	headers_map = {}
	cpu_header = ""
	lines = {}
	file = open(path)
	current_section = ""
	cpus = set()

	while True:
		line = file.readline()
		if line == "":
			break
		line = line.rstrip()
		if line == "":
			continue
		if 0 <= line.find("Average:"):
			continue
		if 0 <= line.find("CPU") and 0 <= line.find("%usr"):
			current_section = "cpu"
			if current_section not in headers_map:
				headers_map[current_section] = line
				print("adding new header ... [{}]".format(line))
			else:
				print("ignoring new header ... [{}]".format(line))
			continue
		elif 0 <= line.find("proc/s") and 0 <= line.find("cswch/s"):
			current_section = "tasks"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		elif 0 <= line.find("pswpin/s") and 0 <= line.find("pswpout/s"):
			current_section = "swap"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		elif 0 <= line.find("pgpgin/s") and 0 <= line.find("pgpgout/s"):
			current_section = "pages"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		elif 0 <= line.find("tps") and 0 <= line.find("bwrtn/s"):
			current_section = "disk"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		elif 0 <= line.find("frmpg/s") and 0 <= line.find("bufpg/s"):
			current_section = "page cache"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		elif 0 <= line.find("kbmemfree") and 0 <= line.find("kbmemused"):
			current_section = "mem"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		elif 0 <= line.find("kbswpfree") and 0 <= line.find("kbswpused"):
			current_section = "swap size"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		elif 0 <= line.find("dentunusd") and 0 <= line.find("file-nr"):
			current_section = "nodes"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		elif 0 <= line.find("ldavg-1"):
			current_section = "load average"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		elif 0 <= line.find("TTY") and 0 <= line.find("rcvin/s"):
			current_section = "TTY"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		elif 0 <= line.find("DEV") and 0 <= line.find("tps"):
			current_section = "DEV"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		elif 0 <= line.find("IFACE") and 0 <= line.find("rxpck/s"):
			current_section = "IFACE"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		elif 0 <= line.find("IFACE") and 0 <= line.find("rxerr/s"):
			current_section = "IFACE error"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		elif 0 <= line.find("call/s") and 0 <= line.find("retrans/s"):
			current_section = "nfs"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		elif 0 <= line.find("scall/s") and 0 <= line.find("badcall/s"):
			current_section = "nfsd"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		elif 0 <= line.find("totsck") and 0 <= line.find("tcpsck"):
			current_section = "SOCK"
			if current_section not in headers_map:
				headers_map[current_section] = line
			continue
		if current_section == "":
			continue

		# if current_section == "cpu":
		# 	fields = line.split()
		# 	cpu = fields[1]
		# 	if cpu == "CPU":
		# 		continue
		# 	del fields[1]
		# 	line = "\t".join(fields)
		# 	filename = "tmp/{}-{}.tsv".format(current_section, cpu)
		# 	if cpu not in cpus:
		# 		header_line = _as_tsv(cpu_header)
		# 		del header_line[1]
		# 		_push_line(filename, _as_tsv(cpu_header))
		# 	cpus.add(cpu)
		# else:
		# 	filename = "tmp/{}.tsv".format(current_section)

		if current_section not in lines:
			lines[current_section] = []
		lines[current_section].append(line)

		# _push_line(filename, line)

	file.close()

	for section in lines:
		contents = lines[section]
		filename = "tmp/{}.tsv".format(section)
		print("[TRACE] creating ... [{}].".format(filename))
		_push_line(filename, headers_map[section])
		for line in contents:
			_push_line(filename, line)

def _visualize_cpu():

	names = glob.glob("tmp/cpu-*.tsv")
	for e in names:
		print("[TRACE] reading [{}]".format(e))
		pyplot.rcParams.update({"legend.labelspacing": 0.25})
		dataframe = pandas.read_table(e, index_col=[0])
		a = dataframe.plot(title="title", figsize=(16, 6))
		# ？
		pyplot.autoscale()
		# グリッド線を表示する
		pyplot.grid()
		# 目盛りを斜めに
		pyplot.xticks(rotation=70)
		# 目盛りが隠れるのを防ぐ
		pyplot.tight_layout()
		# ファイルに保存
		name = e.replace("tmp/", "images/")
		name = e.replace(".tsv", ".png")
		pyplot.savefig("images/cpu.png")

def _visualize_dev():

	pyplot.rcParams.update({"legend.labelspacing": 0.25})
	dataframe = pandas.read_table("tmp/DEV.tsv", index_col=[0])
	a = dataframe.plot(title="title", figsize=(16, 6))
	# ？
	pyplot.autoscale()
	# グリッド線を表示する
	pyplot.grid()
	# 目盛りを斜めに
	pyplot.xticks(rotation=70)
	# 目盛りが隠れるのを防ぐ
	pyplot.tight_layout()
	# ファイルに保存
	pyplot.savefig("images/DEV.png")

def _visualize_disk():

	pyplot.rcParams.update({"legend.labelspacing": 0.25})
	dataframe = pandas.read_table("tmp/disk.tsv", index_col=[0])
	a = dataframe.plot(title="title", figsize=(16, 6))
	# ？
	pyplot.autoscale()
	# グリッド線を表示する
	pyplot.grid()
	# 目盛りを斜めに
	pyplot.xticks(rotation=70)
	# 目盛りが隠れるのを防ぐ
	pyplot.tight_layout()
	# ファイルに保存
	pyplot.savefig("images/disk.png")

def _visualize_iface():
	return

def _visualize_iface_error():
	return

def _visualize_load_average():

	pyplot.rcParams.update({"legend.labelspacing": 0.25})
	dataframe = pandas.read_table("tmp/load average.tsv", index_col=[0])
	del dataframe["runq-sz"]
	del dataframe["plist-sz"]
	a = dataframe.plot(title="title", figsize=(16, 6))
	# ？
	pyplot.autoscale()
	# グリッド線を表示する
	pyplot.grid()
	# 目盛りを斜めに
	pyplot.xticks(rotation=70)
	# 目盛りが隠れるのを防ぐ
	pyplot.tight_layout()
	# ファイルに保存
	pyplot.savefig("images/load average.png")

def _visualize_mem():
	return

def _visualize_nfs():

	pyplot.rcParams.update({"legend.labelspacing": 0.25})
	dataframe = pandas.read_table("tmp/nfs.tsv", index_col=[0])
	a = dataframe.plot(title="title", figsize=(16, 6))
	# ？
	pyplot.autoscale()
	# グリッド線を表示する
	pyplot.grid()
	# 目盛りを斜めに
	pyplot.xticks(rotation=70)
	# 目盛りが隠れるのを防ぐ
	pyplot.tight_layout()
	# ファイルに保存
	pyplot.savefig("images/nfs.png")

def _visualize_nfsd():
	return

def _visualize_nodes():
	return

def _visualize_page_cache():
	return

def _visualize_pages():
	return

def _visualize_sock():
	return

def _visualize_swap():
	return

def _visualize_swap():
	return

def _visualize_tasks():
	return

def _visualize_tty():
	return

def _mkdir(path):

	if os.path.exists(path):
		return
	os.mkdir(path)

def _visualize_main():

	_visualize_cpu()
	_visualize_tasks()
	_visualize_swap()
	_visualize_pages()
	_visualize_disk()
	_visualize_page_cache()
	_visualize_mem()
	_visualize_swap()
	_visualize_nodes()
	_visualize_load_average()
	_visualize_tty()
	_visualize_dev()
	_visualize_iface()
	_visualize_iface_error()
	_visualize_nfs()
	_visualize_nfsd()
	_visualize_sock()

def _main(argv):

	# コマンドラインオプションを読み取り
	p = optparse.OptionParser(usage="usage")
	p.add_option("--sar", default=None, dest="sar", help="path to a sar file.")
	(options, args) = p.parse_args()
	if options.sar is None or options.sar == "":
		p.print_help()
		return
	if options.sar == "":
		p.print_help()
		return
	if not os.path.exists(options.sar):
		p.print_help()
		return

	# 作業ディレクトリを準備
	_mkdir("images")
	_mkdir("tmp")

	# 分割して一時ファイルを出力
	_split_main(options.sar)

	# グラフ出力
	_visualize_main()

_main(sys.argv)
