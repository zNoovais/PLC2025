
a108395 :: José Pedro Flores Novais

# TP3



Construir um analisador lexico para uma linguagem de query com a qual se podem escrever frases do genero

"# DBPedia: obras de Chuck Berry\n" \
        "select ?nome ?desc where {\n" \
        " ?s a dbo:MusicalArtist.\n" \
        " ?s foaf:name \"Chuck Berry\"@en .\n" \
        " ?w dbo:artist ?s.\n" \
        " ?w foaf:name ?nome.\n" \
        " ?w dbo:abstract ?desc\n" \
        "} LIMIT 1000"

