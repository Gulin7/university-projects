%{
#include <stdio.h>
#include "parser.tab.h"
int lines = 1; // Track line numbers
%}

%option noyywrap

DIGIT [0-9]
LETTER [a-zA-Z_]
IDENTIFIER {LETTER}({LETTER}|{DIGIT})*
NUMBER {DIGIT}+(\.{DIGIT}*)?
STRING \"([^"\\]|\\.)*\"
WHITESPACE [ \t]+

%%

"int"               { return INT; }
"float"             { return FLOAT; }
"double"            { return DOUBLE; }
"char"              { return CHAR; }
"if"                { return IF; }
"else"              { return ELSE; }
"for"               { return FOR; }
"while"             { return WHILE; }
"return"            { return RETURN; }
"cout"              { return COUT; }
"cin"               { return CIN; }

{IDENTIFIER}        { yylval.str = strdup(yytext); return IDENTIFIER; }
{NUMBER}            { yylval.num = atof(yytext); return NUMBER; }
{STRING}            { yylval.str = strdup(yytext); return STRING; }

"<<"                { return OUTPUT; }
">>"                { return INPUT; }
"="                 { return ASSIGN; }
"+"                 { return PLUS; }
"-"                 { return MINUS; }
"*"                 { return MULT; }
"/"                 { return DIV; }
"("                 { return LPAREN; }
")"                 { return RPAREN; }
"{"                 { return LBRACE; }
"}"                 { return RBRACE; }
";"                 { return SEMICOLON; }

\n                  { ++lines; }
{WHITESPACE}        { /* Ignore whitespace */ }
.                   { printf("Unknown character '%s' at line %d\n", yytext, lines); }

%%
