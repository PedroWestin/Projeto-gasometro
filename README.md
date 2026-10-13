# Projeto Gasômetro

Aplicativo desktop em **Python + Qt (PySide6)** para o projeto Gasômetro.
A interface tem menu lateral retrátil (com animação), barra superior e páginas
trocadas por botões de navegação.

> **Status:** em desenvolvimento. A estrutura da interface está pronta; as telas
> ainda são páginas de exemplo e serão preenchidas nas próximas versões.

## Tecnologias

- Python 3.12 ou superior
- [PySide6](https://doc.qt.io/qtforpython-6/) (Qt para Python)

## Como executar

```bash
# 1. Clone o repositório
git clone https://github.com/PedroWestin/Projeto-gasometro.git
cd Projeto-gasometro

# 2. (Recomendado) crie um ambiente virtual
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Rode o aplicativo
python main.py
```

## Estrutura do projeto

```
Projeto-gasometro/
├── main.py                      # Janela principal e navegação entre páginas
├── qt_core.py                   # Importações centralizadas do Qt
├── requirements.txt             # Dependências
└── gui/
    ├── images/icons/            # Ícones SVG (home, menu, configurações)
    ├── pages/                   # Páginas do aplicativo (pages.ui e ui_pages.py)
    ├── widgets/                 # Componentes próprios (ex.: PyPushButton)
    └── windows/main_window/     # Layout da janela principal
```

## Roadmap

- [ ] Conteúdo real da página Home
- [ ] Página de Configurações
- [ ] Barra de pesquisa funcional
- [ ] Capturas de tela neste README

## Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE).

## Autor

**Pedro Westin** — [@PedroWestin](https://github.com/PedroWestin)
