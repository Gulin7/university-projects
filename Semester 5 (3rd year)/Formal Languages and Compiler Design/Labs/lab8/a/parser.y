%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void yyerror(const char* s);

extern int yylex();
extern int lines;

typedef union {
    double num;
    char* str;
} YYSTYPE;

#define YYSTYPE YYSTYPE
%}

%union {
    double num;
    char* str;
}

%token <str> IDENTIFIER
%token <num> NUMBER
%token <str> STRING

%token INT FLOAT DOUBLE CHAR
%token IF ELSE FOR WHILE RETURN COUT CIN
%token OUTPUT INPUT
%token ASSIGN PLUS MINUS MULT DIV
%token LPAREN RPAREN LBRACE RBRACE SEMICOLON

%start Program

%%

Program:
    Declarations Statements
    ;

Declarations:
    | Declarations Declaration
    ;

Declaration:
    Type IDENTIFIER SEMICOLON
    ;

Type:
    INT
    | FLOAT
    | DOUBLE
    | CHAR
    ;

Statements:
    | Statements Statement
    ;

Statement:
    Assignment
    | PrintStatement
    | InputStatement
    | IfStatement
    | WhileStatement
    ;

Assignment:
    IDENTIFIER ASSIGN Expression SEMICOLON
    ;

Expression:
    Expression PLUS Term
    | Expression MINUS Term
    | Term
    ;

Term:
    Term MULT Factor
    | Term DIV Factor
    | Factor
    ;

Factor:
    LPAREN Expression RPAREN
    | NUMBER
    | IDENTIFIER
    ;

PrintStatement:
    COUT OUTPUT Expression SEMICOLON
    | COUT OUTPUT STRING SEMICOLON
    ;

InputStatement:
    CIN INPUT IDENTIFIER SEMICOLON
    ;

IfStatement:
    IF LPAREN Expression RPAREN LBRACE Statements RBRACE
    | IF LPAREN Expression RPAREN LBRACE Statements RBRACE ELSE LBRACE Statements RBRACE
    ;

WhileStatement:
    WHILE LPAREN Expression RPAREN LBRACE Statements RBRACE
    ;

%%

void yyerror(const char* s) {
    fprintf(stderr, "Error at line %d: %s\n", lines, s);
}

int main(int argc, char** argv) {
    if (argc > 1) {
        FILE* file = fopen(argv[1], "r");
        if (!file) {
            perror("Failed to open file");
            return 1;
        }
        yyin = file;
    }

    if (!yyparse()) {
        printf("Parsing completed successfully.\n");
    } else {
        printf("Parsing failed.\n");
    }

    return 0;
}
