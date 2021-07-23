def proteins(strand):

    # Dictionary for protein codons
    protein_codons = {'Methionine': ['AUG'], 'Phenylalanine': ['UUU', 'UUC'], 'Leucine': ['UUA', 'UUG'], 
    'Serine': ['UCU','UCC','UCA','UCG'], 'Tyrosine': ['UAU', 'UAC'], 'Cysteine': ['UGU', 'UGC'], 'Tryptophan': ['UGG'], 'STOP':
    ['UAA', 'UAG', 'UGA']}

    # Initialize protein list
    protein_list = []

    # For loop to go through every third character index in strand string 
    for i in range(0, len(strand), 3):

        # Using key/value pair from dictionary
        for k, v in protein_codons.items():

            # If the three character string from current index position is in a value
            if strand[i:i+3] in v:

                # If key is 'STOP' return list
                if k == 'STOP':
                    return protein_list

                # Append codon to list otherwise
                else:
                    protein_list.append(k) 

    return protein_list

