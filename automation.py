import os

print('''
1.Docker
2.LVM
3.Hadoop
4.AWS
	''')
firstInput=int(input('please enter your choice : '))
if firstInput==1:
	print("""
  please enter your choice by pressing the number :
	 1.install docker 
	 2.start docker service
	 3.download docker images
	 4.parmanenly start docker
	 5.run a new container
	 6.show running containers
	 7.start stoped container
	 8.stop running container
	 9.stop all running containers together
	 10.delete os permanently
	 11.delete image permanently
	 12.show downloaded images
	 13.show all the containers
					""")


	A = int(input('enter your choice : '))

	if A==1:
    		os.system('yum install docker-ce')

	elif A==2:
    		os.system('systemctl start docker')

	elif A==3:
    		print('choose your image\n a.centos:latest\n b.ubuntu:latest\n c.ubuntu:14.04\n')
    		B = input('enter your choice : ')
    		if B=='a':
        		os.system('docker pull centos:latest')
    		elif B=='b':
        		os.system('docker pull ubuntu:latest')
    		elif B=='c':
        		os.system('docker pull ubuntu:14.04')


	elif A==4:
    		os.system('systemctl enable docker')

	elif A==5:
    		name = input('give a name to container : ')
    		os.system('docker images')
    		image = input('enter image name with version : ')
    		os.system('docker run -it --name {} {}'.format(name,image))
    
	elif A==6:
    		os.system('docker ps')

	elif A==7:
    		os.system('docker ps -a')
    		name = input('enter container name : ')
    		os.system('docker start {}'.format(name))
    		os.system('docker attach {}'.format(name))
   
	elif A==8:
    		os.system('docker ps')
    		name = input('enter container name : ')
    		os.system('docker stop {}'.format(name))

	elif A==9:
    		os.system('docker ps')
    		os.system('docker stop `docker ps -a -q`')

	elif A==10:
    		os.system('docker ps -a')
    		name = input('enter name of container : ')
    		os.system('docker rm  {}'.format(name))
    		os.system('docker ps -a')

	elif A==11:
    		os.system('docker images')
    		image = input('enter name of image : ')
    		os.system('docker rmi {}'.format(image))

	elif A==12:
		os.system('docker images')

	elif A==13:
		os.system('docker ps -a')
	else:
		('invalid input!!')

elif firstInput==2:
	os.system('espeak-ng "please   enter   your    choice"')
	print('''
	1.create a logical volume(dynamic partition)
	2.increase the size of partition(logical volume)
	3.increase the size of volume group
		''')
	lvminput=int(input('enter your choice : '))
	
	if lvminput==1:
		os.system('fdisk -l')
		pv=int(input('enter number of storage you want to attach\n(min 2 max 6) : '))
		if (pv==1) or (pv>6):
			
			print('invalid input...')
		elif pv==2:
			pv1=input('enter full name of hard disk 1(e.g. /dev/sdb) : ')
			pv2=input('enter full name of hard disk 2 : ')
			#os.system('espeak-ng "creating physical volume"')
			os.system('pvcreate {}'.format(pv1))
			os.system('pvcreate {}'.format(pv2))
			#os.system('espeak-ng  "physical volume is created"')
			os.system('pvdisplay {}'.format(pv1))
			os.system('pvdisplay {}'.format(pv2))
			#os.system('espeak-ng  "know we are creating volume group so please give any name to the volume group"')
			vg=input('give any name to volume group : ')
			os.system('vgcreate {} {} {}'.format(vg,pv1,pv2))
			os.system('vgdisplay {}'.format(vg))
			#os.system('espeak-ng   "volume group is created"')

		elif pv==3:
			pv1=input('enter full name of hard disk 1(e.g. /dev/sdb) : ')
			pv2=input('enter full name of hard disk 2 : ')
			pv3=input('enter full name of hard disk 3 : ')
			#os.system('espeak-ng "creating physical volume"')
			os.system('pvcreate {}'.format(pv1))
			os.system('pvcreate {}'.format(pv2))
			os.system('pvcreate {}'.format(pv3))
			#os.system('espeak-ng  "physical volume is created"')
			os.system('pvdisplay {}'.format(pv1))
			os.system('pvdisplay {}'.format(pv2))
			os.system('pvdisplay {}'.format(pv3))
			#os.system('espeak-ng  "know we are creating volume group so please give any name to the volume group"')
			vg=input('give any name to volume group : ')
			os.system('vgcreate {} {} {} {}'.format(vg,pv1,pv2,pv3))
			os.system('vgdisplay {}'.format(vg))
			#os.system('espeak-ng   "volume group is created"')
		
		elif pv==4:
			pv1=input('enter full name of hard disk 1(e.g. /dev/sdb) : ')
			pv2=input('enter full name of hard disk 2 : ')
			pv3=input('enter full name of hard disk 3 : ')
			pv4=input('enter full name of hard disk 4 : ')
			#os.system('espeak-ng "creating physical volume"')
			os.system('pvcreate {}'.format(pv1))
			os.system('pvcreate {}'.format(pv2))
			os.system('pvcreate {}'.format(pv3))
			os.system('pvcreate {}'.format(pv4))
			#os.system('espeak-ng  "physical volume is created"')
			os.system('pvdisplay {}'.format(pv1))
			os.system('pvdisplay {}'.format(pv2))
			os.system('pvdisplay {}'.format(pv3))
			os.system('pvdisplay {}'.format(pv4))
			#os.system('espeak-ng  "know we are creating volume group so please give any name to the volume group"')
			vg=input('give any name to volume group : ')
			os.system('vgcreate {} {} {} {} {}'.format(vg,pv1,pv2,pv3,pv4))
			os.system('vgdisplay {}'.format(vg))
			#os.system('espeak-ng   "volume group is created"')
		
		elif pv==5:
			pv1=input('enter full name of hard disk 1(e.g. /dev/sdb) : ')
			pv2=input('enter full name of hard disk 2 : ')
			pv3=input('enter full name of hard disk 3 : ')
			pv4=input('enter full name of hard disk 4 : ')
			pv5=input('enter full name of hard disk 5 : ')
			#os.system('espeak-ng "creating physical volume"')
			os.system('pvcreate {}'.format(pv1))
			os.system('pvcreate {}'.format(pv2))
			os.system('pvcreate {}'.format(pv3))
			os.system('pvcreate {}'.format(pv4))
			os.system('pvcreate {}'.format(pv5))
			#os.system('espeak-ng  "physical volume is created"')
			os.system('pvdisplay {}'.format(pv1))
			os.system('pvdisplay {}'.format(pv2))
			os.system('pvdisplay {}'.format(pv3))
			os.system('pvdisplay {}'.format(pv4))
			os.system('pvdisplay {}'.format(pv5))
			#os.system('espeak-ng  "know we are creating volume group so please give any name to the volume group"')
			vg=input('give any name to volume group : ')
			os.system('vgcreate {} {} {} {} {} {}'.format(vg,pv1,pv2,pv3,pv4,pv5))
			os.system('vgdisplay {}'.format(vg))
			#os.system('espeak-ng   "volume group is created"')
		
		elif pv==6:
			pv1=input('enter full name of hard disk 1(e.g. /dev/sdb) : ')
			pv2=input('enter full name of hard disk 2 : ')
			pv3=input('enter full name of hard disk 3 : ')
			pv4=input('enter full name of hard disk 4 : ')
			pv5=input('enter full name of hard disk 5 : ')
			pv6=input('enter full name of hard disk 6 : ')
			#os.system('espeak-ng "creating physical volume"')
			os.system('pvcreate {}'.format(pv1))
			os.system('pvcreate {}'.format(pv2))
			os.system('pvcreate {}'.format(pv3))
			os.system('pvcreate {}'.format(pv4))
			os.system('pvcreate {}'.format(pv5))
			os.system('pvcreate {}'.format(pv6))
			#os.system('espeak-ng  "physical volume is created"')
			os.system('pvdisplay {}'.format(pv1))
			os.system('pvdisplay {}'.format(pv2))
			os.system('pvdisplay {}'.format(pv3))
			os.system('pvdisplay {}'.format(pv4))
			os.system('pvdisplay {}'.format(pv5))
			os.system('pvdisplay {}'.format(pv6))
			#os.system('espeak-ng  "know we are creating volume group so please give any name to the volume group"')
			vg=input('give any name to volume group : ')
			os.system('vgcreate {} {} {} {} {} {} {}'.format(vg,pv1,pv2,pv3,pv4,pv5,pv6))
			os.system('vgdisplay {}'.format(vg))
			#os.system('espeak-ng   "volume group is created"')
		
		lvsize=int(input('enter the size of partition : '))
		lvname=int(input('give any name to partition : '))
		print('creating the partition....')
		os.system('lvcreate --size {} --name {} {}'.format(lvsize,lvname,vg))
		os.system('lvdisplay {}/{}'.format(vg,lvname))
		print('formating the partition....')
		os.system('mkfs.ext4 /dev/mapper/{}-{}'.format(vg,lvname))
		dirname=input('enter directory name to mount the partition : ')
		print('mounting the partition....')
		os.system('mount /dev/mapper/{}-{} /{}'.format(vg,lvname,dirname))
		os.system('df -h')
		print('loading the driver....')
		os.system('udevadm settle')
		
	elif lvminput==2:
		lvname = input('enter full path of the partition(LV) : ')
		lvsize=int(input('enter size to be extend(5G) : '))
		os.system('lvextend --size +{} {}'.format(lvsize,lvname))
		os.system('resize2fs {}'.format(lvname))

	elif lvminput==3:
		vgn=input('enter name of your volume group : ')
		pvname=input('enter name of physical volume to be attached : ')
		os.system('vgextend {} {}'.format(vgn,pvname))

elif firstInput==3:
	print('welcome to Hadoop menu\n')
	print('''
	1.start the name node
	2.start the data node
	3.stop the name node
	4.stop the data node
	5.Format the name node
	6.show cluster report
	7.Run tcpdump
	8.Make a directory
	9.make an empty directory
	10.upload a file
	11.read a file
	12.stop firewall
	13.check used & unused ports
		''')

	choice=int(input('enter your choice : '))
	if choice==1:
		os.system('hadoop-daemon.sh start namenode')
	elif choice==2:
		os.system('hadoop-daemon.sh start datanode')
	elif choice==3:
		os.system('hadoop-daemon.sh stop namenode')
	elif choice==4:
		os.system('hadoop-daemon.sh stop datanode')
	elif choice==5:
		os.system('hadoop namenode -format')
	elif choice==6:
		os.system('hadoop dfsadmin -report')
	elif choice==7:
		os.system('tcpdump -i enp0s3 not port 22 -v -n -X')
	elif choice==8:
		x=input('give the path where you want to make th directory : ')
		os.system('mkdir {}'.format(x))
	elif choice==9:
		n=input('enter full path of empty file : ')
		os.system('hadoop fs -touchz {}'.format(n))
	elif choice==10:
		y=input('enter the block size : ')
		z=input('enter name of file you want to upload : ')
		os.system('hadoop fs -D dfs.block.size={} -put {}'.format(y,z))
	elif choice==11:
		r=input('enter name of file you want to read : ')
		os.system('hadoop fs -cat {}'.format(r))
	elif choice==12:
		os.system('systemctl stop firewalld')
	elif choice==13:
		os.system('netstat -tnlp')
	

else:
	('invalid input!!')    


elif firstInput==4:
	pyttsx3.speak("AWS Menu ")

	AWSData=("""





    =====================================================================================================================

        ################################## *  Aws MENU  * ###########################################

    =====================================================================================================================





            Services :

                

                 1  : Install AWS CLI                      [say: Install AWS]

                 2  : AWS Configure                        [say: Configure]

                 3  : Create Key                           [say: create key]

                 4  : Create Security Group                [say: create SG or create group]

                 5  : Launch New AWS Instance              [say: launch instance]

                 6  : Start Instance                       [say: start instance]

                 7  : Stop Instance                        [say: Stop instance]

                 8  : Create EBS Volume                    [say: create volume]

                 9  : Attach EBS Volume To Instance        [say: Attach Volume]

                 10 : Detach EBS Volume                    [say: remove volume]

                 11 : Delete EBS Volume                    [say: Delete Volume]

                 12 : Create S3 Bucket                     [say : Create bucket]

                 13 : Upload Data in S3 Bucket             [say: upload data]

                 14 : Create Cloud Fornt Distribution      [say: create CDN]

                 15 : Create Snapshot                      [say: create snaps]

                		



                



            

            Say " Menu " For Main Menu & "Exit or bye" for Exit.



            * Adding More Services Soon...



    """)



    while 1:

        print(AWSData)

        pyttsx3.speak("I can help in these services. Portal is under construction. We are adding more services soon. ")

        ch=getAudioInput()

        print(ch)

        

        if ("Install" in ch) or ("AWS CLI" in ch):

            pyttsx3.speak("processing please wait....")

            os.system("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip' ")

            os.system("unzip awscliv2.zip")

            os.system("sudo ./aws/install")

            print(" aws --version   echo \AWS is success fullly installed")



         

        elif ("AWS" in ch) or ("Configure" in ch) or ("AWS Configure" in ch):

            pyttsx3.speak("processing please wait....")

            os.system("aws configure")

        elif ("pair" in ch) or ("key" in ch):

            pyttsx3.speak("processing please wait....")

            na =input("Enter key name : ")

            os.system("aws ec2 create-key-pair --key-name  {} --output text > {}.pem".format(na,na) )

        elif ("security" in ch) or ("group" in ch):

            pyttsx3.speak("processing please wait....")

            nam= input("Enter Security group name : ")

            desc = input("enter description : ")

            os.system("aws ec2 create-security-group --group-name {} --description {}".format(nam,desc))

        elif ("launch" in ch)or ("Instance" in ch):

            pyttsx3.speak("processing please wait....")

            na = input("Enter key name : ")

            sgi = input("Enter Security group id : ")

            co = input("Enter no. of instance you want to launch : ")

            os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --count {} --subnet-id subnet-4d225201 --security-group-ids {} --key-name {}".format(co,sgi,na) )

        elif ("Start" in ch) or ("Instance" in ch) or ("Start Instance" in ch ):

            pyttsx3.speak("processing please wait....")

            ids =input("Enter Instance-Ids : ")

            os.system("aws ec2 start-instances --instance-ids {}".format(ids))

        elif ("Stop" in ch) or ("Instance" in ch) or ("Stop Instance" in ch ):

            pyttsx3.speak("processing please wait....")

            na =input("Enter Instance-Ids : ")

            os.system("aws ec2 stop-instances --instance-ids {} ".format(na) )

        elif ("EBS" in ch) or ("Volume" in ch) or (" Create EBS Volume" in ch ) :

            pyttsx3.speak("processing please wait....")

            sz =input("Enter size in GB's : ")

            os.system("aws ec2 create-volume  --volume-type gp2 --size {}  --availability-zone ap-south-1b".format(sz))

        elif ("attach" in ch) or ("attach volume " in ch) :

            pyttsx3.speak("processing please wait....")

            vid =input("Enter Volume Id : ")

            iid =input("Enter Instance-Ids : ")

            os.system("aws ec2 attach-volume  --volume-id {} --instance-id {} --device /dev/sdf".format(vid,iid))

        elif ("detach" in ch) or (" Detach Volume" in ch) :

            pyttsx3.speak("processing please wait....")

            sz =input("Enter volume Id  : ")

            os.system("aws ec2 detach-volume  --volume-id {} ".format(sz))

        elif ("Delete" in ch) or ("Delete Volume" in ch) :

            pyttsx3.speak("processing please wait....")

            sz =input("Enter volume Id  : ")

            os.system("aws ec2 delete-volume  --volume-id {} ".format(sz))

        elif (" Create Bucket" in ch) or (" Create S3" in ch) or ("S3 Bucket" in ch ):

            pyttsx3.speak("processing please wait....")

            sz =input("Enter Name for Bucket : ")

            os.system("aws s3api create-bucket --bucket {}  --create-bucket-configuration LocationConstraint=ap-south-1".format(sz))

        elif ("upload in s3" in ch) or ("upload in bucket" in ch) or ("upload" in ch ):

            pyttsx3.speak("processing please wait....")

            sz =input("Enter the path of file : ")

            ph =input("Enter Name of Bucket : ")

            os.system("aws s3 cp {} s3://{} --acl public-read-write ".format(sz,ph))

        elif ("cloud front" in ch) or ("Distribution" in ch) or ("Create Distribution " in ch ):

            pyttsx3.speak("processing please wait....")

            sz =input("Enter S3 bucket name : ")

            ph =input("Enter Data Name : ")

            os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {} ".format(sz,ph))

        

        elif ("Snapshot" in ch) or (" create" in ch) or (" create snapshot" in ch ):

            pyttsx3.speak("processing please wait....")

            sz =input("Enter Volume Id : ")

            os.system("aws ec2 create-snapshot --volume-id {}".format(sz))

        elif(("menu" in ch) ):

            break

        elif(("exit"in ch) or ("bye" in ch) ):

            out()

        else:

            print("Input is invalid")

else:

	exit()

