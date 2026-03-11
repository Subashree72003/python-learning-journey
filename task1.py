MARK =[78,45,78,69,87,97]
#1}Class-la highest mark and lowest mark rendu-um kandupidikkanum.
print(min(MARK))
print(max(MARK))

#2..Index 2-la irukura student mark remove panna sollraanga.
MARK.pop(2)
print(MARK)

#3..Ippo class-la ethana students irukaanga nu kekraanga.
print(len(MARK))

#4..Oru student late ah exam ezhudhinaan, avanukku 82 marks.
MARK.append(88)
print(MARK)

#5..Re-exam ezhudhina 2 students ku marks 55, 60
MARK.extend([96,78])
print(MARK)

#6..Rank list prepare panna marks ascending order-la venum.
print(sorted(MARK))

#7..Class oda total marks calculate panna sollraanga.
print(sum(MARK))

#8..Marks-ah reverse order-la display panna sollraanga.
MARK.reverse()
print(MARK)

#9..45 marks ethana students ku vandirku nu teacher kekraanga.
print(MARK.count(45))

#10..45 marks vandha student malpractice panninaanu remove panna sollraanga.
MARK.remove(45)
print(MARK)

#11..2rd position student-ku grace mark 8 add panna.
MARK[2]= MARK[2] +8
print(MARK)

#12.Insert a new mark btw list
MARK.insert(2,78)

#13.New semester start aagudhu. Old marks ellam clear panna sollraanga.
MARK.clear()
print(MARK)

