# Monitor de Integridade de Arquivos Simples

Este projeto é um script simples em Python para monitoramento de integridade de arquivos (FIM - File Integrity Monitor). Sua principal utilidade é garantir que um arquivo não foi alterado ou corrompido, comparando seu estado atual com uma "baseline" (uma versão original e confiável).

É uma ferramenta útil para:
-   Verificar se arquivos de configuração importantes não foram modificados sem autorização.
-   Garantir a integridade de scripts ou executáveis.
-   Detectar atividades suspeitas que resultem em alteração de arquivos.

## Como Funciona

O princípio de funcionamento é baseado em **hashes criptográficos (SHA-256)**.

1.  **Criação da Baseline**: Ao iniciar, o script calcula o hash SHA-256 de um arquivo específico (por padrão, `senha.txt`). Esse hash funciona como uma "impressão digital" única do conteúdo do arquivo. Ele é armazenado na memória como o **hash original**.
2.  **Monitoramento Contínuo**: Ao escolher a opção de monitoramento, o script entra em um loop "ao vivo". A cada segundo, ele recalcula o hash do mesmo arquivo.
3.  **Comparação**: O hash recém-calculado é comparado com o hash original guardado na memória.
    -   Se os hashes forem **idênticos**, significa que o arquivo não sofreu nenhuma alteração e está intacto.
    -   Se os hashes forem **diferentes**, o script emite um alerta, indicando que o conteúdo do arquivo foi modificado.

Isso permite detectar qualquer mudança no arquivo monitorado, por menor que seja, e em tempo real.

## Como Rodar o Projeto

Para executar este monitor em sua máquina local, siga os passos abaixo.

### Pré-requisitos
-   Python 3 instalado em sua máquina.
-   Git instalado (para clonar o repositório).

### Passos para Execução

1.  **Clone o Repositório**:
    Abra seu terminal e clone este repositório para sua máquina local (substitua pela URL real do seu repositório):
    ```bash
    git clone https://github.com/theycallmefreire/File-Integrity-Monitor-FIM-.git
    ```

2.  **Navegue até a Pasta**:
    Entre no diretório que acabou de ser criado:
    ```bash
    cd nome-do-repositorio
    ```

3.  **Execute o Monitor**:
    Inicie o script principal usando Python:
    ```bash
    python main.py
    ```

5.  **Teste o Monitoramento**:
    -   Quando o script iniciar, digite `2` e pressione Enter para começar o monitoramento "ao vivo".
    -   Com o script rodando, abra o arquivo `senha.txt` em outro programa (como o Bloco de Notas), altere o conteúdo e salve.
    -   Volte ao terminal e você verá o alerta de alteração em tempo real.

## Melhorias Futuras

Este é um projeto inicial, e pretendo expandir suas funcionalidades. Os próximos passos incluem:

-   **Monitoramento de Diretórios**: Implementar uma opção para que o usuário possa escolher uma pasta inteira para monitorar, em vez de um único arquivo.
-   **Baseline de Múltiplos Arquivos**: Ao selecionar uma pasta, o sistema irá gerar e armazenar um hash para cada arquivo dentro dela.
-   **Relatório Completo de Mudanças**: O sistema irá comparar o estado atual de todos os arquivos na pasta com a baseline salva, reportando quais arquivos foram **modificados**, **adicionados** ou **removidos** do diretório.
