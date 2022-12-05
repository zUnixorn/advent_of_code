#!/bin/bash

set -e

if [ -z "$1" ]; then
    echo "You need to specify a day"
    exit 1
fi

MESSAGE="The day can only be a number between 1 and 24"

case $1 in
    ''|*[!0-9]*) echo $MESSAGE; exit 1 ;;
    *) ;;
esac

if [ "$1" -lt 1 ] || [ "$1" -gt 24 ]; then
    echo "$MESSAGE"
    exit 1
fi

# from https://stackoverflow.com/questions/59895/how-do-i-get-the-directory-where-a-bash-script-is-located-from-within-the-script
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if [ -z "$TOKEN" ] && [ -f "${SCRIPT_DIR}/../.env" ]; then
    export "$(xargs < ${SCRIPT_DIR}/../.env)"
fi

NODOWNLOAD="0"

if [ -z "$TOKEN" ]; then
    # TODO make continueation optional
    read -p "token unset, only create templates? (y/N): " -r "NODOWNLOAD"
    if [[ ! "$NODOWNLOAD" =~ "^[Yy]$" ]]; then
        NODOWNLOAD="1"
    fi
fi

cd "${SCRIPT_DIR}/Python"

if [ -d "$1" ]; then
    echo "Solution for Day ${1} already exists"
    exit 1
fi

if [ "$NODOWNLOAD" = "0" ]; then
    URL="https://adventofcode.com/2022/day/${1}/input"
    STATUS=$(curl --cookie "session=$TOKEN" -s -o /dev/null -w "%{http_code}" "$URL")

    if [ "$STATUS" = "404" ]; then
        echo "The day is not unlocked yet"
        exit 1
    fi
fi

mkdir $1
cd $1

if [ "$NODOWNLOAD" = "0" ]; then
    curl --cookie "session=$TOKEN" -s -J -o "input" -w "%{http_code}" "$URL"
fi

cat << EOF > main.py
import part1
import part2

if __name__ == "__main__":
    with open("input") as file:
        lines = file.readlines()
    print(part1.solution(lines))
    print(part2.solution(lines))
EOF

cat << EOF > part1.py
def solution(lines):
    return "Not implemented"
EOF

cp part1.py part2.py