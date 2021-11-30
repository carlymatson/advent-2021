adv () {
    typeset -Z 2 day
    day=$1
    infile="inputs/day$day.txt"
    infileex="inputs/day${day}_example.txt"
    dayfile="python_scripts/day$day.py"
    touch $infile
    touch $infileex
    touch $dayfile
    cat "python_scripts/template.py" > $dayfile
    sed -i '' "s/01/${day}/g" $dayfile
}
