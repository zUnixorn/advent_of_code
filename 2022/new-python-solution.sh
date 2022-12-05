set -e

if [ -z "$1" ]; then
    echo "You need to specify a Day"
    exit 1
fi

# from https://stackoverflow.com/questions/59895/how-do-i-get-the-directory-where-a-bash-script-is-located-from-within-the-script
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd "${SCRIPT_DIR}/Python"

if [ -d "$1" ]; then
    echo "Solution for Day ${1} already exists"
    exit 1
fi

mkdir $1
cd $1

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