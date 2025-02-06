🏷️ CountObjects - Contagem de Objetos com Visão Computacional
📌 Descrição

CountObjects é um projeto de visão computacional que utiliza técnicas de processamento de imagens para contar objetos automaticamente em uma imagem. Ele pode ser aplicado em diversos contextos industriais e acadêmicos, facilitando a análise e o controle de itens em imagens digitais.
🔧 Tecnologias Utilizadas

    🐍 Python
    🖼 OpenCV (Processamento de imagem)
    📊 NumPy (Manipulação de arrays)
    📉 Matplotlib (Visualização de dados)

🚀 Funcionalidades

✔ Processamento de imagens para identificar e contar objetos
✔ Aplicação de técnicas de thresholding e segmentação
✔ Exibição dos resultados com a contagem sobreposta na imagem
📂 Estrutura do Projeto

CountObjects/
│── images/           # Imagens de entrada para teste
│── results/          # Imagens processadas com contagem
│── src/              # Código-fonte principal
│   ├── main.py       # Script principal para contagem de objetos
│   ├── utils.py      # Funções auxiliares
│── README.md         # Documentação do projeto
│── requirements.txt  # Dependências do projeto

🛠 Como Executar

    Clone o repositório

git clone https://github.com/anottsu/CountObjetcts.git
cd CountObjetcts

Crie um ambiente virtual (opcional, mas recomendado)

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

Instale as dependências

pip install -r requirements.txt

Execute o script principal

    python src/main.py --image images/exemplo.jpg

📷 Exemplo de Resultado

Exemplo de imagem processada mostrando a contagem de objetos:
🔗 Referências

    OpenCV Documentation
    NumPy Documentation

📌 To-Do

Melhorar a precisão da contagem em imagens complexas
Adicionar interface gráfica simples para facilitar o uso

    Implementar suporte a vídeos para contagem em tempo real

📝 Licença

Este projeto é de código aberto e está licenciado sob a MIT License.
