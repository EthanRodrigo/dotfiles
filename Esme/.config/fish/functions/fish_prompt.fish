function fish_prompt 

	# list of icons
	set I

	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 
	set I $I 

	# list of colors
	set C
	set C $C 5c00e6
	set C $C ff0000
	set C $C 0000ff
	set C $C 00ff00
	set C $C 66ffcc
	set C $C 66ffcc
	set C $C 66ccff
	set C $C 6666ff
	set C $C 006699
	set C $C ff1a8c

	# getting a random icon
	set n (math (random)%(count $I))  
	set m (math $n+1)
	set symbol $I[$m]

	# getting a random color
	set i (math (random) % (count $C))
	set j (math $i+1)
	set pwdColor $C[$j]


	set k (math (random) % (count $C))
	set l (math $i+1)
	set iconColor $C[$l]
	
	set x (math (random) % (count $C))
	set z (math $i+1)
	set symColor $C[$z]

	# prompting with colors
	echo -n (set_color $pwdColor)(prompt_pwd)(set_color $iconColor) $symbol (set_color $symColor) '❯ '
	set_color -o # bold

end
