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

def _push_line(name, line):

	file = open(name, "a+")
	fields = line.split()
	file.write("\t".join(fields))
	file.write("\n")
	file.close()

def _remove(name):

	if not os.path.exists(name):
		return
	os.remove(name)

def _split_main(path):

	_remove("tmp/cpu.tsv")
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

	header = ""
	lines = {}
	file = open(path)
	current_section = ""

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
			header = line
		elif 0 <= line.find("proc/s") and 0 <= line.find("cswch/s"):
			current_section = "tasks"
			header = line
		elif 0 <= line.find("pswpin/s") and 0 <= line.find("pswpout/s"):
			current_section = "swap"
			header = line
		elif 0 <= line.find("pgpgin/s") and 0 <= line.find("pgpgout/s"):
			current_section = "pages"
			header = line
		elif 0 <= line.find("tps") and 0 <= line.find("bwrtn/s"):
			current_section = "disk"
			header = line
		elif 0 <= line.find("frmpg/s") and 0 <= line.find("bufpg/s"):
			current_section = "page cache"
			header = line
		elif 0 <= line.find("kbmemfree") and 0 <= line.find("kbmemused"):
			current_section = "mem"
			header = line
		elif 0 <= line.find("kbswpfree") and 0 <= line.find("kbswpused"):
			current_section = "swap size"
			header = line
		elif 0 <= line.find("dentunusd") and 0 <= line.find("file-nr"):
			current_section = "nodes"
			header = line
		elif 0 <= line.find("ldavg-1"):
			current_section = "load average"
			header = line
		elif 0 <= line.find("TTY") and 0 <= line.find("rcvin/s"):
			current_section = "TTY"
			header = line
		elif 0 <= line.find("DEV") and 0 <= line.find("tps"):
			current_section = "DEV"
			header = line
		elif 0 <= line.find("IFACE") and 0 <= line.find("rxpck/s"):
			current_section = "IFACE"
			header = line
		elif 0 <= line.find("IFACE") and 0 <= line.find("rxerr/s"):
			current_section = "IFACE error"
			header = line
		elif 0 <= line.find("call/s") and 0 <= line.find("retrans/s"):
			current_section = "nfs"
			header = line
		elif 0 <= line.find("scall/s") and 0 <= line.find("badcall/s"):
			current_section = "nfsd"
			header = line
		elif 0 <= line.find("totsck") and 0 <= line.find("tcpsck"):
			current_section = "SOCK"
			header = line
		elif 0 <= line.find("Average:"):
			current_section = ""
		if current_section == "":
			continue
		if current_section not in lines:
			lines[current_section] = []
		lines[current_section].append(line)
		filename = "tmp/{}.tsv".format(current_section)
		_push_line(filename, line)

	file.close()

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

def _mkdir(path):

	if os.path.exists(path):
		return
	os.mkdir(path)

def _visualize_main():

	_visualize_load_average()
	_visualize_nfs()

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
