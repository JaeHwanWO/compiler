from sys import argv

# to make Production Table efficiently, we used excel and included functions managing excel file
import xlrd
book = xlrd.open_workbook('data.xlsx')
sheet = book.sheet_by_name('Sheet1')
data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)]
        for r in range(sheet.nrows)]
# print(data)
productionTable = [['State', 'vtype', 'id', 'semi', 'assign', 'lparen', 'rparen', 'lbrace', 'rbrace', 'comma', 'if', 'while', 'for', 'else', 'literal', 'addsub', 'multdiv', 'num', 'float', 'comp', 'return', '$', 'CODE', 'VDECL', 'FDECL', 'ASSIGN', 'RHS', 'ARG', 'BLOCK', 'RETURN', 'MOREARGS', 'STMT', 'COND', 'ELSE', 'EXPR', 'TERM', 'FACTOR'], [0.0, 'shift(4)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'reduce(CODE→ ε)', 1.0, 2.0, 3.0, '', '', '', '', '', '', '', '', '', '', '', ''], [1.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'accept', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [2.0, 'shift(4)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'reduce(CODE→ ε)', 5.0, 2.0, 3.0, '', '', '', '', '', '', '', '', '', '', '', ''], [3.0, 'shift(4)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'reduce(CODE→ ε)', 6.0, 2.0, 3.0, '', '', '', '', '', '', '', '', '', '', '', ''], [4.0, '', 'shift(7)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 8.0, '', '', '', '', '', '', '', '', '', '', ''], [5.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'reduce(CODE→ VDECL CODE)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [6.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'reduce(CODE→ FDECL CODE)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [7.0, '', '', 'shift(9)', 'shift(11)', 'shift(10)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [8.0, '', '', 'shift(12)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [9.0, 'reduce(VDECL→ vtype id semi)', 'reduce(VDECL→ vtype id semi)', '', '', '', '', '', 'reduce(VDECL→ vtype id semi)', '', 'reduce(VDECL→ vtype id semi)', 'reduce(VDECL→ vtype id semi)', 'reduce(VDECL→ vtype id semi)', '', '', '', '', '', '', '', 'reduce(VDECL→ vtype id semi)', 'reduce(VDECL→ vtype id semi)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [10.0, 'shift(14)', '', '', '', '', 'reduce(ARG→ ε)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 13.0, '', '', '', '', '', '', '', '', ''], [11.0, '', 'shift(21)', '', '', 'shift(20)', '', '', '', '', '', '', '', '', 'shift(17)', '', '', 'shift(22)', 'shift(23)', '', '', '', '', '', '', '', 15.0, '', '', '', '', '', '', '', 16.0, 18.0, 19.0], [12.0, 'reduce(VDECL→ vtype ASSIGN semi)', 'reduce(VDECL→ vtype ASSIGN semi)', '', '', '', '', '', 'reduce(VDECL→ vtype ASSIGN semi)', '', 'reduce(VDECL→ vtype ASSIGN semi)', 'reduce(VDECL→ vtype ASSIGN semi)', 'reduce(VDECL→ vtype ASSIGN semi)', '', '', '', '', '', '', '', 'reduce(VDECL→ vtype ASSIGN semi)', 'reduce(VDECL→ vtype ASSIGN semi)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [13.0, '', '', '', '', '', 'shift(24)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [14.0, '', 'shift(25)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [15.0, '', '', 'reduce(ASSIGN→ id assign RHS)', '', '', 'reduce(ASSIGN → id assign RHS)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [16.0, '', '', 'reduce(RHS → EXPR)', '', '', 'reduce(RHS → EXPR)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [17.0, '', '', 'reduce(RHS → literal)', '', '', 'reduce(RHS → literal)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [18.0, '', '', 'reduce(EXPR→ TERM)', '', '', 'reduce(EXPR → TERM)', '', '', '', '', '', '', '', '', 'shift(26)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [19.0, '', '', 'reduce(TERM→ FACTOR)', '', '', 'reduce(TERM → FACTOR)', '', '', '', '', '', '', '', '', 'reduce(TERM→ FACTOR)', 'shift(27)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [20.0, '', 'shift(21)', '', '', 'shift(20)', '', '', '', '', '', '', '', '', '', '', '', 'shift(22)', 'shift(23)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 28.0, 18.0, 19.0], [21.0, '', '', 'reduce(FACTOR→ id)', '', '', 'reduce(FACTOR → id)', '', '', '', '', '', '', '', '', 'reduce(FACTOR→ id)', 'reduce(FACTOR→ id)', '', '', 'reduce(FACTOR→ id)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [22.0, '', '', 'reduce(FACTOR→ num)', '', '', 'reduce(FACTOR → num)', '', '', '', '', '', '', '', '', 'reduce(FACTOR→ num)', 'reduce(FACTOR→ num)', '', '', 'reduce(FACTOR→ num)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [23.0, '', '', 'reduce(FACTOR→ float)', '', '', 'reduce(FACTOR → float)', '', '', '', '', '', '', '', '', 'reduce(FACTOR→ float)', 'reduce(FACTOR→ float)', '', '', 'reduce(FACTOR→ float)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [24.0, '', '', '', '', '', '', 'shift(29)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [25.0, '', '', '', '', '', 'reduce(MOREARGS→ ε)', '', '', 'shift(31)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 30.0, '', '', '', '', '', ''], [26.0, '', 'shift(21)', '', '', 'shift(20)', '', '', '', '', '', '', '', '', '', '', '', 'shift(22)', 'shift(23)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 32.0, 18.0, 19.0], [27.0, '', 'shift(21)', '', '', 'shift(20)', '', '', '', '', '', '', '', '', '', '', '', 'shift(22)', 'shift(23)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 33.0, 19.0], [28.0, '', '', '', '', '', 'shift(34)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [29.0, 'shift(42)', 'shift(43)', '', '', '', '', '', 'reduce(BLOCK→ ε)', '', 'shift(39)', 'shift(40)', 'shift(41)', '', '', '', '', '', '', '', 'reduce(BLOCK→ ε)', '', '', 37.0, '', 38.0, '', '', 35.0, '', '', 36.0, '', '', '', '', ''], [30.0, '', '', '', '', '', 'reduce(ARG → vtype id MOREARGS)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [31.0, 'shift(44)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [32.0, '', '', 'reduce(EXPR→ TERM addsub EXPR)', '', '', 'reduce(EXPR → TERM addsub EXPR)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [33.0, '', '', 'reduce(TERM→ FACTOR multdiv TERM)', '', '', 'reduce(TERM → FACTOR multdiv TERM)', '', '', '', '', '', '', '', '', 'reduce(TERM→ FACTOR multdiv TERM)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [34.0, '', '', 'reduce(FACTOR→ lparen EXPR rparen)', '', '', 'reduce(FACTOR → lparen EXPR rparen)', '', '', '', '', '', '', '', '', 'reduce(FACTOR→ lparen EXPR rparen)', 'reduce(FACTOR→ lparen EXPR rparen)', '', '', 'reduce(FACTOR→ lparen EXPR rparen)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [35.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'shift(46)', '', '', '', '', '', '', '', '', 45.0, '', '', '', '', '', '', ''], [36.0, 'shift(42)', 'shift(43)', '', '', '', '', '', 'reduce(BLOCK→ ε)', '', 'shift(39)', 'shift(40)', 'shift(41)', '', '', '', '', '', '', '', 'reduce(BLOCK→ ε)', '', '', 37.0, '', 38.0, '', '', 47.0, '', '', 36.0, '', '', '', '', ''], [37.0, 'reduce(STMT→ VDECL)', 'reduce(STMT→ VDECL)', '', '', '', '', '', 'reduce(STMT → VDECL)', '', 'reduce(STMT→ VDECL)', 'reduce(STMT→ VDECL)', 'reduce(STMT→ VDECL)', '', '', '', '', '', '', '', 'reduce(STMT→ VDECL)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [38.0, '', '', 'shift(48)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [39.0, '', '', '', '', 'shift(49)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [40.0, '', '', '', '', 'shift(50)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [41.0, '', '', '', '', 'shift(51)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [42.0, '', 'shift(52)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 8.0, '', '', '', '', '', '', '', '', '', '', ''], [43.0, '', '', '', 'shift(11)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [44.0, '', 'shift(53)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [45.0, '', '', '', '', '', '', '', 'shift(54)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [46.0, '', 'shift(21)', '', '', 'shift(20)', '', '', '', '', '', '', '', '', '', '', '', 'shift(22)', 'shift(23)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 55.0], [47.0, '', '', '', '', '', '', '', 'reduce(BLOCK→ STMT BLOCK)', '', '', '', '', '', '', '', '', '', '', '', 'reduce(BLOCK→ STMT BLOCK)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [48.0, 'reduce(STMT→ ASSIGN semi)', 'reduce(STMT→ ASSIGN semi)', '', '', '', '', '', 'reduce(STMT → ASSIGN semi)', '', 'reduce(STMT→ ASSIGN semi)', 'reduce(STMT→ ASSIGN semi)', 'reduce(STMT→ ASSIGN semi)', '', '', '', '', '', '', '', 'reduce(STMT→ ASSIGN semi)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [49.0, '', 'shift(21)', '', '', 'shift(20)', '', '', '', '', '', '', '', '', '', '', '', 'shift(22)', 'shift(23)', '', '', '', '', '', '', '', '', '', '', '', '', '', 56.0, '', '', '', 57.0], [50.0, '', 'shift(21)', '', '', 'shift(20)', '', '', '', '', '', '', '', '', '', '', '', 'shift(22)', 'shift(23)', '', '', '', '', '', '', '', '', '', '', '', '', '', 58.0, '', '', '', 57.0], [51.0, '', 'shift(43)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 59.0, '', '', '', '', '', '', '', '', '', '', ''], [52.0, '', '', 'shift(9)', 'shift(11)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [53.0, '', '', '', '', '', 'reduce(MOREARGS→ ε)', '', '', 'shift(31)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 60.0, '', '', '', '', '', ''], [54.0, 'reduce(FDECL→ vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'reduce(FDECL→ vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [55.0, '', '', 'shift(61)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [56.0, '', '', '', '', '', 'shift(62)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [57.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'shift(63)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [58.0, '', '', '', '', '', 'shift(64)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [59.0, '', '', 'shift(65)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [60.0, '', '', '', '', '', 'reduce(MOREARGS → comma vtype id MOREARGS)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [61.0, '', '', '', '', '', '', '', 'reduce(RETURN→ return FACTOR semi)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [62.0, '', '', '', '', '', '', 'shift(66)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [63.0, '', 'shift(21)', '', '', 'shift(20)', '', '', '', '', '', '', '', '', '', '', '', 'shift(22)', 'shift(23)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 67.0], [64.0, '', '', '', '', '', '', 'shift(68)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [65.0, '', 'shift(21)', '', '', 'shift(20)', '', '', '', '', '', '', '', '', '', '', '', 'shift(22)', 'shift(23)', '', '', '', '', '', '', '', '', '', '', '', '', '', 69.0, '', '', '', 57.0], [66.0, 'shift(42)', 'shift(43)', '', '', '', '', '', 'reduce(BLOCK→ ε)', '', 'shift(39)', 'shift(40)', 'shift(41)', '', '', '', '', '', '', '', 'reduce(BLOCK→ ε)', '', '', 37.0, '', 38.0, '', '', 70.0, '', '', 36.0, '', '', '', '', ''], [67.0, '', '', 'reduce(COND→ FACTOR comp FACTOR)', '', '', 'reduce(COND → FACTOR comp FACTOR)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [68.0, 'shift(42)', 'shift(43)', '', '', '', '', '', 'reduce(BLOCK→ ε)', '', 'shift(39)', 'shift(40)', 'shift(41)', '', '', '', '', '', '', '', 'reduce(BLOCK→ ε)', '', '', 37.0, '', 38.0, '', '', 71.0, '', '', 36.0, '', '', '', '', ''], [69.0, '', '', 'shift(72)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [70.0, '', '', '', '', '', '', '', 'shift(73)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [71.0, '', '', '', '', '', '', '', 'shift(74)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [72.0, '', 'shift(43)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 75.0, '', '', '', '', '', '', '', '', '', '', ''], [73.0, 'reduce(ELSE→ ε)', 'reduce(ELSE→ ε)', '', '', '', '', '', 'reduce(ELSE → ε)', '', 'reduce(ELSE→ ε)', 'reduce(ELSE→ ε)', 'reduce(ELSE→ ε)', 'shift(77)', '', '', '', '', '', '', 'reduce(ELSE→ ε)', '', '', '', '', '', '', '', '', '', '', '', '', 76.0, '', '', ''], [74.0, 'reduce(STMT→ while lparen COND rparen lbrace BLOCK rbrace)', 'reduce(STMT→ while lparen COND rparen lbrace BLOCK rbrace)', '', '', '', '', '', 'reduce(STMT → while lparen COND rparen lbrace BLOCK rbrace)', '', 'reduce(STMT→ while lparen COND rparen lbrace BLOCK rbrace)', 'reduce(STMT→ while lparen COND rparen lbrace BLOCK rbrace)', 'reduce(STMT→ while lparen COND rparen lbrace BLOCK rbrace)', '', '', '', '', '', '', '', 'reduce(STMT→ while lparen COND rparen lbrace BLOCK rbrace)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [75.0, '', '', '', '', '', 'shift(78)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [76.0, 'reduce(STMT→ if lparen COND rparen lbrace BLOCK rbrace ELSE)', 'reduce(STMT→ if lparen COND rparen lbrace BLOCK rbrace ELSE)', '', '', '', '', '', 'reduce(STMT → if lparen COND rparenl brace BLOCK rbrace ELSE)', '', 'reduce(STMT→ if lparen COND rparen lbrace BLOCK rbrace ELSE)', 'reduce(STMT→ if lparen COND rparen lbrace BLOCK rbrace ELSE)', 'reduce(STMT→ if lparen COND rparen lbrace BLOCK rbrace ELSE)', '', '', '', '', '', '', '', 'reduce(STMT→ if lparen COND rparen lbrace BLOCK rbrace ELSE)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [77.0, '', '', '', '', '', '', 'shift(79)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [78.0, '', '', '', '', '', '', 'shift(80)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [79.0, 'shift(42)', 'shift(43)', '', '', '', '', '', 'reduce(BLOCK→ ε)', '', 'shift(39)', 'shift(40)', 'shift(41)', '', '', '', '', '', '', '', 'reduce(BLOCK→ ε)', '', '', 37.0, '', 38.0, '', '', 81.0, '', '', 36.0, '', '', '', '', ''], [80.0, 'shift(42)', 'shift(43)', '', '', '', '', '', 'reduce(BLOCK→ ε)', '', 'shift(39)', 'shift(40)', 'shift(41)', '', '', '', '', '', '', '', 'reduce(BLOCK→ ε)', '', '', 37.0, '', 38.0, '', '', 82.0, '', '', 36.0, '', '', '', '', ''], [81.0, '', '', '', '', '', '', '', 'shift(83)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [82.0, '', '', '', '', '', '', '', 'shift(84)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [83.0, 'reduce(ELSE→ else lbrace BLOCK rbrace)', 'reduce(ELSE→ else lbrace BLOCK rbrace)', '', '', '', '', '', 'reduce(ELSE → else lbrace BLOCK rbrace)', '', 'reduce(ELSE→ else lbrace BLOCK rbrace)', 'reduce(ELSE→ else lbrace BLOCK rbrace)', 'reduce(ELSE→ else lbrace BLOCK rbrace)', '', '', '', '', '', '', '', 'reduce(ELSE→ else lbrace BLOCK rbrace)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [84.0, 'reduce(STMT→ for lparen ASSIGN semi COND semi ASSIGN rparen lbrace BLOCK rbrace)', 'reduce(STMT→ for lparen ASSIGN semi COND semi ASSIGN rparen lbrace BLOCK rbrace)', '', '', '', '', '', 'reduce(STMT → for lparen ASSIGN semi COND semi ASSIGN rparen lbrace BLOCK rbrace)', '', 'reduce(STMT→ for lparen ASSIGN semi COND semi ASSIGN rparen lbrace BLOCK rbrace)', 'reduce(STMT→ for lparen ASSIGN semi COND semi ASSIGN rparen lbrace BLOCK rbrace)', 'reduce(STMT→ for lparen ASSIGN semi COND semi ASSIGN rparen lbrace BLOCK rbrace)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]

# this is to run '$python3 syntax_analyzer.py input1.out'
script, filename = argv
txt = open(filename, 'r')
outFile = txt.read().replace("[", "").split(']')  # .out 파일에서, [단위로 쪼개서 배열에 넣어준다.
output = ""
outFile.pop()  # split때문에 배열의 마지막 값으로 ""값이 들어간걸 삭제해준다.
# print(outFile)

# 엑셀의 column을 매칭하기 위해서 딕셔너리 형태로 input을 정의했다.
inputs = {"vtype": 1, "id": 2, "semi": 3, "assign": 4, "lparen": 5, "rparen": 6, "lbrace": 7, "rbrace": 8, "comma": 9,
            "if":10, "while": 11, "for": 12, "else": 13, "literal": 14,
          "addsub": 15, "multdiv": 16, "num": 17, "float": 18, "comp": 19, "return": 20, "$": 21, "CODE": 22,
          "VDECL": 23, "FDECL": 24, "ASSIGN": 25, "RHS": 26, "ARG": 27, "BLOCK": 28, "RETURN": 29, "MOREARGS": 30,
          "STMT": 31, "COND": 32, "ELSE": 33, "EXPR": 34, "TERM": 35, "FACTOR": 36}

# symbol table의 단어들을 syntax analyzer에 맞게 바꿔준다.
for i in range(len(outFile)):
    print(outFile[i])
    if outFile[i].startswith("VARIABLE, "):
        outFile[i] = "vtype"
    elif outFile[i].startswith("INT, "):
        outFile[i] = "num"
    elif outFile[i].startswith("STRING, "):
        outFile[i] = "literal"
    elif outFile[i].startswith("FLOAT, "):
        outFile[i] = "float"
    elif outFile[i].startswith("ID, return"):
        outFile[i] = "return"
    elif outFile[i].startswith("ID, "):
        outFile[i] = "id"
    elif outFile[i].startswith("KEYWORD, if"):
        outFile[i] = "if"
    elif outFile[i].startswith("KEYWORD, else"):
        outFile[i] = "else"
    elif outFile[i].startswith("KEYWORD, while"):
        outFile[i] = "while"
    elif outFile[i].startswith("KEYWORD, for"):
        outFile[i] = "for"
    elif outFile[i].startswith("KEYWORD, return"):
        outFile[i] = "return"
    elif outFile[i].startswith("ARITHMETIC, +"):
        outFile[i] = "addsub"
    elif outFile[i].startswith("ARITHMETIC, -"):
        outFile[i] = "addsub"
    elif outFile[i].startswith("ARITHMETIC, *"):
        outFile[i] = "multdiv"
    elif outFile[i].startswith("ARITHMETIC, /"):
        outFile[i] = "multdiv"
    elif outFile[i].startswith("ASSIGNMENT, ="):
        outFile[i] = "assign"
    elif outFile[i].startswith("COMPARISON, "):
        outFile[i] = "comp"
    elif outFile[i].startswith("SEMICOLON, ;"):
        outFile[i] = "semi"
    elif outFile[i].startswith("BRAC, {"):
        outFile[i] = "lbrace"
    elif outFile[i].startswith("BRAC, }"):
        outFile[i] = "rbrace"
    elif outFile[i].startswith("PARAN, ("):
        outFile[i] = "lparen"
    elif outFile[i].startswith("PARAN, )"):
        outFile[i] = "rparen"
    elif outFile[i].startswith("COMMA, ,"):
        outFile[i] = "comma"
    # BITWISE 지워주기
    elif outFile[i].startswith("BITWISE, "):
        outFile[i] = ""
    # WHITESPACE 지워주기
    elif outFile[i].startswith("WHITESPACE,"):
        outFile[i] = ""
    # BOOLEAN 지워주기
    elif outFile[i].startswith("BOOLEAN, "):
        outFile[i] = ""
    else:
        print("난 바보야")

# print(outFile)
outFile = [x for x in outFile if x != '']  # 빈 칸 삭제
outFile.append("$") # lexical analyzer에서 온 data 끝에 $를 붙여준다.
print(outFile)

i = 0 # loop variable
myStack = [0] # 스택 이니셜라이징 시 0을 넣어준다.
myString = [] # spliter의 왼쪽에 있는 string을 담고 있는 배열.
# i가 symbol table의 갯수보다 작을 떄 while 안쪽을 반복한다.
while i < len(outFile):
    row = int(myStack[-1])+1 # row는 stack의 top에 있는 값에다 1을 더해준 것인데, 엑셀 파일에 보면 젤 윗줄의 colum정보 때문에 row가 하나씩 밀렸기 때문이다.
    col = inputs[outFile[i]] # col은 symbol을 inputs에 넣어서 나온 값이다.
    print("======새로운 글자======")
    print("outFile[i]는:", outFile[i])
    print("i는:", i)
    print("col은:", col)
    if productionTable[row][col].startswith("shift("): # shift일 때.
        # shift action
        print("=====[shift]====")
        print("stack은:", myStack)
        print("row값은:", row)
        print("col값은:", col)
        print(productionTable[row][col])
        print("stack에는...", int(productionTable[row][col].replace("shift(", "").replace(")", "")))
        myStack.append(int(productionTable[row][col].replace("shift(", "").replace(")", ""))) # stack에 shift()안에 있는 값을 넣어준다.
        myString.append(outFile[i]) # myString에 append해준다. 즉 indicator을 한 칸 옮긴다.
        print("myString은", myString)
        i += 1

    elif productionTable[row][col].startswith("reduce("): # reduce일 때
        # reduce action
        print("=====[reduce]====")
        print("stack은:", myStack)
        print("body는:", productionTable[row][col])
        reduceStr = productionTable[row][col].replace("reduce(", "").replace(")", "")
        print(reduceStr)
        arrow = reduceStr.split('→') # reduce에 화살표로 표시된 데이터의 leftSide와 rightSide를 나눈다.
        # 화살표 왼쪽
        leftSide = arrow[0].split(' ')
        leftSide = [x for x in leftSide if x != ''] # 공백 삭제
        # 화살표 오른쪽
        rightSide = arrow[1].split(' ')
        rightSide = [x for x in rightSide if x != ''] # 공백 삭제

        print("leftside:", leftSide)
        print("rightside:", rightSide)

        for j in range(len(rightSide)): # rightSide에 있는 원소 갯수만큼 for문을 반복한다.
            # rightSide가 엡실론이 아니라면 stack과 myString에서 pop해준다.
            if rightSide[j] != 'ε':
                print("팝함")
                myStack.pop(-1)
                myString.pop(-1)
        for k in range(len(leftSide)):
            # myString에 append 해준다.
            myString.append(leftSide[k])
        print("마이스트링 타입은:", myString[-1])
        print("전체 mystring은", myString)
        print("마이스트링 숫자는:", inputs[myString[-1]])
        print("!!!!!!!!!!i값은", i)

        row = int(myStack[-1]) + 1 # stack top값에서, 엑셀 파일에 보면 젤 윗줄의 colum정보 때문에 row가 하나씩 밀렸기 때문에 +1 해준다.
        col = inputs[myString[-1]] # myString의 top값을 가져온다.

        print("row는..",row)
        print("col는..", col)
        print(productionTable[row][col])
        # MOVE only
        myStack.append(int(productionTable[row][col])) # GOTO 값을 stack에 push한다.
    elif not productionTable[row][col]:
        # value is empty
        print("=====[error]====")
        print("row는:", row)
        print("col는:", col)
        print("에러는 던진다.던져~던져!")
        print(i,"번째에 있는", outFile[i], "에 대해서 에러가 발생한다.")

        break
    elif productionTable[row][col].startswith("accept"):
        print("success!!!!!!!!!!!!!!!")
        break
    else:
        break