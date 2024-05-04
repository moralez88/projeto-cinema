print("CINEMA ")
#PROJETO LINGUAGEM DE PROGRAMAÇÃO
# 2ºGTI ..  FATEC- JUNDIAI
# WILLIAM PEREIRA MORALEZ

#login e senha para entrar no sitema
#os relatorios apareceram vazios no sistema do gerente ate serem preenchidos pelo funcionario 

login_funcionario="colaborador"
senha_funcionario= "senha123"
login_gerente= "gerente"
senha_gerente= "gerente123"

#variaveis globaist

sitema_escolhido= " "
filme_selecionado=" "
vendas_dia=[]
bilheteria=[]
ocorrencias=[]
while True:
  login_inserido=input("Digite seu Login: ")
  senha_insirida=input("digite a senha: ")
  if login_inserido==login_funcionario and senha_insirida==senha_funcionario:
    sitema_escolhido="funcionario"
    print("Sistema do colaborador ")
    
  elif login_inserido==login_gerente and senha_insirida==senha_gerente:
   sitema_escolhido="gerente"
   print('Sistema do gerente')
   
  else:
   print ("Login ou senha incorretos")

####################################### SITEMA DE CONTROLE DO GERENTE ###############################################

  if sitema_escolhido == 'gerente':
    encerra=True
    while encerra==True:
     opcoes_gerencias= "[l]ista de funcionarios "  , " [e]scolha de filmes "   ,   " [g]anhos"  , "[r]elatorios"  ,  "[s]air",
     print(opcoes_gerencias)
     opcao_selecionada=input("digite o sistema que deseja consultar: ")
    #lista editavel de funcionarios do cinema
     if opcao_selecionada=="l":  
      with open("nome.txt", "r+") as arquivo:
       nome=arquivo.read()
       print(nome)

      while True:
            opcao_edicao = input("Deseja editar a lista? (s/n): ")
            if opcao_edicao=="n":
               break

            if opcao_edicao.lower() == "s":
             while True:
              opcao_editar = input("Deseja adicionar ou remover funcionário? (adicionar/remover/sair): ")
              if opcao_editar.lower() == "adicionar":
                funcionarios=[" "]
                nome = input("Digite o nome do novo funcionário: ")
                sobrenome = input("Digite o sobrenome do novo funcionário: ")
                cargo = input("Digite o cargo do novo funcionário: ")

                funcionarios.append ({ "nome": nome, "sobrenome": sobrenome, "cargo": cargo})
                
                print("Novo funcionário adicionado com sucesso!")
                with open ("nome.txt", "a" ) as edita:
                 edita.write(str(funcionarios)+ "\n")
                 print(edita)
                
                    
              elif opcao_editar.lower() == "remover":
                with open('nome.txt', 'r') as file:
                 conteudo = file.readlines()
                 lista = conteudo
                 for i,linha in enumerate(lista):
                    print(i,linha)
              
        
                index = int(input("Digite o índice do funcionário que deseja remover: "))
                if 0 <= index < len(lista):
                    lista.pop(index)
                    print("Funcionário removido com sucesso!")
                
                with open ("nome.txt","w" ) as edit:
                 nova=edit.writelines (lista)
                 print(nova)
                    
                     
              elif opcao_editar=="sair":
                 break
              
              else:
               print("opção invalida")      
              
            elif opcao_edicao== "n":
               continue
            else:
               print("Opção invalida") 

     # escolha de filmes e edição ///////  criar variavel de filme escolhido para usar no sitema do funcionario
     elif opcao_selecionada=="e": 
         print("Escolha o Genero do filme:") 
         genero=["acao"  ,   "ficção cientica"   ,   "terror"    ,  "comedia "    ,  "romance"   ,  "infantil" , "sair" ] 
         print(genero)
         genero_escolhido=input("genero selecionado: ")
    
         if genero_escolhido=="acao":
          with open("ação.txt","r") as f_a:
            li_a=f_a.readlines()
            print(li_a)
          lista_acao=li_a
          filme_selecionado=input("selecione o filme: ")
          print(f"filme escolhido:",filme_selecionado)
          with open("filme.txt", "w") as f:
           filme_select=f.write(filme_selecionado)  
          print("deseja mudar o filme")
          mudar=input("(sim / nao)")
          if mudar=="sim":
             editar=True
        
             while editar is True:
              editar=True
              print("Opções:")
              print("1. Adicionar filme")
              print("2. Remover filme")
              print("3. Atualizar lista e sair")
              opcao = input("Escolha uma opção (1/2/3): ")

              if opcao == "1":
                 with open("ação.txt", "r") as fa:
                  lista_acao=fa.readlines()
                 novo_filme = input("Digite o nome do novo filme: ")
                 lista_acao.append(novo_filme)
                 with open("ação.txt","a") as la:
                   la.writelines(str(novo_filme)+"\n")
                   print(la)

  
              elif opcao == "2":
                print("Filmes disponíveis para remoção:")
                with open("ação.txt", "r") as tl:
                 lista_acao=tl.readlines()
                 listafilme=lista_acao
                 
                 for i,linha in enumerate(listafilme):
                   print(i,linha)
                indice_remover = int(input("Digite o número do filme a ser removido: ")) 
                if 0 <= indice_remover < len(lista_acao):
                    filme_removido = lista_acao.pop(indice_remover)
                    print(f"Filme {filme_removido} removido com sucesso!")
                    with open("ação.txt","w") as la:
                     la.writelines(lista_acao)
                    print(lista_acao)
                else:
                    print("Índice inválido, tente novamente.")

              elif opcao == "3":
                print("Lista atual de filmes de ação:")
                with open("ação.txt","r") as la:
                   lista_acao=la.readlines()
                   print(lista_acao)
                   
                editar = False

              else:
               print("Opção inválida. Tente novamente.")
             else:
              editar=False
              continue

         elif genero_escolhido=="ficção cientifica":
           with open("ficção.txt","r") as f_c:
            l_f=f_c.readlines()
            print(l_f)
           filme_selecionado=input("selecione o filme: ")
           print(f"filme escolhido:",filme_selecionado)
           with open("filme.txt", "w") as f:
            filme_select=f.write(filme_selecionado)  
           print("deseja mudar o filme")
           mudar=input("(sim / nao)")
           if mudar=="sim":
            editar=True
            
            while editar is True:
              editar=True 
              print("Opções:")
              print("1. Adicionar filme")
              print("2. Remover filme")
              print("3. Atualizar lista e sair")
              opcao = input("Escolha uma opção (1/2/3): ")

              if opcao == "1":
                 with open("ficção.txt", "r") as fc:
                  lista_ficcao=fc.readlines()
                  novo_filme = input("Digite o nome do novo filme: ")
                  lista_ficcao.append(novo_filme)
                 with open("ficção.txt","a") as lf:
                   lf.writelines(str(novo_filme)+"\n")
                   print(lf)

                
              elif opcao == "2":
                with open("ficção.txt", "r") as tf:
                 lista_ficcao=tf.readlines()
                 listafilmef=lista_ficcao

                 for i,linha in enumerate(listafilmef):
                  print(i,linha)
                 indice_remover = int(input("Digite o número do filme a ser removido: ")) 
                 if 0 <= indice_remover < len(lista_ficcao):
                   filme_removido = lista_ficcao.pop(indice_remover)
                   with open("ficção.txt","w") as lf:
                     lf.writelines(lista_ficcao)
                     print(lista_ficcao)
                 else:
                  print("Índice inválido, tente novamente")

              elif opcao == "3":
                print("Lista atualizada AÇÃO")
                with open("ficção.txt","r") as lf:
                   lista_ficcao=lf.readlines()
                   print(lista_ficcao)
                   
                
                editar = False
              else:
               print("Opção inválida. Tente novamente.")

           else:
              editar=False
              continue

         elif genero_escolhido=="terror":
           with open("terror.txt","r") as f_t:
            l_t=f_t.readlines()
            print(l_t)
            filme_selecionado=input("selecione o filme: ")
            print(f"filme escolhido:",filme_selecionado)
           with open("filme.txt", "w") as f:
            filme_select=f.write(filme_selecionado)  
            print("deseja mudar o filme")
            mudar=input("(sim / nao)")
           if mudar=="sim":
           editar=True
         
           while editar:
            editar=True
            print("Opções:")
            print("1. Adicionar filme")
            print("2. Remover filme")
            print("3. Atualizar lista e sair")
            opcao = input("Escolha uma opção (1/2/3): ")

            if opcao == "1":
              with open("terror.txt", "r") as ft:
               lista_terror=ft.readlines()
               novo_filme = input("Digite o nome do novo filme: ")
               lista_terror.append(novo_filme)
              with open("terror.txt","a") as lt:
                lt.writelines(str(novo_filme)+"\n")
                print(lt)
  
            elif opcao == "2":
              with open("terror.txt", "r") as tt:
                 lista_terror=tt.readlines()
                 listafilmet=lista_terror

                 for i,linha in enumerate(listafilmet):
                  print(i,linha)
                 indice_remover = int(input("Digite o número do filme a ser removido: ")) 
                 if 0 <= indice_remover < len(lista_terror):
                   filme_removido = lista_terror.pop(indice_remover)
                   with open("terror.txt","w") as lt:
                     lt.writelines(lista_terror)
                     print(lista_terror) 
               
                 else:
                    print("Índice inválido, tente novamente.")

            elif opcao == "3":
                print("Lista atualizada TERROR")
                print("FILME A SER EXIBIDO:",filme_selecionado)
                for filme in lista_terror:
                    print(filme)
                    
                editar = False
            else:
                print("Opção inválida. Tente novamente.")
           else:
              editar=False
              continue
         
         elif genero_escolhido=="comedia":
           with open("comedia.txt","r") as f_co:
            l_co=f_co.readlines()
            print(l_co)
            filme_selecionado=input("selecione o filme: ")
            print(f"filme escolhido:",filme_selecionado)
           with open("filme.txt", "w") as f:
            filme_select=f.write(filme_selecionado)  
            print("deseja mudar o filme")
            mudar=input("(sim / nao)")
           if mudar=="sim":
            editar=True

           while editar:
             editar=True
             print("Opções:")
             print("1. Adicionar filme")
             print("2. Remover filme")
             print("3. Atualizar lista e sair")
             opcao = input("Escolha uma opção (1/2/3): ")

             if opcao == "1":
              with open("comedia.txt", "r") as fco:
               lista_comedia=fco.readlines()
               novo_filme = input("Digite o nome do novo filme: ")
               lista_comedia.append(novo_filme)
              with open("comedia.txt","a") as lco:
                lco.writelines(str(novo_filme)+"\n")
                print(lco)

             elif opcao == "2":
               with open("comedia.txt", "r") as tco:
                 lista_comedia=tco.readlines()
                 listafilmec=lista_comedia

                 for i,linha in enumerate(listafilmec):
                  print(i,linha)
                 indice_remover = int(input("Digite o número do filme a ser removido: ")) 
                 if 0 <= indice_remover < len(lista_comedia):
                   filme_removido = lista_comedia.pop(indice_remover)
                   with open("comedia.txt","w") as lco:
                     lco.writelines(lista_comedia)
                     print(lista_comedia) 
                 else:
                    print("Índice inválido, tente novamente.")

             elif opcao == "3":
                print("Lista atualizada COMEDIA")
                for filme in lista_comedia:
                    print(filme)
                
                editar = False
             else:
              print("Opção inválida. Tente novamente.")
           else:
              editar=False
              continue  

         elif genero_escolhido=="romance":
           with open("romance.txt","r") as f_ro:
            l_ro=f_ro.readlines()
            print(l_ro)
            filme_selecionado=input("selecione o filme: ")
            print(f"filme escolhido:",filme_selecionado)
           with open("filme.txt", "w") as f:
            filme_select=f.write(filme_selecionado)  
            print("deseja mudar o filme")
            mudar=input("(sim / nao)")
           if mudar=="sim":
            editar=True

           while editar:
             editar=True
             print("Opções:")
             print("1. Adicionar filme")
             print("2. Remover filme")
             print("3. Atualizar lista e sair")
             opcao = input("Escolha uma opção (1/2/3): ")

             if opcao == "1":
               with open("romance.txt", "r") as fro:
                lista_romance=fro.readlines()
               novo_filme = input("Digite o nome do novo filme: ")
               lista_romance.append(novo_filme)
               with open("romance.txt","a") as lro:
                lro.writelines(str(novo_filme)+"\n")
                print(lro)
                
             elif opcao == "2":
               with open("romance.txt", "r") as tro:
                 lista_romance=tro.readlines()
                 listafilmero=lista_romance

                 for i,linha in enumerate(listafilmero):
                  print(i,linha)
                 indice_remover = int(input("Digite o número do filme a ser removido: ")) 
                 if 0 <= indice_remover < len(lista_romance):
                   filme_removido = lista_romance.pop(indice_remover)
                   with open("romance.txt","w") as lro:
                     lco.writelines(lista_romance)
                     print(lista_romance) 
                 else:
                    print("Índice inválido, tente novamente.") 

             elif opcao == "3":
                print("Lista Atualizada ROMANCE")
                for filme in lista_romance:
                    print(filme)
               
                   
                editar = False
             else:
              print("Opção inválida. Tente novamente.")
           else:
              editar=False
              continue  
  
         elif genero_escolhido=="infantil":
           with open("infantil.txt","r") as f_in:
            l_in=f_in.readlines()
            print(l_in)
            filme_selecionado=input("selecione o filme: ")
            print(f"filme escolhido:",filme_selecionado)
           with open("filme.txt", "w") as f:
            filme_select=f.write(filme_selecionado)  
            print("deseja mudar o filme")
            mudar=input("(sim / nao)")
           if mudar=="sim":
            editar=True

           while editar:
             editar=True
             print("Opções:")
             print("1. Adicionar filme")
             print("2. Remover filme")
             print("3. Atualizar lista e sair")
             opcao = input("Escolha uma opção (1/2/3): ")

             if opcao == "1":
               with open("infantil.txt", "r") as fin:
                lista_infantil=fin.readlines()
                novo_filme = input("Digite o nome do novo filme: ")
               lista_infantil.append(novo_filme)
               with open("infantil.txt","a") as lin:
                lin.writelines(str(novo_filme)+"\n")
                print(lin)

             elif opcao == "2":
                 with open("infantil.txt", "r") as tin:
                  lista_infantil=tin.readlines()
                  listafilmeroi=lista_infantil

                 for i,linha in enumerate(listafilmeroi):
                  print(i,linha)
                 indice_remover = int(input("Digite o número do filme a ser removido: ")) 
                 if 0 <= indice_remover < len(lista_infantil):
                   filme_removido = lista_infantil.pop(indice_remover)
                   with open("infantil.txt","w") as lin:
                     lin.writelines(lista_infantil)
                     print(lista_infantil) 
                 else:
                    print("Índice inválido, tente novamente.") 

             elif opcao == "3":
               print("Lista Atualizada INFANTIL")
               for filme in lista_infantil:
                   print(filme)
                  
               editar = False
             else:
                print("Opção inválida. Tente novamente.")
           else:
              editar=False
              continue       
         
         else:
                print("Lista de filmes não editada.")
                continue

#receita e preenchida com irformações de relatorios feito por funcionrios
# sera criado um banco de dados em SQL para guardar os dados "não foi colocado pq estou aprendendo  banco de dados "
     elif opcao_selecionada == "g":
        dias= int(0)
        receitas = []
        while  True:
         seleciona =input("Digite 'sair' para sair ou 'add' para lançar ganhos por data: ")
         if seleciona == "add":
          dias =+1
          data = input("Digite a data: ")
          receita = float(input("Digite a receita do dia: "))
          receitas.append({"data": data, "receita": receita})
          lucro_mensal = sum([dias["receita"] for dias in receitas])
          print("Receita do cinema: ")
          print(receitas)
          print("Mensal: ", lucro_mensal)
          print()
           
         elif seleciona == "sair":
           break
         else:
            print("Opção inválida. Tente novamente.")

     elif opcao_selecionada=="r":
        print("Escolha o relatorio que queira vizualizar")
        print("1.vendas")
        print("2.bilheteria")
        print("3. ocorrencias")
        print("4.sair")
        while True:
         relatorio_vizualizar=input("escolha a opção (1/2/3/4):" )
         if relatorio_vizualizar=="1":
             print("necessario o preenchimento pelo sitema do funcionario")
             print(vendas_dia)
         elif relatorio_vizualizar=="2":
             print("necessario o preenchimento pelo sitema do funcionario")
             print(bilheteria)
         elif relatorio_vizualizar=="3" :
             print("necessario o preenchimento pelo sitema do funcionario")
             print(ocorrencias)
         elif relatorio_vizualizar=="4":
             break
         else:
             print("DIgite um numero valido")
        
     elif opcao_selecionada=="s":
      encerra=False
      break
     else:
         print("Escolha uma opção valida")
         
 ############################# SISTEMA DE CONTROLE DO FUNCIONARIO #####################################
  elif sitema_escolhido== "funcionario":
   while True:
    sistema_funcionario= "[f]ilmes" ,  "[r]elatorios " , "[s]air"
    print(sistema_funcionario)
    sistema_funcionarioescolhido=input("opção selecionada: ")

   #o filme selecionado pelo gerente sera o filme mostrado no sistema do funcionario, filme selecionado eh uma variavel global
   # aqui o funcionario pode ver o filme escolhido pela gerencia 
    if sistema_funcionarioescolhido=="f":
       filme_a_exibir = filme_selecionado
       
       print("filme selecionado pela gestão:///// ",filme_a_exibir,"////////")
       print("OBS: Se vazio aguardar gerente lançar filme ")

    #aqui sera onde lança os relatorios para que apareçam no sitema do gerente
    elif sistema_funcionarioescolhido=="r":
     while True:
      relatorios= "[v]endas loja"  ,  "[b]ilheteria"   ,  "[o]correncias"  , "[s]air"
      print(relatorios)
      relatorio_selecionado=input("digite o relatoria a ser lançado:  ")
      
      if relatorio_selecionado=="v":
        
         while True:
          produto = input("Digite o nome do produto (ou 'sair' para finalizar): ")
          if produto == 'sair':
            break
          preco = float(input(f"Digite o preço de {produto}: "))
          vendas_dia.append({"produto": produto, "preco": preco})
          print("\nLista de produtos:")
          for item in vendas_dia:
            print(f"Produto: {item['produto']}, Preço: {item['preco']}")

      elif relatorio_selecionado=="b":
         
         while True:
          print("Lançar vendas de ingressos : ")
          lanca_ingresso= "[l]ancar" ,  "[s]air"
          print(lanca_ingresso)
          lancado=input("opção escolhida: ")
         
          if lancado=="l":
           ingressos_inteiro=int(input("ingressos interiros vendidos: "))
           ingresso_inteiro_valor=20
           conta_inteiro=ingressos_inteiro
           ingresso_inteiro_dia= ingresso_inteiro_valor * ingressos_inteiro
           print(ingresso_inteiro_dia)
          
           meio_ingresso=int(input("Digite a venda de meios ingressos vendidos: "))
           meio_valor=10
           meio_dia= meio_valor * meio_ingresso
           conta_meio=meio_ingresso

           venda_ingresso= ingresso_inteiro_dia+meio_dia
           print("Receita venda de ingressos : ", venda_ingresso)
           bilheteria.append (venda_ingresso)
           print(bilheteria)
           print("inteiros=" ,conta_inteiro)
           print("meio =",conta_meio)
          
          elif  lancado=="s":
            break 
          else:
             print("invalido")

      elif relatorio_selecionado=="o":
         while True:
          relatorio_ocorrencia=input("Digite a data e descreva a ocorrencia(ou 'sair' para finalizar): ")
          if relatorio_ocorrencia=="sair":
           break
          else:
           ocorrencias.append (relatorio_ocorrencia)
           print(ocorrencias)
        
      elif relatorio_selecionado=="s":
         break
      else:
         print("opção invalida")

    elif sistema_funcionarioescolhido=="s":
       break
    else:
     print("opção invalida")

  
  
          