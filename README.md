my advent of code python solutions for year 2024!


EDIT:

I use these aliases (thanks to hyperneutrino) to efficiently run my code and fetch the input data:

alias aos="python3 solution.py < big"
alias aot="python3 solution.py < small"
alias aoc="aot; echo; aos"

function aol
    if test -n "$argv[1]"
        curl --cookie "session=$AOC_SESSION" -o big "https://adventofcode.com/$argv[1]/day/$argv[2]/input"
    else
        curl --cookie "session=$AOC_SESSION" -o big (date +https://adventofcode.com/%Y/day/%d/input)
    end
end

to make use of these aliases yourself, you have to set the AOC_SESSION variable which you have to find yourself in your browser.
Note that I am using fish shell so the syntax for the function might be different for you.