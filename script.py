import numpy as np

#entrada, geralmente vem de um arquivo texto
palavra = 'void main {inicio ; "fim" }'

#variavel para armazenar o lexema
lexema = ''

#variavel para armazenar a lista de tokes (que ira alimentar o sintatico)
tokens = []
lexemas = []
readString = False

for i in range(len(palavra)): #percorre a entrada
    if palavra[i] == '{':
        if lexema: # Append previous lexema if it exists
            if lexema == 'while': tokens.append(1); lexemas.append(lexema)
            elif lexema == 'var': tokens.append(2); lexemas.append(lexema)
            elif lexema == 'to': tokens.append(3); lexemas.append(lexema)
            elif lexema == 'then': tokens.append(4); lexemas.append(lexema)
            elif lexema == 'string': tokens.append(5); lexemas.append(lexema)
            elif lexema == 'real': tokens.append(6); lexemas.append(lexema)
            elif lexema == 'read': tokens.append(7); lexemas.append(lexema)
            elif lexema == 'program': tokens.append(8); lexemas.append(lexema)
            elif lexema == 'inicio': tokens.append(15); lexemas.append(lexema)
            elif lexema == 'fim': tokens.append(20); lexemas.append(lexema)
            elif lexema == ';': tokens.append(40); lexemas.append(lexema)
            elif lexema == '}': tokens.append(38); lexemas.append(lexema)
            elif lexema == '{': tokens.append(39); lexemas.append(lexema)
            else:
                # Handle other potential lexemes or errors
                pass
        lexema = palavra[i]
        tokens.append(39)
        lexemas.append(lexema)
        lexema = '' # Reset lexema after processing '{'
    elif palavra[i] != ' ':
        if palavra[i] == '"':
            if readString: # Closing quote
                lexema = lexema + palavra[i]
                readString = False
                tokens.append(5) # Assuming strings are token type 5
                lexemas.append(lexema)
                lexema = ''
            else: # Opening quote
                lexema = palavra[i]
                readString = True
        elif readString:
            lexema = lexema + palavra[i]
        else:
            lexema = lexema + palavra[i]
    else:
        if lexema: # Process the completed lexema
            if lexema == 'while': tokens.append(1); lexemas.append(lexema)
            elif lexema == 'var': tokens.append(2); lexemas.append(lexema)
            elif lexema == 'to': tokens.append(3); lexemas.append(lexema)
            elif lexema == 'then': tokens.append(4); lexemas.append(lexema)
            elif lexema == 'string': tokens.append(5); lexemas.append(lexema)
            elif lexema == 'real': tokens.append(6); lexemas.append(lexema)
            elif lexema == 'read': tokens.append(7); lexemas.append(lexema)
            elif lexema == 'program': tokens.append(8); lexemas.append(lexema)
            elif lexema == 'inicio': tokens.append(15); lexemas.append(lexema)
            elif lexema == 'fim': tokens.append(20); lexemas.append(lexema)
            elif lexema == ';': tokens.append(40); lexemas.append(lexema)
            elif lexema == '}': tokens.append(38); lexemas.append(lexema)
            elif lexema == '{': tokens.append(39); lexemas.append(lexema)
            else:
                # Handle other potential lexemes or errors
                pass
        lexema = ''

    print(lexema) #print opcional para ver o andamento

# Process any remaining lexema after the loop
if lexema:
    if lexema == 'while': tokens.append(1); lexemas.append(lexema)
    elif lexema == 'var': tokens.append(2); lexemas.append(lexema)
    elif lexema == 'to': tokens.append(3); lexemas.append(lexema)
    elif lexema == 'then': tokens.append(4); lexemas.append(lexema)
    elif lexema == 'string': tokens.append(5); lexemas.append(lexema)
    elif lexema == 'real': tokens.append(6); lexemas.append(lexema)
    elif lexema == 'read': tokens.append(7); lexemas.append(lexema)
    elif lexema == 'program': tokens.append(8); lexemas.append(lexema)
    elif lexema == 'inicio': tokens.append(15); lexemas.append(lexema)
    elif lexema == 'fim': tokens.append(20); lexemas.append(lexema)
    elif lexema == ';': tokens.append(40); lexemas.append(lexema)
    elif lexema == '}': tokens.append(38); lexemas.append(lexema)
    elif lexema == '{': tokens.append(39); lexemas.append(lexema)
    else:
        # Handle other potential lexemes or errors
        pass

#Entrega do lexico - token - lexema - linha
for i in range(0,len(tokens)):
    print('Token: '+str(tokens[i]) + ' - Lexema: '+str(lexemas[i]) + ' - Linha: 1' )

#print(tokens) # [2, 11, 39, 15, 40, 20, 38]

#salvar do lexico para entregar para o sintático
tokens = np.array(tokens) #converte lista do python para numpy arrays