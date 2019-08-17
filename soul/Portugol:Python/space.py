from re import search
def strToList(string, *char):
    if char!=():
        return String(string).toList(divisor=char)
    else:
        return String(string).toList()

indice = 0

VAR = {}
vetores = []
for indice in range(len(ARQ)):
    if len(ARQ[indice].strip())>0:
        # resolucao do erro no escolha
        if 'escolha' in ARQ[indice]:
            if '# }' in ARQ[indice+1]:
                ARQ[indice+1] = ''

        # resolver erro entre tipos primitivos
        if 'var' in ARQ[indice]:
            for ln in range(indice+1, len(ARQ)):
                if ('inicio' in ARQ[ln]) or ('ini' in ARQ[ln]):
                    break

                if ':' in ARQ[ln]:
                    linha = ARQ[ln].split(':')
                    tipo = linha[1].strip().split()[0]
                    if 'vetor' in tipo:
                       
                        # se matriz
                        tipo = linha[1].strip()
                        rng = search(r'\[.{0,}\]', tipo.strip()).group()
                        tipo = strToList( tipo.strip())[len(strToList( tipo.strip()))-1]
                        
                        if ',' in rng:
                            rnga = rng.split(',')[0].strip()
                            rngb = rng.split(',')[1].strip()

                            ini = search(r'.{0,}\.', rnga).group().strip()
                            fim = search(r'\..{0,}', rnga).group().strip()
                            ini = int(''.join(''.join(ini.split('[')).split('..')).strip())
                            fim = int(''.join(''.join(fim.split(']')).split('..')).strip())+1

                            inib = search(r'.{0,}\.', rngb).group().strip()
                            fimb = search(r'\..{0,}', rngb).group().strip()
                            inib = int(''.join(''.join(inib.split('[')).split('..')).strip())
                            fimb = int(''.join(''.join(fimb.split(']')).split('..')).strip())+1

                            formatVet = {}
                            for i in range(ini, fim):
                                for j in range(inib, fimb):
                                    formatVet['<s>'+str(i)+','+str(j)+'<s>'] = tipo+'()'
                            valor = ''.join( Vetor(String('<d>'.join(str(formatVet).split(':')))).delete("'",'"') ).strip()
                            ARQ[ln] = linha[0].strip() +' <i> <c>'+ ''.join(Vetor('"'.join(valor.split('<s>'))).delete('}','{'))+'<fc>'
                            
                        else:
                            ini = search(r'\[.{0,}\.', rng).group().strip()
                            fim = search(r'\..{0,}\]', rng).group().strip()
                            ini = int(''.join(''.join(ini.split('[')).split('..')).strip())
                            fim = int(''.join(''.join(fim.split(']')).split('..')).strip())+1
                            formatVet = {}
                            for i in range(ini, fim):
                                formatVet['<s>'+str(i)+'<s>'] = tipo+'()'
                            valor = ''.join( Vetor(String('<d>'.join(str(formatVet).split(':')))).delete("'",'"') ).strip()
                            ARQ[ln] = linha[0].strip() +' <i> <c>'+ ''.join(Vetor('"'.join(valor.split('<s>'))).delete('}','{'))+'<fc>'
                        tipo = 'vetor:'+tipo.strip()

                    for var in linha[0].split(','):
                        if ':' in tipo:
                            vetores.append(var.strip())
                            tipo = tipo.split(':')[1].strip()
                        VAR[var.strip()] = tipo
                
        try:           
            if ('<-' in ARQ[indice]) and not('para' in ARQ[indice].split('<-')[0].strip()) and '[' not in ARQ[indice] and not 'dict' in ARQ[indice]:
                ARQ[indice] = ARQ[indice].split('<-')[0].strip()+' <- '+VAR[ARQ[indice].split('<-')[0].strip()]+'('+ARQ[indice].split('<-')[1].strip()+')'
        except:
            pass
        col = 0
        variavel = ''
        Linha = strToList(ARQ[indice].strip())
        while col<len(Linha):

            if (Linha[col] in VAR) or (Linha[col] in vetores):
                variavel = Linha[col]
                #gerenciamento de vetores    
                iniColc = 0
                fimColc = 0
                colchete = False
                if variavel in vetores:
                    #procurando os intervalos da linha
                    while '[' in Linha:
                        for i in range(len(Linha)):
                            if Linha[i]=='[':
                                iniColc = i+1
                                colchete = True
                            elif (Linha[i]==']') and (colchete):
                                fimColc = i
                                break

                        if ',' in ''.join(Linha[iniColc:fimColc]):
                            Linha = Linha[:iniColc-1]+ [''.join('[str('+(''.join(Linha[iniColc:fimColc]).split(','))[0]+')+","+ str('+(''.join(Linha[iniColc:fimColc]).split(','))[1] +')]')] +Linha[fimColc+1:]
                        else:
                            Linha = Linha[:iniColc-1]+ [''.join('[str('+''.join(Linha[iniColc:fimColc])+')]')] +Linha[fimColc+1:]
    
            col += 1
        ARQ[indice] = ''.join(Linha)
# exportando dados
open(DIR+'.tmp', 'w').write('\n'.join(ARQ))
