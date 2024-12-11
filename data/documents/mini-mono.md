# Simplificação de Malhas de Triângulos 3D utilizando Decimação por Quadrics

**Autor:** Antônio Vasconcellos Chaves

**E-mail:** achaves\@inf.puc-rio.br

## Introdução

A simplificação de malhas de triângulos é uma técnica essencial em computação gráfica, aplicada em diversas áreas como renderização em tempo real, simulações científicas, impressão 3D e transmissão de dados em redes. Seu objetivo é reduzir o número de triângulos que compõem uma malha tridimensional, mantendo o mais fielmente possível a geometria original. Essa redução é fundamental para otimizar a performance de aplicações que lidam com grandes modelos 3D sem comprometer a qualidade visual ou os resultados das simulações.

### Objetivo Principal

Este trabalho é uma prova de conceito e demonstração da aplicação de simplificação de malhas 3D em um modelo destinado à impressão 3D. O objetivo é reduzir a complexidade geométrica para deixar o modelo mais leve e, consequentemente, facilitar o processamento em dispositivos de menor capacidade computacional, mantendo a qualidade necessária para a impressão.

O modelo escolhido é um design de código aberto amplamente utilizado na comunidade maker para impressão 3D, representando um objeto decorativo com detalhes complexos.

## Desenvolvimento/Pesquisa

### Escolha do Modelo

O modelo utilizado foi obtido de uma plataforma open-source popular (por exemplo, Thingiverse), representando uma peça decorativa projetada para impressão 3D. A escolha se deu pela complexidade inicial do modelo, com 594.722 triângulos, o que permite avaliar a eficiência do algoritmo em simplificações agressivas e leves. Abaixo está um placeholder para a imagem do modelo original:

![Modelo Original 3D](/data/images/full_shark.png)  
_Figura 1: Modelo original utilizado no experimento._

### Métodos

O algoritmo de Decimação por Quadrics foi utilizado devido à sua eficiência em preservar a forma geral da malha. Ele utiliza uma representação matricial para minimizar a distância entre os triângulos originais e os triângulos resultantes, realizando a fusão de vértices estrategicamente para reduzir o número de triângulos.

Nos experimentos, cada malha foi simplificada para três níveis distintos: 25%, 50% e 75% do número de triângulos originais mantidos. Para cada nível, foram calculadas:

- **Número de triângulos antes e depois da simplificação.**

- **Erro geométrico médio:** a distância média entre os pontos da malha simplificada e os da malha original.

### Ferramentas

A biblioteca **Open3D** foi utilizada para realizar a simplificação das malhas e o cálculo de métricas. O formato STL foi escolhido devido à sua popularidade em aplicações industriais e facilidade de manipulação. A escolha do Open3D se deu por sua robustez em lidar com malhas de alta densidade e por oferecer métodos nativos para simplificação e visualização de malhas.

### Procedimentos

1. **Leitura das malhas:** Carregaram-se modelos 3D no formato STL.

2. **Simplificação:** Aplicou-se o algoritmo de Decimação por Quadrics para reduzir os triângulos em diferentes níveis.

3. **Cálculo de métricas:**

   - O número de triângulos foi registrado antes e após cada simplificação.

   - A métrica de erro geométrico médio foi obtida convertendo as malhas em nuvens de pontos e comparando-as.

4. **Visualização:** As malhas simplificadas foram analisadas para avaliar o impacto visual da redução. Imagens das malhas antes e depois da simplificação foram geradas:

<div align="center">
<img src="/data/images/original.png" alt="Malha Original" width="400"/>

_Figura 2: Modelo original para comparação._

<img src="/data/images/simplificado.png" alt="Malha Simplificada" width="400"/>

_Figura 3: Modelo simplificado com 25% dos triângulos mantidos._

</div>

## Análise dos Resultados

### Resultados Obtidos

Os resultados estão resumidos na tabela abaixo:

| Nível de Simplificação | Triângulos Originais | Triângulos Simplificados | Erro Geométrico Médio |
| ---------------------- | -------------------- | ------------------------ | --------------------- |
| 25%                    | 594722               | 148680                   | 0.698427              |
| 50%                    | 594722               | 297360                   | 0.683599              |
| 75%                    | 594722               | 446040                   | 0.652277              |

![Gráfico de Simplificação](/data/images/graph.png)  
_Figura 4: Relação entre o nível de simplificação e o erro geométrico médio._

### Discussão

Os dados indicam que:

- **Número de triângulos:** A redução segue os níveis esperados, com 75% dos triângulos removidos para a simplificação mais agressiva (25% mantidos).

- **Erro geométrico médio:** O erro aumenta conforme mais triângulos são removidos, refletindo a perda de detalhes geométricos. Por exemplo, a simplificação de 25% gerou um erro maior (0.698) em comparação com 75% (0.652).

Além disso, a análise visual revelou que a simplificação mais agressiva removeu detalhes significativos do modelo, tornando-o menos adequado para aplicações decorativas. Por outro lado, a simplificação de 75% manteve a maior parte dos detalhes, sendo ideal para preservar a estética enquanto reduz a complexidade computacional.

Esses resultados confirmam que a Decimação por Quadrics é eficaz em reduzir significativamente o número de triângulos, mantendo uma boa aproximação da geometria original. A simplificação mais leve (75%) é ideal para aplicações que demandam alta qualidade visual, enquanto simplificações mais agressivas (25%) podem ser usadas em cenários onde o desempenho é prioritário.

## Agradecimentos e Licenciamento

O modelo 3D utilizado neste trabalho, "Stylish Flexi Shark", foi criado por Zentangle99 e está disponível na plataforma Thingiverse sob a licença Creative Commons - Attribution - Non-Commercial - No Derivatives. O link para o modelo é [https://www.thingiverse.com/thing:6828888](https://www.thingiverse.com/thing:6828888). Agradecemos ao autor por disponibilizar este recurso para estudos acadêmicos.

## Conclusão

A simplificação de malhas por Decimação por Quadrics provou-se uma abordagem eficiente para balancear a redução de triângulos e a preservação da geometria. Os resultados mostraram que:

- Níveis mais leves de simplificação mantêm maior fidelidade à malha original.

- Simplificações mais agressivas oferecem ganhos significativos em desempenho, ao custo de maior perda geométrica.

Limitações incluem o uso de apenas um algoritmo para simplificação e uma única métrica de avaliação. Trabalhos futuros podem explorar algoritmos alternativos e incluir métricas perceptuais para melhor compreensão do impacto visual. Além disso, não foi possível realizar testes de tempo para o processamento das malhas simplificadas ou para a impressão 3D devido à falta do instrumental necessário. Testar esses aspectos seria uma análise interessante para complementar os resultados obtidos.

## Código-Fonte e Repositório

O código-fonte desenvolvido para este trabalho, incluindo as implementações para a simplificação de malhas, os gráficos e os heatmaps, está disponível no seguinte repositório GitHub:

[https://github.com/antoniovchaves/INF2604-trabfinal](https://github.com/antoniovchaves/INF2604-trabfinal)

O repositório inclui:

- Código Python completo.
- Instruções para instalação e execução no arquivo `README.md`.
- Exemplos de arquivos STL utilizados nos experimentos (não modificados).

## Referências

- Garland, M., & Heckbert, P. S. (1997). Surface Simplification Using Quadric Error Metrics. _Proceedings of he 24th Annual Conference on Computer Graphics and Interactive Techniques_.

- Open3D Documentation: [https://www.open3d.org](https://www.open3d.org)

- Schroeder, W., Zarge, J., & Lorensen, W. (1992). Decimation of Triangle Meshes. _Computer Graphics (ACM)_.
