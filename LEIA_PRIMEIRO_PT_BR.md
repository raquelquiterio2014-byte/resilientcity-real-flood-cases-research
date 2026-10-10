# ResilientCity AI — Casos Reais — primeira versão

1. Extraia o ZIP em uma pasta nova, separada da V6.
2. No PyCharm, abra essa pasta e execute **main.py**.
3. Deixe **offline** selecionado e clique em **Run research**.
4. O resultado inicial **BLOCKED** é esperado: o caso ainda não tem fontes verificadas.
5. Veja o relatório e a sequência real dos agentes na segunda aba.
6. Para ativar Gemini, instale `requirements.txt` e configure `GEMINI_API_KEY` nas variáveis de ambiente da execução no PyCharm. Depois importe as evidências e escolha **gemini**.

A interface está em inglês para o portfólio. **Case & evidence JSON** permite editar o caso; **Import** importa um JSON, **Save case** salva sua edição e **Export** exporta o relatório. Datas precisam conter fuso horário; exemplo: `2023-11-06T08:00:00Z`.

`verified: true` só deve ser marcado depois de você verificar a fonte e a data em que a evidência estava disponível. Fontes posteriores à data de corte não são enviadas aos agentes. A chave da API não deve entrar nos arquivos de casos.

Esta primeira entrega inclui o cadastro inicial de Pas-de-Calais com o ID e a data de corte fornecidos anteriormente. Os outros dossiês franceses e mundiais precisam ser importados; não foram reconstruídos com informações presumidas. Todos continuam pendentes de validação retrospectiva.

Nome sugerido para o novo GitHub: **resilientcity-real-flood-cases-research**. Primeiro valide a execução local; depois podemos organizar a publicação do novo repositório.
