#if condicao/comparacao
    # tudo que acontece se a condição for verdadeira
    # > maior que
    # < menor que
    # = igual 
    # >= maior ou igual
    # <= menor ou igual
    # == igual (comparação
    # != diferente

vendas = 1500
meta = 1300

if vendas > meta:
    print ("vendedor ganha bonus")
    print ("bateu a meta de vendas")
    bonus = 0.1*vendas
    print ("bonus do vendedor: ", bonus)
    
else:
    print ("Vendedor não ganha bonus")
    print ("Não bateu a meta de vendas")