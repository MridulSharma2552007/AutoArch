import subprocess

def get_disks():
    result=subprocess.run(
        ["lsblk","-d","-o","NAME,SIZE,TYPE"],
        capture_output=True,
        text=True
        )
    lines=result.stdout.strip().split("\n")[1:]
    disk=[]

    for line in lines:
        parts=line.split()

        if len(parts)<3:
            continue
        name,size,dtype=parts
        if dtype=="disk":
            disks.appens({
                "name":name,
                "size":size,
                "path":f"/dev/{name}"
            })
    return disks