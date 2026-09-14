# 📅 Projeto Agenda de Tarefas

Uma aplicação web de **gerenciamento de tarefas** desenvolvida com **Python e Django**, criada para organizar atividades do dia a dia de forma simples, visual e intuitiva.

O projeto também faz parte da minha evolução prática em **desenvolvimento backend**, utilizando Django, banco de dados, autenticação e versionamento com Git/GitHub.

---

## 🚀 Funcionalidades

* 🔐 Sistema de login e autenticação
* 📝 Cadastro de tarefas
* ✅ Marcação de tarefas como concluídas
* 🔄 Alteração do status das tarefas
* 🗑️ Gerenciamento das tarefas
* 📊 Indicador de progresso
* 📱 Interface responsiva
* 🗄️ Persistência dos dados em banco de dados
* 🌐 Execução local através do navegador

---

## 🖥️ Preview

### Tela principal

> Adicione aqui uma captura de tela da aplicação.

![Agenda de Tarefas](docs/preview.png)

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização                   |
| ---------- | ---------------------------- |
| 🐍 Python  | Linguagem principal          |
| 🌐 Django  | Framework web                |
| 🗄️ SQLite | Banco de dados               |
| 🎨 HTML5   | Estrutura das páginas        |
| 🎨 CSS3    | Estilização e responsividade |
| 🔧 Git     | Controle de versão           |
| ☁️ GitHub  | Hospedagem do código         |

---

## 📂 Estrutura do projeto

```text
projeto_agenda_tarefas/
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── tarefas/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── static/
│   └── css/
│       └── style.css
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Lucas-Oliveira-Souzaa/Projeto-Agenda-de-tarefas-com-Python.git
```

### 2. Entre na pasta

```bash
cd Projeto-Agenda-de-tarefas-com-Python
```

### 3. Crie o ambiente virtual

No Windows:

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

```bash
.venv\Scripts\activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute as migrações

```bash
python
```
