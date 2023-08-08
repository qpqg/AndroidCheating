#pylint:disable=C0301
from androidMemoryTool import AndroidMemoryTool
from androidMemoryTool.DataClasses import DataClasses as DT

types = {
	"DWORD": DT.DataTypes.DWORD,
	"BYTE": DT.DataTypes.BYTE,
	"DOUBLE": DT.DataTypes.DOUBLE,
	"FLOAT": DT.DataTypes.FLOAT,
	"STRING/TEXT": DT.DataTypes.UTF_8
}

def checkPid(pkg):
	pid = AndroidMemoryTool.get_pid(pkg)
	if(pid.isdigit()):
		return pid
	return pid

def type_ops(types):
	for k,v in enumerate(types):
		print(f"[{k}]. {v}")
	ops = input("Select: ")
	ops = types.get(list(types.keys())[int(ops)])
	return ops

while 1:
	pkg = input("Input pkg: ")
	pid = checkPid(pkg)
	if(pid):
		print(f"[{pkg}] Running On PID: [{pid}]\r\n")
		search = input("finder, replacer: ")
		finder,replacer = search.split(",")
		
		DATA_TYPE = type_ops(types)
		
		tool = AndroidMemoryTool(
					PKG=pkg,
					TYPE=DATA_TYPE,
					SPEED_MODE=False,
					WORKERS=100,
            		pMAP=AndroidMemoryTool.PMAP(ALL=True)
            )             	
		values = tool.read_value(finder)
		founded_offsets = values[0]
		if(founded_offsets):
			print(f"Search and Replacer: {finder} to {replacer}")
			result = tool.read_write_value(finder, replacer)
			print(f"Result: {result}\nCheck App")
			continue
	else:
		print(pid)
		break