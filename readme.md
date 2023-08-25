# Desafio Técnico: Análise de Pedidos e Motoboys

O projeto tem como objetivo calcular e exibir o ganho de um motoboy com base nos pedidos realizados para as lojas associadas a ele.

## Estrutura

### Arquivos principais:

1. **manager.py**: 
   - Define classes para carregar e gerenciar dados de lojas, pedidos e motoboys.
   - Oferece um método para escolher um motoboy e gerar um relatório detalhado de seus ganhos.
   
2. **models.py**:
   - Define os modelos e estruturas de dados para Lojas, Pedidos e Motoboys usando o `BaseModel` definido em `base_model.py`.
   
3. **base_model.py**: 
   - Define estruturas de validação para modelos de dados como `Field`, `SimpleField`, `ListField` e `BaseModel`.
   
4. **script_calcula_ganhos.py**: 
   - É o script principal que, quando executado, carrega dados, permite ao usuário escolher um motoboy e exibe o relatório correspondente.

## Como Executar

1**Execução**:
   - Abra o terminal ou linha de comando no diretório onde os arquivos estão localizados.
   - Execute o script usando o comando: 
     ```
     python script_calcula_ganhos.py
     ```
   - Siga as instruções na tela para escolher um motoboy.
   - O relatório de ganhos do motoboy escolhido será exibido na tela.

## Explicação

Quando o `script_calcula_ganhos.py` é executado:

1. Os dados de lojas, pedidos e motoboys são carregados dos arquivos JSON.
2. O usuário é solicitado a escolher um motoboy da lista.
3. O programa exibe um relatório detalhando:
   - Lojas atendidas pelo motoboy.
   - Pedidos realizados pelo motoboy.
   - Cálculo de ganhos com base nos pedidos e comissões das lojas.
   
## Considerações

- O projeto foi projetado para ser simples e focado em seu propósito.
