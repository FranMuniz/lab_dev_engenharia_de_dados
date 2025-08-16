flowchart TD
    %% Etapa 1: Python
    A[📌 Fundamentos de Python] --> A1[📄 Sintaxe básica, variáveis, tipos]
    A --> A2[📄 Estruturas de controle (if, for, while)]
    A --> A3[📄 Funções, módulos e pacotes]
    A --> A4[📄 Listas, dicionários, tuplas, sets]
    A --> A5[📄 Manipulação de arquivos (CSV, JSON, TXT)]
    A --> A6[📄 Bibliotecas: pandas, numpy, datetime]

    %% Etapa 2: SQL
    B[📌 Banco de Dados & SQL] --> B1[📄 Conceitos de BD relacional vs não-relacional]
    B --> B2[📄 Criação de tabelas e inserção de dados]
    B --> B3[📄 Consultas básicas: SELECT, WHERE, ORDER BY, GROUP BY]
    B --> B4[📄 Joins: INNER, LEFT, RIGHT, FULL]
    B --> B5[📄 Funções agregadas e de janela (SUM, COUNT, ROW_NUMBER)]
    B --> B6[📄 Subqueries e CTEs (WITH)]
    B --> B7[📄 Indexes e normalização]
    B --> B8[📄 Prática em PostgreSQL]

    %% Etapa 3: Git & GitHub
    C[📌 Git & GitHub] --> C1[📄 Comandos básicos: clone, add, commit, push, pull]
    C --> C2[📄 Branches, merges e pull requests]
    C --> C3[📄 Code review e boas práticas]
    C --> C4[📄 GitHub Actions (CI/CD básico)]

    %% Etapa 4: Manipulação de Dados Python
    D[📌 Manipulação de Dados com Python] --> D1[📄 Leitura/escrita CSV, Excel, Parquet]
    D --> D2[📄 Limpeza: fillna, dropna, duplicados]
    D --> D3[📄 Transformações: apply, map, merge, concat]
    D --> D4[📄 Agregações e pivot tables]
    D --> D5[📄 Validação e qualidade de dados]

    %% Etapa 5: Spark & PySpark
    E[📌 Apache Spark & PySpark] --> E1[📄 RDD, DataFrames, Lazy Evaluation]
    E --> E2[📄 Operações básicas: select, filter, groupBy, join]
    E --> E3[📄 Leitura/escrita: CSV, Parquet, PostgreSQL, S3]
    E --> E4[📄 Transformações avançadas: window, pivot, explode]
    E --> E5[📄 Spark SQL e queries complexas]
    E --> E6[📄 Otimizações: caching, partitioning, broadcast join]
    E --> E7[📄 PySpark UDFs e UDAFs]

    %% Etapa 6: Airflow
    F[📌 Airflow & Orquestração] --> F1[📄 DAGs e scheduling]
    F --> F2[📄 Operadores: PythonOperator, BashOperator, PostgresOperator]
    F --> F3[📄 Variáveis, XCom e templates Jinja]
    F --> F4[📄 SubDAGs e modularização]
    F --> F5[📄 Monitoramento de pipelines e alertas]
    F --> F6[📄 Integração Airflow + Spark/PostgreSQL]

    %% Etapa 7: Engenharia de Dados prática
    G[📌 Engenharia de Dados na Prática] --> G1[📄 Pipelines de ingestão e transformação]
    G --> G2[📄 Integração com APIs e sistemas externos]
    G --> G3[📄 Processamento batch vs streaming]
    G --> G4[📄 Armazenamento em bancos e data lakes]
    G --> G5[📄 Logging, rastreabilidade e testes de dados]

    %% Etapa 8: Boas práticas & Soft Skills
    H[📌 Boas práticas & Soft Skills] --> H1[📄 Estrutura de pastas e organização de código]
    H --> H2[📄 Variáveis de ambiente e .env]
    H --> H3[📄 Controle de dependências: requirements.txt, pipenv, poetry]
    H --> H4[📄 Documentação clara e README amigável]
    H --> H5[📄 Comunicação com time e stakeholders]

    %% Etapa 9: Extras
    I[📌 Extras para Diferencial] --> I1[📄 Docker para ambientes isolados]
    I --> I2[📄 CI/CD para pipelines de dados]
    I --> I3[📄 Visualização de dados: Matplotlib, Seaborn, Plotly]
    I --> I4[📄 Noções de Big Data: Kafka, Hive, Hudi, Delta Lake]
    I --> I5[📄 Aprendizado contínuo: cursos, documentação e projetos]

    %% Conexões de sequência
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I

    %% Cores para cada etapa
    style A fill:#f9c74f,stroke:#000,stroke-width:1px
    style B fill:#90be6d,stroke:#000,stroke-width:1px
    style C fill:#f94144,stroke:#000,stroke-width:1px
    style D fill:#577590,stroke:#000,stroke-width:1px
    style E fill:#43aa8b,stroke:#000,stroke-width:1px
    style F fill:#f3722c,stroke:#000,stroke-width:1px
    style G fill:#577590,stroke:#000,stroke-width:1px
    style H fill:#f8961e,stroke:#000,stroke-width:1px
    style I fill:#90be6d,stroke:#000,stroke-width:1px
