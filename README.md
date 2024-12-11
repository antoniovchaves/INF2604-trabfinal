# Simplificação de Malhas de Triângulos 3D

Este projeto realiza a simplificação de malhas de triângulos 3D utilizando o algoritmo de Decimação por Quadrics. Ele analisa diferentes níveis de simplificação (25%, 50%, 75%) para avaliar o impacto geométrico e a redução no número de triângulos. Os resultados são gerados como gráficos, heatmaps e visualizações comparativas.

## Pré-requisitos

Antes de executar o código, instale as dependências necessárias com o seguinte comando:

```bash
pip install open3d matplotlib numpy
```

## Alteração do Caminho dos Arquivos

Certifique-se de alterar o caminho dos arquivos STL no código Python para o formato correto. Por exemplo:

```python
path = "C:/Users/<seu_usuario>/<caminho_da_pasta>/data/models/Stylish Flexi Shark - 6828888/files/"
files = {
    "original": path + "Shark.stl",
    "25": path + "Shark_25.stl",
    "50": path + "Shark_50.stl",
    "75": path + "Shark_75.stl",
}
```

Substitua `<seu_usuario>` e `<caminho_da_pasta>` pelos valores correspondentes no seu sistema.

## Como Executar

1. Clone o repositório:

   ```bash
   git clone <link-do-repositorio>
   cd <nome-do-repositorio>
   ```

2. Execute o script principal:
   ```bash
   python mini-mono.py
   ```

## Modelo Utilizado

O modelo 3D utilizado, "Stylish Flexi Shark", foi criado por Zentangle99 e está disponível na plataforma Thingiverse sob a licença Creative Commons - Attribution - Non-Commercial - No Derivatives. O link para o modelo é: [https://www.thingiverse.com/thing:6828888](https://www.thingiverse.com/thing:6828888).

## Resultados

O script gera:

- **Gráficos**: Relação entre nível de simplificação e erro geométrico médio.
- **Heatmaps**: Diferenças geométricas visualizadas por cores.
- **Visualizações**: Comparações lado a lado entre as malhas simplificadas e a original.

## Contribuições

Contribuições são bem-vindas! Caso encontre problemas ou deseje adicionar novos recursos, abra uma issue ou envie um pull request.
