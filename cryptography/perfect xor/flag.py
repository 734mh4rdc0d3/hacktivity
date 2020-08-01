cipher = [114, 84, 437, 8095, 33550434, 8589869170, 137438691376, 2305843008139952235, 2658455991569831744654692615953842245, 191561942608236107294793378084303638130997321548169294, 13164036458569648337239753460458722910223472318386943117783728223, 14474011154664524427946373126085988481573677491474835889066354349131199152216, 23562723457267347065789548996709904988477547858392600710143027597506337283178622239730365539602600561360255566462503270175052892578043215543382498428777152427010394496918664028644534128033831439790236838624033171435922356643219703101720713163527487298747400647801939587165936401087419375649057918549492160555647087, 141053783706712069063207958086063189881486743514715667838838675999954867742652380114104193329037690251561950568709829327164087724366370087116731268159313652487450652439805877296207297446723295166658228846926807786652870188920867879451478364569313922060370695064736073572378695176473055266826253284886383715072974324463835300053138429460296575143368065570759537328242]


perfect = [6,28,496,8128,33550336,8589869056,137438691328,2305843008139952128,2658455991569831744654692615953842176,191561942608236107294793378084303638130997321548169216, (2**107 -1)*2**(107-1) , (2**127 -1)*2**(127-1) ,(2**521 -1)*2**(521-1) ,(2**607 -1)*2**(607-1)]

ans = ""

for i in range(len(perfect)):
	ans+= chr(cipher[i]^perfect[i])

print(ans)