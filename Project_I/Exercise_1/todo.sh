#!/bin/bash

if [[ ! -d ~/todo ]]; then
	mkdir ~/todo
fi

touch ~/todo/list.txt

todo_data=$(cat ~/todo/list.txt)

case "$1" in
	help )
		echo "Usage: ${0##*/} [OPTION] [ARGS]..."
		printf "Manages a todo list.\n\nOPTIONS:\n\n"
		printf " %-50s %s\n\n" "help" "Displays usage and commands."
		printf " %-50s %s\n\n" "add \"task in quotes\" [optional date string]" "Saves the task to the todo list. Date optional in format [DD-MM-YYYY]."
		printf " %-50s %s\n\n" "list [optional date string]" "Displays the tasks in the todo list. Date optional [DD-MM-YYYY]"
		printf " %-50s %s\n\n" "del <index>" "Deletes a task at a certain."
		;;
	del )
		if [[ ! "$2" =~ ^[0-9]{1,4}$ ]] || [ $# -gt 2 ]; then
			echo "Invalid or missing arguments."
			echo "Usage: ${0##*/} del <index>"
			exit 1
		fi
		todelete=$(grep -P "^$2\t.*\t.*$" ~/todo/list.txt)
		if [[ ! -z "$todelete" ]] ; then
			echo "Deleted: $todelete"
			grep -Pv "^$2\t.*\t.*$" ~/todo/list.txt > temp
			mv temp ~/todo/list.txt
		else
			echo "Index invalid. Please use list to check indices."
		fi
		;;
	list )
		mydate=($(echo "$2" | sed 's/-/ /g'))
		date -d "${mydate[2]}-${mydate[1]}-${mydate[0]}" "+%d/%m/%Y"> /dev/null  2>&1
		if [[ "$?" -eq 1 ]] || ([[ ! "$2" =~ ^([0-9]{2}-){2}[0-9]{4}$ ]] && [ ! -z "$2" ]); then
			echo "Wrong date format"
			echo "Usage: ${0##*/} list [DD-MM-YYYY]"
			exit 1
		fi
		if [[ -z "$todo_data" ]]; then
			echo "No tasks available!"
			exit 1		
		else
			echo "Upcoming Items:"
		fi
		indices=($(echo "$todo_data" | cut -f1))
		tasks=($(echo "$todo_data" | cut -f2))
		dates=($(echo "$todo_data" | cut -f3))
		maxlen=${#tasks[0]}

		for (( i = 1; i < ${#tasks[@]}; i++ )); do
			if [[ maxlen -le ${#tasks[i]} ]]; then
				maxlen=${#tasks[i]}
			fi
		done
		if [[ -z "$2" ]]; then
			for (( i = 0; i < ${#indices[@]}; i++ )); do
				printf "%3s: %-${maxlen}s %-10s\n" "${indices[$i]}" "${tasks[$i]}" "${dates[$i]}"
			done
		else
			for (( i = 0; i < ${#indices[@]}; i++ )); do
				if [[ "${dates[$i]}" -eq "$2" ]]; then
					printf "%3s: %-${maxlen}s %-10s\n" "${indices[$i]}" "${tasks[$i]}" "${dates[$i]}"
				fi
			done
		fi
		;;
	add )
		if [ -z "$2" ] || [ $# -gt 3 ] ; then
			echo "Invalid number of arguments."
			echo "Usage: ${0##*/} add \"task\" [DD-MM-YYYY]"
			exit 1
		fi
		mydate=($(echo "$3" | sed 's/-/ /g'))
		date -d "${mydate[2]}-${mydate[1]}-${mydate[0]}" "+%d/%m/%Y"> /dev/null  2>&1
		if  [[ "$?" -eq 1 ]] || ([[ ! "$3" =~ ^([0-9]{2}-){2}[0-9]{4}$ ]] && [ ! -z "$3" ]); then
			echo "Wrong date format"
			echo "Usage: ${0##*/} add \"task\" [DD-MM-YYYY]"
			exit 1
		fi

		if [[ -z "$todo_data" ]]; then
			echo -e "Added: #0 - \"$2\" ${3:-"NA"}"
			echo -e "0\t$2\t${3:-"NA"}" >> ~/todo/list.txt
			exit 0
		fi

		task=$(echo "$todo_data" | grep -Pine "\t$2\t")
		if [[ ! -z "$task" ]]; then
			date_exists=$(echo "$task" | cut -f3 | grep "${3:-"NA"}")
			if [[ -z "$date_exists" ]]; then
				index=$(tail -n1 ~/todo/list.txt | cut -f1)
				echo -e "Added: #$(($index+1)) - \"$2\" ${3:-"NA"}"
				echo -e "$(($index+1))\t$2\t${3:-"NA"}" >> ~/todo/list.txt
			else
				echo "Error: Same task already set."
				exit 1
			fi
		else
			index=$(tail -n1 ~/todo/list.txt | cut -f1)
			echo -e "Added: #$(($index+1)) - \"$2\" ${3:-"NA"}"
			echo -e "$(($index+1))\t$2\t${3:-"NA"}" >> ~/todo/list.txt	
		fi
		;;
	* )
		echo "Usage: ${0##*/} [OPTION] [ARGS]..."
		exit 1
		;;
esac

exit 0