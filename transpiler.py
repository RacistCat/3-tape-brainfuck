# 3-tape-brainfuck to brainfuck compiler
# have 24 instructions

INIT = ">>>>>->>+>>+>>+<<<<<<"
translation =
{
"+1": "<<<[-<+<+>>]<<[->>+<<]>>[->>>>>-[+>>>>>>>-]>>>>>>>+<<+[-<<<<<<<+]-<<<]<[->+<]>>>>>>-[+>>>>>>>-]<+<+[-<<<<<<<+]->>+<<",
"-1": "<<<[-<+<+>>]<<[->>+<<]>>[->>>>>-[+>>>>>>>-]>>>>>>>+<<+[-<<<<<<<+]-<<<]<[->+<]>>>>>>-[+>>>>>>>-]<-<+[-<<<<<<<+]->>+<<",
",1": "<<<[-<+<+>>]<<[->>+<<]>>[->>>>>-[+>>>>>>>-]>>>>>>>+<<+[-<<<<<<<+]-<<<]<[->+<]>>>>>>-[+>>>>>>>-]<,<+[-<<<<<<<+]->>+<<",
".1": "<<<[-<+<+>>]<<[->>+<<]>>[->>>>>-[+>>>>>>>-]>>>>>>>+<<+[-<<<<<<<+]-<<<]<[->+<]>>>>>>-[+>>>>>>>-]<.<+[-<<<<<<<+]->>+<<",
"[1": "<<<[-<+<+>>]<<[->>+<<]>>[->>>>>-[+>>>>>>>-]>>>>>>>+<<+[-<<<<<<<+]-<<<]<[->+<]>>>>>>-[+>>>>>>>-]<[<+[-<<<<<<<+]->>+<<",
"]1": "<<<[-<+<+>>]<<[->>+<<]>>[->>>>>-[+>>>>>>>-]>>>>>>>+<<+[-<<<<<<<+]-<<<]<[->+<]>>>>>>-[+>>>>>>>-]<]<+[-<<<<<<<+]->>+<<",
"<1": "<<<->>>",
">1": "<<<+>>>",
# tape 1 instructions
"+2":"<<[-<<+<+>>>]<<<[->>>+<<<]>>>[->>>>>>-[+>>>>>>>-]>>>>>>>+>>>+[-<<<<<<<+]-<<]<<[->>+<<]>>>>>>>>-[+>>>>>>>-]<+<<<+[-<<<<<<<+]->>>>+<<<<",
"-2":"<<[-<<+<+>>>]<<<[->>>+<<<]>>>[->>>>>>-[+>>>>>>>-]>>>>>>>+>>>+[-<<<<<<<+]-<<]<<[->>+<<]>>>>>>>>-[+>>>>>>>-]<-<<<+[-<<<<<<<+]->>>>+<<<<",
",2":"<<[-<<+<+>>>]<<<[->>>+<<<]>>>[->>>>>>-[+>>>>>>>-]>>>>>>>+>>>+[-<<<<<<<+]-<<]<<[->>+<<]>>>>>>>>-[+>>>>>>>-]<,<<<+[-<<<<<<<+]->>>>+<<<<",
".2":"<<[-<<+<+>>>]<<<[->>>+<<<]>>>[->>>>>>-[+>>>>>>>-]>>>>>>>+>>>+[-<<<<<<<+]-<<]<<[->>+<<]>>>>>>>>-[+>>>>>>>-]<.<<<+[-<<<<<<<+]->>>>+<<<<",
"[2":"<<[-<<+<+>>>]<<<[->>>+<<<]>>>[->>>>>>-[+>>>>>>>-]>>>>>>>+>>>+[-<<<<<<<+]-<<]<<[->>+<<]>>>>>>>>-[+>>>>>>>-]<[<<<+[-<<<<<<<+]->>>>+<<<<",
"]2":"<<[-<<+<+>>>]<<<[->>>+<<<]>>>[->>>>>>-[+>>>>>>>-]>>>>>>>+>>>+[-<<<<<<<+]-<<]<<[->>+<<]>>>>>>>>-[+>>>>>>>-]<]<<<+[-<<<<<<<+]->>>>+<<<<",
"<2": "<<->>",
">2": "<<+>>",
# tape 2 instructions
"+3": "<[-<<<+<+>>>>]<<<<[->>>>+<<<<]>>>>[->>>>>>>-[+>>>>>>>-]>>>>>>>+>+[-<<<<<<<+]-<]<<<[->>>+<<<]>>>>>>>>>>-[+>>>>>>>-]<+>>+[-<<<<<<<+]->>>>>>+<<<<<<",
"-3": "<[-<<<+<+>>>>]<<<<[->>>>+<<<<]>>>>[->>>>>>>-[+>>>>>>>-]>>>>>>>+>+[-<<<<<<<+]-<]<<<[->>>+<<<]>>>>>>>>>>-[+>>>>>>>-]<->>+[-<<<<<<<+]->>>>>>+<<<<<<",
",3": "<[-<<<+<+>>>>]<<<<[->>>>+<<<<]>>>>[->>>>>>>-[+>>>>>>>-]>>>>>>>+>+[-<<<<<<<+]-<]<<<[->>>+<<<]>>>>>>>>>>-[+>>>>>>>-]<,>>+[-<<<<<<<+]->>>>>>+<<<<<<",
".3": "<[-<<<+<+>>>>]<<<<[->>>>+<<<<]>>>>[->>>>>>>-[+>>>>>>>-]>>>>>>>+>+[-<<<<<<<+]-<]<<<[->>>+<<<]>>>>>>>>>>-[+>>>>>>>-]<.>>+[-<<<<<<<+]->>>>>>+<<<<<<",
"[3": "<[-<<<+<+>>>>]<<<<[->>>>+<<<<]>>>>[->>>>>>>-[+>>>>>>>-]>>>>>>>+>+[-<<<<<<<+]-<]<<<[->>>+<<<]>>>>>>>>>>-[+>>>>>>>-]<[>>+[-<<<<<<<+]->>>>>>+<<<<<<",
"]3": "<[-<<<+<+>>>>]<<<<[->>>>+<<<<]>>>>[->>>>>>>-[+>>>>>>>-]>>>>>>>+>+[-<<<<<<<+]-<]<<<[->>>+<<<]>>>>>>>>>>-[+>>>>>>>-]<]>>+[-<<<<<<<+]->>>>>>+<<<<<<",
"<3": "<->",
">3": "<+>"
# tape 3 instructions
}

def transpile(program):
	output = INIT + program
	for instr in translation.keys():
		output= output.replace(instr, translation[instr])
	return output
		
