#dataset = dw.load_dataset('https://data.world/stephen-hoover/chicago-city-council-votes')

# Use the dataframes property to assign the alderman_votes table to the variable votes_dataframe.
# votes_dataframe = dataset.dataframes['alderman_votes']

# Use the pandas shape property to get rows/columns size for the `votes_dataframe` dataframe.
#pp.pprint(votes_dataframe.shape)
#pp.pprint(votes_dataframe.head(3))


print('Mary had a little lamp.')
print('Its fleece was whie as {}.'.format('snow'))
print('and everzwhere that mary went.')
print('.' * 10) # what'd that do?

end1 = 'C'
end2 = "h"
end3 = "e"
end4 = "e"

print(end1 + end2 + end3 + end4, end=' ')

formatter = "{} {} {},{}"
print(formatter.format('one', 'two', 'three', 'four'))

days = 'Mon Tue Wed Thu Fri Sa Sun'
months = 'Jan\nFeb\nMar\nApr\n'

print('Here are the days: ', days)
print('Here are the months: ', months)

print('''
There is something about this.
going on here,
I dont know quite what
''')

Escape What it does.
\\ Backslash (\)
\' Single- quote (')
\" Double- quote (")
\a ASCII bell (BEL)
\b ASCII backspace (BS)
\f ASCII formfeed (FF)
\n ASCII linefeed (LF)
\N{name} Character named name in the Unicode database (Unicode only)
\r ASCII carriage return (CR)
\t ASCII horizontal tab (TAB)
\uxxxx Character with 16- bit hex value xxxx (Unicode only)
\Uxxxxxxxx Character with 32- bit hex value xxxxxxxx (Unicode only)
\v ASCII vertical tab (VT)
\ooo Character with octal value oo
\xhh Character with hex value hh
