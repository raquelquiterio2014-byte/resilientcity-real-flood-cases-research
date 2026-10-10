# ResilientCity AI — Casos Reais — primeira versão

1. Extraia o ZIP em uma pasta nova, separada da V6.
2. No PyCharm, abra essa pasta e execute **main.py**.
3. Deixe **offline** selecionado e clique em **Run research**.
4. O resultado inicial **BLOCKED** é esperado: o caso ainda não tem fontes verificadas.
5. Veja o relatório e a sequência real dos agentes na aba **Report & agent trace**.
6. Para ativar Gemini, instale `requirements.txt` e configure `GEMINI_API_KEY` nas variáveis de ambiente da execução no PyCharm. Depois importe as evidências e escolha **gemini**.

A interface está em inglês para o portfólio. **Case & evidence JSON** permite editar o caso; **Import** importa um JSON, **Register / update** salva seu cadastro e **Export** exporta o relatório. Datas precisam conter fuso horário; exemplo: `2023-11-06T08:00:00Z`.

`verified: true` só deve ser marcado depois de você verificar a fonte e a data em que a evidência estava disponível. Fontes posteriores à data de corte não são enviadas aos agentes. A chave da API não deve entrar nos arquivos de casos.

A versão 0.2 inclui o cadastro dos dez casos e as fontes de pesquisa. Todos continuam pendentes de validação retrospectiva.

Nome sugerido para o novo GitHub: **resilientcity-real-flood-cases-research**. O repositório já contém a versão atualizada. A execução visual no seu computador continua pendente.

## Versão 0.2 — cadastro dos dez casos

Os dez casos estão no seletor. A aba **Sources & registration** mostra as fontes levantadas e lacunas. Edite o JSON e clique em **Register / update** para salvar o cadastro na pasta do projeto. **Export case** salva uma cópia individual.

Nove casos ainda têm data de corte `null`. Isso é aceito no cadastro, mas a análise ficará **BLOCKED**, sem chamadas à API. As fontes de pesquisa não são evidências admitidas automaticamente. Todos os casos continuam pendentes de validação retrospectiva.
