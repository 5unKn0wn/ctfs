#!/bin/bash
for b in {1..5}
do
	for c in {1..5}
	do
		for d in {1..5}
		do
			for e in {1..5}
			do
				for f in {1..5}
				do
					for g in {1..5}
					do
						for h in {1..5}
						do
							for i in {1..5}
							do
								for j in {1..5}
								do
									if [ "`(echo "4 $b $c $d $e $f $g $h $i $j") | ./unlock_me | grep \"Congrats\"`" ]
									then
										echo "find!!!!!!!!!!"
										echo "4 $b $c $d $e $f $g $h $i $j"
										exit
									fi
								done
							echo "4 $b $c $d $e $f $g $h $i $j"
							done
						done
					done
				done
			done
		done
	done
done
