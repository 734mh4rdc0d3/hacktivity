#!/bin/bash
while  [ 1 ]
do
	for i in $(ls)
	do
		if [[ $(file -ib $i | cut -d ';' -f 1) == "application/gzip" ]]
		then
			if  [[ $i == *.gz ]]
			then
				gunzip -q $i;

			else
				mv $i $i.gz;
				echo "removing by adding extension";
				gunzip -q $i;
			fi
		fi
		if [[ $(file -ib $i | cut -d ';' -f 1) == "application/x-xz" ]]
		then
			if  [[ $i == *.xz ]]
			then
				unxz $i && rm $i;

			else
				mv $i $i.xz;
				echo "removing by adding extension";
				unxz $i && rm $i;
			fi
		fi
		if [[ $(file -ib $i | cut -d ';' -f 1) == "application/zip" ]]
		then
			if  [[ $i == *.zip ]]
			then
				unzip -q $i && rm $i;

			else
				mv $i $i.zip;
				echo "removing by adding extension";
				unzip -q $i && rm $i;
			fi
		fi
		if [[ $(file -ib $i | cut -d ';' -f 1) == "application/x-bzip2" ]]
		then
			if  [[ $i == *.bz2 ]]
			then
				bzip2 -d $i;

			else
				mv $i $i.bz2;
				echo "removing by adding extension";
				bzip2 -d $i;
			fi
		fi
	done
done
# Although this worked but elegant solution would be to use 7z instead of seperate tools for every one
# while true; do find . -type f | while read f; do mv "$f" "1";7z -y e "1"; done; done