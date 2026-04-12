import subprocess

def get_disks():
    result=subprocess.run(
        ["lsblk","-d","-o","NAME,SIZE,TYPE"],
        capture_output=True,
        text=True
        )
    lines=result.stdout.strip().split("\n")[1:]
    disks=[]

    for line in lines:
        parts=line.split()

        if len(parts)<3:
            continue
        name,size,dtype=parts
        if dtype=="disk":
            disks.append({
                "name":name,
                "size":size,
                "path":f"/dev/{name}"
            })
    return disks

def get_partitions(disk):
    result=subprocess.run(
        ["lsblk","-o","NAME,SIZE,TYPE,MOUNTPOINT",disk],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    lines=result.stdout.strip().split("\n")[1:]
    partitions=[]

    for line in lines:
        data=line.split()
        if len(data)<3:
            continue
        name = data[0].replace("├─", "").replace("└─", "")
        size=data[1]
        dtype=data[2]
        mountpoint = data[3] if len(data) > 3 else ""

        if dtype=="part":
            partitions.append({
                 "path": f"/dev/{name}",
                "size": size,
                "mount": mountpoint
})
    return partitions


        
    