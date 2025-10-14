import ply.lex as lex

texto = """
# DBPedia: obras de Chuck Berry
        select ?nome ?desc where {
         ?s a dbo:MusicalArtist.
         ?s foaf:name "Chuck Berry"@en .
         ?w dbo:artist ?s.
         ?w foaf:name ?nome.
         ?w dbo:abstract ?desc
        } LIMIT 1000
"""



tokens = (
   'COMMENT',
   'FUNCTION',
   'TAG', #?x
   'ATRIB', # xx:xx
   'LIMIT', 
   'CA', # {
   'CF', # }
   'DOT', # .
   'NAME', #"nome"
   'LANG', #@en
)

# Regular expression rules for simple tokens
t_DOT = r'\.'

t_CA = r'\{'

t_CF = r'\}'

def t_COMMENT(t):
    r'\#.*'
    return t

def t_NAME(t):
    r'\"[^"]+\"'
    return t

def t_LANG(t):
    r'@\w\w'
    return t

def t_TAG(t):
    r'\?\w+'
    return t

def t_ATRIB(t):
    r'\w+:\w+'
    return t

def t_LIMIT(t):
    r'LIMIT\s\d+'
    return t

def t_FUNCTION(t):
    r'\w+'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

lexer.input(texto)
for tok in lexer:
    print(tok)


